from tkinter import messagebox
import os
from tkinter import *
from tkinter import filedialog

def creat_file():
    text = taxt_1.get()
    try:
        with open(text,"x")as f:
            print("Successfully")
            messagebox.showinfo("File Create","File Create Successfully")
    except FileExistsError:
        messagebox.showinfo("File Create","File All ready Exists!")
    except Exception:
        messagebox.showinfo("File Create","File Not Exists!")
def view_file():
    a = 1
    files = os.listdir()
    for i in files:
        print(f"{a}: {i}")
        a += 1
def delete_file():
    text = taxt_1.get()
    try:
        os.remove(text)
        messagebox.showinfo("File Delete","File Deleted Successfully")
    except FileNotFoundError:
        messagebox.showinfo("File Delete",f"[{text}] File Not Exists!")
    except Exception:
        messagebox.showinfo("File Delete","File Not Exists!")
def read_file():
    text = taxt_1.get()
    try:
        with open(text,"r")as f:
            content = f.read()
            print(f"Your File Content\n{content}")
            messagebox.showinfo("File Content",content)
    except FileNotFoundError:
        messagebox.showinfo("File content","File Not Exists!")
    except Exception:
        messagebox.showinfo("File content","File Not!")
def New_File():
    def save():
        try:
            with open(taxt_1.get(),"w")as f:
                f.write(text2.get(1.0, END))
                messagebox.showinfo("File Delete","File Deleted Successfully")
        except FileNotFoundError:
            messagebox.showinfo("File Save","File Not Exists!")
        except Exception as f:
            messagebox.showinfo("File Save",f)
    root1 = Toplevel(root)
    root1.title("Edit File")
    root1.geometry("300x300")
    root1.config(bg="grey")
    text2= Text(root1,wrap=WORD,font=("Time New Roman",10,"bold"),fg="black",)
    text2.place(x=10,y=10,width=280,height=200)

    button1 = Button(root1,text="Clock Save",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=save)
    button1.place(x=50,y=230,width=200,height=50)
    
    root1.mainloop()

#==========================================

root = Tk()
root.title("File App")
root.geometry("400x500")
root.config(bg="grey")

taxt_1 = StringVar()

button = Button(root,text="File Create",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=creat_file)
button.place(x=100,y=50,width=200,height=50)
button = Button(root,text="Files View",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=view_file)
button.place(x=100,y=120,width=200,height=50)
button = Button(root,text="File Delete",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=delete_file)
button.place(x=100,y=190,width=200,height=50)
button = Button(root,text="File Read",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=read_file)
button.place(x=100,y=260,width=200,height=50)
button = Button(root,text="New File Edit",font=("Times New Roman",20),bg="black",fg="white",relief=RAISED,command=New_File)
button.place(x=100,y=330,width=200,height=50)
#=============================================
label = Label(root,text="Enter File Nama",font=("Times New Roman",17),fg="black",bg="grey")
label.place(x=95,y=390,width=210,height=50)
label_entry = Entry(root,font=("Time New Roman",15,"bold"),fg="black",textvariable=taxt_1)
label_entry.place(x=85,y=430,width=230,height=30)
root.mainloop()

        
