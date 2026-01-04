import pywhatkit
import webbrowser
import pyautogui as pag
import time



# syntax: phone number with country code, message, hour and minutes
#pywhatkit.sendwhatmsg('+918883747058', 'Hi This msg is sent thru python', 8, 8)
#pywhatkit.sendwhatmsg_to_group("https://chat.whatsapp.com/D7ClNYrSbJM0fq0TjJg1WJ", "Hey All!", 8, 14)
webbrowser.open("https://web.whatsapp.com/")
time.sleep(10)

pag.press('tab',presses=4)

time.sleep(1)
pag.write('xp95')
time.sleep(1)
pag.press('down')
time.sleep(1)
pag.press('enter')
time.sleep(1)
n=int((pag.prompt(text='Indent of XP for the day in KL', title='MSG Box' , default='')))
time.sleep(1)
pag.write('Sir,MDUIII-'+str(n)+'kl')
time.sleep(15)
pag.press('enter')



