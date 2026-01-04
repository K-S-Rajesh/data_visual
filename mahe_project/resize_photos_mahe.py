from PIL import Image
import glob
import os

# lst_imgs=[i for i in glob.glob("*.jpg")]
# print(os.getcwd())

# print(os.getcwd())
os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\mahe\DM visit to Mahe 180724')

x=os.listdir()

#
# folPath=r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos\Kanhangad\ALSAFAR FUELS'
#
print(len(x))
for i in range(len(x)):
    print(x[i])
    folder_name = 'C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\mahe\\DM visit to Mahe 180724\\' +x[i]
    os.chdir(folder_name)
    lst_imgs=glob.glob("*.jpg")
    # print(lst_imgs)
    for j in lst_imgs:
        print((j))
        img = Image.open(j)
        img = img.resize((int(img.width / 6), int(img.height / 6)))
        img.save(j[:-4] + "_new.png")

    # im=Image.open('IMG_1646.JPG')
    # im.show()

    # img=Image.open(C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\Kanhangad\\ALSAFAR FUELS\\IMG_1646.JPG)


