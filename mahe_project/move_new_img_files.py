import os
import glob
import shutil

os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\mahe\DM visit to Mahe 180724')

x=os.listdir()
# print(len(x))


for i in range(len(x)):
    # print(x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\"+x[i])
    y=os.listdir()
    # print(len(y))
    parent_dir = "C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\"+x[i]
    directory = "new"
    path = os.path.join(parent_dir, directory)
    # print(path)
    os.chdir(parent_dir)
    files_to_move = glob.glob("*.png")
    ftm = len(files_to_move)
    for k in range(ftm):
        print(files_to_move[k])
        source=os.path.join(parent_dir,files_to_move[k])
        print(source)
        destination=os.path.join(path)
        print(destination)
        # shutil.move(source,destination)
