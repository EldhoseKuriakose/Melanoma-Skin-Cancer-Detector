#!/usr/bin/env python2

import cv2
import os

def load_images(folder):
        print "entered"
        image_list=[]
        for filename in sorted(os.listdir(folder)):
            img=cv2.imread(os.path.join(folder,filename))
            image_list.append(filename)
        print "Images are loaded"
        return image_list

def RemoveBackground(Image):
    Image=cv2.imread(Image)
    IGray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    ret,BW=cv2.threshold(IGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #ret1,thresh1 = cv2.threshold(th,127,255,cv2.THRESH_BINARY)
    ret2,thresh2 = cv2.threshold(BW,127,255,cv2.THRESH_BINARY_INV)
    maskedImage=cv2.bitwise_and(Image,Image,mask=thresh2)
    return maskedImage,IGray

l=load_images(os.getcwd()+"\\Normalized")
print l
for i in l:
    BGImage,A=RemoveBackground(os.getcwd()+"\\Normalized\\"+i)
    cv2.imshow("sh",BGImage)
    cv2.waitKey()
    cv2.imwrite(os.getcwd()+"\\bgremoved\\"+i+"bgremoved.jpg",BGImage)
