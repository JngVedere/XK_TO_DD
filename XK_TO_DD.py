# // Library for setting default value
from collections import defaultdict
# from X11 keycode to DD keycode
# X11 keycode used for tkinter
# DD keycode used for classDD dll

# // Supports only for most basic keys
# // Designated to Korean Keyboard

XK_TO_DD = {'27':100, #ESCAPE 
            '112':101, #F1 
            '113':102, #F2 
            '114':103, #F3 
            '115':104, #F4 
            '116':105, #F5
            '117':106, #F6 
            '118':107, #F7 
            '119':108, #F8 
            '120':109, #F9 
            '121':110, #F10 
            '122':111, #F11 
            '123':112, #F12 
            '192':200, #GRAVE 
            '49':201, #TOP ROW '1' 
            '50':202, #TOP ROW '2' 
            '51':203, #TOP ROW '3' 
            '52':204, #TOP ROW '4'
            '53':205, #TOP ROW '5' 
            '54':206, #TOP ROW '6' 
            '55':207, #TOP ROW '7' 
            '56':208, #TOP ROW '8' 
            '57':209, #TOP ROW '9' 
            '48':210, #TOP ROW '0' 
            '189':211, #MINUS
            '187':212, #EQUAL
            '220':213, #BACKSLASH
            '8':214, #BACKSPACE
            '9':300, #TAB
            '81':301,#Q
            '87':302,#W
            '69':303,#E
            '82':304,#R
            '84':305,#T
            '89':306,#Y
            '85':307,#U
            '73':308,#I
            '79':309,#O
            '80':310,#P
            '219':311,#[
            '221':312,#]
            '13':313,#RETURN
            '20':400,#CAPLCK
            '65':401,#A
            '83':402,#S
            '68':403,#D
            '70':404,#F
            '71':405,#G
            '72':406,#H
            '74':407,#J
            '75':408,#K
            '76':409,#L
            '186':410,#SEMI-COLON & COLON
            '222':411,#APOSTROPHE
            '16':500,#SHIFT_LOCK
            '50':500,#SHIFT_LEFT
            '90':501,#Z
            '88':502,#X
            '67':503,#C
            '86':504,#V
            '66':505,#B
            '78':506,#N
            '77':507,#M
            '188':508,#COMMA
            '190':509,#PERIOD
            '191':510,#SLASH
            '62':511,#SHIFT_LEFT
            '17':600,#CTRL-L
            '91':601,#WIN-L
            '64':602,#ALT-L     !!PLATFORM_DEPENDING VALUE
            '108':602,#ALT-L     !!PLATFORM_DEPENDING VALUE
            '32':603,#SPACE BAR
            '108':604,#ALT-R
            '92':605,#WIN-R
            '93':606,#MENU
            '19':607,#CTRL-R     !!PLATFORM_DEPENDING VALUE
            '44':700,#PRTSCR
            '145':701,#SCRLCK
            '19':702,#PAUBRK
            '45':703,#INS
            '36':704,#HOME
            '33':705,#PGUP(PRIOR)
            '46':706,#DEL
            '35':707,#END
            '34':708,#PGDN(NEXT)
            '38':709,#UP ARROW
            '37':710,#LEFT ARROW
            '40':711,#DOWN ARROW
            '39':712,#RIGHT ARROW
            '96':800,#NUMPAD 0
            '97':801,#NUMPAD 1
            '98':802,#NUMPAD 2
            '99':803,#NUMPAD 3
            '100':804,#NUMPAD 4
            '101':805,#NUMPAD 5
            '102':806,#NUMPAD 6
            '103':807,#NUMPAD 7
            '104':808,#NUMPAD 8
            '105':809,#NUMPAD 9
            '144':810,#NUMLCK
            '111':811,#NUMPAD SLASH
            '106':812,#ASTERISK
            '109':813,#NUMPAD MINUS
            '107':814,#NUMPAD PLUS
            '36':815,#NUMPAD RETURN
            '110':816,#NUMPAD DOT

            # From here, special exception
            '12':805, #CLEAR
            '18':602,#UNEXPECTED ALT-L
            '25':607, #UNEXPECTED CTRL-R
            '229':604,#UNEXPECTED ALT-R
            '65317':604, #Korean Keyboard 'Han/Yeong' key
            '65329':605 #Korean Keyboard 'Hanja' key
            }

#DEFAULT VALUE IS 'SPACE BAR'
XK_TO_DD = defaultdict(lambda:603, XK_TO_DD)
