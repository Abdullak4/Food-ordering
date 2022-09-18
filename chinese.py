from tkinter import*
import random
import time;
import datetime
import csv
from tkinter import Tk, StringVar, ttk,messagebox
root=Tk()
root.geometry("1750x750+0+0")
root.title("Chinese")
Tops=Frame(root,width=1550,height=100,bd=12,relief="raise")
Tops.pack(side=TOP)
lblTitle=Label(Tops,font=("ariel",50,"bold"),text="\t MainLand China\t\t")
lblTitle.grid(row=0 , column=0)
btmmainframe=Frame(root,width=1350,height=650,bd=12,relief="raise")
btmmainframe.pack(side=BOTTOM)


f1=Frame(btmmainframe,width=450,height=650,bd=12,relief="raise")
f1.pack(side=LEFT)
f2=Frame(btmmainframe,width=450,height=450,bd=12,relief="raise")
f2.pack(side=LEFT)
f2top=Frame(f2,width=450,height=300,bd=4,relief="raise")
f2top.pack(side=TOP)
f2btm=Frame(f2,width=450,height=300,bd=4,relief="raise")
f2btm.pack(side=BOTTOM)
f3top=Frame(btmmainframe,width=450,height=300,bd=12,relief="raise")
f3top.pack(side=RIGHT)

 
x1=IntVar()
x2=IntVar()
x3=IntVar()
x4=IntVar()
x5=IntVar()
x6=IntVar()
x7=IntVar()
x8=IntVar()
x9=IntVar()
x10=IntVar()
x11=IntVar()
x12=IntVar()
x13=IntVar()
x14=IntVar()
x15=IntVar()
x16=IntVar()
x17=IntVar()
x18=IntVar()
x19=IntVar()
x20=IntVar()
x21=IntVar()
x22=IntVar()
x23=IntVar()

x1.set(0)
x2.set(0)
x3.set(0)
x4.set(0)
x5.set(0)
x6.set(0)
x7.set(0)
x8.set(0)
x9.set(0)
x10.set(0)
x11.set(0)
x12.set(0)
x13.set(0)
x14.set(0)
x15.set(0)
x16.set(0)
x17.set(0)
x18.set(0)
x19.set(0)
x20.set(0)
x21.set(0)
x22.set(0)
x23.set(0)

xGrilledidlis=StringVar()
xMasalaIdli=StringVar()
xRavaMasalaIdli=StringVar()
xSoojiMasalaIdli=StringVar()
xRavaIdli=StringVar()
xSojiIdli=StringVar()
xfriedidli=StringVar()
xravaidlifried=StringVar()
xsoojiFriedidli=StringVar()
xplaneidli=StringVar()
xRavaMasalaDosa=StringVar()
xMasalaDosa=StringVar()
xPlainDosa=StringVar()
xRavaDosa=StringVar()
xSoojiMasalaDosa=StringVar()
xmoj=StringVar()
xlir=StringVar()
xspt=StringVar()
xbm=StringVar()
xcok=StringVar()
xfan=StringVar()
xChange=StringVar()
x22=StringVar()
xSubTotal=StringVar()
xTax=StringVar()
xTotal=StringVar()

 

 

xGrilledidlis.set("0")
xMasalaIdli.set("0")
xRavaMasalaIdli.set("0")
xSoojiMasalaIdli.set("0")
xRavaIdli.set("0")
xSojiIdli.set("0")
xfriedidli.set("0")
xravaidlifried.set("0")
xsoojiFriedidli.set("0")
xplaneidli.set("0")
xRavaMasalaDosa.set("0")
xMasalaDosa.set("0")
xPlainDosa.set("0")
xRavaDosa.set("0")
xSoojiMasalaDosa.set("0")
xmoj.set("0")
xlir.set("0")
xspt.set("0")
xbm.set("0")
xcok.set("0")
xfan.set("0")
xChange.set("0")
x22.set("0")
x23.set("0")
xSubTotal.set("0")
xTax.set("0")
xTotal.set("0")


#==================================================================================#
 

#=====================================frame1=======================================#

 
#==================================================================================#

 

 

 

lblTitle=Label(f1,font=("ariel",18,"bold"),text="Appitizers")
lblTitle.grid(row=0 , column=0)

 

 

Grilledidlis=Checkbutton(f1,text="Crispy Corns Cubes\t\t₹50",variable=x1,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=1,column=0,sticky=W)

 

txtGrilledidlis=Entry(f1, font=('arial',16,'bold'),textvariable=xGrilledidlis,width=6,justify='right').grid(row=1,column=1)          

 

 

 

 

 

MasalaIdli=Checkbutton(f1,text="Chilly cottage cheese\t\t₹80",variable=x2,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=2,column=0,sticky=W)

 

txtMasalaIdli=Entry(f1, font=('arial',16,'bold'),textvariable=xMasalaIdli,width=6,justify='right').grid(row=2,column=1)

 

 

 

 

RavaMasalaIdli=Checkbutton(f1,text="Crackling Spinach\t\t₹70",variable=x3,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=3,column=0,sticky=W)

 

txtRavaMasalaIdli=Entry(f1, font=('arial',16,'bold'),textvariable=xRavaMasalaIdli,width=6,justify='right').grid(row=3,column=1)

 

 

 

 

 

SoojiMasalaIdli=Checkbutton(f1,text="Chilly Potatoes\t\t\t₹100",variable=x4,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=4,column=0,sticky=W)

 

txtSoojiMasalaIdli=Entry(f1, font=('arial',16,'bold'),textvariable=xSoojiMasalaIdli,width=6,justify='right').grid(row=4,column=1)

 

 

 

 

RavaIdli=Checkbutton(f1,text="Rava Idli\t\t\t\t₹110",variable=x5,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=5,column=0,sticky=W)

 

txtRavaIdli=Entry(f1, font=('arial',16,'bold'),textvariable=xRavaIdli,width=6,justify='right').grid(row=5,column=1)

 

 

 

SojiIdli=Checkbutton(f1,text="CornChilyPapers\t\t\t₹80",variable=x6,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=6,column=0,sticky=W)

 

txtSojiIdli=Entry(f1, font=('arial',16,'bold'),textvariable=xSojiIdli,width=6,justify='right').grid(row=6,column=1)

 

 

 

 

friedidli=Checkbutton(f1,text="GiangsChillyPepper\t\t₹80",variable=x7,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=8,column=0,sticky=W)

 

txtfriedidli=Entry(f1, font=('arial',16,'bold'),textvariable=xfriedidli,width=6,justify='right').grid(row=8,column=1)

 

 

ravaidlifried=Checkbutton(f1,text="ChillyPotatoes\t\t\t₹90",variable=x8,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=9,column=0,sticky=W)

 

txtravaidlifried=Entry(f1, font=('arial',16,'bold'),textvariable=xravaidlifried,width=6,justify='right').grid(row=9,column=1)

 

 

 

soojiFriedidli=Checkbutton(f1,text="Corn Dumplings\t\t\t₹100",variable=x9,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=10,column=0,sticky=W)

 

txtsoojiFriedidli=Entry(f1, font=('arial',16,'bold'),textvariable=xsoojiFriedidli,width=6,justify='right').grid(row=10,column=1)

 

 

 

planeidli=Checkbutton(f1,text="VegetableDumplings\t\t₹30",variable=x11,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=12,column=0,sticky=W)

 

Entry(f1, font=('arial',16,'bold'),textvariable=xplaneidli,width=6,justify='right').grid(row=12,column=1)

#==================================================================================#

 

#=====================================frame2=======================================#

 

#==================================================================================#

 

lbldess=Label(f2top,font=("ariel",18,"bold"),text="\tSOUPS")

 

lbldess.grid(row=0 , column=0)

 

 

PlainDosa=Checkbutton(f2top,text="Eight Treasure Soup\t\t₹100",variable=x12,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=1,column=0,sticky=W)

 

txtPlainDosa=Entry(f2top, font=('arial',16,'bold'),textvariable=xPlainDosa,width=6,justify='right').grid(row=1,column=1)

 

 

 

MasalaDosa=Checkbutton(f2top,text="Hot And Sour\t\t\t₹100",variable=x13,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=2,column=0,sticky=W)

 

txtMasalaDosa=Entry(f2top, font=('arial',16,'bold'),textvariable=xMasalaDosa,width=6,justify='right').grid(row=2,column=1)

 

 

 

 

 

RavaDosa=Checkbutton(f2top,text="Sweet Corn\t\t\t₹100",variable=x14,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=3,column=0,sticky=W)

 

txtRavaDosa=Entry(f2top, font=('arial',16,'bold'),textvariable=xRavaDosa,width=6,justify='right').grid(row=3,column=1)

 

 

 

 

 

RavaMasalaDosa=Checkbutton(f2top,text="Lemon Coriender\t\t\t₹100",variable=x15,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=4,column=0,sticky=W)

 

txtRavaMasalaDosa=Entry(f2top, font=('arial',16,'bold'),textvariable=xRavaMasalaDosa,width=6,justify='right').grid(row=4,column=1)

 

 

 

 

 

SoojiMasalaDosa=Checkbutton(f2top,text="Tomatoe Soup\t\t\t₹100",variable=x16,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=5,column=0,sticky=W)

 

txtSoojiMasalaDosa=Entry(f2top, font=('arial',16,'bold'),textvariable=xSoojiMasalaDosa,width=6,justify='right').grid(row=5,column=1)

 

 

 

 

 

#==================================================================================#

 

#=====================================frame3=======================================#

 

#==================================================================================#

 

 

lbldess=Label(f3top,font=("ariel",18,"bold"),text="Noodles&RICE")

 

lbldess.grid(row=0 , column=0)

 

 

cok=Checkbutton(f3top,text="PhadThai\t\t₹40",variable=x17,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=1,column=0,sticky=W)

 

txtcok=Entry(f3top, font=('arial',16,'bold'),textvariable=xcok,width=6,justify='right').grid(row=1,column=1)

 

 

moj=Checkbutton(f3top,text="Stir Fried\t\t₹120",variable=x18,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=2,column=0,sticky=W)

 

txtmoj=Entry(f3top, font=('arial',16,'bold'),textvariable=xmoj,width=6,justify='right').grid(row=2,column=1)

 

bm=Checkbutton(f3top,text="Yaki Udon\t\t₹130",variable=x19,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=3,column=0,sticky=W)

 

txtbm=Entry(f3top, font=('arial',16,'bold'),textvariable=xbm,width=6,justify='right').grid(row=3,column=1)

 

 

 

spt=Checkbutton(f3top,text="Khao Pad\t\t₹180",variable=x20,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=4,column=0,sticky=W)

 

 

txtspt=Entry(f3top, font=('arial',16,'bold'),textvariable=xspt,width=6,justify='right').grid(row=4,column=1)

 

 

lir=Checkbutton(f3top,text="Corn Fried Rice\t\t₹200",variable=x21,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=5,column=0,sticky=W)

 

txtlir=Entry(f3top, font=('arial',16,'bold'),textvariable=xlir,width=6,justify='right').grid(row=5,column=1)

 

fan=Checkbutton(f3top,text="Nasi Goreng\t\t₹30",variable=x22,onvalue=1,offvalue=0,

 

                   font=("ariel",18,"bold")).grid(row=6,column=0,sticky=W)

 

txtfan=Entry(f3top, font=('arial',16,'bold'),textvariable=xfan,width=6,justify='right').grid(row=6,column=1)

 

 

#==================================================================================#

 

#=====================================Frame Button=======================================#

 

#==================================================================================#

 

 

lb1PaymentMethod = Label(f2btm , font=('arial',14, 'bold'), text="Payment Method", bd=10, width= 16, anchor='w')

 

lb1PaymentMethod.grid(row=0,column=0)

 

 


 

cmbPaymentMethod = ttk.Combobox(f2btm , textvariable = x23, state='readonly', font=('arial',10, 'bold'), width= 20)

 

cmbPaymentMethod['value']=('Cash','Master Card','Visa Card','Debit Card')

 

cmbPaymentMethod.current(0)

 

cmbPaymentMethod.grid(row=1,column=0)

 

 

 

lb1SubTotal = Label(f2btm , font=('arial',14, 'bold'),text="SubTotal ", bd=10, anchor='w').grid(row=1 , column=1)

 

txtSubTotal = Entry(f2btm, font=('arial',16,'bold'),textvariable=xSubTotal,width=6,justify='right').grid(row=1,column=2)

 

lb1Total = Label(f2btm , font=('arial',14, 'bold'),text="Total inc Taxes ", bd=10, anchor='w').grid(row =3 , column =1)

 

 

txtTotal =  Entry(f2btm, font=('arial',16,'bold'),textvariable=xTotal,width=6,justify='right').grid(row=3,column=2)

#==================================================================================#

 

#=====================================Frame Button=======================================#

 

#==================================================================================#

 
def order():

   

    if messagebox.showinfo("South Corner","Thank you for ordering " ):
        root.destroy()

        
 

  

 

def exit():

   

    if messagebox.askyesno("South Corner","ARE u sure u want to exit " )== True:

       

        root.destroy()

    else:

        return()

def Reset ():

    xGrilledidlis.set("0")

    xMasalaIdli.set("0")

    xRavaMasalaIdli.set("0")

    xSoojiMasalaIdli.set("0")

    xRavaIdli.set("0")

    xSojiIdli.set("0")

    xfriedidli.set("0")

    xravaidlifried.set("0")

    xsoojiFriedidli.set("0")

    xplaneidli.set("0")

    xRavaMasalaDosa.set("0")

    xMasalaDosa.set("0")

    xPlainDosa.set("0")

    xRavaDosa.set("0")

    xSoojiMasalaDosa.set("0")

    xmoj.set("0")

    xlir.set("0")

    xspt.set("0")

    xbm.set("0")

    xcok.set("0")

    xfan.set("0")

    xChange.set("0")

    xSubTotal.set("0")

    xTotal.set("0")

def costofmeal():
        meal1 = float(xGrilledidlis.get())
        meal2 = float(xMasalaIdli.get())
        meal3 = float(xRavaMasalaIdli.get())
        meal4 = float(xSoojiMasalaIdli.get())
        meal5 = float(xRavaIdli.get())
        meal6 = float(xSojiIdli.get())
        meal7 = float(xfriedidli.get())
        meal8 = float(xravaidlifried.get())
        meal9 = float(xsoojiFriedidli.get())
        meal10 = float(xplaneidli.get())
        meal11 = float(xRavaMasalaDosa.get())
        meal12 = float(xMasalaDosa.get())
        meal13 = float(xPlainDosa.get())
        meal14 = float(xRavaDosa.get())
        meal15 = float(xSoojiMasalaDosa.get())
        meal16 = float(xmoj.get())
        meal17 = float(xlir.get())
        meal18 = float(xspt.get())
        meal19 = float(xbm.get())
        meal20 = float(xcok.get())
        meal21 = float(xfan.get()) 


        iTotal1 =((meal1 * 50)+ (meal2 * 80) +(meal3 * 70) +(meal4 * 100))
        iTotal2 =((meal5 * 110)+ (meal6 * 80) +(meal7 * 80) +(meal8 * 90))
        iTotal3 =((meal9 * 100)+ (meal10 * 30) +(meal11 * 100) +(meal12 * 100))
        iTotal4 =((meal13 * 100)+ (meal14 * 100) +(meal15 * 100) +(meal16 * 120))
        iTotal5 =((meal17 * 200)+ (meal18 * 180) +(meal19 * 130) +(meal20 * 40))
        iTotal6 =((meal21 * 30))

        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5 + iTotal6)
        iTax = (iCost * 2.8)/100
        xSubTotal.set(iCost)
        xTotal.set(iCost + iTax)
        cv_1=xTotal.get()
        cv_2=xSubTotal.get()   
        with open("chinabill.csv",mode="a") as f: 
            w=csv.writer(f,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL) 
            w.writerow([cv_1,cv_2]) 
        




        
btnTotal=Button(f2btm,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5, text="Total ",command= costofmeal).grid(row=4, column=0)

 

btnReset=Button(f2btm,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5, text="Reset",command= Reset).grid(row=4, column=3)

 

btnExit=Button(f2btm,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5, text="Exit",command=exit).grid(row=4, column=1)

 
btnorder=Button(f2btm,padx=16,pady=1, bd=4, fg="black",font=('arial', 16,'bold'), width=5, text="Order",command=order).grid(row=5, column=1)
 

lblspace=Label( f2btm, text="\n\n\n\n\n\n\n")

 

lblspace.grid(row =5, column=0)

 

 

 

 

 

            

 

 

 

 

 

 

 

 

            

 

 

 

 

 

 

 

 

            

 

root.mainloop()
