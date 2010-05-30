# pulled from http://www.bitbucket.org/mu_mind/pycaca, r11:b97c9bd8e08a

class Colors:
    BLACK = 0x00
    BLUE = 0x01
    GREEN = 0x02
    CYAN = 0x03
    RED = 0x04
    MAGENTA = 0x05
    BROWN = 0x06
    LIGHTGRAY = 0x07
    DARKGRAY = 0x08
    LIGHTBLUE = 0x09
    LIGHTGREEN = 0x0a
    LIGHTCYAN = 0x0b
    LIGHTRED = 0x0c
    LIGHTMAGENTA = 0x0d
    YELLOW = 0x0e
    WHITE = 0x0f
    DEFAULT = 0x10
    TRANSPARENT = 0x20
    BOLD = 0x01
    ITALICS = 0x02
    UNDERLINE = 0x04
    BLINK = 0x08
    MAGIC_FULLWIDTH = 0x000ffffe

class Events:
    NONE = 0x0000
    KEY_PRESS = 0x0001
    KEY_RELEASE =   0x0002
    MOUSE_PRESS =   0x0004
    MOUSE_RELEASE = 0x0008
    MOUSE_MOTION =  0x0010
    RESIZE =        0x0020
    QUIT =          0x0040
    ANY =           0xffff

class Keys:
    UNKNOWN = 0x00

    CTRL_A =    0x01
    CTRL_B =    0x02
    CTRL_C =    0x03
    CTRL_D =    0x04
    CTRL_E =    0x05
    CTRL_F =    0x06
    CTRL_G =    0x07
    BACKSPACE = 0x08
    TAB =       0x09
    CTRL_J =    0x0a
    CTRL_K =    0x0b
    CTRL_L =    0x0c
    RETURN =    0x0d
    CTRL_N =    0x0e
    CTRL_O =    0x0f
    CTRL_P =    0x10
    CTRL_Q =    0x11
    CTRL_R =    0x12
    PAUSE =     0x13
    CTRL_T =    0x14
    CTRL_U =    0x15
    CTRL_V =    0x16
    CTRL_W =    0x17
    CTRL_X =    0x18
    CTRL_Y =    0x19
    CTRL_Z =    0x1a
    ESCAPE =    0x1b
    DELETE =    0x7f

    UP =    0x111
    DOWN =  0x112
    LEFT =  0x113
    RIGHT = 0x114

    INSERT =   0x115
    HOME =     0x116
    END =      0x117
    PAGEUP =   0x118
    PAGEDOWN = 0x119

    F1 =  0x11a
    F2 =  0x11b
    F3 =  0x11c
    F4 =  0x11d
    F5 =  0x11e
    F6 =  0x11f
    F7 =  0x120
    F8 =  0x121
    F9 =  0x122
    F10 = 0x123
    F11 = 0x124
    F12 = 0x125
    F13 = 0x126
    F14 = 0x127
    F15 = 0x128
