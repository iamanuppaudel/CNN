import tkinter
import os
from tkinter import Tk,Button, Frame, messagebox
from PIL import ImageTk, Image

top = tkinter.Tk()
top.geometry("750x760")
top.title('SLRS')
def predict():
   os.system('python recognise.py')

def about():
	messagebox.showinfo("About Us", "WE are SLRS")

def testmodel():
	os.system('python test_model.py')


B = tkinter.Button(top, text ="Predict", command = predict, bg='grey',height=2,width=50)
B2= tkinter.Button(top, text="About SLRS",command=about,bg='grey', height=2,width=50)
B3= tkinter.Button(top, text="Train Model",bg='grey', height=2,width=50)
B4= tkinter.Button(top, text="Test Model",command=testmodel,bg='grey', height=2,width=50)
img= ImageTk.PhotoImage(Image.open("lbimg.jpg"))
imglabel= tkinter.Label(top, image=img,height=540,width=750)
L = tkinter.Label(top, text="Sign Language Recognition System",  font=("Helvetica",20))


L.grid(row=1,column=0, padx=(80,0), pady=(0,5))
imglabel.grid(row=2,column=0,pady=(0,0),padx=(0,3))
B.grid(row=3,column=0, padx=(80,0),pady=(0,5))
B2.grid(row=4,column=0,padx=(80,0),pady=(0,5))
B3.grid(row=5,column=0,padx=(80,0),pady=(0,5))
B4.grid(row=6,column=0,padx=(80,0))
#L.pack()

#B.pack()

top.mainloop()
