import random
import sys
import time
import numpy as np
from pykeyboard import PyKeyboard

# Load OS-specific libraries
LINUX = 'linux'
WINDOWS = 'win32'
if sys.platform == LINUX:
    pass
elif sys.platform == WINDOWS:
    import win32gui
    import re
print("whatever")

def generate_settings(n_settings=3, file_name=None):

    file = open(file_name, 'w')
    for i in range(n_settings):
        Mat = np.random.randint(0, 41)  #choose between 40 materials.
        HDRI = np.random.randint(0, 30) #choose between 29 HDRI maps.
        Lighting = np.random.randint(0, 6) #choose Lighting position
        ToteBox = np.random.randint(0,2) #totebox or no totebox
        file.write(','.join([str(Mat), str(HDRI), str(Lighting), str(ToteBox)]))
        file.write('\n')
    file.close()

class Probe:
    def __init__(self):
        self.k = PyKeyboard()

    def press(self, key):
        self.k.press_key(key)
        time.sleep(0.5)
        self.k.release_key(key)

    def screenshot(self):
        self.press('c')

    def reset(self):
        self.press('q')

    def outline(self):
        self.press('o')

    def no_caustic(self):
        self.press('e')

    def global_gt(self):
        self.press('g')

    def depth(self):
        self.press('t')

    def surface_normal(self):                        
        self.press('r')

    def rtx(self):
        self.press('d')

    def capture(self):
        
        self.rtx()
        time.sleep(0.1)
        self.screenshot()


        self.no_caustic()
        time.sleep(0.05)
        self.screenshot()
        self.rtx()

        self.depth()  # depth
        time.sleep(0.05)
        self.screenshot()
        self.depth()

        self.surface_normal()
        time.sleep(0.05)
        self.screenshot()
        self.surface_normal()

        self.outline()
        time.sleep(0.05)
        self.screenshot()
        self.outline()

        self.global_gt()  # global gt
        time.sleep(0.05)
        self.screenshot()       
        self.global_gt()




class WindowMgr:
    # Obtained from https://stackoverflow.com/a/2091530

    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)


class KeyUtils:

    def __init__(self):
        self.k = PyKeyboard()

    def alt_tab(self):
        self.k.press_key(self.k.alt_key)
        self.k.tap_key(self.k.tab_key)
        self.k.release_key(self.k.alt_key)

    # Send a keystroke with a lag
    def move(self, key, lag=1.5):
        self.k.press_key(key)
        # We need to pause, otherwise the game will not register the keypress
        time.sleep(lag)
        self.k.release_key(key)

    def press(self, key):
        self.k.press_key(key)
        time.sleep(0.1)
        self.k.release_key(key)

    def read_look(self, filename):
        with open(filename) as f:
            for mi in f.readlines():
                yield mi.split(',')

    def read_move(self, filename):
        with open(filename) as f:
            for line in f.readline():
                yield int(line)


MK = {}
MK['LOOK_UP'] = [5]
MK['LOOK_DOWN'] = [6]
MK['LOOK_RIGHT'] = [7, 8, 9, 10]
MK['LOOK_LEFT'] = [4]
MK['TURN_AROUND'] = [11]
