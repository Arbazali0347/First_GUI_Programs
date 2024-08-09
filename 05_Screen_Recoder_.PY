
from tkinter import *
import cv2
import pyautogui
import numpy as np
import time
from win32api import GetSystemMetrics

def ScreenRecoding():
    waith = GetSystemMetrics(0)
    hait = GetSystemMetrics(1)
    dim = (waith,hait)
    f = cv2.VideoWriter_fourcc(*"XVID")
    output  = cv2.VideoWriter("01_My_Video.mp4",f,20,dim)

    start = time.time()
    dur = 20
    end_time = start + dur
    print("\nStart Recoding....")
    while True:
        image = pyautogui.screenshot()
        frame = np.array(image)
        frame_1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        output.write(frame_1)
        c_time = time.time()
        if c_time > end_time:
            break
    output.release()
    print("\n\tArbaz your Recoding is succefully")
    recod.config(text="Recoding Successfully")
fram = Tk()
fram.title("arbaz")
fram.config(bg="grey")
fram1 = Label(fram,text="Arbaz Recoder",font=("Time New Roman",15,"bold"),bg="black",fg="white")
fram1.place(x=0,y=20,width=200,height=50)
bt = Button(fram,text="click Recode",fg="white",bg="black",font=("Time New Roman",10,"bold"),relief=RAISED,command=ScreenRecoding)
bt.place(x=25,y=100,width=150,height=40)
recod = Label(fram,text="Recoding Start",fg="black",font=("Time New Roman",10,"bold"))
recod.place(x=0,y=150,width=200,height=40)
fram.mainloop()
