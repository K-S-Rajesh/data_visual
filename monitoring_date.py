import os
import tkinter as tk
import time
import sys
import pyautogui as pag
import pandas as pd
import numpy as np
import openpyxl
from pyscreeze import ImageNotFoundException
from pyautogui import ImageNotFoundException

# os.system('start sapshcut.exe -system=PRD -client=310 -user=00500230 -pw=Iocl@0923')

# i=1
# while i<=1:
#     #im = pag.screenshot("Full screen.png")
#     try:
#         x, y = pag.locateCenterOnScreen("saplogonentry.png", confidence=0.7)
#     except TypeError:
#         i = 1
#     else:
#         break


# time.sleep(1)
# pag.hotkey('alt','space')
# time.sleep(0.3)
# pag.press('x')
# time.sleep(1)
pag.hotkey('alt', 'tab')
time.sleep(0.5)
pag.hotkey('ctrl', '/')
time.sleep(1)
pag.write('/nfd32')
time.sleep(1)
pag.press('enter')
time.sleep(2)



cust=[
"265571",
"253771",
"365054",
"371471",
"380447",
"124960",
"217846",
"352890",
"365126",
"265734",
"187702",
"289942",
"207093",
"378648",
"347063",
"358811",
"269683",
"371070",
"328646",
"207214",
"191385",
"367902",
"234524",
"350906",
"350918",
"373520",
"352482",
"166573",
"340827",
"188261",
"187722",
"187719",
"215272",
"376239",
"124973",
"309127",
"261817",
"372969",
"187709",
"335703",
"368417",
"348239",
"125002",
"332996",
"352555",
"124968",
"289404",
"205143",
"207966",
"346735",
"187707",
"194088",
"187714",
"241821",
"355613",
"358163",
"350407",
"363206",
"289385",
"188270",
"377040",
"188264",
"381096",
"131244",
"216215",
"124998",
"204257",
"360862",
"217045",
"197752",
"344299",
"188268",
"202917",
"345519",
"194519",
"339128",
"188272",
"346512",
"371076",
"203302",
"273981",
"332991",
"207065",
"328647",
"337390",
"259622",
"374993",
"289393",
"217844",
"352531",
"362526",
"345520",
"124993",
"344242",
"355490",
"191384",
"366336",
"374566",
"189873",
"188260",
"188269",
"344941",
"197319",
"208907",
"265742",
"125233",
"252626",
"333742",
"187732",
"345545",
"273371",
"352223",
"272261",
"124995",
"188646",
"352889",
"187723",
"330085",
"288174",
"343597",
"124952",
"124955",
"124963",
"124965",
"124970",
"124972",
"124975",
"124984",
"124985",
"124991",
"124994",
"125003",
"125007",
"125010",
"125012",
"125020",
"125027",
"125030",
"125035",
"125132",
"125144",
"125234",
"125237",
"131378",
"135023",
"135576",
"150889",
"150891",
"150892",
"150924",
"175973",
"185760",
"185764",
"187698",
"187706",
"187712",
"187717",
"187720",
"187724",
"188249",
"188250",
"299051",
"217848",
"125236",
"311234",
"187727",
"245308"

]


x=len(cust)
#print(x)

time.sleep(2)
pag.write(cust[0])
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.write('c004')
time.sleep(1)
pag.press('tab',presses=4)
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('enter')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)
pag.hotkey('ctrl','tab')
time.sleep(1)

pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)

pag.write('30.04.2026')
time.sleep(1)
#pag.press('space')
time.sleep(1)
pag.hotkey('ctrl','s')
time.sleep(1)
# pag.press('enter')
# time.sleep(2)


#sys.exit()


for i in range(x):
    time.sleep(5)
    pag.write(cust[i+1])
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.hotkey('ctrl','tab')
    time.sleep(1)
    pag.hotkey('ctrl', 'tab')
    time.sleep(1)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('30.04.2026')
    time.sleep(1)
    # pag.press('space')
    time.sleep(1)
    pag.hotkey('ctrl', 's')
    time.sleep(1)
    # pag.press('enter')
    time.sleep(1)


    j = 1
    while j <= 1:
        try:
            x, y = pag.locateCenterOnScreen("customer_code.png", confidence=0.5)
            time.sleep(2)
            pag.moveTo(x,y)
            print('i found it')
            j=j+1
        except ImageNotFoundException:
            time.sleep(1)
            pag.press('enter')
            time.sleep(1)
            j = 1
        else:
            break




























