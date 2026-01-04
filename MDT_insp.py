import pyautogui as pag
import time


pag.hotkey('alt', 'tab')
time.sleep(2)



# DSR review
pag.press('tab')
time.sleep(0.3)
pag.press('space')
time.sleep(0.3)
pag.press('tab')
time.sleep(0.3)
pag.press('space')
time.sleep(0.3)
pag.press('tab')
pag.press('down')
time.sleep(0.3)
for i in range(6):
    pag.press('tab')
    time.sleep(0.3)
time.sleep(0.3)
pag.press('space')
time.sleep(0.3)
for i in range(6):
    pag.hotkey('shift', 'tab')
time.sleep(0.3)
pag.press('down')
for i in range(6):
    pag.press('tab')
    time.sleep(0.3)
time.sleep(5)
pag.press('space')
# pag.press('tab')
# pag.press('space')

# Facilities
time.sleep(1)
pag.write(pag.prompt(text='Should i continue', title='', default=''))
time.sleep(1)
pag.press('tab', presses=5)
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(5)


# safety
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(1)
pag.press('tab')

for i in range(7):
    pag.press('down')
    time.sleep(1)
    pag.press('tab', presses=3)
time.sleep(.3)
pag.press('space')
time.sleep(5)


#Automation
pag.press('tab')
time.sleep(5)
pag.press('space')
time.sleep(5)
pag.press('tab')

for i in range(6):
    pag.press('down')
    time.sleep(.2)
    pag.press('tab',presses=3)
time.sleep(3)
for i in range(3):
    pag.press('down',presses=2)
    time.sleep(.2)
    pag.press('tab',presses=3)
time.sleep(3)
for i in range(2):
    pag.press('down')
    time.sleep(.2)
    pag.press('tab',presses=3)
time.sleep(1)
pag.press('space')
time.sleep(10)

# DU logs
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(2)
pag.press('tab')

for i in range(5):
    pag.press('down', presses=2)
    time.sleep(.2)
    pag.press('tab', presses=3)
time.sleep(3)
pag.press('space')
time.sleep(5)


# Miscellaneous
pag.press('tab')
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(2)
pag.press('tab')

for i in range(31):
    pag.press('down')
    time.sleep(.2)
    pag.press('tab', presses=2)
time.sleep(1)
pag.press('space')
time.sleep(5)

# Washroom
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(2)
pag.press('tab')

for i in range(13):
    pag.press('down')
    time.sleep(2)
    pag.press('tab', presses=2)
time.sleep(1)
# pag.press('tab')
time.sleep(1)
pag.press('tab')
pag.press('space')
time.sleep(5)

# Wage Payment
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(2)
pag.press('tab')
for i in range(9):
    pag.press('down')
    time.sleep(2)
    pag.press('tab', presses=2)
time.sleep(1)
pag.press('space')
time.sleep(5)







