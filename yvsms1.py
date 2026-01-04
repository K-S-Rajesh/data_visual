import os
import tkinter as tk
import time
import pyautogui as pag



pag.hotkey('alt','tab')
time.sleep(2)

cust=[
"125033",
"125035",
"131378",
"133458",
"135376",
"150892",
"187706",
"187727",
"188250",
"188256",
"188258",
"188261",
"188264",
"188271",
"189873",
"191384",
"194088",
"194967",
"197320",
"197735",
"197961",
"198725",
"198758",
"198825",
"204257",
"205050",
"208096",
"208908",
"208939",
"209208",
"216240",
"216348",
"217849",
"222080",
"225894",
"234524",
"252626",
"259622",
"261664",
"265571",
"269683",
"272261",
"273929",
"273981",
"289396",
"289966",
"290577",
"291445",
"296704",
"299071",
"305286",
"306972",
"313478",
"315379",
"328648",
"330115",
"330792",
"333010",
"337391",
"339065",
"343598",
"344242",
"344299",
"345545",
"346511",
"346512",
"346533",
"347061",
"352482",
"352555",
"352890",
"355766",
"359379",
"368417",
"369496"

]


x=len(cust)

for i in range(x):
    pag.write('4200')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('re')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('16741')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write(cust[i])
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('4247')
    time.sleep(0.5)
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('01')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write(cust[i])
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.write('zodd')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('space')
    time.sleep(2)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('tab')
    time.sleep(0.5)
    pag.press('space')
    time.sleep(3)
    image_found = False
    time.sleep(1)
    while not image_found:
        try:
            x1, y1 = pag.center(pag.locateOnScreen("yvsms_create.png", confidence=0.7))
            time.sleep(2)
            pag.click(x1, y1)
            time.sleep(2)
            print('Hurray! image found')
            image_found = True
        except:
            print(f'image not found trying again in next 2 seconds. ')
            time.sleep(2)



