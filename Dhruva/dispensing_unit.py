import pyautogui as pag
import subprocess
import time
import os
import sys

pag.hotkey('alt', 'tab')
time.sleep(2)

cust=[
"225894",
"200435",
"207093",
"352482",
"352555",
"197320",
"352531",
"125002",
"217846",
"187699",
"131236",
"188256",
"124983",
"125001",
"150924",
"259622",
"217844",
"216215",
"194096",
"150923",
"182983",
"323646",
"187720",
"198725",
"187727",
"135576",
"133462",
"290434",
"208908",
"205817",
"337736",
"187730",
"188261",
"252626",
"345545",
"187732",
"175585",
"290572",
"188267",
"124956",
"188269",
"212532",
"272261",
"217847",
"124958",
"299051",
"191385",
"124955",
"188270",
"124961",
"273371",
"294837",
"187718",

]
x=len(cust)
for i in range(x):

    pag.press('tab')
    time.sleep(0.3)
    pag.write('19102024')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.write('19102024')
    time.sleep(0.3)
    pag.press('tab', presses=2)
    time.sleep(0.3)
    pag.press('space')
    time.sleep(2)
    pag.write('du.png')
    time.sleep(2)
    pag.press('e1ter')
    time.sleep(5)
    pag.press('tab', presses=2)
    time.sleep(1)
    pag.write('complied')
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('space')
    time.sleep(3)
    pag.click(x=1412, y=237)
    time.sleep(1)
    pag.hotkey('fn', 'pageup')
    time.sleep(1)
    pag.click(x=483, y=511)
    pag.press('del', presses=10)
    time.sleep(2)
    pag.write(cust[i])
    time.sleep(3)
    pag.click(x=813, y=640)
    time.sleep(30)
    pag.press('tab', presses=2)
    # pag.click(x = 1332, y = 289)
    # time.sleep(1)
    pag.scroll(-10)
    time.sleep(1)
    i = 1
    while i <= 1:
        # im = pag.screenshot("Full screen.png")
        try:
            x, y = pag.locateCenterOnScreen("duicon.png", confidence=0.7)
            pag.click(x, y)
        except TypeError:
            i = 1
        else:
            break

    time.sleep(3)
    # pag.scroll(-30)
    # time.sleep(3)
    # i = 1
    # while i <= 1:
    #     # im = pag.screenshot("Full screen.png")
    #     try:
    #         x, y = pag.locateCenterOnScreen("canopy.png", confidence=0.7)
    #         pag.click(x, y)
    #     except TypeError:
    #         i = 1
    #     else:
    #         break

    time.sleep(1)
    # pag.write(pag.prompt(text='Should i continue', title='' , default=''))
    time.sleep(1)
    # pag.hotkey('alt','tab')
    # time.sleep(2)
    # pag.hotkey('shift','f10')
    # time.sleep(1)
    # pag.press('enter')

