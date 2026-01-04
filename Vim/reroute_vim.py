import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(3)

# for i in range(12):
#     pag.press('up')
#     time.sleep(1)
#     pag.press('tab')
#     time.sleep(1)
#     pag.press('space')
#     time.sleep(10)
#
pag.click(x=165, y=358)
for i in range(9):
    pag.press('tab')
    time.sleep(2)
pag.press('space')
time.sleep(10)

for i in range(4):
    pag.press('tab')
    time.sleep(1)

pag.write('routed through SIC')
time.sleep(2)
pag.hotkey('ctrl','s')
time.sleep(2)
pag.press('f5') 