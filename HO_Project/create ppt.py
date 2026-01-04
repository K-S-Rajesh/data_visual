from pptx import Presentation
import os
import glob
import shutil


# os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_photos')
# ppt_to_copy=glob.glob("*.pptx")
# file_to_copy=ppt_to_copy[0]
# print(file_to_copy)
source=(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_photos\newPPT.pptx')



os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos')

x=os.listdir()

for i in range(len(x)):
    # print(x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\"+x[i])
    y=os.listdir()
    # print(len(y))

    for j in range(len(y)):

        parent_dir="C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\"+x[i]+"\\"+y[j]
        directory="new\\"
        path=os.path.join(parent_dir,directory)
        print(path)
        # os.mkdir(path)
        os.chdir(path)
        z=os.listdir()
        # ppt=glob.glob("*.pptx")
        # print((ppt[0]))
        # os.remove(ppt[0])
        # #
        shutil.copy(source,path)


