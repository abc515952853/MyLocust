import glob
import os
import time
import random


class get_image():
    def chosePic(self):
        pic_list = glob.glob('image\*.jpg')
        up_pic = random.sample(pic_list, random.randint(1,9))
        return up_pic
