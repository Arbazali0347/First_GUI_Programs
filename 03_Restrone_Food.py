from tkinter import *
from tkinter import messagebox
data = 0
counte = 0
def caffe():
        global data
        global counte
        order = {
            "pizza":500,
            "burgur":600,
            "coffee":200,
            "chips":390,
            "layes":200,
            "biryani":200,
            "roll":399,
            "chicken":499,
            "sambosa":100,
            "sanvich":290
            }
        bye = text_Entry.get()
        if bye in order:
            data += spin_text.get() * order[bye]
            counte += spin_text.get()
            messagebox.showinfo("order",f"[ {counte} ]\nSuccessfully")
            print(data)
        else:
            messagebox.showinfo("order","This Food is Not Avalible")
def Total():
        pay_entry.delete(0,10)
        global data
        global counte
        try:
            if data > 0:
                def pay1():
                    global counte
                    global data

                    paise = var.get()
                    if data <= paise:
                        pay.delete(0,100)
                        dataall = data - paise
                        messagebox.showinfo("Payment",f"Thanks\n Retrune Rs{dataall}")
                        pay.destroy()
                        entre1.destroy()
                        button1.config(text="Total",command=Total)
                        total_text.config(text="00")
                        counte = 0
                        data = 0
                    else:
                        messagebox.showinfo("Payment",f"Please Pay\n Rs{data}\nDont This Rs{paise}")
                total_text.config(text=data)
                button1.config(text="Pay",command=pay1)
                var = IntVar()
                pay = Entry(root,font=("Times New Roman",15,"bold"),relief="ridge",textvariable=var,bd=4,)
                pay.place(x=390,y=345,height=35,width=260)
                entre1 = Label(root,text="Enter Paymente",font=("Times New Roman",15,"bold"),bg="red",fg="black",justify=LEFT)
                entre1.place(x=220,y=345,height=35,width=160) 
            else:
                messagebox.showinfo("Peoducts","Please Choice Food")
        except:
            messagebox.showinfo("Peoducts","Please Enter Payment!")

root = Tk()
root.geometry("700x400")
root.config(bg="red")
root.title("Mr Arbaz Restrone")
#------------------------------------------------------
text = Label(root,text="Mr Aro Restrone",font=("Times New Roman",25,"bold"),bg="red",fg="black",justify=LEFT)
text.place(x=10,y=10,height=40,width=280)
text = Label(root,text="*Roll Rs399",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=60,height=30,width=150)
text = Label(root,text="*Chicken Rs499",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=100,height=30,width=150)
text = Label(root,text="*Biryani Rs200",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=140,height=30,width=150)
text = Label(root,text="*Layes Rs200",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=180,height=30,width=150)
text = Label(root,text="*Roll Rs500",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=220,height=30,width=150)
text = Label(root,text="*Burgur Rs700",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=260,height=30,width=150)
text = Label(root,text="*coffee Rs200",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=10,y=300,height=30,width=150)
#----------------------------------------------
text = Label(root,text="*Pizza Rs500",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=60,height=30,width=150)
text = Label(root,text="*Burgur Rs600",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=100,height=30,width=150)
text = Label(root,text="*Biryani Rs400",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=140,height=30,width=150)
text = Label(root,text="*FG Chips Rs390",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=180,height=30,width=150)
text = Label(root,text="*Sabosa Rs100",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=220,height=30,width=150)
text = Label(root,text="*Burgur Rs220",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=260,height=30,width=150)
text = Label(root,text="*Sanvisch Rs290",font=("Times New Roman",15,"bold"),fg="black",justify=LEFT)
text.place(x=180,y=300,height=30,width=150)
#---------------------------------
text_Entry = StringVar()
pay_entry = Entry(root,font=("Times New Roman",15),relief="sunken",textvariable=text_Entry,bd=4)
pay_entry.place(x=390,y=60,height=35,width=260)
#---------------------------------------------------------------
button = Button(root,text="Click",font=("Times New Roman",15,"bold"),relief=RAISED,bg="black",fg="white",command=caffe)
button.place(x=390,y=110,height=35,width=260)
button1 = Button(root,text="Total",font=("Times New Roman",15,"bold"),relief=RAISED,bg="black",fg="white",command=Total)
button1.place(x=390,y=290,height=35,width=260)
total_text1 = Label(root,text="Total",font=("Times New Roman",30),fg="black")
total_text1.place(x=390,y=170,height=35,width=260)

total_text = Label(root,text="00",font=("Times New Roman",30),fg="black")
total_text.place(x=390,y=220,height=35,width=260)

entre = Label(root,text="Enter Your Food",font=("Times New Roman",15,"bold"),bg="red",fg="black",justify=LEFT)
entre.place(x=390,y=30,height=30,width=260)
#---------------------------------------------
spin_text = IntVar()
spin = Spinbox(root,from_=1,to=30,relief="sunken",bd=5,textvariable=spin_text)
spin.place(x=10,y=350,height=30,width=150)
root.mainloop()
