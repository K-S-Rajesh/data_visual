import time
import pyautogui as pag



sale_order=[
"394028856",
"394052075",
"394054596",
"394058624",
"394056916",
"394085764",
"394088268",
"394091312",
"394093502",
"394092599",
"394089391"

]



pag.hotkey('alt','tab')
time.sleep(2)
for l in range(100):
    pag.hotkey('ctrl','/')
    time.sleep(1)
    pag.write('/nva02')
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    x=sale_order[l]
    pag.write(x)
    time.sleep(1)
    pag.press('enter')
    time.sleep(3)
    pag.press('enter')
    time.sleep(2)

    for i in range(5):
        pag.press('tab')
        time.sleep(0.5)
    pag.write('4247')
    time.sleep(0.5)
    for i in range(11):
        pag.press('tab')
        time.sleep(0.75)
    pag.write('4247')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.hotkey('ctrl','s')
    time.sleep(1)
    pag.press('enter')
    time.sleep(2)
    l=l+1



        
