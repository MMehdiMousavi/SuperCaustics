##############################################################################
# IMPORTS, FLAGS, AND FOLDERS
##############################################################################
import os
import sys
import time
from pykeyboard import PyKeyboard
from Probe_utils import MK, Probe, WindowMgr, KeyUtils, generate_settings

LINUX = 'linux'
WINDOWS = 'win32'

# Switch focus to the game window             
if sys.platform == LINUX:
    # In Linux, we can shift focus to a window by using the wmctrl program

    gameName = "Loft (64-bit, PCD3D_SM5)"
    os.system('wmctrl -a ' + gameName)
elif sys.platform == WINDOWS:
    # In Windows, we can use the class defined above
    w = WindowMgr()
    w.find_window_wildcard(".*64-bit/Windows")
    #w.find_window_wildcard(".*(64-bit Development PCD3D_SM5)")
    #w.find_window_wildcard(".*Unreal Editor")
    w.set_foreground()


interval = 0.05 #Interval in seconds
moves_file = "ProbeLog\Supercaustics_12Cameras.txt"

ku = KeyUtils()
pkey = Probe()
k = PyKeyboard()
setsize = 15
generate_settings(setsize, moves_file)

##############################################################################
# GATHER DATA
##############################################################################
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("starting...")

file = open(moves_file)
counter = 0
for action in list(file.readlines()):
    Mat, HDRI, Lighting, ToteBox = action.split(',')

    Mat = int(Mat)
    HDRI = int(HDRI)
    Lighting = int(Lighting)
    ToteBox = int(ToteBox)

    print('image set ' + str(counter) + ' of ' + str(setsize))
    print("settings: " + str(action)) 
    counter += 1

    pkey.reset()

    if ToteBox % 20 == 0:
        k.tap_key('U', n=1, interval=interval)

    time.sleep(5)
                         
    #k.tap_key('M', n=Mat, interval=interval)
    # k.tap_key('H', n=HDRI, interval=interval)

    for angle in range(0, 12):
        k.tap_key('V', n=1, interval=interval)
        pkey.capture()
        time.sleep(1*interval)


    # for lighting in range(0,5):
    #     k.tap_key('L', n=1, interval=interval)
    #     for angle in range(0, 12):
    #         k.tap_key('V', n=1, interval=interval)
    #         pkey.capture()
    #         time.sleep(1*interval)



# Pause at the end to avoid transitioning away from the game too abruptly
time.sleep(0.5)

# Switch focus back to the Python window
if sys.platform == LINUX:
    # Using Alt-Tab in Linux. A more robust way would be to identify the
    # window from which the script was launched
    ku.alt_tab()
elif sys.platform == WINDOWS:
    # Assumes that the Python script was launched from a command window
    w.find_window_wildcard(".*PyCharm*.")
    w.set_foreground()