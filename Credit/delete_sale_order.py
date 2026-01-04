import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(3)


sale=[
"386738518",
"386751116",
"386725948"
]

x=len(sale)

for i in range(x):
    pag.write(sale[i])
    time.sleep(2)
    pag.press('enter')
    time.sleep(7)
    pag.press('enter')
    time.sleep(1)
    pag.press('alt')
    time.sleep(1)
    pag.press('e')
    time.sleep(1)
    pag.hotkey('shift','tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('enter')
    time.sleep(5)




