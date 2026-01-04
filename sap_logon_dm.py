import os
import tkinter as tk
import time
import pyautogui as pag
#WIDTH = 200

#HEIGHT = 300

#root = tk.Tk()

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)

#canvas.pack()
#def myClick1():

os.system('start sapshcut.exe -system=PRD -client=310 -user=00081845 -pw=Password@5')


time.sleep(10)
pag.hotkey('alt','space')
time.sleep(0.3)
pag.press('x')


#pag.hotkey('','pageup')
#def myClick2():

    #<SID1> = os.system('start sapshcut.exe -system=<SID> -client=<NUM> -user=<UserName> -pw=<Password>')

    #<SID1>.pack()

#button1 = tk.Button(root, text="<SID>", command=myClick1)

#button1.pack()

#button2 = tk.Button(root, text="<SID1>", command=myClick2)

#button2.pack()

#root.mainloop()

