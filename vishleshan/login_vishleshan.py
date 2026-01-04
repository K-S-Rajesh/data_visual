import webbrowser
import time
import pyautogui as pag

url = "https://ioclanalytics.net/wsp/users/login"

webbrowser.open(url)
time.sleep(3)
pag.write("00501203")
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write("Lumbar@123")
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write(pag.prompt("enter password"))
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')


