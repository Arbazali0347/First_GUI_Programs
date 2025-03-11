from tkinter import *
import os
import shutil
from tkinter import messagebox
root = Tk()
root.config(bg="grey")
root.title("file handling App")
root.geometry("400x550")
subfolder_path = ["C:\Mr Aro gaming\DCIM\project"]
o = 1
n = 1
def creat_txt():
    try:
        global n
        global subfolder_path
        file = "".join(subfolder_path)
        file_path = os.path.join(file, f"example{n}.txt")
        with open(file_path,"w")as f:
            f.write("")
        n += 1
        file_box.delete(0,END)
        files = os.listdir("".join(subfolder_path))
        for file in files:
            file_box.insert(END,file)
    except Exception:
        print("Not creat Your Text file!")
        n += 1
def delete():
    global subfolder_path
    try:
        task = str(file_box.get(ANCHOR))
        if task[-4:] == ".txt":
            os.remove(f"{"".join(subfolder_path)}/{task}")
            print("aa")
        else:
            shutil.rmtree(f"{"".join(subfolder_path)}/{task}")
        file_box.delete(0,END)
        files = os.listdir("".join(subfolder_path))
        for file in files:
            file_box.insert(END,file)
    except Exception:
        print("Error File NO!")
def creat_file():
    global o
    try:
        global subfolder_path
        os.makedirs(f"{"".join(subfolder_path)}/newFolder{o}")
        messagebox.showinfo("create","Your Folder Craete succsufully")
        files = os.listdir("".join(subfolder_path))
        o += 1
        file_box.delete(0,END)
        for file in files:
            file_box.insert(END,file)
    except Exception:
        print("Please File Not Avalible!")
        o += 1
def back_file():
    try:
        global subfolder_path
        if len(subfolder_path) > 1:
            subfolder_path = subfolder_path[:-1]
            name_entry.delete("1.0", END)
            name_entry.insert(END,"".join(subfolder_path))
            print(subfolder_path)
            files = os.listdir("".join(subfolder_path))
            file_box.delete(0,END)
            for file in files:
                file_box.insert(END,file)
    except Exception:
        print("Please No back!")
def open_file():
    name_entry.delete("1.0", END)
    try:
        global subfolder_path
        task = str(file_box.get(ANCHOR))
        subfolder_path.append(f"/{task}")
        print(subfolder_path)
        name_entry.insert(END,"".join(subfolder_path))
        files = os.listdir("".join(subfolder_path))
        file_box.delete(0,END)
        for file in files:
            file_box.insert(END,file)
    except Exception:
        print("Please Enter the values")

#----------------------------------------------
#-----Yes No______
def on_button_click():
    # Confirmation box open karo
    task = str(file_box.get(ANCHOR))
    if task == "":
        messagebox.showinfo("selection","please selete the values!")
    else:
        result = messagebox.askyesno("Confirmation", f"Do you want to Delete this {task}?")
        if result:
            # Agar "Yes" select kiya to command run karo
            delete()
        else:
            # Agar "No" select kiya to kuch mat karo
            print("Command canceled.")


title_name = Label(root,text="File Handling",font=("Times New Roman",20,"bold"),bg="black",fg="white")
title_name.place(x=0,y=10,width=400,height=40)

delete_bt = Button(root,text=("Delete"),font=("Times New Roman",15),bg="white",fg="black",relief=RAISED,command=on_button_click)
delete_bt.place(x=0,y=60,width=200,height=30)

ceart_bt = Button(root,text=("Create Folder"),font=("Times New Roman",15),bg="white",fg="black",relief=RAISED,command=creat_file)
ceart_bt.place(x=0,y=90,width=200,height=30)

select_bt = Button(root,text=("Select Add"),font=("Times New Roman",15),bg="white",fg="black",relief=RAISED)
select_bt.place(x=200,y=60,width=200,height=30)

ceart_txt_bt = Button(root,text=("Create txt file"),font=("Times New Roman",15),bg="white",fg="black",relief=RAISED,command=creat_txt)
ceart_txt_bt.place(x=200,y=90,width=200,height=30)

open_bt = Button(root,text=("OPEN"),font=("Times New Roman",15),bg="red",fg="black",relief=RAISED,command=open_file)
open_bt.place(x=0,y=120,width=400,height=30)

name_entry = Text(root,font=("Times New Roman",15),relief="sunken",bd=3)
name_entry.place(x=70,y=160,width=320,height=30)

back_arrow = Button(root,text=("<"),font=("Times New Roman",20,"bold"),bg="white",fg="black",relief=RAISED,command=back_file)
back_arrow.place(x=10,y=160,width=55,height=30)

file_box = Listbox(root,font=("Times New Roman",15),relief="sunken",bd=3)
file_box.place(x=10,y=200,width=380,height=270)

Scrollbar_bt = Scrollbar(root,bg="black")
Scrollbar_bt.place(x=365,y=200,width=25,height=270)
title_name = Label(root,text="File is very important handling your file and\nkeep enjoy",font=("Times New Roman",15),bg="black",fg="white",)
title_name.place(x=0,y=480,width=400,height=70)

file_box.config(yscrollcommand=Scrollbar_bt.set)
Scrollbar_bt.config(command=file_box.yview)

results = os.listdir("C:\Mr Aro gaming\DCIM\project")
for result in results:
    file_box.insert(END, result,)
root.mainloop()