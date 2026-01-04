import time
import pyautogui as pag





pag.hotkey('alt','tab')
time.sleep(1)
x=int(pag.prompt(text='how many times do you want to run', title='MSG Box' , default=''))

for i in range(x):
    pag.click(x=143, y=438)
    time.sleep(2)
    pag.hotkey('ctrl','f5')
    time.sleep(2)
    pag.press('del',presses=10)
    time.sleep(2)
    pag.write('0000')
    time.sleep(2)
    pag.write((pag.prompt(text='Enter sap code', title='MSG Box' , default='')))
    time.sleep(3)
    pag.press('enter')
    time.sleep(2)
    pag.doubleClick(x=132, y=482)
    time.sleep(15)

