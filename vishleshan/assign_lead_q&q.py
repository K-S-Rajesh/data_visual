#before running this program ensure that vishleshan is open in chrome window and if u press alt+tab, the landing screen should be vishleshan


#select detailed report
#select Q&Q in category

import pyautogui as pag
import time



ro_code=[


"307322",
"309102",
"309127",
"323646",
"342105",
"343598",
"367186",
"376600"

]




pag.hotkey('alt','tab')
time.sleep(1)

c=len(ro_code)
time.sleep(1)
for i in range(c):
    pag.click(x=459, y=476)
    # time.sleep(1)
    # for j in range(10):
    #     pag.press('tab')
    #     time.sleep(0.5)
    time.sleep(2)
    pag.press('backspace',presses=10)
    time.sleep(1)
    pag.press('del', presses=10)
    time.sleep(1)
    pag.write(ro_code[i])
    time.sleep(1)
    for k in range(4):
        pag.press('tab')
        time.sleep(0.5)
    # pag.press('enter')
    # time.sleep(5)
    #pag.click(x=1027, y=527)
    pag.click(x=1460, y=549)#click on lead
    # pag.click(x=813, y=617)
    # pag.click(x=1462, y=532)
    time.sleep(10)  #wait for the lead to load in another window
    pag.click(1757, y=456)  #click on edit button in lead
    time.sleep(5)
    pag.click(x=397, y=755)# click on select action planned
    time.sleep(2)
    # pag.click(x=1243, y=298)
    # time.sleep(0.5)
    for l in range(5):
        pag.press('down')
        time.sleep(0.5)
    time.sleep(2)

    pag.press('enter')
    time.sleep(5)
    pag.click(x=1282, y=858)
    time.sleep(2)
    pag.click(x=1282, y=858)
    time.sleep(10)
    pag.click(x=302, y=962)

    # for i in range(10):
    #     pag.press('tab')
    #     time.sleep(0.5)

    # pag.click(x=1243, y=298)
    # time.sleep(0.5)
    # for m in range(6):
    #     pag.press('tab')
    #     time.sleep(0.5)
    #
    # pag.hotkey('alt','down')
    # time.sleep(15)
    # pag.press('tab')
    time.sleep(3)
    pag.write('review and submit ATR')
    time.sleep(3)
    pag.press('tab')
    time.sleep(3)
    pag.press('space')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(10)

    # time.sleep(10)


    pag.hotkey('ctrl','w')
    time.sleep(5)
    # # pag.hotkey('ctrl', 'w')
    # # time.sleep(1)


