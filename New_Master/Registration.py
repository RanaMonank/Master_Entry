from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import pymysql
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        # BG Imag
        self.bg=ImageTk.PhotoImage(file="Images/Jiyan.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        # Left Imag
        self.left=ImageTk.PhotoImage(file="Images/Monank2.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        # Register Frame
        frame1=Frame(self.root,bg='white')
        frame1.place(x=480,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTER HERE",font=("Arial",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        # self.var_fname=StringVar() # varible Fetch Data
        f_name=Label(frame1,text="First Name",font=("Arial",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        #  txt_fname = Entry(frame1,font=("Arial",15),bg='lightgray',textvariable=self.var_fname).place(x=50,y=130,width=250)
        self.txt_fname = Entry(frame1,font=("Arial",15),bg='lightgray')
        self.txt_fname.place(x=50,y=130,width=250)


        l_name = Label(frame1, text="Last Name", font=("Arial", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font=("Arial", 15), bg='lightgray')
        self.txt_lname.place(x=370, y=130, width=250)

        # --------------------------------Row 2

        contact = Label(frame1, text="Contact No.", font=("Arial", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font=("Arial", 15), bg='lightgray')
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=("Arial", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font=("Arial", 15), bg='lightgray')
        self.txt_email.place(x=370, y=200, width=250)

        # --------------------------------Row 3

        department = Label(frame1, text="Department", font=("Arial", 15, "bold"), bg="white", fg="gray").place(x=50,y=240)
        self.cmb_dept = ttk.Combobox(frame1, font=("Arial", 13),state='readonly',justify=CENTER)
        self.cmb_dept['values'] = ('Select','IT','HR/Admin','Production','Packing')
        self.cmb_dept.place(x=50, y=270, width=290)
        self.cmb_dept.current(0)

        gender = Label(frame1, text="Gender", font=("Arial", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)
        self.cmb_gender = ttk.Combobox(frame1, font=("Arial", 13),state='readonly',justify=CENTER)
        self.cmb_gender['values']=('Select','Male','Female','Other')
        self.cmb_gender.place(x=370, y=270, width=250)
        self.cmb_gender.current(0)

        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Trems & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg='white',font=("Arial",15,"bold")).place(x=50,y=310)

        self.btn_img=ImageTk.PhotoImage(file="Images/Submit2.png")
        btn_register= Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.regsiter_data).place(x=50,y=380)
        # btn_register = Button(frame1,text='Submit', font=('Arial',16, "bold"),bg='green',bd=0,cursor='hand2',command=self.regsiter_data).place(x=50,y=380)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_dept.current(0)
        self.cmb_gender.current(0)

    def regsiter_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_dept.get() == 'Select'\
                or self.cmb_gender.get() == 'Select':
            messagebox.showerror("Error","All Fields Are Requied",parent=self.root)

        elif self.var_chk.get()==0:
            messagebox.showerror("Error",'Please Agree Terms & conditions')
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employees")
                cur=con.cursor()

                cur.execute("select * from emp_master where email=%s",self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error", 'User Alredy Exxist, Please try with another email')
                else:
                    cur.execute("insert into emp_master (f_name,l_name,contact,email,dept,gender) values(%s,%s,%s,%s,%s,%s)",
                                (
                                    self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_dept.get(),
                                    self.cmb_gender.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully...!")
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root = Tk()
obj=Register(root)
root.mainloop()