import subprocess
import pyautogui as pag
import time
import pyttsx3

#firefox in 100 zoom should be landing screen in alt+tab
#chrome in 100 zoom should be landing in Alt+Tab
ms_qty=4
hsd_qty=8



can_cust=[

]
khng_cust=[

]

kkde_cust=[

]

kkdw_cust=[


]

mal_cust=[
]



tir_cust=[

]










pag.hotkey('alt','tab')
time.sleep(4)
x=len(can_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l07')
    time.sleep(2)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(can_cust[i],interval=0.01)
    time.sleep(5)
    print(can_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    #pag.click(x=673, y=590) Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite('4247')
    time.sleep(2)
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
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
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
engine.say("The program has finished executing Kannur")
engine.runAndWait()


#pag.hotkey('alt','tab')
time.sleep(4)
x=len(khng_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l06')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(khng_cust[i])
    time.sleep(5)
    print(khng_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    # pag.click(x=673, y=590)Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4247')
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
    time.sleep(2)
    pag.press('tab')
    time.sleep(2)
    # MS indent Qty
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
engine.say("The program has finished executing kanhangad.")
engine.runAndWait()


#pag.hotkey('alt','tab')
time.sleep(4)
x=len(kkde_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l05')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(kkde_cust[i])
    time.sleep(5)
    print(kkde_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    # pag.click(x=673, y=590) Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4247')
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
    time.sleep(2)
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
engine.say("The program has finished executing Kozhikode east .")
engine.runAndWait()

#pag.hotkey('alt','tab')
time.sleep(4)
x=len(kkdw_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l08')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(kkdw_cust[i])
    time.sleep(5)
    print(kkdw_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    # pag.click(x=673, y=590) Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4247')
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
engine.say("The program has finished executing Kozhikode West RSA.")
engine.runAndWait()



#pag.hotkey('alt','tab')
time.sleep(4)
x=len(mal_cust)
for i in range(x):

    pag.click(x=690, y=874)
    time.sleep(1)
    pag.press('pageup')
    time.sleep(1)
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l04')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(mal_cust[i])
    time.sleep(5)
    print(mal_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    # pag.click(x=673, y=590)Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4247')
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
    #pag.click(x=138, y=558) Firefox
    pag.click(x=117, y=615)
    time.sleep(4)
    for j in range(3):
        pag.press('tab')
        time.sleep(1)
# sales area
    pag.typewrite('l21')
    time.sleep(1)
    pag.press('tab')
    time.sleep(3)
    pag.typewrite(tir_cust[i])
    time.sleep(5)
    print(tir_cust[i])
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)
    # pag.click(x=673, y=590)Firefox
    pag.click(x=643, y=643)
    time.sleep(4)
    pag.press('tab')
    time.sleep(2)
    pag.typewrite('4247')
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







