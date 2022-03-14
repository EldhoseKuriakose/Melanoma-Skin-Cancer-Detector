from tkinter import *
import PIL.Image
import tkinter.filedialog as t
from PIL import ImageTk
import time,random,cv2
import tkinter.messagebox
import melanomatesting

def window(idd):
    melanomatesting.detection(idd)
def main(idd):
    top =Toplevel()
    top.title("Index")
    top.configure(background='white')	

    btn_fs=Button(top,text="Upload an Image",height="0",width="15",command=lambda: window(idd))

    fp = open("de.jpg","rb")
    img_ar = PIL.Image.open(fp)

    ph_ar = ImageTk.PhotoImage(img_ar)
    lbl_ar = Label(top,image=ph_ar)
    lbl_ar.image = ph_ar

    lbl_ar.grid(row=1,columnspan=5)
    btn_fs.grid(row=0,column=3)

    top.mainloop()
