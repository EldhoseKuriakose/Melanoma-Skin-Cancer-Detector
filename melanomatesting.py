import numpy as np
import os,cv2
from tkinter import *
from keras.preprocessing import image
from keras.models import load_model
import dbase1
import tkinter.messagebox
import datetime,sqlite3

def detection(idd):
  root=Tk()
  root.withdraw()
  import tkinter.filedialog
  path=tkinter.filedialog.askopenfile()
  test_image = image.load_img(path.name, target_size = (128,128))
  os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
  img=cv2.imread(path.name)
  test_image = image.img_to_array(test_image)
  test_image = np.expand_dims(test_image, axis = 0)
  classifier=load_model("mymodel1.h5")
  test_image = image.load_img(path.name, target_size = (128,128))
  test_image = image.img_to_array(test_image)
  test_image = np.expand_dims(test_image, axis = 0)
  result = classifier.predict(test_image)
  print(result)
  y_pred = (result >0.5)*1
  print(y_pred)
  if y_pred[0] == 1:
    prediction = 'Melanoma'
  elif y_pred[0]==0:
    prediction = 'Not Melanoma'
  print(prediction)
  db=sqlite3.connect("melanoma.db")
  c=db.cursor()
  query="INSERT INTO result (userid,melornot,date) VALUES (%d,'%s','%s')"%(idd,prediction,datetime.datetime.now())
  c.execute(query)
  db.commit()
  print("success")
  tkinter.messagebox.showinfo("result", prediction)
	#img=cv2.resize(img,(400,400))
	#cv2.putText(img,"prediction:"+prediction, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0),2)
	#cv2.imshow("result",img)
	#cv2.waitKey(0)
	#cv2.destroyAllwindows()
        
