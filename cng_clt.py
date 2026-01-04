import subprocess
import webbrowser
import pyautogui as pag
import time



subprocess.run('C:\\Users\\ksraj\\OneDrive\\Desktop\\saplogon.bat',shell=True)
time.sleep(40)
pag.hotkey('alt','space')
time.sleep(1)
pag.press('x')
time.sleep(3)
pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nycng')
time.sleep(2)
pag.press('enter')
time.sleep(2)
pag.write('4203')
time.sleep(2)
pag.press('f8')
time.sleep(2)

