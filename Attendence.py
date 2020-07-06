from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
from tkinter import *
import time
import datetime


#----------------------------------------------------------------------Frames---------------------------------------------------------------------------------------------

#Part 1:Creating the main Frame which will going to display the Register
#devide whole frame into two part-left and right
root=Tk()
root.title("Attendence Register")
root.geometry('1350x650+0+0')
root.configure(background="black")
 
LeftMayFrame=Frame(root,width=1000,height=650,bd=8,relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(root,width=350,height=650,bd=8,relief="raise")
RightMayFrame.pack(side=RIGHT)


#Part2:Devide the left frame into two part -top and bottom
LeftMayFrame1=Frame(LeftMayFrame,width=1000,height=100,bd=8,relief="raise")
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=1000,height=550,bd=8,relief="raise")
LeftMayFrame2.pack(side=TOP)

RightMayFrame1=Frame(RightMayFrame,width=350,height=215,bd=8,relief="raise")
RightMayFrame1.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=350,height=415,bd=8,relief="raise")
RightMayFrame2.pack(side=TOP)


#to add the picture to the right side
#-------------------------------------------------Canvas---------------------------
cont1=Canvas(RightMayFrame2,width=350,height=425,bg="black")
cont1.grid(row=0,column=0)
image5=PhotoImage(file="MNIT.png")
cont1.create_image(200,200,image=image5)
#-----------------------------------------------------------------
cont =Canvas(RightMayFrame1,width=350,height=215)
cont.grid(row=0,column=0)
image1=PhotoImage(file="MNIT.png")
image=cont.create_image(200,200,image=image1)


def pic1():
 image=cont.create_image(200,200,image=image1)
image2=PhotoImage(file="MNIT.png")

def pic1():
 image=cont.create_image(200,200,image=image1)
image2=PhotoImage(file="MNIT.png")
def pic2():
 image=cont.create_image(200,200,image=image2)
image3=PhotoImage(file="MNIT.png")
def pic3():
 image=cont.create_image(200,200,image=image3)
image4=PhotoImage(file="MNIT.png")
def pic4():
 image=cont.create_image(200,200,image=image4)
image5=PhotoImage(file="MNIT.png")
def pic5():
 image=cont.create_image(200,200,image=image5)
image6=PhotoImage(file="MNIT.png")
def pic6():
 image=cont.create_image(200,200,image=image6)
image7=PhotoImage(file="MNIT.png")
def pic7():
 image=cont.create_image(200,200,image=image7)
image8=PhotoImage(file="MNIT.png")
def pic8():
 image=cont.create_image(200,200,image=image8)
image9=PhotoImage(file="MNIT.png")
def pic9():
 image=cont.create_image(200,200,image=image9)
image10=PhotoImage(file="MNIT.png")
def pic10():
 image=cont.create_image(200,200,image=image10)


#----------------------------------------------------------------------Variables declaration------------------------------------------------------------------------------


#Part3:include sone component on to the top part of the left side frame
DateofOrder=StringVar()
value0=StringVar()
value1=StringVar()
value2=StringVar()
value3=StringVar()
value4=StringVar()
value5=StringVar()
value6=StringVar()
value7=StringVar()
value8=StringVar()
value9=StringVar()
value10=StringVar()

#----------------------------------------------------Fill up ComboBox---------------------------------------------------------
#click events
def Mark_Register():
 if value0.get()=="/":#present
  value1.set("/")
  value2.set("/")
  value3.set("/")
  value4.set("/")
  value5.set("/")
  value6.set("/")
  value7.set("/")
  value8.set("/")
  value9.set("/")
  value10.set("/")
 elif (value0.get()=="0"):#a
  value1.set("0")
  value2.set("0")
  value3.set("0")
  value4.set("0")
  value5.set("0")
  value6.set("0")
  value7.set("0")
  value8.set("0")
  value9.set("0")
  value10.set("0")
 elif (value0.get()=="S"):
  value1.set("S")
  value2.set("S")
  value3.set("S")
  value4.set("S")
  value5.set("S")
  value6.set("S")
  value7.set("S")
  value8.set("S")
  value9.set("S")
  value10.set("S")
 elif (value0.get()=="A"):
  value1.set("A")
  value2.set("A")
  value3.set("A")
  value4.set("A")
  value5.set("A")
  value6.set("A")
  value7.set("A")
  value8.set("A")
  value9.set("A")
  value10.set("A")
 elif (value0.get()=="L"):
  value1.set("L")
  value2.set("L")
  value3.set("L")
  value4.set("L")
  value5.set("L")
  value6.set("L")
  value7.set("L")
  value8.set("L")
  value9.set("L")
  value10.set("L")
 elif (value0.get()==" "):
  value1.set(" ")
  value2.set(" ")
  value3.set(" ")
  value4.set(" ")
  value5.set(" ")
  value6.set(" ")
  value7.set(" ")
  value8.set(" ")
  value9.set(" ")
  value10.set(" ")




#----------------------------------------------------Reset---------------------------------------------------------

def Reset():
 value0.set("")
 value1.set("")
 value2.set("")
 value3.set("")
 value4.set("")
 value5.set("")
 value6.set("")
 value7.set("")
 value8.set("")
 value9.set("")
 value10.set("")

#----------------------------------------------------Exit---------------------------------------------------------

def qExit():
 qExit=messagebox.askyesno("Exit System ","Do you want to quit?")
 if qExit > 0:
  root.destroy()
  return


#------------------------------------------------------------------------Components---------------------------------------------------------------------------------------
DateofOrder.set(time.strftime("%d/%m/%Y"))

#--------------------------------------------------------------------LeftMayFrame1-------------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame1,font=('arial',10,'bold'),text="No.",bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblStudentNo=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student No.",bd=16)
lblStudentNo.grid(row=0,column=1,sticky=W)
lblStudentName=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Student Name",bd=16)
lblStudentName.grid(row=0,column=2,sticky=W)
lblCourseCode=Label(LeftMayFrame1,font=('arial',10,'bold'),text="Course Code",bd=16)
lblCourseCode.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame1,textvariable=value0,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnFill=Button(LeftMayFrame1,text='Fill',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=Mark_Register).grid(row=0,column=5)
btnReset=Button(LeftMayFrame1,text='Reset',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=Reset).grid(row=0,column=6)
btnExit=Button(LeftMayFrame1,text='Exit',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=qExit).grid(row=0,column=7)


lblDateofOrder=Label(LeftMayFrame1,font=('arial',10,'bold'),textvariable=DateofOrder,padx=2,pady=2,bd=2,fg='black',bg='white',relief='sunken')
lblDateofOrder.grid(row=0,column=8,sticky=W)


#--------------------------------------------------------------------LeftMayFrame2(row1)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1",bd=16)
lblNo.grid(row=0,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1001",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=0,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Amit Parmar",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=0,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1789",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=0,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value1,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=0,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=0,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=0,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=0,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=0,column=8)


#--------------------------------------------------------------------LeftMayFrame2(row2)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="2",bd=16)
lblNo.grid(row=1,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1002",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=1,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Twinkal",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=1,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=1,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value2,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=1,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=1,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=1,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=1,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=1,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row3)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="3",bd=16)
lblNo.grid(row=3,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1003",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=3,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Kajal",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=3,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="2005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=3,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value3,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=3,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=3,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=3,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=3,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=3,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row4)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="4",bd=16)
lblNo.grid(row=4,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1004",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=4,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Shweta",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=4,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="4005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=4,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value4,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=4,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=4,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=4,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=4,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=4,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row5)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="5",bd=16)
lblNo.grid(row=5,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1005",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=5,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Hiten",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=5,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="5005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=5,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value5,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=5,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=5,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=5,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=5,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=5,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row6)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="6",bd=16)
lblNo.grid(row=6,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1006",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=6,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Sakshi",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=6,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="6005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=6,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value6,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=6,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=6,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=6,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=6,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=6,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row7)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="7",bd=16)
lblNo.grid(row=7,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1007",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=7,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Pooja",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=7,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="7005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=7,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value7,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=7,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=7,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=7,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=7,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=7,column=8)

#--------------------------------------------------------------------LeftMayFrame2(row8)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="8",bd=16)
lblNo.grid(row=8,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1008",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=8,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Pratibha",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=8,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="8005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=8,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value8,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=8,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=8,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=8,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=8,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=8,column=8)


#--------------------------------------------------------------------LeftMayFrame2(row9)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="9",bd=16)
lblNo.grid(row=9,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1009",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=9,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Preksha",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=9,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="9005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=9,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value9,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=9,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=9,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=9,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=9,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=9,column=8)



#--------------------------------------------------------------------LeftMayFrame2(row10)---------------------------------------------------------------------------------
#creating the first row
lblNo=Label(LeftMayFrame2,font=('arial',10,'bold'),text="10",bd=16)
lblNo.grid(row=10,column=0,sticky=W)
lblStudentNo_No_1=Label(LeftMayFrame2,font=('arial',10,'bold'),text="1010",padx=2,pady=2,bd=2,fg='black',width=18)
lblStudentNo_No_1.grid(row=10,column=1,sticky=W)
lblStudent_Name=Label(LeftMayFrame2,font=('arial',10,'bold'),text="Noor",padx=2,pady=2,bd=2,fg='black',width=12)
lblStudent_Name.grid(row=10,column=2,sticky=W)
lblCourse_Code=Label(LeftMayFrame2,font=('arial',10,'bold'),text="10005",padx=2,pady=2,bd=2,fg='black',width=12)
lblCourse_Code.grid(row=10,column=3,sticky=W)

box=ttk.Combobox(LeftMayFrame2,textvariable=value10,state='readonly')
box['values']=(' ','/','L','0','A','S')
box.current(0)
box.grid(row=10,column=4)

btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=12,height=1,command=pic1).grid(row=10,column=5)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic2).grid(row=10,column=6)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic3).grid(row=10,column=7)
btnSpace=Button(LeftMayFrame2,text='',padx=2,pady=2,bd=2,fg="black",font=('arial',10,'bold'),width=11,height=1,command=pic4).grid(row=10,column=8)

root.mainloop()



