import webbrowser
import pyautogui as pag
import time




n=int((pag.prompt(text='How many days you wish to post cng sales', title='MSG Box' , default='')))

for i in range(n):
    webbrowser.open("https://erpweb.indianoil.in:8022/sap/bc/gui/sap/its/webgui?sap-client=310&sap-language=EN")
    time.sleep(8)
    pag.press('down')
    time.sleep(5)
    pag.press('enter')
    time.sleep(5)
    pag.press('tab',presses=3)
    time.sleep(5)
    pag.press('space')
    time.sleep(5)
    pag.moveTo(x=146, y=177)
    time.sleep(2)
    pag.click(x=146, y=177)
    time.sleep(2)
    pag.write('/nycng')
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.write('4103')
    time.sleep(2)
    pag.press('f8')
    time.sleep(2)
    pag.moveTo(x=31, y=303)
    time.sleep(2)
    pag.click(x=31, y=303)
    time.sleep(2)
    pag.moveTo(x=692, y=244)
    time.sleep(2)
    pag.click(x=692, y=244)
    time.sleep(2)
    time.sleep(2)
    pag.moveTo(x=31, y=303)
    time.sleep(2)
    pag.click(x=31, y=303)
    time.sleep(2)
    pag.moveTo(x=812, y=249)
    time.sleep(2)
    pag.click(x=812, y=249)
    time.sleep(2)
    pag.moveTo(x=542, y=302)
    time.sleep(2)
    pag.click(x=542, y=302)
    time.sleep(2)
    pag.write((pag.prompt(text='Enter the Cng sales Qty for the day', title='MSG Box' , default='')))
    time.sleep(2)
    pag.moveTo(x=317, y=174)
    time.sleep(2)
    pag.click(x=317, y=174)
    time.sleep(2)
    pag.press('enter')
    time.sleep(2)
    pag.moveTo(x=656, y=244)
    time.sleep(2)
    pag.click(x=656, y=244)

    time.sleep(2)
    pag.moveTo(x=31, y=303)
    time.sleep(2)
    pag.click(x=31, y=303)

    time.sleep(2)
    pag.moveTo(x=719, y=239)
    time.sleep(2)
    pag.click(x=719, y=239)
    time.sleep(2)
    pag.moveTo(x=866, y=610)
    time.sleep(5)
    pag.click(x=866, y=610)
    time.sleep(10)
    pag.moveTo(x=916, y=958)
    time.sleep(5)
    pag.click(x=916, y=958)
    time.sleep(5)
    pag.hotkey('ctrl','w')
















