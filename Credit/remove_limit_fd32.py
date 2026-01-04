import time
import pyautogui as pag
from pyautogui import ImageNotFoundException

pag.hotkey('alt', 'tab')
time.sleep(3)




cust=[
"359455",
"124956",
"309127",
"124998",
"217028",
"133462",
"124974",
"124975",
"141044",
"335819",
"343560",
"157000",
"124958",
"187702",
"330096",
"334108",
"344242",
"196682",
"344299",
"281505",
"330085",
"187727",
"245308",
"195920",
"352531"

]



x=len(cust)
for i in range(x):
    pag.write(cust[i])
    time.sleep(2)
    pag.press('enter')
    time.sleep(3)
    pag.press('del',presses=2)
    time.sleep(3)
    pag.hotkey('ctrl','s')
    time.sleep(3)


    j = 1
    while j <= 1:
        try:
            x, y = pag.locateCenterOnScreen("customer_code.png", confidence=0.5)
            time.sleep(2)
            pag.moveTo(x,y)
            print('i found it')
            j=j+1
        except ImageNotFoundException:
            time.sleep(2)
            pag.press('enter')
            time.sleep(2)
            j = 1
        else:
            break
