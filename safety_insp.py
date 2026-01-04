import pyautogui as pag
import time

pag.hotkey('alt','tab')
time.sleep(3)
pag.press('tab')

# Section 1
for i in range(3):
    time.sleep(.5)
    pag.press('down',presses=2)
    time.sleep(.5)
    pag.press('tab',presses=2)
time.sleep(.3)


# Section 2
for i in range(3):
    time.sleep(.5)
    pag.press('down',presses=2)
    time.sleep(.5)
    pag.press('tab', presses=2)
# Section 3
for i in range(10):
    time.sleep(.5)
    pag.press('down',presses=2)
    time.sleep(.5)
    pag.press('tab', presses=2)
time.sleep(.3)

# Section 4
for i in range(14):
    time.sleep(.5)
    pag.press('down',presses=2)
    time.sleep(.5)
    pag.press('tab', presses=2)




# Section 3
for i in range(9):
    time.sleep(.5)
    pag.press('down',presses=2)
    time.sleep(.5)
    pag.press('tab', presses=2)
time.sleep(.3)

# Section 4
for i in range(14):
    time.sleep(.3)
    pag.press('down',presses=2)
    time.sleep(.3)
    pag.press('tab',presses=2)
    time.sleep(.5)


# Section 5
#for i in range(12):
#    time.sleep(.3)
#    pag.press('down',presses=2)
#    time.sleep(.3)
#    pag.press('tab',presses=2)

# Section 6
####for i in range(9):
    #time.sleep(.3)
   # pag.press('down',presses=2)
  #  time.sleep(.3)
 #   pag.press('tab',presses=2)
#time.sleep(.3)
#pag.press('down',presses=3)
#time.sleep(.3)
#pag.press('tab',presses=5)
#for i in range(2):
    #time.sleep(.3)
    #pag.press('down',presses=2)
    #time.sleep(.3)
    ####pag.press('tab',presses=2)


