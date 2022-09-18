from tkinter import *
import os
from PIL import ImageTk
from tkinter import messagebox 
import time
import csv




class Login_System:
    def __init__(self,root):
       self.root=root
       self.root.title("spring food court")
       self.root.geometry("1920x1080+0+0")
       self.img=ImageTk.PhotoImage(file="7.jpg")
       self.img_Label=Label(image=self.img,bd=0)
       self.img_Label.place(x=00,y=00)
       
       #============================Lables and entries for Gui============================

       title=Label(text="Sign Up",font=("Times new roman",40,),bd=10,relief=GROOVE,bg="light yellow")
       title.place(x=0,y=0,relwidth=1)

       lbl_user=Label(text="Name:",font=("Times new roman",24,"bold"),bg="orange")
       lbl_user.place(x=500,y=200)

       self.txt_user=Entry(font=("times new roman",20),bg="white",bd=5,relief=GROOVE)
       self.txt_user.place(x=700,y=200,width=250,height=40)
       
       lbl_mobile=Label(text="Mobile:",font=("Times new roman",24,"bold"))
       lbl_mobile.place(x=500,y=300)

       self.txt_mobile=Entry(font=("times new roman",20),bg="white",bd=5,relief=GROOVE)
       self.txt_mobile.place(x=700,y=300,width=250,height=40)
       

       lbl_add=Label(text="Address:",font=("Times new roman",24,"bold"))
       lbl_add.place(x=500,y=400)

       self.txt_add=Entry(font=("times new roman",20),bg="white",bd=5,relief=GROOVE)
       self.txt_add.place(x=700,y=400,width=250,height=40)

       
       

        #==========================================Button=================================
       Login_btn_emp=Button(self.root,command=self.login_function,text="ENter",width=25,height=2,font=("Times new roman",14,"bold"),fg="black",bg="Light yellow")
       Login_btn_emp.place(x=645,y=450)
      

        #=========================================Clock & Date=============================

       def clock():
           hour=time.strftime("%I")
           minute=time.strftime("%M")
           second=time.strftime("%S")

           clock_lable.config(text=hour + ':' + minute + ':' + second)
           clock_lable.after(1000,clock)
       
       clock_lable=Label(root, text="", font=("Times new roman",20))
       clock_lable.place(x=15,y=35)
       clock()

       Date_lable=Label(root,text="Date:8/1/2021",font=("Times new roman",15,"bold"))
       Date_lable.place(x=15,y=10)

    #============================Button function=================================
    def login_function(self):
        if self.txt_user.get()=="" or self.txt_mobile.get()=="" or self.txt_add.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            os.system("1.py")
        cv_1= self.txt_user.get()
        cv_2=self.txt_mobile.get()
        cv_3=self.txt_add.get()
        with open("user.csv",mode="a") as f: 
            w=csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL) 
            w.writerow([cv_1,cv_2,cv_3])
            
root=Tk()
obj=Login_System(root)
root.mainloop()
