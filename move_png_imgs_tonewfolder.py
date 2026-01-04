import os
import glob


os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos\Kanhangad\ALSAFAR FUELS')

files_to_move=glob.glob("*.png")
print(len(files_to_move))

for i in range(len(files_to_move)):
    print(files_to_move[i])


