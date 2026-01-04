import os
import glob
import shutil



# dest_dir=r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROs_Each_ppt'


os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos')

x=os.listdir()
# print(len(x))
for i in range(len(x)):
    # print(x[i])
    # os.mkdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROs_Each_ppt\\"+x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\"+x[i])

    y=os.listdir()
    # print(len(y))

    for j in range(len(y)):
        # os.mkdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROs_Each_ppt\\" + x[i]+"\\"+y[j])
        parent_dir="C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\"+x[i]+"\\"+y[j]
        directory="new\\"
        path=os.path.join(parent_dir,directory)
        # print(path)
        os.chdir(path)
        files_to_move=glob.glob("*.pptx")
        # print(len(files_to_move))
        ftm=len(files_to_move)

        for k in range(ftm):
                source = os.path.join(path, files_to_move[k])
                print(source)
                dest_dir="C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROs_Each_ppt\\"+x[i]+"\\"+y[j]+"\\"
                # os.mkdir(dest_dir)
                destination = os.path.join(dest_dir)
                print(dest_dir)
                # os.mkdir(destination)
                shutil.copy(source,destination)



