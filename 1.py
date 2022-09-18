from tkinter import*
import os
from PIL import ImageTk
from tkinter import messagebox
root=Tk()
root.title("Welcome")
root.configure(background="light Yellow")
title=Label(text="Choose Restaurant",font=("Times new roman",40,),fg="black",bg="light pink")
title.place(x=0,y=0,relwidth=1)



def indian():
    os.system("south.py")
    
       
def indian1():
    os.system("chinese.py")

def indian2():
    os.system("nonveg.py")

def indian3():
    os.system("street.py")

        
my_img=ImageTk.PhotoImage(file="12.jpg")
my_label=Label(image=my_img)
my_label.place(x=1000,y=100,height="250",width="500")          
a=Button(root,command=indian,text="South Corner",height=2,width=16, font=("Times new roman",14,"bold"),fg="black",bg="cyan")
a.place(x=1000,y=100)

my_i=ImageTk.PhotoImage(file="chinese.jfif")
my_labl=Label(image=my_i)
my_labl.place(x=50,y=100,height="250",width="500")
a1=Button(root,command=indian1,text="MainLand China",height=2,font=("Times new roman",14,"bold"),fg="black",bg="cyan")
a1.place (x=50,y=100)

my1=ImageTk.PhotoImage(file="nv1.jpg")
my_=Label(image=my1)
my_.place(x=50,y=400,height="250",width="500")
           
a2=Button(root,command=indian2,text="Kareems Rolls",height=2,font=("Times new roman",14,"bold"),fg="black",bg="cyan")
a2.place(x=50,y=400)

my=ImageTk.PhotoImage(file="ff.jpg")
my_=Label(image=my)
my_.place(x=1000,y=400,height="250",width="500")
a3=Button(root,command=indian3,text="Street Style Food",height=2,font=("Times new roman",14,"bold"),fg="black",bg="cyan")
a3.place(x=1000,y=400)

root.geometry("1920x1080+0+0")
root.mainloop()
