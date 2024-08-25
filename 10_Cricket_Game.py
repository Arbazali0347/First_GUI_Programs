from tkinter import *
from tkinter import messagebox
import random
import pyttsx3
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
#--------------------------------------
c = ""
v = ""
computer = random.choice(["A","B"])
if computer == "A":
    c += "B"
else:
    c += "A"
#-----------------------------
#---------------------------------------
oo = ""
matche = -1
target = 0
score = 0
out = 0
bolls = 0
over = 0
#-------------------------------------------------------------------------------------
def chack():
    global c
    global bolls
    global over
    global score
    global out
    global target
    global matche
    global computer
    if matche == -1:
        if over == 1 or out == 10:
            target += score + 1
            matche += 1
            speak(f"Target {target}\nScore {score}out{out}\nOvers {over}")
            messagebox.showinfo("targer",f"Target {target}\nScore {score}/{out}\nOvers {bolls}/{over}")
            target_text = Label(root,text=f"Target : {target}",font=("Times New Roman",20,"bold"),fg="black")
            target_text.place(x=265,y=350,width=180,height=40)
            score = 0
            over = 0
            bolls = 0
            out = 0
            bolls += 1
            overs = Label(root,text=f"{bolls}/{over}",font=("Times New Roman",30,"bold"),fg="black")
            overs.place(x=495,y=95,width=200,height=40)
            score_text = Label(root,text=f"{score}/{out}",font=("Times New Roman",30,"bold"),fg="black")
            score_text.place(x=5,y=95,width=200,height=40)
            print(target)
    elif matche == 0:
        if score >= target:
            speak("Batting Team You Win")
            messagebox.showinfo("WIN",f"** Batting Team ***\nYou Win\nScore {score}/{out}\nTarget{target}\nOvers {bolls}/{over}")
            print("finish")
    elif matche == 0:
        if over == 1 or out == 10:
            speak("Bolling Team You Win")
            messagebox.showinfo("WIN",f"** Bolling Team ***\nYou Win\nScore {score}/{out}\nTarget{target}\nOvers {bolls}/{over}")
            print("finish")
            root.destroy()
    else:
        print(score)
def set_score(score):
    global bolls
    set_text = Label(root,text=score,font=("Times New Roman",25,"bold"),bg="grey")
    set_text.place(x=285,y=250,width=150,height=50)
def set_1(text):
    set1 = Label(root,text=text,font=("Times New Roman",25,"bold"),bg="white")
    set1.place(x=370,y=170,width=150,height=50)
def set_2(text):
    set = Label(root,text=text,font=("Times New Roman",25,"bold"),bg="white")
    set.place(x=180,y=170,width=150,height=50)
#-------------------------------------------------------------------------------------
def out_boll():
    global oo
    oo = "out"
    set_1("Out")
    chack()
def miss_boll():
    global oo
    oo = "out"
    set_1("Miss")
    chack()
def bownser_boll():
    global oo
    oo = "out"
    set_1("Bownser")
    chack()
def Yurker_boll():
    global oo
    oo = "out"
    set_1("Yorker")
    chack()
#---------------------------------------
def hit_boll():
    set_2("HIT")
    global score
    global out
    outer = random.choice([6,"catch",4,"out","bold",1,2,3,0,6,oo,6,4,3,2,0,3,3,4,6,0,4,1,2,0])
    if outer == "out" or outer == "catch" or outer == "bold":
        out += 1
        speak("out")
        messagebox.showinfo("Match",f"** {outer} **")
    elif outer == 6:
        set_score(outer)
        score += outer
        speak("6")
        messagebox.showinfo("Match",f"** {outer} **")
    elif outer == 4:
        speak("4")
        set_score(outer)
        score += outer
        messagebox.showinfo("Match",f"** {outer} **")
    else:
        score += outer
        set_score(outer)
    chack()
    matchs()
    set_score(outer)
def drow_boll():
    set_2("DROW")
    global score
    global out
    outer = random.choice(["out",1,2,3,0,0,3,2,1,oo,2,1,0,1,])
    if outer == "out":
        # speak("out")
        out += 1
        messagebox.showinfo("Match",f"** {outer} **")
    else:
        score += outer
    chack()
    matchs()
    set_score(outer)
def slite_boll():
    set_2("SLITE")
    global score
    global out
    outer = random.choice(["ciper catch",4,"out",1,2,3,0,4,3,2,3,oo])
    if outer == "out" or outer == "ciper catch":
        out += 1
        speak("out")
        messagebox.showinfo("Match",f"** {outer} **")
    elif outer == 4:
        set_score(outer)
        score += outer
        speak("4")
        messagebox.showinfo("Match",f"** {outer} **")
    else:
        score += outer
        set_score(outer)
    chack()
    matchs()
    set_score(outer)
def runs_boll():
    set_2("RUNS")
    global score
    global out
    outer = random.choice(["out",1,2,3,0,oo])
    if outer == "out":
        out += 1
        speak("out")
        messagebox.showinfo("Match",f"** {outer} **")
    else:
        score += outer
        set_score(outer)
    chack()
    matchs()
    set_score(outer)
#-----------------------------------------------------------
def matchs():
        global over
        global bolls
        vs_text = Label(root,text="A vs B",font=("Times New Roman",20,"bold"),fg="black")
        vs_text.place(x=285,y=70,width=130,height=30)
        score1 = Label(root,text=f"SCORE",font=("Times New Roman",15,"bold"),fg="black",bg="grey",)
        score1.place(x=5,y=70,width=80,height=25)
        score_text = Label(root,text=f"{score}/{out}",font=("Times New Roman",30,"bold"),fg="black")
        score_text.place(x=5,y=95,width=200,height=40)

        overs_text = Label(root,text=f"OVERS",font=("Times New Roman",15,"bold"),fg="black",bg="grey",)
        overs_text.place(x=615,y=70,width=80,height=25)
        overs = Label(root,text=f"{bolls}/{over}",font=("Times New Roman",30,"bold"),fg="black")
        overs.place(x=495,y=95,width=200,height=40)
        if bolls == 6:
            over += 1
            bolls = 0
        else:
            bolls += 1
        #------------------------------------------
        out_bt = Button(root,text="Out",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=out_boll)
        out_bt.place(x=540,y=170,width=150,height=30)
        miss_bt = Button(root,text="Miss",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=miss_boll)
        miss_bt.place(x=540,y=220,width=150,height=30)
        bownser_bt = Button(root,text="bownser",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=bownser_boll)
        bownser_bt.place(x=540,y=270,width=150,height=30)
        yarker_bt = Button(root,text="Yorker",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=Yurker_boll)
        yarker_bt.place(x=540,y=320,width=150,height=30)
        #--------------------------------------------
        hit_bt = Button(root,text="Hit",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=hit_boll)
        hit_bt.place(x=10,y=170,width=150,height=30)
        drow_bt = Button(root,text="Drow",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=drow_boll)
        drow_bt.place(x=10,y=220,width=150,height=30)
        slite_bt = Button(root,text="Slite",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=slite_boll)
        slite_bt.place(x=10,y=270,width=150,height=30)
        runs_bt = Button(root,text="Runs",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=runs_boll)
        runs_bt.place(x=10,y=320,width=150,height=30)
        #--------------------------------------------
        if v == "bat":
            team_bat = Label(root,text=computer,font=("Times New Roman",15,"bold"),fg="black",bg="green",)
            team_bat.place(x=125,y=70,width=80,height=25)
            team_bol = Label(root,text=c,font=("Times New Roman",15,"bold"),fg="black",bg="blue",)
            team_bol.place(x=495,y=70,width=80,height=25)
        else:
            team_bol = Label(root,text=computer,font=("Times New Roman",15,"bold"),fg="black",bg="blue",)
            team_bol.place(x=495,y=70,width=80,height=25)
            team_bat = Label(root,text=c,font=("Times New Roman",15,"bold"),fg="black",bg="green",)
            team_bat.place(x=125,y=70,width=80,height=25)
        #-------------------------------------------
        set = Label(root,text="***",font=("Times New Roman",25,"bold"),bg="white")
        set.place(x=180,y=170,width=150,height=50)
        set1 = Label(root,text="***",font=("Times New Roman",25,"bold"),bg="white")
        set1.place(x=370,y=170,width=150,height=50)
        #-------------------------------------------
        set_text = Label(root,text="*****",font=("Times New Roman",25,"bold"),bg="grey")
        set_text.place(x=285,y=250,width=150,height=50)

def Toss_choice():
    def bolling():
        global v
        messagebox.showinfo("Cricker","**Ok**\nYour Bolling")
        hat_toos.destroy()
        tall_toos.destroy()
        vs_text.destroy()
        Toos_text.destroy()
        Toss_win.destroy()
        choice1_text.destroy()
        choice2_text.destroy()
        choice_00_text.destroy()
        choice1_00_text.destroy()
        batting_bt.destroy()
        bolling_bt.destroy()
        v += "boll"
        matchs()
    def batting():
        global v
        messagebox.showinfo("Cricker","**Ok**\nYour Batting")
        hat_toos.destroy()
        tall_toos.destroy()
        vs_text.destroy()
        Toos_text.destroy()
        Toss_win.destroy()
        choice1_text.destroy()
        choice2_text.destroy()
        choice_00_text.destroy()
        choice1_00_text.destroy()
        batting_bt.destroy()
        bolling_bt.destroy()
        v += "bat"
        matchs()
    Toos_text.config(text="** TOSS WIN **",font=("Times New Roman",25,"bold"))
    Toss_win.config(text=computer)
    batting_bt = Button(root,text="Batting",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=batting)
    batting_bt.place(x=250,y=290,width=200,height=40)
    bolling_bt = Button(root,text="Bolling",font=("Times New Roman",20,"bold"),relief=RAISED,bg="red",command=bolling)
    bolling_bt.place(x=250,y=340,width=200,height=40)
a = 0
def Had():
    global a
    choice_00_text.config(text="A = Hade")
    if a == 1:
        choice_00_text.config(text="B = Hade")
        Toss_choice()
    a += 1
def tall():
    global a
    if a == 1:
        choice1_00_text.config(text="B = Tall")
        Toss_choice()
    if a == 0:
        choice1_00_text.config(text="A = Tall")
    a += 1
root = Tk()
root.geometry("700x400")
root.config(bg="grey")
root.title("Cricket")
#-----------------------------
title = Label(root,text="Wellcom To Arbaz Cricket Stadiam",font=("Times New Roman",20,"bold"),bg="black",fg="white")
title.place(x=0,y=10,width=700,height=50)
#----------------------------------------
hat_toos = Button(root,text="Hat",font=("Times New Roman",30,"bold"),relief=RAISED,bg="red",command=Had)
hat_toos.place(x=20,y=80,width=160,height=160)
tall_toos = Button(root,text="Tall",font=("Times New Roman",30,"bold"),relief=RAISED,bg="red",command=tall)
tall_toos.place(x=520,y=80,width=160,height=160)
#-----------------------------------------
vs_text = Label(root,text="A vs B",font=("Times New Roman",50,"bold"),fg="black")
vs_text.place(x=250,y=80,width=220,height=70)
#-----------------------------------------
Toos_text = Label(root,text="TOSS",font=("Times New Roman",40,"bold"),fg="black",bg="grey")
Toos_text.place(x=225,y=170,width=250,height=50)
Toss_win = Label(root,text="**",font=("Times New Roman",30,"bold"),fg="black",bg="grey")
Toss_win.place(x=225,y=230,width=250,height=50)
#-----------------------------------------
choice1_text = Label(root,text="Choice 1",font=("Times New Roman",20,"bold"),fg="black")
choice1_text.place(x=20,y=260,width=160,height=50)
choice2_text = Label(root,text="Choice 2",font=("Times New Roman",20,"bold"),fg="black")
choice2_text.place(x=520,y=260,width=160,height=50)
#---------------------------------------------
choice_00_text = Label(root,text="****",font=("Times New Roman",20,"bold"),fg="black")
choice_00_text.place(x=20,y=320,width=160,height=50)
choice1_00_text = Label(root,text="****",font=("Times New Roman",20,"bold"),fg="black")
choice1_00_text.place(x=520,y=320,width=160,height=50)
root.mainloop()