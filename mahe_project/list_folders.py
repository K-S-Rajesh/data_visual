import os
import glob


os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\mahe\DM visit to Mahe 180724')

x=os.listdir()
print(len(x))
for i in range(len(x)):
    print(x[i])
    os.chdir("C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\" + x[i])
    y = os.listdir()
    print(len(y))

    for j in range(len(y)):
        parent_dir = "C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\" + x[i] + "\\" + y[j]
        directory = "new\\"
        path = os.path.join(parent_dir, directory)
        print(path)
        os.mkdir(path)
