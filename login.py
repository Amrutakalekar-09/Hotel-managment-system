from tkinter import*
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
from hotel import HotelManagementSystem
from register import Register
import mysql.connector


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file="C:/Users/amrut/.ipython/Hotel/images1.PNG")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("C:/Users/amrut/.ipython/Hotel/images1.PNG")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)   

        # label
        username=lbl=Label(frame,text="User Name",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.textpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textpass.place(x=40,y=250,width=270)

        #====================Icon image=================
        img2=Image.open("C:/Users/amrut/.ipython/Hotel/person-icon-creative-trendy-colorful-round-button-illustration-isolated-156511182.JPG")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=323,width=25,height=25)

        img3=Image.open("C:/Users/amrut/.ipython/Hotel/lock-icon-on-black-background-black-flat-style-vector-25959812.JPG")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblim3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblim3.place(x=650,y=395,width=25,height=25)

        #=========login button============
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="red",fg="white",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn=Button(frame,text="New User Register",command=self.register,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        forgetpassbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=10,y=370,width=160)

    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All Filds Required")
        elif self.textuser.get()=="Amruta" and self.textpass.get()=="Amu":
            messagebox.showinfo("success","Welcome to Hotel Management System")
        else:
            #messagebox.showinfo("Error","Invalid")
             self.new_window=Toplevel(self.root)
             self.app=HotelManagementSystem(self.new_window)
    

    #======================forget password================
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Amruta@24",database="employees")
            my_cursor=conn.cursor()
            query=("select * from new where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("MY Error","Please Enter The Valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"),bg="white")
                security_Q.place(x=50,y=80)

                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["value"]=("Select","Your Birth Place","Your Favorite Dish name","Your Pet Name")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpassword.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
   
    
    #======================reset passwort===================
    def reset_pass(self):
        if self.combo_security_Q.get()=="select":
            messagebox.showerror("Error","select sucurity Quetion",parent=self.root)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please Enter The Answer",parent=self.root)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("Error","Please Enter The New Password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Amruta@24",database="employees")
            my_cursor=conn.cursor()
            
            query=("update new set password=%s where email=%s")
            value=(self.txt_newpassword.get(),self.textuser.get())
            my_cursor.execute(query,value)

            conn.commit()
            conn.close()
            messagebox.showinfo("Info","Your password has been reset,Please login new password",parent=self.root)
            self.root2.destroy()
          

                







    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

        


if __name__ == "__main__":
    root = Tk()
    obj=Login_Window(root)
    root.mainloop()