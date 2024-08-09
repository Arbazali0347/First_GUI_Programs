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
        password += password1.get()
        with open("Scrite_Code.txt","w")as f:
            f.write(new)
        with open("Scrite_Password.txt","w")as f:
            f.write(password)
        entry_password.delete(0,20)
        messagebox.showinfo("Scrite Code","The Password Successfully code")
        text_code.insert("1.0",new)
        password_text.destroy()
        entry_password.destroy()
        button.destroy()
    password_text = Label(root,text="New Password:",font=("Time New Roman",15,"bold"),bg="grey",fg="black")
    password_text.place(x=20,y=380,height=30,width=360)
#-------------------------------------------------
    password1 = StringVar()
    entry_password = Entry(root,font=("Time New Roman",13),textvariable=password1)
    entry_password.place(x=20,y=420,height=30,width=360)
#-------------------------------------
    button = Button(root,text="Ok",font=("Time New Roman",15,"bold"),bg="red",fg="black",command=password_fuc)
    button.place(x=20,y=460,height=30,width=360)
    text_code.delete("1.0",END)
dicodes = ""
def dicode():
    def dicodepass():
        news = text_code.get("1.0","end")
        global password
        global dicodes
        with open("Scrite_Password.txt","r")as f:
            content = f.read()
        news = news.split(" ")
        if password1.get() == password or content == password1.get():
            if True:
                messagebox.showinfo("Password","Unlock dicode Successfully")
                password_text.destroy()
                entry_password.destroy()
                button.destroy()
                for word in news:
                    if len(word)>=3:
                        words = word[3:-3]
                        dicodes += words[-1] + words[:-1] + " "
                    else:
                        dicodes += word[::-1] + " "
                text_code.delete("1.0","end")
                text_code.insert("1.0",dicodes)
                print(dicodes)
        else:
            messagebox.showinfo("Password","Password Rong!")
            
    password_text = Label(root,text="Enter Password:",font=("Time New Roman",15,"bold"),bg="grey",fg="black")
    password_text.place(x=20,y=380,height=30,width=360)
#-------------------------------------------------
    password1 = StringVar()
    entry_password = Entry(root,font=("Time New Roman",13),textvariable=password1)
    entry_password.place(x=20,y=420,height=30,width=360)
#-------------------------------------
    button = Button(root,text="Ok",font=("Time New Roman",15,"bold"),bg="red",fg="black",command=dicodepass)
    button.place(x=20,y=460,height=30,width=360)

#    fskrbazasdk fskhaibsdk fskaremsdk fsk0001sdk fskaihsdk fskaldijsdk fskoasdk


root = Tk()
root.geometry("400x500")
root.config(bg="black")
root.title("MR ARO SCRITE CODE")
text = Label(root,text=("MR BLACK ARO"),font=("Times New Roman",30,"bold"))
text.place(x=0,y=20,width=400,height=60)
text_code = Text(root,font=("Times New Roman",15),wrap=WORD)
text_code.place(x=15,y=90,width=370,height=220)
#-------------------------------------------------------
button_code = Button(root,text="Code",font=("Times New Roman",15,"bold"),relief=RAISED,bg="red",command=coder)
button_code.place(x=205,y=320,width=180,height=50)
#--------------------------
button_dicode = Button(root,text="Dicocde",font=("Times New Roman",15,"bold"),relief=RAISED,bg="red",command=dicode)
button_dicode.place(x=20,y=320,width=180,height=50)

root.mainloop()