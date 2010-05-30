# pulled from http://www.bitbucket.org/mu_mind/pycaca, r11:b97c9bd8e08a

import ctypes
from . import (_caca, canvas, event)

__all__ = ['Display']

class Display(object):
    def __init__(self, canvas=None, driver=None):
        _canvas = (canvas._internal if canvas is not None else None)
        if driver is not None:
            self._internal = _caca.caca_create_display_with_driver(_canvas, driver)
        else:
            self._internal = _caca.caca_create_display(_canvas)
    
    def get_canvas(self):
        return canvas.Canvas(_caca.caca_get_canvas(self._internal))

    def set_title(self, title):
        _caca.caca_set_display_title(self._internal, title)

    def refresh(self):
        _caca.caca_refresh_display(self._internal)

    def _get_event(self, mask=0xffff, timeout=-1):
        ev = _caca.caca_event_t()
        status = _caca.caca_get_event(self._internal, mask, ctypes.byref(ev), timeout)
        return (ev if status else None)

    def get_event(self, mask=0xffff, timeout=-1):
        ev = self._get_event(mask, timeout)
        if ev:
            return event.Event.pythonize(ev)
        else:
            return None

    def __del__(self):
        # TODO: right place for that?
        _caca.caca_free_display(self._internal)
