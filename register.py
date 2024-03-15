from tkinter import*
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #==============================variables=====================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #==========bg image========================
        self.bg=ImageTk.PhotoImage(file="C:/Users/amrut/.ipython/Hotel/arushi-boutique-hotel-deluxe-room.JPG")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #==========bg image========================
        self.bg1=ImageTk.PhotoImage(file="C:/Users/amrut/.ipython/Hotel/beautiful-unicorn-in-forest-fantasy-computer-desktop-wallpapers-hd-2560×1600-wallpaper-preview.PNG")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        #==================main frame=============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #============label and entry==============
        #================row1=======================
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_l_name=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_l_name.place(x=370,y=130,width=250)

         #================row2=======================
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #================row3=======================
        security_Q=Label(frame,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["value"]=("Select","Your Birth Place","Your Favorite Dish name","Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #================row4=======================
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #====================check btn=================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #=====================btn==================
        img=Image.open("C:/Users/amrut/.ipython/Hotel/download (14).JPG")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimg,command=self.add_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=10,y=420,width=200)

        img1=Image.open("C:/Users/amrut/.ipython/Hotel/images (19).JPG")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white")
        b1.place(x=330,y=420,width=200)

    
    def add_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirmation Of Password Is Required")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Amruta@24",database="employees")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into new values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_fname.get(),
                                                                                                    self.var_lname.get(),
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_SecurityQ.get(),
                                                                                                    self.var_SecurityA.get(),
                                                                                                    self.var_pass.get()
                                                                                                    
                                                                                                    ))
                conn.commit()
                conn.close()                                                                                    
                messagebox.showinfo("success","Registration is Succesfull",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)  

    def return_login(self):
        self.root.destroy()  
           


 

        



if __name__ == "__main__":
    root = Tk()
    obj=Register(root)
    root.mainloop()