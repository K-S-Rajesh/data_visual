import webbrowser
import pyautogui as pag
import time
import os








#s=pag.screenshot("big_ip_edge.png",region=(1200,1020,60,60))

#x,y=pag.locateCenterOnScreen("big_ip_edge.png")
#print(x,y)




#pag.click(x,y)

os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\BIG-IP Edge Client.lnk')

time.sleep(2)
pag.hotkey('alt','f4')
time.sleep(1)
pag.press('enter')
time.sleep(1)


#c=pag.screenshot("connect.png",region=(100,200,300,100))

a, b = pag.locateCenterOnScreen("connect_1.png", confidence=0.7)
pag.click(a, b)
time.sleep(40)
x, y = pag.locateCenterOnScreen("connect.png", confidence=0.7)
pag.click(x, y)
time.sleep(5)
pag.write('Ulnar@123')
time.sleep(0.5)
pag.press('tab')
time.sleep(0.5)
pag.press('space')
time.sleep(20)
i=1

while i==1:
    if pag.locateCenterOnScreen("password.png",confidence=0.7) == None:
        time.sleep(1)

    else:
        c,d=pag.locateCenterOnScreen("password.png", confidence=0.7)
        pag.click(c, d)
        time.sleep(1)
        pag.press('backspace' ,presses=11)
        time.sleep(3)
        pag.write((pag.prompt(text='Enter OTP', title='MSG Box' , default='')))
        time.sleep(2)
        time.sleep(0.5)

        pag.press('tab')
        time.sleep(0.5)
        pag.press('space')
        i=i-1

time.sleep(5)
e, f = pag.locateCenterOnScreen("vpn_1.png", confidence=0.7)
pag.click(e, f)







         























































































