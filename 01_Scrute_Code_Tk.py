from tkinter import *
from tkinter import messagebox
password = ""
new = ""
def coder():
    global new
    code = text_code.get("1.0","end")
    coder = code.split(" ")
    if True:
        for word in coder:
            if len(word)>=3:
                s1 = "fsk"
                s2 = "sdk"
                new += s1 + word[1:] + word[0] + s2 + " "
            else:
                new += word[::-1] + " "
    def password_fuc():
        global password
        if password1.get() == password2.get():
            root1.destroy()
            messagebox.showinfo("Counfrom Password","Code Successfully")
            password += password1.get()
            text_dicode.delete("1.0","end")
            text_dicode.insert("1.0",new)
            with open("Scrite_Code.txt","w")as f:
                f.write(new)
            with open("Scrite_Password.txt","w")as f:
                f.write(password)
        else:
            messagebox.showinfo("Counfrom Password","Counfrom Password Rong!")

    root1 = Toplevel(root)
    root1.geometry("400x200")
    root1.config(bg="grey")
    root1.title("Dicode Password") 
    password_text = Label(root1,text="New Password:",font=("Time New Roman",15,"bold"),bg="grey",fg="black")
    password_text.place(x=20,y=20,height=30,width=360)
#-------------------------------------------------
    password1 = StringVar()
    entry_password = Entry(root1,font=("Time New Roman",13),textvariable=password1)
    entry_password.place(x=20,y=50,height=30,width=360)
    password_text1 = Label(root1,text="Counfrom:",font=("Time New Roman",15,"bold"),bg="grey",fg="black")
    password_text1.place(x=20,y=85,height=30,width=360)
#-----------------------------------
    password2 = StringVar()
    entry_password1 = Entry(root1,font=("Time New Roman",13),textvariable=password2)
    entry_password1.place(x=20,y=115,height=30,width=360)
#-------------------------------------
    button = Button(root1,text="Ok",font=("Time New Roman",15,"bold"),bg="black",fg="white",command=password_fuc)
    button.place(x=20,y=155,height=30,width=360)
    text_code.delete("1.0",END)
dicodes = ""
def dicode():
    def dicodepass():
        global password
        global dicodes
        with open("Scrite_Password.txt","r")as f:
                content = f.read()
        news = text_code.get("1.0","end")
        news = news.split(" ")
        if password1.get() == password or content == password1.get():
            root2.destroy()
            if True:
                for word in news:
                    if len(word)>=3:
                        words = word[3:-3]
                        dicodes += words[-1] + words[:-1] + " "
                    else:
                        dicodes += word[::-1] + " "
            root.destroy()
            messagebox.showinfo("The Message",dicodes)
            # text_dicode.delete("1.0",END)
            # text_dicode.insert("1.0",dicodes)
        else:
            messagebox.showinfo("Password","Password Rong!")
    root2 = Toplevel(root)
    root2.geometry("400x200")
    root2.config(bg="grey")
    root2.title("Dicode Password") 
    password_text1 = Label(root2,text="Enter Password:",font=("Time New Roman",15,"bold"),bg="grey",fg="black")
    password_text1.place(x=20,y=35,height=30,width=360)
    password1 = StringVar()
    entry_dipassword = Entry(root2,font=("Time New Roman",13),textvariable=password1)
    entry_dipassword.place(x=20,y=65,height=30,width=360)
    button = Button(root2,text="Ok",font=("Time New Roman",15,"bold"),bg="black",fg="white",command=dicodepass)
    button.place(x=20,y=145,height=30,width=360)
    text_dicode.delete("1.0","end")
    
#    fskrbazasdk fskhaibsdk fskaremsdk fsk0001sdk fskaihsdk fskaldijsdk fskoasdk


root = Tk()
root.geometry("400x500")
root.config(bg="black")
root.title("MR ARO SCRITE CODE")
text = Label(root,text=("MR BLACK ARO"),font=("Times New Roman",30,"bold"))
text.place(x=0,y=20,width=400,height=60)
text_code = Text(root,font=("Times New Roman",15),wrap=WORD,)
text_code.place(x=15,y=100,width=370,height=170)
text_dicode = Text(root,font=("Times New Roman",15),wrap=WORD)
text_dicode.place(x=15,y=340,width=370,height=150)
#-------------------------------------------------------
button_code = Button(root,text="Code",font=("Times New Roman",15,"bold"),relief=RAISED,bg="red",command=coder)
button_code.place(x=205,y=280,width=180,height=50)
#--------------------------
button_dicode = Button(root,text="Dicocde",font=("Times New Roman",15,"bold"),relief=RAISED,bg="red",command=dicode)
button_dicode.place(x=20,y=280,width=180,height=50)

root.mainloop()