import webbrowser
import pyautogui as pag
import time

webbrowser.open("https://secureaccess.indianoil.co.in/")
time.sleep(3)
pag.press('space')
time.sleep(2)
pag.press('space')
time.sleep(2)
pag.press('space')

image_found=False
time.sleep(1)
while not image_found:
    try:
        x1, y1=pag.center(pag.locateOnScreen("sign_in.png", confidence=0.7))
        time.sleep(2)
        pag.moveTo(x1,y1)
        print('Hurray! image found')
        image_found = True
    except:
        print(f'image not found trying again in next 2 seconds. ')
        time.sleep(2)

time.sleep(2)
# time.sleep(20)
pag.click(x=1373, y=286)
time.sleep(2)
pag.click(x=1294, y=691)
time.sleep(2)
pag.click(x=1286, y=534)
time.sleep(2)
pag.click(x=1304, y=710)
time.sleep(3)
pag.click(x=1304, y=750)
time.sleep(5)
time.sleep(5)

image_found=False

while not image_found:
    try:
        pag.scroll(-800)
        time.sleep(3)
        x1, y1=pag.center(pag.locateOnScreen("netaccess.png", confidence=0.6))
        time.sleep(2)
        pag.moveTo(x1,y1)
        pag.click(x1,y1)
        time.sleep(1)
        pag.click(x=233, y=796)
        print('Hurray! image found')
        image_found = True
    except:
        print(f'image not found trying again in next 2 seconds. ')
time.sleep(2)
time.sleep(10)
pag.press('space')
