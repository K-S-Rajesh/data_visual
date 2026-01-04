import time
import pyautogui as pag

pag.hotkey('alt','tab')

# time.sleep(1)
# pag.hotkey('ctrl','/')
# time.sleep(1)
# pag.write('/nyv41')
# time.sleep(1)
# pag.press('enter')
# time.sleep(1)


tt=[
"AP16TH9411",
"AP31TF4769",
"TS12UD3980"
]

invoice=["192972035",
"192975163",
"192974196"

]

tt_count=len(tt)
print(tt_count)

for i in range(tt_count):
    time.sleep(1)
    pag.hotkey('ctrl','/')
    time.sleep(1)
    pag.write('/nyv41')
    time.sleep(1)
    pag.press('enter')
    time.sleep(1)
    pag.press('del', presses=15)
    time.sleep(1)

    pag.write(tt[i])
    time.sleep(1)
    pag.press('tab')
    time.sleep(1)
    pag.press('del',presses=15)
    time.sleep(1)
    pag.write(invoice[i])
    time.sleep(2)
    pag.hotkey('ctrl','s')
    time.sleep(1)