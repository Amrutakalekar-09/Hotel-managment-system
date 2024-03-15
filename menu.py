from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Menu_card:
    def __init__(self,root):
        self.root=root
        self.root.title("Menu Card")
        self.root.geometry("1550x800+0+0")

        #==============title=======================
        lbl_title=Label(self.root,text="MENU CARD",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1520,height=50)

        #=================logo=====================
        img2=Image.open("C:/Users/amrut/.ipython/Hotel/images1.PNG")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #============================main frame=============
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50,width=1520,height=700)

        #====================== image==========
        img3=Image.open("C:/Users/amrut/.ipython/Hotel/make-food-menu-restaurant-menu-and-menu-board-design.JPG")
        img3=img3.resize((500,700),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=500,height=700)

        img4=Image.open("C:/Users/amrut/.ipython/Hotel/design-amazing-food-menu.JPG")
        img4=img4.resize((530,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=500,y=0,width=530,height=700)

        
        img6=Image.open("C:/Users/amrut/.ipython/Hotel/2d7b210b6f7c0d25d1626888406b426c.JPG")
        img6=img6.resize((530,700),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        lblimg1=Label(main_frame,image=self.photoimg6,bd=4,relief=RIDGE)
        lblimg1.place(x=1030,y=0,width=530,height=700)

        


if __name__ == "__main__":
    root = Tk()
    obj=Menu_card(root)
    root.mainloop()