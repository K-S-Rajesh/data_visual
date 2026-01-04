import pyautogui as pag
import time
import pyttsx3


pag.hotkey('alt','tab')
time.sleep(1)
#click on the first id before executing
#ensure public notes are included
for j in range(8):
    for i in range(7):
        pag.press('tab')
        time.sleep(0.5)

    pag.write('complied')
    time.sleep(1)

    for i in range(4):
        pag.hotkey('shift','tab')
        time.sleep(0.5)


    # for i in range(9):
    #     pag.press('tab')
    #     time.sleep(1)
    # pag.write('engineering dept')
    # time.sleep(1)
    # for i in range(13):
    #     pag.hotkey('shift','tab')
    #     time.sleep(1)
    pag.press('down')
    time.sleep(2)
    pag.press('down')
    time.sleep(0.5)
    pag.press('down')
    time.sleep(0.5)
    pag.press('down')
    time.sleep(0.5)
    pag.press('enter')
    time.sleep(2)

    for i in range(14):
        pag.press('tab')
        time.sleep(0.75)
    time.sleep(3)


#
# for i in range(7):
#     pag.press('tab')
#     time.sleep(0.5)
#
#     pag.write('complied')
#     time.sleep(1)
#
# for i in range(4):
#         pag.hotkey('shift','tab')
#         time.sleep(0.5)
#
#
#     # for i in range(9):
#     #     pag.press('tab')
#     #     time.sleep(1)
#     # pag.write('engineering dept')
#     # time.sleep(1)
#     # for i in range(13):
#     #     pag.hotkey('shift','tab')
#     #     time.sleep(1)
# pag.press('down')
# time.sleep(2)
# pag.press('down')
# time.sleep(0.5)
# pag.press('down')
# time.sleep(0.5)
# pag.press('down')
# time.sleep(0.5)
# pag.press('enter')
# time.sleep(2)
#
#
engine = pyttsx3.init()
engine.say("The program has finished executing its time for you you to look into it and restart the program .")
engine.runAndWait()
