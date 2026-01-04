import time
import pyautogui as pag


pag.hotkey('alt', 'tab')
time.sleep(3)



cust=[
"195654",
"291447",
"187726",
"284065",
"273371",
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
pag.hotkey('ctrl','/')
time.sleep(1)
pag.write('/nyv281')
time.sleep(3)
pag.press('enter')
time.sleep(5)
pag.hotkey('ctrl','tab')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(1)



x=len(cust)
for i in range(x):
    pag.write(cust[i])
    time.sleep(1)
    pag.press('tab',presses=2)
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.hotkey('ctrl','tab')
    time.sleep(2)
    pag.hotkey('ctrl', 'tab')
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    pag.write('900')
    time.sleep(2)
    pag.click(127,263)
    time.sleep(3)
    pag.press('enter')
    time.sleep(3)
