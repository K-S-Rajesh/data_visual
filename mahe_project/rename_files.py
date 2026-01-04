from PIL import Image
import os
import glob
import shutil

os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\mahe\DM visit to Mahe 180724')

x=os.listdir()
# print(len(x))


for i in range(len(x)):
    print(x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\"+x[i]+"\\"+"new"+"\\")
    lst_imgs= glob.glob("*.png")
      # print(ftm)
    for j in lst_imgs:
        print((j))
        img = Image.open(j)
        # img = img.resize((int(img.width / 6), int(img.height / 6)))
        img.save(j[:-9]+".png")

