

import cv2
import os
import numpy as np
from PIL import Image
folder="Sample"
path1=folder
path2="Normalized"
def load_images(folder):
        print "entered"
        image_list=[]
        for filename in sorted(os.listdir(folder)):
            img=cv2.imread(os.path.join(folder,filename))
            image_list.append(filename)
        print "Images are loaded"
        RemoveBackground(image_list)
        Resize_Images(image_list)
   

def RemoveBackground(Imagelist):
   bgremoved=[]
   for i in Imagelist:
    print os.getcwd()+"\\"+"Sample\\"
    image=cv2.imread(os.getcwd()+"\\"+folder+"\\"+i)
    IGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,BW=cv2.threshold(IGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret1,thresh1 = cv2.threshold(th,127,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(BW,127,255,cv2.THRESH_BINARY_INV)
    Image=np.asarray(image)
    maskedImage=cv2.bitwise_and(Image,Image,mask=thresh2)
    bgremoved.append(maskedImage)
#print bgremoved

def Resize_Images(imagelist):
    for x in imagelist:
        im1 = Image.open(path1+"\\"+x)
        im2 = im1.resize((64, 64))    
        im2.save(path2+"\\"+"resized"+x)
    print "Images are stored at {} folder".format(path2) 

        
