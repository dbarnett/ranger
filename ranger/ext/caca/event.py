# -*- coding: utf-8 -*-
# pulled from http://www.bitbucket.org/mu_mind/pycaca, r11:b97c9bd8e08a

import ctypes
from . import (_caca, const)

__all__ = ['Event', 'MouseMotionEvent', 'MouseButtonEvent', 'MousePressEvent',
'MouseReleaseEvent', 'KeyEvent', 'KeyPressEvent', 'KeyReleaseEvent',
'QuitEvent', 'ResizeEvent']

class Event(object):
    def __init__(self, _event):
        self._internal = _event

    @staticmethod
    def pythonize(_event):
        return EVENT_MAP[_caca.caca_get_event_type(_event)](_event)

class MouseMotionEvent(Event):
    def __init__(self, _event):
        super(MouseMotionEvent, self).__init__(_event)
        self.x = _caca.caca_get_event_mouse_x(_event)
        self.y = _caca.caca_get_event_mouse_y(_event)

    def __repr__(self):
        return '<%s x=%d y=%d>' % (self.__class__.__name__, self.x, self.y)

class MouseButtonEvent(Event):
    def __init__(self, _event):
        super(MouseButtonEvent, self).__init__(_event)
        self.button = _caca.caca_get_event_mouse_button(_event)

    def __repr__(self):
        return '<%s button=%d>' % (self.__class__.__name__, self.button)

class MousePressEvent(MouseButtonEvent):
    pass

class MouseReleaseEvent(MouseButtonEvent):
    pass

class KeyEvent(Event):
    def __init__(self, _event):
        super(KeyEvent, self).__init__(_event)
        chars = ctypes.create_string_buffer(8)
        ch = _caca.caca_get_event_key_ch(ctypes.byref(_event))
        self.key = ch
        # TODO: umlauts
#        assert chars[1] == '\x00', 'We have strange characters. Please report this to me!'
#        self.key = unichr(ord(chars[0])) # TODO: that could be better

    def __repr__(self):
        return '<%s ordinal=%d>' % (self.__class__.__name__, self.key)

class KeyPressEvent(KeyEvent):
    pass

class KeyReleaseEvent(KeyEvent):
    pass

class QuitEvent(Event):
    pass

class ResizeEvent(Event):
    def __init__(self, _event):
        super(ResizeEvent, self).__init__(_event)
        self.width = _caca.caca_get_event_resize_width(_event)
        self.height = _caca.caca_get_event_resize_height(_event)

EVENT_MAP = {
            const.Events.MOUSE_PRESS: MousePressEvent,
            const.Events.MOUSE_RELEASE: MouseReleaseEvent,
            const.Events.MOUSE_MOTION: MouseMotionEvent,
            const.Events.KEY_PRESS: KeyPressEvent,
            const.Events.KEY_RELEASE: KeyReleaseEvent,
            const.Events.QUIT: QuitEvent,
            const.Events.RESIZE: ResizeEvent,
        }
