from tkinter import *
from tkinter.messagebox import askokcancel

def get_date():
    st_name = name_1.get()
    st_urdo = urdo_1.get()
    st_English = English_1.get()
    st_math = math_1.get()
    st_science = science_1.get()
    st_sst = sst_1.get()

    total = st_English + st_math + st_science + st_sst + st_urdo

    per = round(((total/500)*100),4)

    div = ""
    if per >= 60:
        div = "1 ST Div"
    elif per < 60 and per >= 50:
        div = "2 ND Div"
    elif per < 50 and per >= 35:
        div = "3 RD Div"
    else:
        div = "Fail"
    print(total)
    print(per)
    print(div)
    massagebox(st_name,total,per,div)

def massagebox(*date):
    printn_1 = f"""
    Name : {date[0]}
    Total : {date[1]}
    Percentage : {date[2]}
    Division : {date[3]}
    """
    askokcancel(title="Mr Arbaz School",message=printn_1)


School = Tk()
School.title("Arbaz School")
School.geometry("500x540")
School.config(bg="grey")
School.resizable(False,False)
#--------------------------
title = Label(School,text="MR.ARBAZ SCHOOL",font=("Times New Roman",30,"bold"),bg="grey",)
title.place(x=40,y=20,height=40,width=420)
#------------------------------
name = Label(School,text="Student Name :",font=("Times New Roman",20,"bold"),bg="white")
name.place(x=40,y=80,height=30,width=200)
name_1 = StringVar()
name_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=name_1)
name_entry.place(x=270,y=80,height=30,width=200)
#-------------------------------
title2 = Label(School,text="Subject Numbers",font=("Times New Roman",30,"bold"),bg="black",fg="white")
title2.place(x=90,y=130,height=50,width=320)
#-----------------------------------
urdo_1 = DoubleVar()
English_1 = DoubleVar()
sst_1 = DoubleVar()
science_1 = DoubleVar()
math_1 = DoubleVar()

#-----------------------------------
urdo = Label(School,text="Urdo",font=("Times New Roman",20,"bold"),bg="white")
urdo.place(x=40,y=210,height=30,width=200)

urdo_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=urdo_1)
urdo_entry.place(x=270,y=210,height=30,width=200)
#----------------------------------
English = Label(School,text="English",font=("Times New Roman",20,"bold"),bg="white")
English.place(x=40,y=260,height=30,width=200)

English_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=English_1)
English_entry.place(x=270,y=260,height=30,width=200)
#-----------------------------------
math = Label(School,text="Maths",font=("Times New Roman",20,"bold"),bg="white")
math.place(x=40,y=310,height=30,width=200)

math_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=math_1)
math_entry.place(x=270,y=310,height=30,width=200)
#-----------------------------------
Science = Label(School,text="Science",font=("Times New Roman",20,"bold"),bg="white")
Science.place(x=40,y=360,height=30,width=200)

Science_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=science_1)
Science_entry.place(x=270,y=360,height=30,width=200)

#-----------------------------------
sst = Label(School,text="SST",font=("Times New Roman",20,"bold"),bg="white")
sst.place(x=40,y=410,height=30,width=200)

sst_entry = Entry(School,font=("Times New Roman",15,"bold"),bg="white",textvariable=sst_1)
sst_entry.place(x=270,y=410,height=30,width=200)
#---------------------------
# Button
button = Button(School,text="Done",font=("Times New Roman",15,"bold"),bg="white",relief=RAISED,command=get_date)
button.place(x=140,y=470,height=40,width=200)


School.mainloop()