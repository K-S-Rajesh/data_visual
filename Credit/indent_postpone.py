import subprocess
import pyautogui as pag
import time

#subprocess.run('C:\\Users\\ksraj\\OneDrive\\Desktop\\saplogon.bat',shell=True)
#time.sleep(60)
pag.hotkey('alt','tab')
#time.sleep(5)
# pag.press('x')
time.sleep(5)
for i in range(40):
    # pag.press('down')
    # time.sleep(1)
    # pag.press('down')
    # time.sleep(1)

    pag.hotkey('shift','space')
    time.sleep(6)
    pag.hotkey('alt','f12')
    time.sleep(4)
    pag.press('down',presses=2)
    time.sleep(4)
    pag.press('enter')
    time.sleep(4)
    pag.write('22.12.2025')
    time.sleep(4)
    pag.press('enter')
    time.sleep(4)
    pag.write('request from FO')
    time.sleep(4)
    pag.press('enter')
    time.sleep(7)
    pag.press('f5')
    time.sleep(12)




