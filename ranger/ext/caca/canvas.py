# pulled from http://www.bitbucket.org/mu_mind/pycaca, r11:b97c9bd8e08a

from . import _caca

import ctypes, struct
import sys

__all__ = ['Canvas', 'CuculBuffer']

class CuculBuffer(object):
    def __init__(self, _cucul_buffer):
        self._internal = _cucul_buffer

    def get_data(self):
        buf_size = _caca.cucul_get_buffer_size(self._internal)
        buf_data = ctypes.cast(_caca.cucul_get_buffer_data(self._internal), ctypes.POINTER(ctypes.c_char))[:buf_size]
        return buf_data

    def __del__(self):
        _caca.cucul_free_buffer(self._internal)

class Canvas(object):
    def __init__(self, _canvas):
        self._internal = _canvas

    @classmethod
    def create(cls, width, height):
        _canvas = _caca.caca_create_canvas(width, height)
        return cls(_canvas)

    def set_color_ansi(self, foreground, background):
        assert _caca.caca_set_color_ansi(self._internal, foreground, background) == 0
        
    def put_str(self, x, y, string):
        _caca.caca_put_str(self._internal, x, y, string)

    def put_char(self, x, y, char):
        _caca.caca_put_char(self._internal, x, y, ord(char))

    def clear(self):
        _caca.caca_clear_canvas(self._internal)

    def get_cursor_position(self):
        return (_caca.caca_get_cursor_x(self._internal), _caca.caca_get_cursor_y(self._internal))

    def get_width(self):
        return _caca.caca_get_canvas_width(self._internal)

    def get_height(self):
        return _caca.caca_get_canvas_height(self._internal)

    def get_size(self):
        return (self.get_width(), self.get_height())

    def _rgba_dither(self, w, h):
        if sys.byteorder == 'big':
            rgba_mask = [0xff<<24, 0xff<<16, 0xff<<8, 0xff]
        else:
            rgba_mask = [0xff, 0xff<<8, 0xff<<16, 0xff<<24]
        return _caca.caca_create_dither(32, w, h, 4*w, *rgba_mask)

    def put_pil_image(self, x, y, w, h, img):
        w_px, h_px = img.size
        n_pixels = (w_px*h_px)
        pixels_array = (ctypes.c_int * n_pixels)()
        ctypes.memmove(pixels_array, img.convert('RGBA').tostring(), n_pixels*4)
        dither = self._rgba_dither(w_px, h_px)
        _caca.caca_dither_bitmap(self._internal, x, y, w, h, dither, pixels_array)

    def export(self, fmt="ansi"):
        cucul_buffer = CuculBuffer(_caca.cucul_export_canvas(self._internal, fmt))
        return cucul_buffer.get_data()
