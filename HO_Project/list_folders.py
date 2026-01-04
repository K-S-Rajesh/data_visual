import os
import glob



os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos')

x=os.listdir()
# print(len(x))
#
# x=os.listdir()
# print(len(x))

for i in range(len(x)):
    print(x[i])
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
        # print(len(z))
        loi=glob.glob("*.png")
        # files_to_move=glob.glob("*.pptx")
        # print(len(loi))
        # ftm=len(files_to_move)
        for k in range(len(loi)):
            print(loi[k])
