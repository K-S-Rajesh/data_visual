import os
import glob
import shutil

os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\mahe\DM visit to Mahe 180724')

x=os.listdir()
print(len(x))


for i in range(len(x)):
    print(x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\"+x[i])
    y=os.listdir()
    print(len(y))
    parent_dir = "C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\"+x[i]
    directory = "new"
    path = os.path.join(parent_dir, directory)
    print(path)
    os.mkdir(path)

    # for j in range(len(y)):
    #
    #     parent_dir="C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\"+x[i]+"\\"+y[j]
    #     directory="new"
    #     path=os.path.join(parent_dir,directory)
    #     print(path)
    #     os.mkdir(path)
    # #     os.chdir(parent_dir)
    #     # files_to_move=glob.glob("*.png")
    #     files_to_move=glob.glob("*.pptx")
    #     print(len(files_to_move))
    #     ftm=len(files_to_move)
    #     for k in range(ftm):
    #         # print(files_to_move[k])
    #         source=os.path.join(parent_dir,files_to_move[k])
    #         print(source)
    #         destination=os.path.join(path)
    #         print(destination)
    #         # shutil.move(source,destination)
