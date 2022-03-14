import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Melanoma")
window.configure(background='grey')

def preprocess():
    from train_network import *
def test():
    from melanomatesting import *



path = "mel.jpg"
size=700,500
im=Image.open(path)
img= im.resize(size, Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)


panel = tk.Label(window, image = img)

panel.pack(side = "bottom", fill = "both", expand = "yes")

b1=tk.Button(panel,text="Train The System", command=preprocess)
b1.pack(side="left")
b1.place(x=150,y=400)

b3=tk.Button(panel,text="Test the system", command=test)
b3.pack(side="left")
b3.place(x=450,y=400)


window.geometry('700x500')
window.mainloop()
