import pyautogui
import snp

pyautogui.FAILSAFE = True

i = 0
change = 0

jump_pos = [720, 540]
jump_pos_corner = [772, 590]
jump_diff = [jump_pos_corner[0] - jump_pos[0], jump_pos_corner[1] - jump_pos[1]]

dino_high = [636, 406]
dino_high_corner = [670, 445]
dino_diff = [dino_high_corner[0] - dino_high[0], dino_high_corner[1] - dino_high[1]]

under_dino = [630, 545]
under_dino_corner = [707, 585]
under_diff = [under_dino_corner[0] - under_dino[0], under_dino_corner[1] - under_dino[1]]

while True:
    i = i + 1

    if i > 1000 and change == 0:
        jump_pos[0] = jump_pos[0]+20
        jump_pos_corner[0] = jump_pos_corner[0]+20
        change = 1
        print("Change mode1")

    if i > 2500 and change == 1:
        jump_pos[0] = jump_pos[0] + 5
        jump_pos_corner[0] = jump_pos_corner[0] + 5
        change = 2
        print("Change mode2")

    if i > 5000 and change == 2:
        jump_pos[0] = jump_pos[0] + 2
        jump_pos_corner[0] = jump_pos_corner[0] + 2
        change = 3
        print("Change mode3")

    jump_scan = snp.locateCenterOnScreen('jump_blank.jpeg', threshold = 0.3, region = jump_pos + jump_diff)

    if jump_scan == None: #Not blank
        pyautogui.press('space')

    dino_scan = snp.locateCenterOnScreen('dino_head.jpeg', threshold = 0.5, region = dino_high + dino_diff)

    if dino_scan != None: #Is Head
        #print("detec dino head")
        under_dino_scan = snp.locateCenterOnScreen('under_dino_3.jpeg', threshold = 0.4, region = under_dino + under_diff)
        if under_dino_scan != None: #Is Blank
            pyautogui.keyDown('down')

