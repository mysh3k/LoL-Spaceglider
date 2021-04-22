import time
import requests
import ctypes
import keyboard
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
SendInput = ctypes.windll.user32.SendInput


PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]



def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



def getAS():
    req = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify=False)
    data = req.json()
    attackSpeed = data['activePlayer']['championStats']['attackSpeed']
    return attackSpeed

def ow():
    sleeper = 1 * (1/getAS()/2)
    PressKey(0x1E)
    ReleaseKey(0x1E)
    time.sleep(sleeper)
    PressKey(0x1F)
    ReleaseKey(0x1F)
    time.sleep(sleeper)

def kalista():
    sleeper = 1 * (1/getAS())
    PressKey(0x1E)
    ReleaseKey(0x1E)
    time.sleep(sleeper/2)
    PressKey(0x1E)
    ReleaseKey(0x1E)
    time.sleep(sleeper / 2)

# while True:
#     if keyboard.is_pressed('SPACE'):  # if key 'Space' is pressed
#         hold = True
#     else:
#         hold = False
#
#     if hold == True:
#         ow()

while True:
    if keyboard.is_pressed('SPACE'):
        ow()