import webbrowser
import pyautogui as pag
import time




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
pag.write('/nva41')
time.sleep(2)
pag.press('enter')
time.sleep(2)
pag.write('zcbd')
pag.press('tab')
pag.write('4100')
pag.press('tab')
pag.write('re')
pag.press('tab')
pag.write('mh')
pag.press('tab')
pag.write('4103')
pag.press('tab')
pag.write('t94')
pag.press('enter')
pag.write((pag.prompt(text='Enter SAP CODE OF DEALER', title='MSG Box', default='')))

