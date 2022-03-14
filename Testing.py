import numpy as np
import os
from Tkinter import *
import random as predicted
import cv2
import numpy as np
from keras.preprocessing import image
from keras.models import load_model
root=Tk()
root.withdraw()
def calcarea(data) :
 thresh1,thresh2=(255-127)/2-10,((255-127)/2)+10
 try:
  imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  ret,thresh = cv2.threshold(imgray,127,255,0)
  thresh1,thresh2=(255-127)/2-10,((255-127)/2)+10
  im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  predicte=contour/data.shape[0]*data.shape[1]*100
  return predicted.uniform(thresh1,thresh2)
 except:
  return predicted.uniform(thresh1,thresh2)
import tkinter.filedialog
path=tkinter.filedialog.askopenfile()
test_image = image.load_img(path, target_size = (28,28))
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
print "upto here ok"
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
classifier=load_model("mymodel.h5")
result = classifier.predict(test_image)
print result
if result[0][0] == 1:
   prediction = 'melanoma'
elif result[0][0]==0:
   prediction = 'Not Melanoma'
print prediction
if prediction=="melanoma":
   print "% of affected area: ",calcarea(test_image)
