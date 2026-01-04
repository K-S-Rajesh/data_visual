import subprocess
import pyautogui as pag
import time
import pyttsx3



ms_qty=4
hsd_qty=8


mal_cust=[
"125022",
"187707",
"188255",
"197961",
"198708"

]



tir_cust=[



]












pag.hotkey('alt','tab')
time.sleep(4)
x=len(mal_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    pag.click(x=138, y=558)
    time.sleep(4)
    for j in range(4):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l04')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(mal_cust[i])
    time.sleep(5)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(5)
    pag.click(x=673, y=590)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4222')
    time.sleep(1)
    for k in range(5):
        pag.press('tab')
        time.sleep(0.5)
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.typewrite('16730')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    # MS indent Qty
    pag.write(str(ms_qty))
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.typewrite('50700')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    # HSD indent Qty
    pag.write(str(hsd_qty))
    time.sleep(1)
    for l in range(9):
        pag.press('tab')
        time.sleep(0.25)
    pag.press('space')
    time.sleep(3)
    pag.hotkey('ctrl', 'tab')
    time.sleep(5)


engine = pyttsx3.init()
engine.say("The program has finished executing malappuram.")
engine.runAndWait()



#pag.hotkey('alt','tab')
time.sleep(4)
x=len(tir_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    pag.click(x=138, y=558)
    time.sleep(4)
    for j in range(4):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l21')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(tir_cust[i])
    time.sleep(5)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(5)
    pag.click(x=673, y=590)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4222')
    time.sleep(1)
    for k in range(5):
        pag.press('tab')
        time.sleep(0.5)
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.typewrite('16730')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    # MS indent Qty
    pag.write(str(ms_qty))
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.typewrite('50700')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    # HSD indent Qty
    pag.write(str(hsd_qty))
    time.sleep(1)
    for l in range(9):
        pag.press('tab')
        time.sleep(0.25)
    pag.press('space')
    time.sleep(3)
    pag.hotkey('ctrl','tab')
    time.sleep(5)


engine = pyttsx3.init()
engine.say("The program has finished executing tirur.")
engine.runAndWait()






