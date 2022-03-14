from tkinter import *
import PIL.Image
from PIL import ImageTk
from userRegistration import *
from login import *

def main():
    top =Tk()
    top.title("Index")
    top.configure(background='white')	

    btn_hs=Button(top,text="Register",height="0",width="15",command=lambda: user())
    btn_fs=Button(top,text="Login",height="0",width="15",command=lambda: window())

    fp = open("mel.jpg","rb")
    img_ar = PIL.Image.open(fp)

    ph_ar = ImageTk.PhotoImage(img_ar)
    lbl_ar = Label(top,image=ph_ar)
    lbl_ar.image = ph_ar

    lbl_ar.grid(row=1,columnspan=5)
    btn_hs.grid(row=0,column=1)
    btn_fs.grid(row=0,column=3)

    top.mainloop()

main()
