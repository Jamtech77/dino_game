import pyautogui
import snp
import numpy as np
import sys
try:
    from PIL import ImageGrab
except ImportError:
    import pyscreenshot as ImageGrab

pyautogui.FAILSAFE = True

i = 0
change = 0

# Create a flexible window to display
screen = np.asarray(ImageGrab.grab(), dtype=np.uint8)

# Identify main screen resolution
if len(screen.shape) == 3:
    h, w, c = screen.shape
elif len(screen.shape) == 2:
    h, w = screen.shape
else:
    raise ValueError('Unknown screen resolution')

# Search left half screen
def find_dino():
    left_up = [0, 0]
    right_bottom = [w // 2, h]
    diff = [right_bottom[0] - left_up[0], right_bottom[1] - left_up[1]]
    dino_scan = snp.locateCenterOnScreen('dino_head.jpeg', threshold = 0.8, region = left_up + diff)
    return dino_scan

dino_pos = find_dino()

if dino_pos == None:
    print("Can not find Dino")
    sys.exit()
else:
    print("Found Dino's position:" + str(dino_pos))

# Relative Position
jump_pos = [-25+dino_pos[0]+67, dino_pos[1]+11]
jump_pos_corner = [-25+dino_pos[0]+119, dino_pos[1]+61]
jump_diff = [jump_pos_corner[0] - jump_pos[0], jump_pos_corner[1] - jump_pos[1]]

dino_high = [dino_pos[0]-17, dino_pos[1]-123]
dino_high_corner = [dino_pos[0]+17, dino_pos[1]-84]
dino_diff = [dino_high_corner[0] - dino_high[0], dino_high_corner[1] - dino_high[1]]

under_dino = [dino_pos[0]-23, dino_pos[1]+16]
under_dino_corner = [dino_pos[0]+54, dino_pos[1]+56]
under_diff = [under_dino_corner[0] - under_dino[0], under_dino_corner[1] - under_dino[1]]

while True:
    i = i + 1
    if i > 1000 and change == 0:
        jump_pos[0] = jump_pos[0]+20
        jump_pos_corner[0] = jump_pos_corner[0]+20
        change = 1
        print("Clutch 1")

    if i > 2500 and change == 1:
        jump_pos[0] = jump_pos[0] + 5
        jump_pos_corner[0] = jump_pos_corner[0] + 5
        change = 2
        print("Clutch 2")

    if i > 5000 and change == 2:
        jump_pos[0] = jump_pos[0] + 2
        jump_pos_corner[0] = jump_pos_corner[0] + 2
        change = 3
        print("Clutch 3")

    jump_scan = snp.locateCenterOnScreen('jump_blank.jpeg', threshold = 0.3, region = jump_pos + jump_diff)

    if jump_scan == None: #Not blank
        pyautogui.press('space')

    dino_scan = snp.locateCenterOnScreen('dino_head.jpeg', threshold = 0.5, region = dino_high + dino_diff)

    if dino_scan != None: #Is Head
        #print("detec dino head")
        under_dino_scan = snp.locateCenterOnScreen('under_dino.jpg', threshold = 0.4, region = under_dino + under_diff)
        if under_dino_scan != None: #Is Blank
            pyautogui.keyDown('down')
