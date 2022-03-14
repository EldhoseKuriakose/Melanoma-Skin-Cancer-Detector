from tkinter import *
import tkinter.messagebox
import PIL.Image
from PIL import ImageTk
from adminhome import *
from userhome import *
import dbase1

def insert():
    username=ety_username.get()
    password=ety_password.get()
    if username=="admin" and password=="admin":
       admain()
    else:
        result,idd = dbase1.logcheck(username, password)
        print (result)
        if result==1:
            print ("Login Successful")
            main(idd)
        else:
            tkinter.messagebox.showinfo("Status", "Invalid username or password")
            clr()

def clr():
    ety_username.delete(0,END)
    ety_password.delete(0,END)


def window():
    top = Toplevel()
    top.title("Login")
    top.configure(background='white')
##	img_home = Image.open("0.jpeg")
    fp = open("0.jpeg","rb")
    img_home = PIL.Image.open(fp)
    ph_home  = ImageTk.PhotoImage(img_home)
    lbl_home  = Label(top,image=ph_home )
    lbl_home.image = ph_home
	

    lbl_username = Label( top, text="Username",bg="white")
    lbl_password = Label( top, text="Password",bg="white" )
    global ety_username
    global ety_password
    ety_username=Entry(top)
    ety_password=Entry(top,show="*")



    btn_login=Button(top,text="Login",width=7,command=insert)
    btn_cancel=Button(top,text="Reset",width=7,command=lambda:clr())
    lbl_home.grid(row=0,columnspan=2)
    lbl_username.grid(row=1,column=0)
    lbl_password.grid(row=2,column=0)
    
    ety_username.grid(row=1,column=1)
    
    ety_password.grid(row=2,column=1)
    btn_login.grid(row=3,column=0)
    btn_cancel.grid(row=3,column=1)


    top.mainloop()
