import webbrowser
import pyautogui as pag
import time

webbrowser.open("https://spandan.indianoil.co.in/RetailNew/Login.jsp")
time.sleep(10)
pag.press('tab')
time.sleep(2)
pag.write('00501203')
time.sleep(1)
pag.press('tab')
time.sleep(1)
pag.press('backspace',presses=10)
time.sleep(1)
pag.write('Carpals@123')
time.sleep(1)
pag.press('tab',presses=2)
pag.write((pag.prompt(text='Enter the capcha', title='MSG Box' , default='')))
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(15)
pag.click(577,298)
time.sleep(5)
pag.click(577,298)
time.sleep(4)
pag.click(x=1103, y=406)
pag.click(x=1103, y=406)
time.sleep(4)
pag.click(144,461)
pag.click(144,461)
time.sleep(4)
pag.click(x=1563, y=593)
pag.click(x=1563, y=593)



