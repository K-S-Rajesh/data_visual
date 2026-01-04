import subprocess
import pyautogui as pag
import time
import os
from datetime import date
from datetime import date,datetime,timedelta

#alt+tab landing screen should be in SAP , with already yv40 , waiting for TT no

tt=[



"kl55aa1728"
]
invoice=[
"7001526933"

]


pag.hotkey('alt', 'tab')
time.sleep(1)


for i in range(20):
    pag.press('del',presses=15)
    time.sleep(0.25)
    pag.write(tt[i])
    time.sleep(1)
    pag.press('tab')
    time.sleep(0.25)
    pag.press('del', presses=15)
    time.sleep(0.25)
    pag.write(invoice[i])
    time.sleep(0.25)
    pag.press('tab')
    time.sleep(0.25)
    pag.press('backspace')
    time.sleep(0.25)
    pag.press('down')
    time.sleep(0.25)
    pag.press('enter')
    time.sleep(0.25)
    pag.press('tab')
    time.sleep(0.25)
    pag.press('backspace')
    time.sleep(0.25)
    pag.press('down')
    time.sleep(0.25)
    pag.press('enter')
    time.sleep(0.25)
    pag.press('enter')
    time.sleep(2)
    pag.write('0')
    time.sleep(0.25)
    pag.press('tab',presses=2)
    time.sleep(0.25)
    pag.write('0')
    time.sleep(0.25)
    pag.press('tab', presses=2)
    time.sleep(0.25)
    pag.write('0')
    time.sleep(0.25)
    pag.press('tab', presses=2)
    time.sleep(0.25)
    pag.write('0')
    time.sleep(0.25)
    pag.press('tab', presses=2)
    time.sleep(0.25)
    time.sleep(5)




