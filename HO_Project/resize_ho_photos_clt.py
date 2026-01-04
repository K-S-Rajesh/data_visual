from PIL import Image
import glob
import os

# lst_imgs=[i for i in glob.glob("*.jpg")]
# print(os.getcwd())

# print(os.getcwd())
os.chdir(r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos\K S Rajesh')

x=os.listdir()

#
# folPath=r'C:\Users\ksraj\OneDrive - Indian Oil Corporation Limited\HO_10ROS_Each_25_Photos\Kanhangad\ALSAFAR FUELS'
#
print(len(x))
for i in range(len(x)):

    folder_name = 'C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\K S Rajesh\\all photos' +x[i]
    os.chdir(folder_name)
    lst_imgs=glob.glob("*.jpeg")
    print(lst_imgs)
    for i in lst_imgs:
        print(i)
        img = Image.open(i)
        img = img.resize((int(img.width / 6), int(img.height / 6)))
        img.save(i[:-4] + "_new.png")

    # im=Image.open('IMG_1646.JPG')
    # im.show()

    # img=Image.open(C:\\Users\\ksraj\\OneDrive - Indian Oil Corporation Limited\\HO_10ROS_Each_25_Photos\\Kanhangad\\ALSAFAR FUELS\\IMG_1646.JPG)


