from Tkinter import *
##from PIL import Image
import PIL.Image
from PIL import ImageTk
import sqlite3,csv
import tkMessageBox
def train():
    import train_network
def generate():
	db=sqlite3.connect("melanoma.db")
        c=db.cursor()
	query="select r.id,r.name,r.age,r.phone,r.email,res.melornot,res.date from regis r join result res on r.id=res.userid;"
	c.execute(query)
        result=c.fetchall()
	#for i in result
	with open('data.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["Id","Name","Age","Phone","Email","Melanoma or not","Date"])
            writer.writerows(result)
        db.close()
        print "success"
	tkMessageBox.showinfo("Status", "Success")
def admain():
    top =Toplevel()
    top.title("Index")
    top.configure(background='white')	

    fp = open("de.jpg","rb")
    img_ar = PIL.Image.open(fp)
    ph_ar = ImageTk.PhotoImage(img_ar)
    lbl_ar = Label(top,image=ph_ar)
    lbl_ar.image = ph_ar
    btn_hs=Button(top,text="Train the system",height="0",width="15",command=train)
    btn_fs=Button(top,text="Generate Result",height="0",width="15",command=generate)

    lbl_ar.grid(row=1,columnspan=5)
    btn_hs.grid(row=0,column=1)
    btn_fs.grid(row=0,column=3)

    top.mainloop()
#admain()
