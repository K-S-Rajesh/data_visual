import webbrowser
import pyautogui as pag
import time

webbrowser.open("https://spandan.indianoil.co.in/dhruva2/#/signin?continue=%2Fhome%2Fdashboard%2Fstate-office%2Fmaster-dashboard")
time.sleep(10)
pag.press('tab')
time.sleep(2)
pag.write('00501203')
time.sleep(1)
pag.press('tab',presses=2)
pag.write((pag.prompt(text='Enter the capcha', title='MSG Box' , default='')))
time.sleep(2)
pag.press('tab')
time.sleep(2)
pag.press('space')
time.sleep(15)