# Copyright (C) 2009, 2010  Roman Zimbelmann <romanz@lavabit.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
The File Manager, putting the pieces together
"""

from time import time
from collections import deque
import mimetypes
import os
import sys

import ranger
from ranger.core.actions import Actions
from ranger.container.tags import Tags
from ranger.gui.defaultui import DefaultUI
from ranger.container import Bookmarks
from ranger.core.runner import Runner
from ranger.ext.get_executables import get_executables
from ranger.fsobject import Directory
from ranger.ext.signal_dispatcher import SignalDispatcher
from ranger import __version__
from ranger.core.loader import Loader

TICKS_BEFORE_COLLECTING_GARBAGE = 100
TIME_BEFORE_FILE_BECOMES_GARBAGE = 1200

class FM(Actions, SignalDispatcher):
	input_blocked = False
	input_blocked_until = 0
	def __init__(self, ui=None, bookmarks=None, tags=None):
		"""Initialize FM."""
		Actions.__init__(self)
		SignalDispatcher.__init__(self)
		self.ui = ui
		self.log = deque(maxlen=20)
		self.bookmarks = bookmarks
		self.tags = tags
		self.tabs = {}
		self.current_tab = 1
		self.loader = Loader()

		self.log.append('Ranger {0} started! Process ID is {1}.' \
				.format(__version__, os.getpid()))
		self.log.append('Running on Python ' + sys.version.replace('\n',''))

	# COMPAT
	@property
	def executables(self):
		"""For compatibility. Calls get_executables()"""
		return get_executables()

	def initialize(self):
		"""If ui/bookmarks are None, they will be initialized here."""
		if self.bookmarks is None:
			if ranger.arg.clean:
				bookmarkfile = None
			else:
				bookmarkfile = self.confpath('bookmarks')
			self.bookmarks = Bookmarks(
					bookmarkfile=bookmarkfile,
					bookmarktype=Directory,
					autosave=self.settings.autosave_bookmarks)
			self.bookmarks.load()

		else:
			self.bookmarks = bookmarks

		if not ranger.arg.clean and self.tags is None:
			self.tags = Tags(self.confpath('tagged'))

		if self.ui is None:
			self.ui = DefaultUI()
			self.ui.initialize()

		def mylogfunc(text):
			self.notify(text, bad=True)
		self.run = Runner(ui=self.ui, apps=self.apps,
				logfunc=mylogfunc)

		self.env.signal_bind('cd', self._update_current_tab)

		mimetypes.knownfiles.append(os.path.expanduser('~/.mime.types'))
		mimetypes.knownfiles.append(self.relpath('data/mime.types'))
		self.mimetypes = mimetypes.MimeTypes()

	def block_input(self, sec=0):
		self.input_blocked = sec != 0
		self.input_blocked_until = time() + sec

	def input_is_blocked(self):
		if self.input_blocked and time() > self.input_blocked_until:
			self.input_blocked = False
		return self.input_blocked

	def confpath(self, *paths):
		"""returns the path relative to rangers configuration directory"""
		if ranger.arg.clean:
			assert 0, "Should not access relpath_conf in clean mode!"
		else:
			return os.path.join(ranger.arg.confdir, *paths)

	def relpath(self, *paths):
		"""returns the path relative to rangers library directory"""
		return os.path.join(ranger.RANGERDIR, *paths)

	def loop(self):
		"""
		The main loop consists of:
		1. reloading bookmarks if outdated
		2. letting the loader work
		3. drawing and finalizing ui
		4. reading and handling user input
		5. after X loops: collecting unused directory objects
		"""

		self.env.enter_dir(self.env.path)

		gc_tick = 0

		# for faster lookup:
		ui = self.ui
		throbber = ui.throbber
		loader = self.loader
		env = self.env
		has_throbber = hasattr(ui, 'throbber')

		try:
			while True:
				loader.work()
				if has_throbber:
					if loader.has_work():
						throbber(loader.status)
					else:
						throbber(remove=True)

				ui.redraw()

				ui.set_load_mode(loader.has_work())

				ui.handle_input()

				gc_tick += 1
				if gc_tick > TICKS_BEFORE_COLLECTING_GARBAGE:
					gc_tick = 0
					env.garbage_collect(TIME_BEFORE_FILE_BECOMES_GARBAGE)

		except KeyboardInterrupt:
			# this only happens in --debug mode. By default, interrupts
			# are caught in curses_interrupt_handler
			raise SystemExit

		finally:
			self.bookmarks.remember(env.cwd)
			self.bookmarks.save()
