from tkinter import *
import tkinter
import tkinter.messagebox
import dbase1
from PIL import Image
from PIL import ImageTk


def insert():
  name=ety_name.get()
  age=ety_age.get()
  contact=ety_contact.get()
  mailid=ety_mail.get()
  username=ety_username.get()
  password1=ety_password.get()
  password2=ety_confirm.get()
  if name!="" or age!="" or contact!="" or mailid!="" or username!="" or password1!="" or password2!="":
    if age.isdigit() and '@' in mailid and '.' in mailid and contact.isdigit(): 
      if(password1==password2):
        password=password2
        k = dbase1.regis(name,age,contact,mailid,username,password)
        tkinter.messagebox.showinfo("Status", "Successfully Inserted")
        clr()
      else:
        tkinter.messagebox.showinfo("Status", "Password not matched")
    else:
	    tkinter.messagebox.showinfo("Status", "Plese enter valid Phone number/ Age / Email")
	
  else:
    tkinter.messagebox.showinfo("Status", "Enter Complete Details")

def clr():
  ety_name.delete(0,END)
  ety_age.delete(0,END)
  ety_contact.delete(0,END)
  ety_mail.delete(0,END)
  ety_username.delete(0,END)
  ety_password.delete(0,END)
  ety_confirm.delete(0,END)

def cancel():
  root.withdraw()
    
def user():  
	#try:
    top = Toplevel()

    img_home = Image.open("8.jpeg")
    ph_home = ImageTk.PhotoImage(img_home)
    lbl_home = Label(top,image=ph_home)

    lbl_home.image = ph_home
    lbl_name = Label( top, text="Name" )
    lbl_age = Label( top, text="Age" )
    lbl_contact = Label( top, text="Contact no" )
    lbl_mailid = Label( top, text="Email ID" )
    lbl_username=Label(top,text="Username")
    lbl_password=Label(top,text="Password")
    lbl_confirm=Label(top,text="Confirm Password")
    global ety_name
    global ety_age

    global ety_contact
    global ety_mail
    global ety_username
    global ety_password
    global ety_confirm
    ety_name = Entry(top)
    ety_age = Entry(top)
    ety_contact = Entry(top)
    ety_mail = Entry(top)
    ety_username=Entry(top)
    ety_password=Entry(top,show="*")
    ety_confirm=Entry(top,show="*")

    btn_save=tkinter.Button(top,text="Save",width=7,command=lambda:insert())
    btn_reset=tkinter.Button(top,text="Reset",width=7,command=lambda:clr())
##		btn_cancel=tkinter.Button(top,text="Cancel",width=7,command=lambda:cancel())
    lbl_home.grid(row=0,columnspan=2)
    lbl_name.grid(row=1,column=0)
    lbl_age.grid(row=4,column=0)

    lbl_contact.grid(row=6,column=0)
    lbl_mailid.grid(row=7,column=0)
    lbl_username.grid(row=8,column=0)
    lbl_password.grid(row=9,column=0)
    lbl_confirm.grid(row=10,column=0)


	

    ety_name.grid(row=1,column=1)
    ety_age.grid(row=4,column=1)

    ety_contact.grid(row=6,column=1)
    ety_mail.grid(row=7,column=1)
    ety_username.grid(row=8,column=1)
    ety_password.grid(row=9,column=1)
    ety_confirm.grid(row=10,column=1)

    btn_save.grid(row=11,column=0)
##		btn_cancel.grid(row=11,column=1)
    btn_reset.grid(row=11,column=1)

    top.mainloop()
	#except:
		#tkinter.messagebox.showinfo("Info","An error occured")

