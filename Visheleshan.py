import webbrowser
import pyautogui as pag
import time

webbrowser.open("https://ioclanalytics.net/wsp/users/login")
time.sleep(10)
pag.press('backspace',presses=12)
time.sleep(1)
pag.write('00501203')
time.sleep(1)
pag.press('tab')
time.sleep(1)

pag.press('backspace',presses=12)
time.sleep(1)
pag.write('Epicon@456')
pag.press('tab')
time.sleep(1)
pag.write((pag.prompt(text='Enter OTP', title='MSG Box' , default='')))

time.sleep(1)
for i in range(2):
    pag.press('tab')
    time.sleep(1)
time.sleep(1)
pag.press('space')
time.sleep(10)
#pag.moveTo(34,266)
#a, b = pag.locateCenterOnScreen("racer.png", confidence=0.7)
pag.click(23,338)
time.sleep(3)
#c, d = pag.locateCenterOnScreen("racer1.png", confidence=0.7)
#pag.click(c, d)
#time.sleep(3)

#pag.scroll(40)
#time.sleep(10)
pag.click(x=149, y=433)
time.sleep(15)
#pag.click(x=1783, y=225)
#time.sleep(5)
#pag.moveTo(x=1765, y=337)
#p

