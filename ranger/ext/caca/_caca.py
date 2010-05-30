# pulled from http://www.bitbucket.org/mu_mind/pycaca, r11:b97c9bd8e08a

'''Wrapper for /usr/local/include/caca

Generated with:
wrap.py -l caca -o _caca.py /usr/local/include/caca.h

modified this file for better opaque struct handling
'''

__docformat__ =  'restructuredtext'
__version__ = '$Id: wrap.py 1694 2008-01-30 23:12:00Z Alex.Holkner $'

import ctypes
from ctypes import *

_lib = cdll.LoadLibrary('libcaca.so')

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]



class struct_caca_canvas(Structure):
    __slots__ = [
    ]
struct_caca_canvas._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_canvas(Structure):
    __slots__ = [
    ]
struct_caca_canvas._fields_ = [
    ('_opaque_struct', c_int)
]

caca_canvas_t = struct_caca_canvas 	# /usr/local/include/caca.h:46
class struct_caca_dither(Structure):
    __slots__ = [
    ]
struct_caca_dither._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_dither(Structure):
    __slots__ = [
    ]
struct_caca_dither._fields_ = [
    ('_opaque_struct', c_int)
]

caca_dither_t = struct_caca_dither 	# /usr/local/include/caca.h:48
class struct_caca_font(Structure):
    __slots__ = [
    ]
struct_caca_font._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_font(Structure):
    __slots__ = [
    ]
struct_caca_font._fields_ = [
    ('_opaque_struct', c_int)
]

caca_font_t = struct_caca_font 	# /usr/local/include/caca.h:50
class struct_caca_file(Structure):
    __slots__ = [
    ]
struct_caca_file._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_file(Structure):
    __slots__ = [
    ]
struct_caca_file._fields_ = [
    ('_opaque_struct', c_int)
]

caca_file_t = struct_caca_file 	# /usr/local/include/caca.h:52
class struct_caca_display(Structure):
    __slots__ = [
    ]
struct_caca_display._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_display(Structure):
    __slots__ = [
    ]
struct_caca_display._fields_ = [
    ('_opaque_struct', c_int)
]

caca_display_t = struct_caca_display 	# /usr/local/include/caca.h:54
class struct_caca_event(Structure):
    __slots__ = [
    ]
struct_caca_event._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_caca_event(Structure):
    __slots__ = [
    ]
struct_caca_event._fields_ = [
        ('_opaque_struct', c_int*9) # XXX: necessary because caca_event has a size of 36. if I don't set this, I will get errors with Py_Malloc.
]

caca_event_t = struct_caca_event 	# /usr/local/include/caca.h:56
CACA_BLACK = 0 	# /usr/local/include/caca.h:63
CACA_BLUE = 1 	# /usr/local/include/caca.h:64
CACA_GREEN = 2 	# /usr/local/include/caca.h:65
CACA_CYAN = 3 	# /usr/local/include/caca.h:66
CACA_RED = 4 	# /usr/local/include/caca.h:67
CACA_MAGENTA = 5 	# /usr/local/include/caca.h:68
CACA_BROWN = 6 	# /usr/local/include/caca.h:69
CACA_LIGHTGRAY = 7 	# /usr/local/include/caca.h:70
CACA_DARKGRAY = 8 	# /usr/local/include/caca.h:71
CACA_LIGHTBLUE = 9 	# /usr/local/include/caca.h:72
CACA_LIGHTGREEN = 10 	# /usr/local/include/caca.h:73
CACA_LIGHTCYAN = 11 	# /usr/local/include/caca.h:74
CACA_LIGHTRED = 12 	# /usr/local/include/caca.h:75
CACA_LIGHTMAGENTA = 13 	# /usr/local/include/caca.h:76
CACA_YELLOW = 14 	# /usr/local/include/caca.h:77
CACA_WHITE = 15 	# /usr/local/include/caca.h:78
CACA_DEFAULT = 16 	# /usr/local/include/caca.h:79
CACA_TRANSPARENT = 32 	# /usr/local/include/caca.h:80
CACA_BOLD = 1 	# /usr/local/include/caca.h:82
CACA_ITALICS = 2 	# /usr/local/include/caca.h:83
CACA_UNDERLINE = 4 	# /usr/local/include/caca.h:84
CACA_BLINK = 8 	# /usr/local/include/caca.h:85
# /usr/local/include/caca.h:203
caca_create_canvas = _lib.caca_create_canvas
caca_create_canvas.restype = POINTER(caca_canvas_t)
caca_create_canvas.argtypes = [c_int, c_int]

# /usr/local/include/caca.h:204
caca_manage_canvas = _lib.caca_manage_canvas
caca_manage_canvas.restype = c_int
caca_manage_canvas.argtypes = [POINTER(caca_canvas_t), CFUNCTYPE(c_int, POINTER(None)), POINTER(None)]

# /usr/local/include/caca.h:205
caca_unmanage_canvas = _lib.caca_unmanage_canvas
caca_unmanage_canvas.restype = c_int
caca_unmanage_canvas.argtypes = [POINTER(caca_canvas_t), CFUNCTYPE(c_int, POINTER(None)), POINTER(None)]

# /usr/local/include/caca.h:206
caca_set_canvas_size = _lib.caca_set_canvas_size
caca_set_canvas_size.restype = c_int
caca_set_canvas_size.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:207
caca_get_canvas_width = _lib.caca_get_canvas_width
caca_get_canvas_width.restype = c_int
caca_get_canvas_width.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:208
caca_get_canvas_height = _lib.caca_get_canvas_height
caca_get_canvas_height.restype = c_int
caca_get_canvas_height.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:209
caca_get_canvas_chars = _lib.caca_get_canvas_chars
caca_get_canvas_chars.restype = POINTER(c_uint8)
caca_get_canvas_chars.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:210
caca_get_canvas_attrs = _lib.caca_get_canvas_attrs
caca_get_canvas_attrs.restype = POINTER(c_uint8)
caca_get_canvas_attrs.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:211
caca_free_canvas = _lib.caca_free_canvas
caca_free_canvas.restype = c_int
caca_free_canvas.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:212
caca_rand = _lib.caca_rand
caca_rand.restype = c_int
caca_rand.argtypes = [c_int, c_int]

# /usr/local/include/caca.h:213
caca_get_version = _lib.caca_get_version
caca_get_version.restype = c_char_p
caca_get_version.argtypes = []

CACA_MAGIC_FULLWIDTH = 1048574 	# /usr/local/include/caca.h:222
# /usr/local/include/caca.h:223
caca_gotoxy = _lib.caca_gotoxy
caca_gotoxy.restype = c_int
caca_gotoxy.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:224
caca_get_cursor_x = _lib.caca_get_cursor_x
caca_get_cursor_x.restype = c_int
caca_get_cursor_x.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:225
caca_get_cursor_y = _lib.caca_get_cursor_y
caca_get_cursor_y.restype = c_int
caca_get_cursor_y.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:226
caca_put_char = _lib.caca_put_char
caca_put_char.restype = c_int
caca_put_char.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_uint32]

# /usr/local/include/caca.h:227
caca_get_char = _lib.caca_get_char
caca_get_char.restype = c_uint32
caca_get_char.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:228
caca_put_str = _lib.caca_put_str
caca_put_str.restype = c_int
caca_put_str.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_char_p]

# /usr/local/include/caca.h:229
caca_printf = _lib.caca_printf
caca_printf.restype = c_int
caca_printf.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_char_p]

# /usr/local/include/caca.h:230
caca_clear_canvas = _lib.caca_clear_canvas
caca_clear_canvas.restype = c_int
caca_clear_canvas.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:231
caca_set_canvas_handle = _lib.caca_set_canvas_handle
caca_set_canvas_handle.restype = c_int
caca_set_canvas_handle.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:232
caca_get_canvas_handle_x = _lib.caca_get_canvas_handle_x
caca_get_canvas_handle_x.restype = c_int
caca_get_canvas_handle_x.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:233
caca_get_canvas_handle_y = _lib.caca_get_canvas_handle_y
caca_get_canvas_handle_y.restype = c_int
caca_get_canvas_handle_y.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:234
caca_blit = _lib.caca_blit
caca_blit.restype = c_int
caca_blit.argtypes = [POINTER(caca_canvas_t), c_int, c_int, POINTER(caca_canvas_t), POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:236
caca_set_canvas_boundaries = _lib.caca_set_canvas_boundaries
caca_set_canvas_boundaries.restype = c_int
caca_set_canvas_boundaries.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:244
caca_invert = _lib.caca_invert
caca_invert.restype = c_int
caca_invert.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:245
caca_flip = _lib.caca_flip
caca_flip.restype = c_int
caca_flip.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:246
caca_flop = _lib.caca_flop
caca_flop.restype = c_int
caca_flop.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:247
caca_rotate_180 = _lib.caca_rotate_180
caca_rotate_180.restype = c_int
caca_rotate_180.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:248
caca_rotate_left = _lib.caca_rotate_left
caca_rotate_left.restype = c_int
caca_rotate_left.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:249
caca_rotate_right = _lib.caca_rotate_right
caca_rotate_right.restype = c_int
caca_rotate_right.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:250
caca_stretch_left = _lib.caca_stretch_left
caca_stretch_left.restype = c_int
caca_stretch_left.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:251
caca_stretch_right = _lib.caca_stretch_right
caca_stretch_right.restype = c_int
caca_stretch_right.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:259
caca_get_attr = _lib.caca_get_attr
caca_get_attr.restype = c_uint32
caca_get_attr.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:260
caca_set_attr = _lib.caca_set_attr
caca_set_attr.restype = c_int
caca_set_attr.argtypes = [POINTER(caca_canvas_t), c_uint32]

# /usr/local/include/caca.h:261
caca_put_attr = _lib.caca_put_attr
caca_put_attr.restype = c_int
caca_put_attr.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_uint32]

# /usr/local/include/caca.h:262
caca_set_color_ansi = _lib.caca_set_color_ansi
caca_set_color_ansi.restype = c_int
caca_set_color_ansi.argtypes = [POINTER(caca_canvas_t), c_uint8, c_uint8]

# /usr/local/include/caca.h:263
caca_set_color_argb = _lib.caca_set_color_argb
caca_set_color_argb.restype = c_int
caca_set_color_argb.argtypes = [POINTER(caca_canvas_t), c_uint16, c_uint16]

# /usr/local/include/caca.h:264
caca_attr_to_ansi = _lib.caca_attr_to_ansi
caca_attr_to_ansi.restype = c_uint8
caca_attr_to_ansi.argtypes = [c_uint32]

# /usr/local/include/caca.h:265
caca_attr_to_ansi_fg = _lib.caca_attr_to_ansi_fg
caca_attr_to_ansi_fg.restype = c_uint8
caca_attr_to_ansi_fg.argtypes = [c_uint32]

# /usr/local/include/caca.h:266
caca_attr_to_ansi_bg = _lib.caca_attr_to_ansi_bg
caca_attr_to_ansi_bg.restype = c_uint8
caca_attr_to_ansi_bg.argtypes = [c_uint32]

# /usr/local/include/caca.h:267
caca_attr_to_rgb12_fg = _lib.caca_attr_to_rgb12_fg
caca_attr_to_rgb12_fg.restype = c_uint16
caca_attr_to_rgb12_fg.argtypes = [c_uint32]

# /usr/local/include/caca.h:268
caca_attr_to_rgb12_bg = _lib.caca_attr_to_rgb12_bg
caca_attr_to_rgb12_bg.restype = c_uint16
caca_attr_to_rgb12_bg.argtypes = [c_uint32]

# /usr/local/include/caca.h:269
caca_attr_to_argb64 = _lib.caca_attr_to_argb64
caca_attr_to_argb64.restype = None
caca_attr_to_argb64.argtypes = [c_uint32, c_uint8 * 8]

# /usr/local/include/caca.h:277
caca_utf8_to_utf32 = _lib.caca_utf8_to_utf32
caca_utf8_to_utf32.restype = c_uint32
caca_utf8_to_utf32.argtypes = [c_char_p, POINTER(c_size_t)]

# /usr/local/include/caca.h:278
caca_utf32_to_utf8 = _lib.caca_utf32_to_utf8
caca_utf32_to_utf8.restype = c_size_t
caca_utf32_to_utf8.argtypes = [c_char_p, c_uint32]

# /usr/local/include/caca.h:279
caca_utf32_to_cp437 = _lib.caca_utf32_to_cp437
caca_utf32_to_cp437.restype = c_uint8
caca_utf32_to_cp437.argtypes = [c_uint32]

# /usr/local/include/caca.h:280
caca_cp437_to_utf32 = _lib.caca_cp437_to_utf32
caca_cp437_to_utf32.restype = c_uint32
caca_cp437_to_utf32.argtypes = [c_uint8]

# /usr/local/include/caca.h:281
caca_utf32_to_ascii = _lib.caca_utf32_to_ascii
caca_utf32_to_ascii.restype = c_char
caca_utf32_to_ascii.argtypes = [c_uint32]

# /usr/local/include/caca.h:282
caca_utf32_is_fullwidth = _lib.caca_utf32_is_fullwidth
caca_utf32_is_fullwidth.restype = c_int
caca_utf32_is_fullwidth.argtypes = [c_uint32]

# /usr/local/include/caca.h:291
caca_draw_line = _lib.caca_draw_line
caca_draw_line.restype = c_int
caca_draw_line.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:292
caca_draw_polyline = _lib.caca_draw_polyline
caca_draw_polyline.restype = c_int
caca_draw_polyline.argtypes = [POINTER(caca_canvas_t), POINTER(c_int), POINTER(c_int), c_int, c_uint32]

# /usr/local/include/caca.h:294
caca_draw_thin_line = _lib.caca_draw_thin_line
caca_draw_thin_line.restype = c_int
caca_draw_thin_line.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:295
caca_draw_thin_polyline = _lib.caca_draw_thin_polyline
caca_draw_thin_polyline.restype = c_int
caca_draw_thin_polyline.argtypes = [POINTER(caca_canvas_t), POINTER(c_int), POINTER(c_int), c_int]

# /usr/local/include/caca.h:298
caca_draw_circle = _lib.caca_draw_circle
caca_draw_circle.restype = c_int
caca_draw_circle.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:299
caca_draw_ellipse = _lib.caca_draw_ellipse
caca_draw_ellipse.restype = c_int
caca_draw_ellipse.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:300
caca_draw_thin_ellipse = _lib.caca_draw_thin_ellipse
caca_draw_thin_ellipse.restype = c_int
caca_draw_thin_ellipse.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:301
caca_fill_ellipse = _lib.caca_fill_ellipse
caca_fill_ellipse.restype = c_int
caca_fill_ellipse.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:303
caca_draw_box = _lib.caca_draw_box
caca_draw_box.restype = c_int
caca_draw_box.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:304
caca_draw_thin_box = _lib.caca_draw_thin_box
caca_draw_thin_box.restype = c_int
caca_draw_thin_box.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:305
caca_draw_cp437_box = _lib.caca_draw_cp437_box
caca_draw_cp437_box.restype = c_int
caca_draw_cp437_box.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:306
caca_fill_box = _lib.caca_fill_box
caca_fill_box.restype = c_int
caca_fill_box.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:308
caca_draw_triangle = _lib.caca_draw_triangle
caca_draw_triangle.restype = c_int
caca_draw_triangle.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:310
caca_draw_thin_triangle = _lib.caca_draw_thin_triangle
caca_draw_thin_triangle.restype = c_int
caca_draw_thin_triangle.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_int, c_int]

# /usr/local/include/caca.h:312
caca_fill_triangle = _lib.caca_fill_triangle
caca_fill_triangle.restype = c_int
caca_fill_triangle.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, c_int, c_int, c_uint32]

# /usr/local/include/caca.h:322
caca_get_frame_count = _lib.caca_get_frame_count
caca_get_frame_count.restype = c_int
caca_get_frame_count.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:323
caca_set_frame = _lib.caca_set_frame
caca_set_frame.restype = c_int
caca_set_frame.argtypes = [POINTER(caca_canvas_t), c_int]

# /usr/local/include/caca.h:324
caca_get_frame_name = _lib.caca_get_frame_name
caca_get_frame_name.restype = c_char_p
caca_get_frame_name.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:325
caca_set_frame_name = _lib.caca_set_frame_name
caca_set_frame_name.restype = c_int
caca_set_frame_name.argtypes = [POINTER(caca_canvas_t), c_char_p]

# /usr/local/include/caca.h:326
caca_create_frame = _lib.caca_create_frame
caca_create_frame.restype = c_int
caca_create_frame.argtypes = [POINTER(caca_canvas_t), c_int]

# /usr/local/include/caca.h:327
caca_free_frame = _lib.caca_free_frame
caca_free_frame.restype = c_int
caca_free_frame.argtypes = [POINTER(caca_canvas_t), c_int]

# /usr/local/include/caca.h:336
caca_create_dither = _lib.caca_create_dither
caca_create_dither.restype = POINTER(caca_dither_t)
caca_create_dither.argtypes = [c_int, c_int, c_int, c_int, c_uint32, c_uint32, c_uint32, c_uint32]

# /usr/local/include/caca.h:339
caca_set_dither_palette = _lib.caca_set_dither_palette
caca_set_dither_palette.restype = c_int
caca_set_dither_palette.argtypes = [POINTER(caca_dither_t), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]

# /usr/local/include/caca.h:342
caca_set_dither_brightness = _lib.caca_set_dither_brightness
caca_set_dither_brightness.restype = c_int
caca_set_dither_brightness.argtypes = [POINTER(caca_dither_t), c_float]

# /usr/local/include/caca.h:343
caca_get_dither_brightness = _lib.caca_get_dither_brightness
caca_get_dither_brightness.restype = c_float
caca_get_dither_brightness.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:344
caca_set_dither_gamma = _lib.caca_set_dither_gamma
caca_set_dither_gamma.restype = c_int
caca_set_dither_gamma.argtypes = [POINTER(caca_dither_t), c_float]

# /usr/local/include/caca.h:345
caca_get_dither_gamma = _lib.caca_get_dither_gamma
caca_get_dither_gamma.restype = c_float
caca_get_dither_gamma.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:346
caca_set_dither_contrast = _lib.caca_set_dither_contrast
caca_set_dither_contrast.restype = c_int
caca_set_dither_contrast.argtypes = [POINTER(caca_dither_t), c_float]

# /usr/local/include/caca.h:347
caca_get_dither_contrast = _lib.caca_get_dither_contrast
caca_get_dither_contrast.restype = c_float
caca_get_dither_contrast.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:348
caca_set_dither_antialias = _lib.caca_set_dither_antialias
caca_set_dither_antialias.restype = c_int
caca_set_dither_antialias.argtypes = [POINTER(caca_dither_t), c_char_p]

# /usr/local/include/caca.h:349
caca_get_dither_antialias_list = _lib.caca_get_dither_antialias_list
caca_get_dither_antialias_list.restype = POINTER(c_char_p)
caca_get_dither_antialias_list.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:351
caca_get_dither_antialias = _lib.caca_get_dither_antialias
caca_get_dither_antialias.restype = c_char_p
caca_get_dither_antialias.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:352
caca_set_dither_color = _lib.caca_set_dither_color
caca_set_dither_color.restype = c_int
caca_set_dither_color.argtypes = [POINTER(caca_dither_t), c_char_p]

# /usr/local/include/caca.h:353
caca_get_dither_color_list = _lib.caca_get_dither_color_list
caca_get_dither_color_list.restype = POINTER(c_char_p)
caca_get_dither_color_list.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:355
caca_get_dither_color = _lib.caca_get_dither_color
caca_get_dither_color.restype = c_char_p
caca_get_dither_color.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:356
caca_set_dither_charset = _lib.caca_set_dither_charset
caca_set_dither_charset.restype = c_int
caca_set_dither_charset.argtypes = [POINTER(caca_dither_t), c_char_p]

# /usr/local/include/caca.h:357
caca_get_dither_charset_list = _lib.caca_get_dither_charset_list
caca_get_dither_charset_list.restype = POINTER(c_char_p)
caca_get_dither_charset_list.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:359
caca_get_dither_charset = _lib.caca_get_dither_charset
caca_get_dither_charset.restype = c_char_p
caca_get_dither_charset.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:360
caca_set_dither_algorithm = _lib.caca_set_dither_algorithm
caca_set_dither_algorithm.restype = c_int
caca_set_dither_algorithm.argtypes = [POINTER(caca_dither_t), c_char_p]

# /usr/local/include/caca.h:361
caca_get_dither_algorithm_list = _lib.caca_get_dither_algorithm_list
caca_get_dither_algorithm_list.restype = POINTER(c_char_p)
caca_get_dither_algorithm_list.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:363
caca_get_dither_algorithm = _lib.caca_get_dither_algorithm
caca_get_dither_algorithm.restype = c_char_p
caca_get_dither_algorithm.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:364
caca_dither_bitmap = _lib.caca_dither_bitmap
caca_dither_bitmap.restype = c_int
caca_dither_bitmap.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_int, c_int, POINTER(caca_dither_t), POINTER(None)]

# /usr/local/include/caca.h:366
caca_free_dither = _lib.caca_free_dither
caca_free_dither.restype = c_int
caca_free_dither.argtypes = [POINTER(caca_dither_t)]

# /usr/local/include/caca.h:375
caca_load_font = _lib.caca_load_font
caca_load_font.restype = POINTER(caca_font_t)
caca_load_font.argtypes = [POINTER(None), c_size_t]

# /usr/local/include/caca.h:376
caca_get_font_list = _lib.caca_get_font_list
caca_get_font_list.restype = POINTER(c_char_p)
caca_get_font_list.argtypes = []

# /usr/local/include/caca.h:377
caca_get_font_width = _lib.caca_get_font_width
caca_get_font_width.restype = c_int
caca_get_font_width.argtypes = [POINTER(caca_font_t)]

# /usr/local/include/caca.h:378
caca_get_font_height = _lib.caca_get_font_height
caca_get_font_height.restype = c_int
caca_get_font_height.argtypes = [POINTER(caca_font_t)]

# /usr/local/include/caca.h:379
caca_get_font_blocks = _lib.caca_get_font_blocks
caca_get_font_blocks.restype = POINTER(c_uint32)
caca_get_font_blocks.argtypes = [POINTER(caca_font_t)]

# /usr/local/include/caca.h:380
caca_render_canvas = _lib.caca_render_canvas
caca_render_canvas.restype = c_int
caca_render_canvas.argtypes = [POINTER(caca_canvas_t), POINTER(caca_font_t), POINTER(None), c_int, c_int, c_int]

# /usr/local/include/caca.h:382
caca_free_font = _lib.caca_free_font
caca_free_font.restype = c_int
caca_free_font.argtypes = [POINTER(caca_font_t)]

# /usr/local/include/caca.h:390
caca_canvas_set_figfont = _lib.caca_canvas_set_figfont
caca_canvas_set_figfont.restype = c_int
caca_canvas_set_figfont.argtypes = [POINTER(caca_canvas_t), c_char_p]

# /usr/local/include/caca.h:391
caca_put_figchar = _lib.caca_put_figchar
caca_put_figchar.restype = c_int
caca_put_figchar.argtypes = [POINTER(caca_canvas_t), c_uint32]

# /usr/local/include/caca.h:392
caca_flush_figlet = _lib.caca_flush_figlet
caca_flush_figlet.restype = c_int
caca_flush_figlet.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:400
caca_file_open = _lib.caca_file_open
caca_file_open.restype = POINTER(caca_file_t)
caca_file_open.argtypes = [c_char_p, c_char_p]

# /usr/local/include/caca.h:401
caca_file_close = _lib.caca_file_close
caca_file_close.restype = c_int
caca_file_close.argtypes = [POINTER(caca_file_t)]

# /usr/local/include/caca.h:402
caca_file_tell = _lib.caca_file_tell
caca_file_tell.restype = c_uint64
caca_file_tell.argtypes = [POINTER(caca_file_t)]

# /usr/local/include/caca.h:403
caca_file_read = _lib.caca_file_read
caca_file_read.restype = c_size_t
caca_file_read.argtypes = [POINTER(caca_file_t), POINTER(None), c_size_t]

# /usr/local/include/caca.h:404
caca_file_write = _lib.caca_file_write
caca_file_write.restype = c_size_t
caca_file_write.argtypes = [POINTER(caca_file_t), POINTER(None), c_size_t]

# /usr/local/include/caca.h:405
caca_file_gets = _lib.caca_file_gets
caca_file_gets.restype = c_char_p
caca_file_gets.argtypes = [POINTER(caca_file_t), c_char_p, c_int]

# /usr/local/include/caca.h:406
caca_file_eof = _lib.caca_file_eof
caca_file_eof.restype = c_int
caca_file_eof.argtypes = [POINTER(caca_file_t)]

__ssize_t = c_int 	# /usr/include/bits/types.h:180
ssize_t = __ssize_t 	# /usr/include/unistd.h:191
# /usr/local/include/caca.h:416
caca_import_memory = _lib.caca_import_memory
caca_import_memory.restype = ssize_t
caca_import_memory.argtypes = [POINTER(caca_canvas_t), POINTER(None), c_size_t, c_char_p]

# /usr/local/include/caca.h:418
caca_import_file = _lib.caca_import_file
caca_import_file.restype = ssize_t
caca_import_file.argtypes = [POINTER(caca_canvas_t), c_char_p, c_char_p]

# /usr/local/include/caca.h:420
caca_get_import_list = _lib.caca_get_import_list
caca_get_import_list.restype = POINTER(c_char_p)
caca_get_import_list.argtypes = []

# /usr/local/include/caca.h:421
caca_export_memory = _lib.caca_export_memory
caca_export_memory.restype = POINTER(c_void)
caca_export_memory.argtypes = [POINTER(caca_canvas_t), c_char_p, POINTER(c_size_t)]

# /usr/local/include/caca.h:423
caca_get_export_list = _lib.caca_get_export_list
caca_get_export_list.restype = POINTER(c_char_p)
caca_get_export_list.argtypes = []

# /usr/local/include/caca.h:432
caca_create_display = _lib.caca_create_display
caca_create_display.restype = POINTER(caca_display_t)
caca_create_display.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:433
caca_create_display_with_driver = _lib.caca_create_display_with_driver
caca_create_display_with_driver.restype = POINTER(caca_display_t)
caca_create_display_with_driver.argtypes = [POINTER(caca_canvas_t), c_char_p]

# /usr/local/include/caca.h:435
caca_get_display_driver_list = _lib.caca_get_display_driver_list
caca_get_display_driver_list.restype = POINTER(c_char_p)
caca_get_display_driver_list.argtypes = []

# /usr/local/include/caca.h:436
caca_get_display_driver = _lib.caca_get_display_driver
caca_get_display_driver.restype = c_char_p
caca_get_display_driver.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:437
caca_set_display_driver = _lib.caca_set_display_driver
caca_set_display_driver.restype = c_int
caca_set_display_driver.argtypes = [POINTER(caca_display_t), c_char_p]

# /usr/local/include/caca.h:438
caca_free_display = _lib.caca_free_display
caca_free_display.restype = c_int
caca_free_display.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:439
caca_get_canvas = _lib.caca_get_canvas
caca_get_canvas.restype = POINTER(caca_canvas_t)
caca_get_canvas.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:440
caca_refresh_display = _lib.caca_refresh_display
caca_refresh_display.restype = c_int
caca_refresh_display.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:441
caca_set_display_time = _lib.caca_set_display_time
caca_set_display_time.restype = c_int
caca_set_display_time.argtypes = [POINTER(caca_display_t), c_int]

# /usr/local/include/caca.h:442
caca_get_display_time = _lib.caca_get_display_time
caca_get_display_time.restype = c_int
caca_get_display_time.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:443
caca_get_display_width = _lib.caca_get_display_width
caca_get_display_width.restype = c_int
caca_get_display_width.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:444
caca_get_display_height = _lib.caca_get_display_height
caca_get_display_height.restype = c_int
caca_get_display_height.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:445
caca_set_display_title = _lib.caca_set_display_title
caca_set_display_title.restype = c_int
caca_set_display_title.argtypes = [POINTER(caca_display_t), c_char_p]

# /usr/local/include/caca.h:446
caca_set_mouse = _lib.caca_set_mouse
caca_set_mouse.restype = c_int
caca_set_mouse.argtypes = [POINTER(caca_display_t), c_int]

# /usr/local/include/caca.h:447
caca_set_cursor = _lib.caca_set_cursor
caca_set_cursor.restype = c_int
caca_set_cursor.argtypes = [POINTER(caca_display_t), c_int]

# /usr/local/include/caca.h:456
caca_get_event = _lib.caca_get_event
caca_get_event.restype = c_int
caca_get_event.argtypes = [POINTER(caca_display_t), c_int, POINTER(caca_event_t), c_int]

# /usr/local/include/caca.h:457
caca_get_mouse_x = _lib.caca_get_mouse_x
caca_get_mouse_x.restype = c_int
caca_get_mouse_x.argtypes = [POINTER(caca_display_t)]

# /usr/local/include/caca.h:458
caca_get_mouse_y = _lib.caca_get_mouse_y
caca_get_mouse_y.restype = c_int
caca_get_mouse_y.argtypes = [POINTER(caca_display_t)]

enum_caca_event_type = c_int
# /usr/local/include/caca.h:459
caca_get_event_type = _lib.caca_get_event_type
caca_get_event_type.restype = enum_caca_event_type
caca_get_event_type.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:460
caca_get_event_key_ch = _lib.caca_get_event_key_ch
caca_get_event_key_ch.restype = c_int
caca_get_event_key_ch.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:461
caca_get_event_key_utf32 = _lib.caca_get_event_key_utf32
caca_get_event_key_utf32.restype = c_uint32
caca_get_event_key_utf32.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:462
caca_get_event_key_utf8 = _lib.caca_get_event_key_utf8
caca_get_event_key_utf8.restype = c_int
caca_get_event_key_utf8.argtypes = [POINTER(caca_event_t), c_char_p]

# /usr/local/include/caca.h:463
caca_get_event_mouse_button = _lib.caca_get_event_mouse_button
caca_get_event_mouse_button.restype = c_int
caca_get_event_mouse_button.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:464
caca_get_event_mouse_x = _lib.caca_get_event_mouse_x
caca_get_event_mouse_x.restype = c_int
caca_get_event_mouse_x.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:465
caca_get_event_mouse_y = _lib.caca_get_event_mouse_y
caca_get_event_mouse_y.restype = c_int
caca_get_event_mouse_y.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:466
caca_get_event_resize_width = _lib.caca_get_event_resize_width
caca_get_event_resize_width.restype = c_int
caca_get_event_resize_width.argtypes = [POINTER(caca_event_t)]

# /usr/local/include/caca.h:467
caca_get_event_resize_height = _lib.caca_get_event_resize_height
caca_get_event_resize_height.restype = c_int
caca_get_event_resize_height.argtypes = [POINTER(caca_event_t)]

class struct_cucul_buffer(Structure):
    __slots__ = [
    ]
struct_cucul_buffer._fields_ = [
    ('_opaque_struct', c_int)
]

class struct_cucul_buffer(Structure):
    __slots__ = [
    ]
struct_cucul_buffer._fields_ = [
    ('_opaque_struct', c_int)
]

cucul_buffer_t = struct_cucul_buffer 	# /usr/local/include/caca.h:472
# /usr/local/include/caca.h:484
cucul_putchar = _lib.cucul_putchar
cucul_putchar.restype = c_int
cucul_putchar.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_ulong]

# /usr/local/include/caca.h:486
cucul_getchar = _lib.cucul_getchar
cucul_getchar.restype = c_ulong
cucul_getchar.argtypes = [POINTER(caca_canvas_t), c_int, c_int]

# /usr/local/include/caca.h:488
cucul_putstr = _lib.cucul_putstr
cucul_putstr.restype = c_int
cucul_putstr.argtypes = [POINTER(caca_canvas_t), c_int, c_int, c_char_p]

# /usr/local/include/caca.h:490
cucul_set_color = _lib.cucul_set_color
cucul_set_color.restype = c_int
cucul_set_color.argtypes = [POINTER(caca_canvas_t), c_ubyte, c_ubyte]

# /usr/local/include/caca.h:492
cucul_set_truecolor = _lib.cucul_set_truecolor
cucul_set_truecolor.restype = c_int
cucul_set_truecolor.argtypes = [POINTER(caca_canvas_t), c_uint, c_uint]

# /usr/local/include/caca.h:494
cucul_get_canvas_frame_count = _lib.cucul_get_canvas_frame_count
cucul_get_canvas_frame_count.restype = c_uint
cucul_get_canvas_frame_count.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:496
cucul_set_canvas_frame = _lib.cucul_set_canvas_frame
cucul_set_canvas_frame.restype = c_int
cucul_set_canvas_frame.argtypes = [POINTER(caca_canvas_t), c_uint]

# /usr/local/include/caca.h:498
cucul_create_canvas_frame = _lib.cucul_create_canvas_frame
cucul_create_canvas_frame.restype = c_int
cucul_create_canvas_frame.argtypes = [POINTER(caca_canvas_t), c_uint]

# /usr/local/include/caca.h:500
cucul_free_canvas_frame = _lib.cucul_free_canvas_frame
cucul_free_canvas_frame.restype = c_int
cucul_free_canvas_frame.argtypes = [POINTER(caca_canvas_t), c_uint]

# /usr/local/include/caca.h:502
cucul_load_memory = _lib.cucul_load_memory
cucul_load_memory.restype = POINTER(cucul_buffer_t)
cucul_load_memory.argtypes = [POINTER(None), c_ulong]

# /usr/local/include/caca.h:504
cucul_load_file = _lib.cucul_load_file
cucul_load_file.restype = POINTER(cucul_buffer_t)
cucul_load_file.argtypes = [c_char_p]

# /usr/local/include/caca.h:505
cucul_get_buffer_size = _lib.cucul_get_buffer_size
cucul_get_buffer_size.restype = c_ulong
cucul_get_buffer_size.argtypes = [POINTER(cucul_buffer_t)]

# /usr/local/include/caca.h:507
cucul_get_buffer_data = _lib.cucul_get_buffer_data
cucul_get_buffer_data.restype = POINTER(c_void)
cucul_get_buffer_data.argtypes = [POINTER(cucul_buffer_t)]

# /usr/local/include/caca.h:508
cucul_free_buffer = _lib.cucul_free_buffer
cucul_free_buffer.restype = c_int
cucul_free_buffer.argtypes = [POINTER(cucul_buffer_t)]

# /usr/local/include/caca.h:509
cucul_export_canvas = _lib.cucul_export_canvas
cucul_export_canvas.restype = POINTER(cucul_buffer_t)
cucul_export_canvas.argtypes = [POINTER(caca_canvas_t), c_char_p]

# /usr/local/include/caca.h:511
cucul_import_canvas = _lib.cucul_import_canvas
cucul_import_canvas.restype = POINTER(caca_canvas_t)
cucul_import_canvas.argtypes = [POINTER(cucul_buffer_t), c_char_p]

# /usr/local/include/caca.h:513
cucul_rotate = _lib.cucul_rotate
cucul_rotate.restype = c_int
cucul_rotate.argtypes = [POINTER(caca_canvas_t)]

# /usr/local/include/caca.h:514
cucul_set_dither_invert = _lib.cucul_set_dither_invert
cucul_set_dither_invert.restype = c_int
cucul_set_dither_invert.argtypes = [POINTER(caca_dither_t), c_int]

# /usr/local/include/caca.h:515
cucul_set_dither_mode = _lib.cucul_set_dither_mode
cucul_set_dither_mode.restype = c_int
cucul_set_dither_mode.argtypes = [POINTER(caca_dither_t), c_char_p]

# /usr/local/include/caca.h:517
cucul_get_dither_mode_list = _lib.cucul_get_dither_mode_list
cucul_get_dither_mode_list.restype = POINTER(c_char_p)
cucul_get_dither_mode_list.argtypes = [POINTER(caca_dither_t)]

CUCUL_COLOR_BLACK = 0 	# /usr/local/include/caca.h:519
CUCUL_COLOR_BLUE = 1 	# /usr/local/include/caca.h:520
CUCUL_COLOR_GREEN = 2 	# /usr/local/include/caca.h:521
CUCUL_COLOR_CYAN = 3 	# /usr/local/include/caca.h:522
CUCUL_COLOR_RED = 4 	# /usr/local/include/caca.h:523
CUCUL_COLOR_MAGENTA = 5 	# /usr/local/include/caca.h:524
CUCUL_COLOR_BROWN = 6 	# /usr/local/include/caca.h:525
CUCUL_COLOR_LIGHTGRAY = 7 	# /usr/local/include/caca.h:526
CUCUL_COLOR_DARKGRAY = 8 	# /usr/local/include/caca.h:527
CUCUL_COLOR_LIGHTBLUE = 9 	# /usr/local/include/caca.h:528
CUCUL_COLOR_LIGHTGREEN = 10 	# /usr/local/include/caca.h:529
CUCUL_COLOR_LIGHTCYAN = 11 	# /usr/local/include/caca.h:530
CUCUL_COLOR_LIGHTRED = 12 	# /usr/local/include/caca.h:531
CUCUL_COLOR_LIGHTMAGENTA = 13 	# /usr/local/include/caca.h:532
CUCUL_COLOR_YELLOW = 14 	# /usr/local/include/caca.h:533
CUCUL_COLOR_WHITE = 14 	# /usr/local/include/caca.h:534
CUCUL_COLOR_DEFAULT = 16 	# /usr/local/include/caca.h:535
CUCUL_COLOR_TRANSPARENT = 32 	# /usr/local/include/caca.h:536
CUCUL_BLACK = 0 	# /usr/local/include/caca.h:546
CUCUL_BLUE = 1 	# /usr/local/include/caca.h:547
CUCUL_GREEN = 2 	# /usr/local/include/caca.h:548
CUCUL_CYAN = 3 	# /usr/local/include/caca.h:549
CUCUL_RED = 4 	# /usr/local/include/caca.h:550
CUCUL_MAGENTA = 5 	# /usr/local/include/caca.h:551
CUCUL_BROWN = 6 	# /usr/local/include/caca.h:552
CUCUL_LIGHTGRAY = 7 	# /usr/local/include/caca.h:553
CUCUL_DARKGRAY = 8 	# /usr/local/include/caca.h:554
CUCUL_LIGHTBLUE = 9 	# /usr/local/include/caca.h:555
CUCUL_LIGHTGREEN = 10 	# /usr/local/include/caca.h:556
CUCUL_LIGHTCYAN = 11 	# /usr/local/include/caca.h:557
CUCUL_LIGHTRED = 12 	# /usr/local/include/caca.h:558
CUCUL_LIGHTMAGENTA = 13 	# /usr/local/include/caca.h:559
CUCUL_YELLOW = 14 	# /usr/local/include/caca.h:560
CUCUL_WHITE = 14 	# /usr/local/include/caca.h:561
CUCUL_DEFAULT = 16 	# /usr/local/include/caca.h:562
CUCUL_TRANSPARENT = 32 	# /usr/local/include/caca.h:563
CUCUL_BOLD = 1 	# /usr/local/include/caca.h:565
CUCUL_ITALICS = 2 	# /usr/local/include/caca.h:566
CUCUL_UNDERLINE = 4 	# /usr/local/include/caca.h:567
CUCUL_BLINK = 8 	# /usr/local/include/caca.h:568

__all__ = ['caca_canvas_t', 'caca_dither_t', 'caca_font_t', 'caca_file_t',
'caca_display_t', 'caca_event_t', 'CACA_BLACK', 'CACA_BLUE', 'CACA_GREEN',
'CACA_CYAN', 'CACA_RED', 'CACA_MAGENTA', 'CACA_BROWN', 'CACA_LIGHTGRAY',
'CACA_DARKGRAY', 'CACA_LIGHTBLUE', 'CACA_LIGHTGREEN', 'CACA_LIGHTCYAN',
'CACA_LIGHTRED', 'CACA_LIGHTMAGENTA', 'CACA_YELLOW', 'CACA_WHITE',
'CACA_DEFAULT', 'CACA_TRANSPARENT', 'CACA_BOLD', 'CACA_ITALICS',
'CACA_UNDERLINE', 'CACA_BLINK', 'caca_create_canvas', 'caca_manage_canvas',
'caca_unmanage_canvas', 'caca_set_canvas_size', 'caca_get_canvas_width',
'caca_get_canvas_height', 'caca_get_canvas_chars', 'caca_get_canvas_attrs',
'caca_free_canvas', 'caca_rand', 'caca_get_version', 'CACA_MAGIC_FULLWIDTH',
'caca_gotoxy', 'caca_get_cursor_x', 'caca_get_cursor_y', 'caca_put_char',
'caca_get_char', 'caca_put_str', 'caca_printf', 'caca_clear_canvas',
'caca_set_canvas_handle', 'caca_get_canvas_handle_x',
'caca_get_canvas_handle_y', 'caca_blit', 'caca_set_canvas_boundaries',
'caca_invert', 'caca_flip', 'caca_flop', 'caca_rotate_180',
'caca_rotate_left', 'caca_rotate_right', 'caca_stretch_left',
'caca_stretch_right', 'caca_get_attr', 'caca_set_attr', 'caca_put_attr',
'caca_set_color_ansi', 'caca_set_color_argb', 'caca_attr_to_ansi',
'caca_attr_to_ansi_fg', 'caca_attr_to_ansi_bg', 'caca_attr_to_rgb12_fg',
'caca_attr_to_rgb12_bg', 'caca_attr_to_argb64', 'caca_utf8_to_utf32',
'caca_utf32_to_utf8', 'caca_utf32_to_cp437', 'caca_cp437_to_utf32',
'caca_utf32_to_ascii', 'caca_utf32_is_fullwidth', 'caca_draw_line',
'caca_draw_polyline', 'caca_draw_thin_line', 'caca_draw_thin_polyline',
'caca_draw_circle', 'caca_draw_ellipse', 'caca_draw_thin_ellipse',
'caca_fill_ellipse', 'caca_draw_box', 'caca_draw_thin_box',
'caca_draw_cp437_box', 'caca_fill_box', 'caca_draw_triangle',
'caca_draw_thin_triangle', 'caca_fill_triangle', 'caca_get_frame_count',
'caca_set_frame', 'caca_get_frame_name', 'caca_set_frame_name',
'caca_create_frame', 'caca_free_frame', 'caca_create_dither',
'caca_set_dither_palette', 'caca_set_dither_brightness',
'caca_get_dither_brightness', 'caca_set_dither_gamma',
'caca_get_dither_gamma', 'caca_set_dither_contrast',
'caca_get_dither_contrast', 'caca_set_dither_antialias',
'caca_get_dither_antialias_list', 'caca_get_dither_antialias',
'caca_set_dither_color', 'caca_get_dither_color_list',
'caca_get_dither_color', 'caca_set_dither_charset',
'caca_get_dither_charset_list', 'caca_get_dither_charset',
'caca_set_dither_algorithm', 'caca_get_dither_algorithm_list',
'caca_get_dither_algorithm', 'caca_dither_bitmap', 'caca_free_dither',
'caca_load_font', 'caca_get_font_list', 'caca_get_font_width',
'caca_get_font_height', 'caca_get_font_blocks', 'caca_render_canvas',
'caca_free_font', 'caca_canvas_set_figfont', 'caca_put_figchar',
'caca_flush_figlet', 'caca_file_open', 'caca_file_close', 'caca_file_tell',
'caca_file_read', 'caca_file_write', 'caca_file_gets', 'caca_file_eof',
'caca_import_memory', 'caca_import_file', 'caca_get_import_list',
'caca_export_memory', 'caca_get_export_list', 'caca_create_display',
'caca_create_display_with_driver', 'caca_get_display_driver_list',
'caca_get_display_driver', 'caca_set_display_driver', 'caca_free_display',
'caca_get_canvas', 'caca_refresh_display', 'caca_set_display_time',
'caca_get_display_time', 'caca_get_display_width', 'caca_get_display_height',
'caca_set_display_title', 'caca_set_mouse', 'caca_set_cursor',
'caca_get_event', 'caca_get_mouse_x', 'caca_get_mouse_y',
'caca_get_event_type', 'caca_get_event_key_ch', 'caca_get_event_key_utf32',
'caca_get_event_key_utf8', 'caca_get_event_mouse_button',
'caca_get_event_mouse_x', 'caca_get_event_mouse_y',
'caca_get_event_resize_width', 'caca_get_event_resize_height',
'cucul_buffer_t', 'cucul_putchar', 'cucul_getchar', 'cucul_putstr',
'cucul_set_color', 'cucul_set_truecolor', 'cucul_get_canvas_frame_count',
'cucul_set_canvas_frame', 'cucul_create_canvas_frame',
'cucul_free_canvas_frame', 'cucul_load_memory', 'cucul_load_file',
'cucul_get_buffer_size', 'cucul_get_buffer_data', 'cucul_free_buffer',
'cucul_export_canvas', 'cucul_import_canvas', 'cucul_rotate',
'cucul_set_dither_invert', 'cucul_set_dither_mode',
'cucul_get_dither_mode_list', 'CUCUL_COLOR_BLACK', 'CUCUL_COLOR_BLUE',
'CUCUL_COLOR_GREEN', 'CUCUL_COLOR_CYAN', 'CUCUL_COLOR_RED',
'CUCUL_COLOR_MAGENTA', 'CUCUL_COLOR_BROWN', 'CUCUL_COLOR_LIGHTGRAY',
'CUCUL_COLOR_DARKGRAY', 'CUCUL_COLOR_LIGHTBLUE', 'CUCUL_COLOR_LIGHTGREEN',
'CUCUL_COLOR_LIGHTCYAN', 'CUCUL_COLOR_LIGHTRED', 'CUCUL_COLOR_LIGHTMAGENTA',
'CUCUL_COLOR_YELLOW', 'CUCUL_COLOR_WHITE', 'CUCUL_COLOR_DEFAULT',
'CUCUL_COLOR_TRANSPARENT', 'CUCUL_BLACK', 'CUCUL_BLUE', 'CUCUL_GREEN',
'CUCUL_CYAN', 'CUCUL_RED', 'CUCUL_MAGENTA', 'CUCUL_BROWN', 'CUCUL_LIGHTGRAY',
'CUCUL_DARKGRAY', 'CUCUL_LIGHTBLUE', 'CUCUL_LIGHTGREEN', 'CUCUL_LIGHTCYAN',
'CUCUL_LIGHTRED', 'CUCUL_LIGHTMAGENTA', 'CUCUL_YELLOW', 'CUCUL_WHITE',
'CUCUL_DEFAULT', 'CUCUL_TRANSPARENT', 'CUCUL_BOLD', 'CUCUL_ITALICS',
'CUCUL_UNDERLINE', 'CUCUL_BLINK']
