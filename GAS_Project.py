from tkinter import*
from tkinter import messagebox
import database as db
import tkinter as tk
import string
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
#import pymysql
import random
import os
from tkinter import simpledialog
import database as db
from tkinter import font  as tkfont
global app
try:
    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            
            self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
            self.title("Graphical Authentication System")
            self.geometry("1366x768+0+0")
            # the container is where we'll stack a bunch of frames
            # on top of each other, then the one we want visible
            # will be raised above the others
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (Graph_Home, Graph_Autentication,Graph_Registration,Graph_Updation,Graph_Admin):
                page_name = F.__name__
                frame = F(parent=container, controller=self)
                self.frames[page_name] = frame

                # put all of the pages in the same location;
                # the one on the top of the stacking order
                # will be the one that is visible.
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("Graph_Home")
            
        def show_frame(self, page_name):
            '''Show a frame for the given page name'''
            frame = self.frames[page_name]
            frame.tkraise()

    class Graph_Home(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)
            self.H_controller = controller
            Graph_Functions.G_upload_image(self,"bg3.jpg",1366, 700,self,-2,0)
            title=tk.Label(self,text="Graphical Authentication System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#800000",fg="white",)
            title.pack(side=TOP,fill=X)

            #=========All Variables===========================

            self.H_name_var=StringVar()
            self.H_email_var=StringVar()
            self.H_contact_var=StringVar()
            self.H_question_var=StringVar()
            self.H_answer_var=StringVar()
            self.H_filename=StringVar()
            self.H_cues_var=StringVar()
            self.H_Picture_Canvas=tk.Canvas()
            self.H_Image_Canvas=tk.Canvas()
            self.H_Register_Canvas=tk.Canvas()
            self.H_img=tk.Label()    # displays image
            self.H_img1=tk.Label()
            self.H_mousePosition = StringVar() # displays mouse position
            
            try:
                Graph_Functions.G_upload_image(self,'Keylogo.png',580, 400,self,20,190)
                #=========Right Canvas===========================

                H_Right_Canvas=Canvas(self,bd=2,relief=RIDGE,bg="#C3F74A")
                H_Right_Canvas.place(x=960,y=110,width=370,height=560)

                H_lbl_phase1=Label(H_Right_Canvas,text="REGISTRATION PHASE",bg="#C3F74A",fg="red",font=("Courier New",15,"bold"))
                H_lbl_phase1.place(x=10,y=15)

                H_txt_phase1=Text(H_Right_Canvas,height=4,wrap=WORD,width=42,bg="#C3F74A",border=0)
                H_quote="""This Phase is meant for New User Registration and also include selecting of pictures and cue points needed for password!"""
                H_txt_phase1.insert(tk.END, H_quote,'black')
                H_txt_phase1.config(state=DISABLED)
                H_txt_phase1.place(x=15,y=45)

                H_Right_Canvas.create_line(50, 120, 320, 120, width=3)

                H_lbl_phase2=Label(H_Right_Canvas,text="LOGIN PHASE",bg="#C3F74A",fg="red",font=("Courier New",15,"bold"))
                H_lbl_phase2.place(x=10,y=135)

                H_txt_phase2=Text(H_Right_Canvas,height=6,wrap=WORD,width=42,bg="#C3F74A",border=0)
                H_quote="""This Phase is accessible only to legitimate users. This phase includes immediate and knowledge based feedback methods(ease for the users).\nNote:-Please ensure that the points are same that used while registering!"""
                H_txt_phase2.insert(tk.END, H_quote,'black')
                H_txt_phase2.config(state=DISABLED)
                H_txt_phase2.place(x=15,y=165)

                H_Right_Canvas.create_line(50, 270, 320, 270, width=3)

                H_lbl_phase3=Label(H_Right_Canvas,text="ABOUT US PHASE",bg="#C3F74A",fg="red",font=("Courier New",15,"bold"))
                H_lbl_phase3.place(x=10,y=285)

                H_txt_phase3=Text(H_Right_Canvas,height=3,wrap=WORD,width=42,bg="#C3F74A",border=0)
                H_quote="""This Phase displays the details about the authors of the project:- GRAPHICAL AUTHENTICATION SYSTEM...!"""
                H_txt_phase3.insert(tk.END, H_quote,'black')
                H_txt_phase3.config(state=DISABLED)
                H_txt_phase3.place(x=15,y=315)

                H_Right_Canvas.create_line(50, 370, 320, 370, width=3)

                H_lbl_phase4=Label(H_Right_Canvas,text="ADMIN PHASE",bg="#C3F74A",fg="red",font=("Courier New",15,"bold"))
                H_lbl_phase4.place(x=10,y=385)

                H_txt_phase4=Text(H_Right_Canvas,height=2,wrap=WORD,width=42,bg="#C3F74A",border=0)
                H_quote="""This Phase is used to Verify_Function as an Administrator, who manages all the users!"""
                H_txt_phase4.insert(tk.END, H_quote,'black')
                H_txt_phase4.config(state=DISABLED)
                H_txt_phase4.place(x=15,y=415)

                H_Right_Canvas.create_line(50, 460, 320, 460, width=3)

                H_lbl_phase5=Label(H_Right_Canvas,text="EXIT PHASE",bg="#C3F74A",fg="red",font=("Courier New",15,"bold"))
                H_lbl_phase5.place(x=10,y=475)

                H_txt_phase5=Text(H_Right_Canvas,height=2,wrap=WORD,width=42,bg="#C3F74A",border=0)
                H_quote="""This Phase is used to shutdown(close) the program(system)!"""
                H_txt_phase5.insert(tk.END, H_quote,'black')
                H_txt_phase5.config(state=DISABLED)
                H_txt_phase5.place(x=15,y=505)

                Graph_Functions.G_upload_image(self,'lock2.jpg',40, 40,self,660,150)
                Graph_Functions.G_upload_image(self,'key1.png',40, 40,self,660,260)
                Graph_Functions.G_upload_image(self,'about1.png',40, 40,self,660,370)
                Graph_Functions.G_upload_image(self,'admin.png',40, 40,self,660,480)
                Graph_Functions.G_upload_image(self,'error1.png',40, 40,self,660,590)

                H_reg_btn=Button(self,text="REGISTRATION",command=lambda: controller.show_frame("Graph_Registration"),bg="#4A8AF7",font=("times new roman",15,"bold")).place(x=740,y=150)           
                H_log_btn=Button(self,text="         LOGIN        ",fg="black",command=lambda: controller.show_frame("Graph_Autentication"),bg="#4A8AF7",font=("times new roman",15,"bold")).place(x=740,y=260)
                H_abt_btn=Button(self,text="     ABOUT US     ",command=self.H_About_Function,font=("times new roman",15,"bold"),bg="#4A8AF7").place(x=740,y=370)
                H_admin_btn=Button(self,text="        ADMIN        ",command=lambda: controller.show_frame("Graph_Admin"),font=("times new roman",15,"bold"),bg="#4A8AF7").place(x=740,y=480)
                H_exit_btn=Button(self,text="          EXIT          ",font=("times new roman",15,"bold"),bg="#4A8AF7",command = self.close_window ).place(x=740,y=590)

            except Exception as e:
                print(e)
        def H_About_Function(self):
            messagebox.showinfo("GAS","The Graphical Authentication System Project is made by\n-MUZAMMIL AHSAN\n-IMAN ABBAS\n-PRAKHAR SINGH")

        def close_window (self):
            x=messagebox.askquestion("Confirm","Are you sure?") 
            if(x=="yes"):
                app.destroy()

    class Graph_Registration(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)
            self.R_controller = controller
            Graph_Functions.G_upload_image(self,"bg7.jpg",1366, 700,self,-2,0)
            R_title=tk.Label(self,text="New User Registration",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#006666",fg="white",)
            R_title.pack(side=TOP,fill=X)

            #=========All Variables===========================
            self.R_image_count_var=[0,0,0]
            self.R_path_list_var=["","",""]
            self.i=0
            self.R_point_count_var=0
            self.R_name_var=StringVar()
            self.R_email_var=StringVar()
            self.R_contact_var=StringVar()
            self.R_question_var=StringVar()
            self.R_answer_var=StringVar()
            self.filename=StringVar()
            self.R_cues_var=StringVar()
            self.R_Picture_Canvas=tk.Canvas()
            self.R_Image_Canvas=tk.Canvas()
            self.R_Left_Canvas=tk.Canvas()
            self.R_img=tk.Label()    # displays image
            self.R_img1=tk.Label()
            self.R_img2=tk.Label()
            self.R_img3=tk.Label()
            self.R_mousePosition = StringVar() # displays mouse position

            try:            
                #=========Register Canvas===========================

                self.R_Left_Canvas=tk.Canvas(self,bd=0,relief=RIDGE,bg="#C79408")
                self.R_Left_Canvas.place(x=10,y=90,width=545,height=512)

                self.R_Left_Canvas.create_line(0, 3, 545, 3, width=3)  
                self.R_Left_Canvas.create_line(475, 2, 542, 70, width=3)
                self.R_Left_Canvas.create_line(541, 0, 541, 512, width=3)
                self.R_Left_Canvas.create_line(542, 369, 475, 437, width=3)
                self.R_Left_Canvas.create_line(0, 436, 545, 436, width=3)
                self.R_Left_Canvas.create_line(3, 0, 3, 512, width=3) 
                self.R_Left_Canvas.create_line(0, 508, 545, 508, width=3)

                R_Registration_title=tk.Label(self.R_Left_Canvas,text="REGISTRATION PROCESS",pady=0,bg="#C79408",fg="black",font=("times new roman",18,"bold"))
                R_Registration_title.place(x=9,y=8)
                
                self.R_Left_Canvas.create_line(11, 41, 311, 41, width=3) 
                self.R_Left_Canvas.create_line(12, 53, 12, 275, width=2)

                Graph_Functions.G_upload_image(self,'close_lock.jpg',127, 140,self.R_Left_Canvas,355,25)

                R_lbl_name=tk.Label(self.R_Left_Canvas,text="NAME",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_name.place(x=20,y=55,width=65,height=22)
                R_txt_name=tk.Entry(self.R_Left_Canvas,textvariable=self.R_name_var,width=25,font=("times new roman",15,""),bd=2,relief=GROOVE)
                R_txt_name.place(x=90,y=52)

                R_lbl_email=tk.Label(self.R_Left_Canvas,text="EMAIL",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_email.place(x=20,y=88,width=68,height=22)
                R_txt_email=tk.Entry(self.R_Left_Canvas,width=25,font=("times new roman",15,""),textvariable = self.R_email_var,bd=2,relief=GROOVE)
                R_txt_email.place(x=90,y=85)

                R_lbl_mob=tk.Label(self.R_Left_Canvas,text="CONTACT",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_mob.place(x=20,y=121,height=22)
                R_txt_mob=tk.Entry(self.R_Left_Canvas,width=21,font=("times new roman",15,""),textvariable = self.R_contact_var,bd=2,relief=GROOVE)
                R_txt_mob.place(x=130,y=118)

                R_lbl_pts=tk.Label(self.R_Left_Canvas,text="CUE POINTS COLLECTED",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_pts.place(x=20,y=150)
                self.R_Scroll_Frame = tk.Frame(self.R_Left_Canvas, bd=2, relief=SUNKEN)
                self.R_Scroll_Frame.place(x=20,y=175,width=400,height=100)

                self.R_xscroll = tk.Scrollbar(self.R_Scroll_Frame, orient=HORIZONTAL)
                self.R_xscroll.pack(side=BOTTOM,fill=X)
                self.R_yscroll = tk.Scrollbar(self.R_Scroll_Frame, orient=VERTICAL)
                self.R_yscroll.pack(side=RIGHT,fill=Y)
                self.R_mylist = tk.Listbox(self.R_Scroll_Frame, yscrollcommand=self.R_yscroll.set)
                
                R_forgot_title=tk.Label(self.R_Left_Canvas,text="FORGOT PASSWORD",pady=0,bg="#C79408",fg="black",font=("times new roman",18,"bold"))
                R_forgot_title.place(x=9,y=280)

                self.R_Left_Canvas.create_line(11, 313, 256, 313, width=3)
                self.R_Left_Canvas.create_line(12, 322, 12, 430, width=2)

                R_lbl_ques=tk.Label(self.R_Left_Canvas,text="CUSTOM QUESTION",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_ques.place(x=20,y=318)
                R_txt_ques=tk.Entry(self.R_Left_Canvas,textvariable = self.R_question_var,width=40,font=("times new roman",15,""),bd=2,relief=GROOVE)
                R_txt_ques.place(x=20,y=345)

                R_lbl_ans=tk.Label(self.R_Left_Canvas,text="CUSTOM ANSWER",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                R_lbl_ans.place(x=20,y=375)
                R_txt_ans=tk.Entry(self.R_Left_Canvas,textvariable = self.R_answer_var,width=40,font=("times new roman",15,""),bd=2,relief=GROOVE)
                R_txt_ans.place(x=20,y=402)

                R_lbl_register=tk.Label(self.R_Left_Canvas,text ="REGISTER\nTO DB",bg="#C79408",fg="black",font=("Franklin Gothic Book",12,"bold"))
                R_lbl_register.place(x=29,y=452,width=104,height=44)
                R_register_btn=tk.Button(self.R_Left_Canvas,text="REGISTER",command = self.registerfn,font=("times new roman",15,"bold")).place(x=135,y=454)

                R_lbl_save=tk.Label(self.R_Left_Canvas,text ="SAVE",bg="#C79408",fg="black",font=("Franklin Gothic Book",15,"bold"))
                R_lbl_save.place(x=350,y=459,width=60)
                R_save_btn=tk.Button(self.R_Left_Canvas,text="SAVE",command=self.collection,font=("times new roman",15,"bold")).place(x=425,y=454)

                R_reset_btn=tk.Button(self,text="RESET",command=self.clear,bg="#FF6666",font=("times new roman",15,"bold")).place(x=593,y=543)
                #=========Image Canvas===========================

                self.R_Image_Canvas=tk.Canvas(self,bd=4,relief=RIDGE,bg="#B999FA")
                self.R_Image_Canvas.place(x=715,y=90,width=637,height=512)

                R_Image_title=tk.Label(self.R_Image_Canvas,text="IMAGE",bg="#B999FA",fg="black",font=("times new roman",25,"bold"))
                R_Image_title.place(x=270,y=6)

                self.R_Image_Canvas.create_line(270, 50, 390, 50, width=3)

                #=========Picture Canvas===========================

                self.R_Picture_Canvas=Canvas(self.R_Image_Canvas,bd=0,relief=RIDGE,bg="crimson")
                self.R_Picture_Canvas.place(x=18,y=60,width=600,height=437)

                for i in range(25,600,25):
                    self.R_Picture_Canvas.create_line(i,3,i,434,fill="black")
                
                for i in range(25,437,25):
                    self.R_Picture_Canvas.create_line(3,i,597,i,fill="black")

                #=========Bottom self.R_Scroll_Frame===========================

                R_Bottom_Canvas=Frame(self,bd=4,relief=RIDGE,bg="#1E90FF")
                R_Bottom_Canvas.place(x=10,y=610,width=1340,height=80)

                R_lbl_load_pic=Label(R_Bottom_Canvas,text="LOAD\nPICTURE",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                R_lbl_load_pic.place(x=70,y=15,width=75,height=44)

                R_load_pic_btn=Button(R_Bottom_Canvas,text="LOAD PIC",command=self.fileDialog,font=("times new roman",15,"bold")).place(x=155,y=17)

                R_lbl_cue=Label(R_Bottom_Canvas,text="CUE\nPOINTS",bg="#1E90FF",fg="black",font=("times new roman",13,"bold"))
                R_lbl_cue.place(x=563,y=15,width=67,height=44)

                R_lbl_points=Label(R_Bottom_Canvas,textvariable = self.R_mousePosition,bd=3,relief=RIDGE,bg="white",fg="black",font=("times new roman",18,"bold"))
                R_lbl_points.place(x=640,y=15,width=150,height=45)             
                
                R_lbl_exit=Label(R_Bottom_Canvas,text ="EXIT TO\nMAIN MENU",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                R_lbl_exit.place(x=1066,y=15,width=104,height=44)

                R_cancel_btn=Button(R_Bottom_Canvas,text="CANCEL",fg="black",command=lambda: controller.show_frame("Graph_Home"),bg="white",font=("times new roman",15,"bold")).place(x=1180,y=17)

            except Exception as e:
                print(e)

        #=========Image Loading function===========================
        def fileDialog(self): 
            self.filename = filedialog.askopenfilename(initialdir =  "S:/", title = "Select A File", filetype =
            (("jpeg files","*.jpg"),("all files","*.*")) )
            if(self.filename!="" and self.i<3):
                self.R_image_count_var[self.i]=1
                load = Image.open(self.filename)
                load = load.resize((594, 431), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                self.R_img = Label(self.R_Picture_Canvas, image=render)
                self.R_img.image = render  
                self.R_img.place(x=3, y=3 ,width=594, height=431)
                self.R_img.bind("<Button-1>",self.printcoords)
                
                if(self.i==0):
                    load1 = Image.open(self.filename)
                    load1 = load1.resize((151, 110), Image.ANTIALIAS)
                    render1 = ImageTk.PhotoImage(load1)
                    self.R_img1 = Label(self, image=render1)
                    self.R_img1.image = render1
                    self.R_img1.place(x=560, y=115 ,width=151, height=110)
                elif(self.i==1):
                    load2 = Image.open(self.filename)
                    load2 = load2.resize((151, 110), Image.ANTIALIAS)
                    render2 = ImageTk.PhotoImage(load2)
                    self.R_img2 = Label(self, image=render2)
                    self.R_img2.image = render2
                    self.R_img2.place(x=560, y=255 ,width=151, height=110)
                elif(self.i==2):
                    load3 = Image.open(self.filename)
                    load3 = load3.resize((151, 110), Image.ANTIALIAS)
                    render3 = ImageTk.PhotoImage(load3)
                    self.R_img3 = Label(self, image=render3)
                    self.R_img3.image = render3
                    self.R_img3.place(x=560, y=395 ,width=151, height=110)
            elif(self.filename!="" and self.i>=3):
                messagebox.showerror("GAS","Images are over...!")    
                
        #Function to be called when mouse is clicked on the image
        def printcoords(self,event):
            self.R_point_count_var=1
            self.R_cues_var.set("[ " + str( event.x ) +  ", " + str( event.y ) + " ]")
            self.R_mousePosition.set( "[ " + str( event.x ) + ", " + str( event.y ) + " ]" )

        #Function to be called when save button is clicked
        def collection(self):   
            if(self.i<3):
                if(self.R_image_count_var[self.i]!=0) : 
                    if(self.R_point_count_var!=0) :
                        self.R_path_list_var[self.i]=self.filename +"  #"+ self.R_cues_var.get()
                        self.R_point_count_var=0  
                        self.R_mylist.insert(END, self.filename +"  #"+ self.R_cues_var.get() )  
                        self.R_mylist.pack( side = TOP ,fill=BOTH)
                        self.R_xscroll.config(command=self.R_mylist.xview)
                        self.R_yscroll.config(command=self.R_mylist.yview)
                        self.R_mousePosition.set("")
                        self.R_cues_var.set("")
                        self.R_img.destroy()
                        self.i=self.i+1
                    else:
                        self.R_mousePosition.set("")
                        self.R_cues_var.set("")
                        self.R_point_count_var=0
                        messagebox.showerror("GAS","Please Select Cue Point on the Image first...!")    
                else:
                    self.R_mousePosition.set("")
                    self.R_mousePosition.set("")
                    self.R_cues_var.set("")
                    self.R_point_count_var=0
                    messagebox.showerror("GAS","Please Upload the Image first...!")
            else:
                self.R_mousePosition.set("")
                self.R_mousePosition.set("")
                self.R_cues_var.set("")
                self.R_point_count_var=0
                messagebox.showinfo("GAS","All the Images and Cue Points\nare saved successfully...!")
        
        #Function to be called when register button is clicked !
        def registerfn(self):
            ob = db.database()
            is_success=0
            if(self.R_name_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the name")
            elif(self.R_email_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the email")
            elif(self.R_contact_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the contact number")
            

            if( self.R_image_count_var[0]!=0 and self.R_image_count_var[1]!=0 and self.R_image_count_var[2]!=0 and self.R_name_var!="" and self.R_email_var!="" and self.R_question_var!="" and self.R_answer_var!="" ):
                query = "insert into registration_table(name,email,contact,question,answer,p1,p2,p3) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (self.R_name_var.get(),self.R_email_var.get(),self.R_contact_var.get(),self.R_question_var.get(),self.R_answer_var.get(),self.R_path_list_var[0],self.R_path_list_var[1],self.R_path_list_var[2])
                is_success = ob.universal_Transact(query, val)
            if is_success == 1:
                messagebox.showinfo("GAS","done")
            else:
                messagebox.showinfo("GAS","not done")
            self.clear()
                
        #Function to be called when reset button is clicked...!
        def clear(self):
            if( self.R_image_count_var[0]==0 and self.R_image_count_var[1]==0 and self.R_image_count_var[2]==0 and self.i==0 and self.R_point_count_var==0 and self.R_name_var=="" and self.R_email_var=="" and self.R_contact_var=="" and self.R_question_var=="" and self.R_answer_var=="" and self.filename=="" and self.R_cues_var=="" and self.R_mousePosition == "" ):
                messagebox.showerror("Error","All Fields are already Empty!!!")
            else:
                self.R_image_count_var[0]=0
                self.R_image_count_var[1]=0
                self.R_image_count_var[2]=0
                self.i=0
                self.R_point_count_var=0
                self.R_name_var.set("")
                self.R_email_var.set("")
                self.R_contact_var.set("")
                self.R_question_var.set("")
                self.R_answer_var.set("")
                self.filename=""
                self.R_cues_var.set("")
                self.R_mousePosition.set("")
                self.R_img.destroy()
                self.R_img1.destroy()
                self.R_img2.destroy()
                self.R_img3.destroy()
                self.R_mylist.delete(0,END)
                self.R_path_list_var[0]=""
                self.R_path_list_var[1]=""
                self.R_path_list_var[2]=""

    class Graph_Autentication(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)
            self.A_controller = controller
            Graph_Functions.G_upload_image(self,"bg1.png",1366, 700,self,-2,0)
            A_title=tk.Label(self,text="User Authentication",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#610351",fg="white",)
            A_title.pack(side=TOP,fill=X)

            #=========All Variables===========================
            self.A_name_var=StringVar()
            self.A_email_var=StringVar()
            self.A_contact_var=StringVar()
            self.A_question_var=StringVar()
            self.A_answer_var=StringVar()
            self.A_filename=StringVar()
            self.A_cues_var=StringVar()
            self.A_Picture_Canvas=tk.Canvas()
            self.A_Image_Canvas=tk.Canvas()
            self.A_Left_Canvas=tk.Canvas()
            self.A_img=tk.Label()    # displays image
            self.A_img1=tk.Label()
            self.A_mousePosition = StringVar() # displays mouse position
            self.A_v = IntVar()
            self.j=0
            self.k=0
            self.imgs=["S:/background-1992153_1920.jpg","S:/background-378781_1920.jpg","S:/bg2.jpg","S:/bg3.jpg","S:/black-2398956_1920.jpg","S:/background-378781_1920.jpg"]
            try:            
                #=========Register Canvas===========================
                self.A_Left_Canvas=tk.Canvas(self,bd=0,relief=RIDGE,bg="#33FF77")
                self.A_Left_Canvas.place(x=10,y=120,width=545,height=452)

                self.A_Left_Canvas.create_line(0, 3, 545, 3, width=3)  
                self.A_Left_Canvas.create_line(475, 2, 542, 70, width=3)
                self.A_Left_Canvas.create_line(541, 0, 541, 512, width=3)
                self.A_Left_Canvas.create_line(545, 377, 475, 448, width=3)
                self.A_Left_Canvas.create_line(3, 0, 3, 452, width=3) 
                self.A_Left_Canvas.create_line(0, 448, 545, 448, width=3)

                self.A_Left_Canvas.create_line(12, 50, 12, 140, width=2)   

                A_lbl_email=Label(self.A_Left_Canvas,text="EMAIL",bg="#33FF77",fg="black",font=("times new roman",19,"bold"))
                A_lbl_email.place(x=20,y=50)
                A_txt_email=Entry(self.A_Left_Canvas,textvariable=self.A_email_var,width=30,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
                A_txt_email.place(x=120,y=50)

                self.A_verify_btn=Button(self.A_Left_Canvas,command=self.Verify_Function,text="Verify",font=("times new roman",15,"bold")).place(x=160,y=98)
                self.A_proceed_btn=Button(self.A_Left_Canvas,text="Proceed",command=self.Proceed_Function,font=("times new roman",15,"bold")).place(x=300,y=98)
                #self.A_proceed_btn.state=NORMAL
                A_lbl_feedback=Label(self.A_Left_Canvas,text="FEEDBACK METHODS",bg="#33FF77",fg="black",font=("Courier New",20,"bold"))
                A_lbl_feedback.place(x=10,y=158)

                self.A_Left_Canvas.create_line(11,196, 270, 196, width=3) 
                self.A_Left_Canvas.create_line(12, 210, 12, 280, width=2)

                A_immediate_radio_btn = tk.Radiobutton(self.A_Left_Canvas, text="IMMEDIATE FEEDBACK", variable=self.A_v, value=1,bg="#33FF77",fg="crimson",font=("Franklin Gothic Book",14,"bold"))
                A_immediate_radio_btn.place(x=30,y=200)
                print(self.A_v.get())
                A_immediate_txt=Text(self.A_Left_Canvas,height=3,wrap=WORD,width=50,bg="#33FF77",border=0)
                A_quote="""Immediate feedback method is a fast reply system. Click Radio Button to activate this method,It will give reply only when user click wrong point!"""
                A_immediate_txt.insert(tk.END, A_quote,'black')
                A_immediate_txt.config(state=DISABLED)
                A_immediate_txt.place(x=50,y=234)
                
                self.A_Left_Canvas.create_line(12, 311, 12, 412, width=2)

                A_knowledge_radio_btn = tk.Radiobutton(self.A_Left_Canvas, text="KNOWLEDGE BASED FEEDBACK", variable=self.A_v, value=2,bg="#33FF77",fg="crimson",font=("Franklin Gothic Book",14,"bold"))
                A_knowledge_radio_btn.place(x=30,y=301)

                A_knowledge_txt=Text(self.A_Left_Canvas,height=5,wrap=WORD,width=50,bg="#33FF77",border=0)
                A_quote="""Knowledge Based Feedback method is NO-REPLY SYSTEM. It will not provide the user any information. If the user click wrong point. User have to identify the image and point.\nHighly Secured!"""
                A_knowledge_txt.insert(tk.END, A_quote,'black')
                A_knowledge_txt.config(state=DISABLED,highlightbackground="#33FF77")
                A_knowledge_txt.place(x=50,y=335)
                print(self.A_v.get())
                Graph_Functions.G_upload_image(self,'close_lock.jpg',137, 150,self,565,250)

                #=========Image Canvas===========================

                self.A_Image_Canvas=tk.Canvas(self,bd=4,relief=RIDGE,bg="#F04BA9")
                self.A_Image_Canvas.place(x=715,y=90,width=637,height=512)

                A_Image_title=tk.Label(self.A_Image_Canvas,text="IMAGE",bg="#F04BA9",fg="black",font=("times new roman",25,"bold"))
                A_Image_title.place(x=270,y=6)

                self.A_Image_Canvas.create_line(270, 50, 390, 50, width=3)

                #=========Picture Canvas===========================

                self.A_Picture_Canvas=Canvas(self.A_Image_Canvas,bd=0,relief=RIDGE,bg="#0B7945")
                self.A_Picture_Canvas.place(x=18,y=60,width=600,height=437)

                for i in range(25,600,25):
                    self.A_Picture_Canvas.create_line(i,3,i,434,fill="black")
                
                for i in range(25,437,25):
                    self.A_Picture_Canvas.create_line(3,i,597,i,fill="black")

                #=========Bottom self.A_Scroll_Frame===========================

                A_Bottom_Canvas=Frame(self,bd=4,relief=RIDGE,bg="#1E90FF")
                A_Bottom_Canvas.place(x=10,y=610,width=1340,height=80)

                A_lbl_forgot_password=Label(A_Bottom_Canvas,text="FORGOT\nPASSWORD",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                A_lbl_forgot_password.place(x=60,y=15,width=104,height=44)

                A_forgot_password_btn=Button(A_Bottom_Canvas,text="PASSWORD",command=self.Forgot_Function,font=("times new roman",15,"bold")).place(x=165,y=17)          
                
                A_lbl_exit=Label(A_Bottom_Canvas,text ="EXIT TO\nMAIN MENU",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                A_lbl_exit.place(x=1066,y=15,width=104,height=44)

                A_cancel_btn=Button(A_Bottom_Canvas,text="CANCEL",fg="black",command=lambda: controller.show_frame("Graph_Home"),bg="white",font=("times new roman",15,"bold")).place(x=1180,y=17)

            except Exception as e:
                print(e)

        def Verify_Function(self):
            ob1 = db.database()
            query = "select email from registration_table where email = '"+self.A_email_var.get()+"'"
            ob1.datalist = ob1.universal_getdata(query)
            print(self.A_v.get())
            if(len(ob1.datalist)!=0):
                st=str(ob1.datalist[0])
                st=st[2:st.rindex("'",0,len(st))]
            else:st=""
            if( self.A_email_var.get()==""):
                messagebox.showerror("GAS","Text Field is empty!!!")
            elif st == self.A_email_var.get() and self.A_email_var.get()!="":
                self.j=1
                messagebox.showinfo("GAS","Verified")
                #self.A_proceed_btn.config(bg="red")
                #self.A_proceed_btn["state"] = NORMAL

            else:
                messagebox.showerror("GAS","Not verified")
            '''i=0
            for i in range(0,len(ob1.datalist)):
                print(ob1.datalist[i])
                if ob1.datalist[i].email == self.A_email_var.get():
                    messagebox.showinfo("GAS","Verified")
                else:
                    messagebox.showerror("GAS","Not verified")'''

        def Proceed_Function(self):
            if(self.j==1):
                self.j=0
                #print(self.A_v.get())
                if(self.A_v.get()==0):
                    messagebox.showerror("GAS","Please Select the radio button first...!")
                elif(self.A_v.get()==1):  
                    p="p1"
                    self.A_fileDialog(p)  
                elif(self.A_v.get()==2):  
                    p="p1"
                    self.A_fileDialog(p)
                else:
                    messagebox.showerror("GAS","Hii!")
            else:
                messagebox.showerror("GAS","Please Verify Email first!")


        def A_fileDialog(self,pts): 
            ob2 = db.database()
            query = "select "+pts+" from registration_table where email = '"+self.A_email_var.get()+"'"
            ob2.datalist = ob2.universal_getdata(query)
            print(ob2.datalist)
            st=""
            self.st1=""
            self.st2=""
            if(len(ob2.datalist)!=0):
                st=str(ob2.datalist[0])
                st=st[2:st.index("#",0,len(st))-1]
                print(st)
                self.st1=str(ob2.datalist[0])
                self.st1=self.st1[len(st)+6:self.st1.index(",",0,len(self.st1))]
                print(self.st1)
                self.st2=str(ob2.datalist[0])
                self.st2=self.st2[self.st2.index(" ",len(st)+6,len(self.st2))+1:self.st2.rindex(" ",len(st)+6,len(self.st2))]
                print(self.st2)
            
                if(st!="" ):
                    load = Image.open(st)
                    load = load.resize((594, 431), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    self.R_img = Label(self.A_Picture_Canvas, image=render)
                    self.R_img.image = render  
                    self.R_img.place(x=3, y=3 ,width=594, height=431)
                    self.R_img.bind("<Button-1>",self.A_printcoords)
                   
        def A_printcoords(self,event):
            print(event.x )
            print(event.y )
            self.k=self.k+1
            if(event.x>=int(self.st1)-10 and event.x<=int(self.st1)+10 and event.y>=int(self.st2)-10 and event.y<=int(self.st2)+10 and self.k==1):
                self.R_img.destroy()
                p="p2" 
                self.A_fileDialog(p)
            elif(event.x>=int(self.st1)-10 and event.x<=int(self.st1)+10 and event.y>=int(self.st2)-10 and event.y<=int(self.st2)+10 and self.k==2):
                self.R_img.destroy()
                p="p3" 
                self.A_fileDialog(p)
            elif(event.x>=int(self.st1)-10 and event.x<=int(self.st1)+10 and event.y>=int(self.st2)-10 and event.y<=int(self.st2)+10 and self.k==3):
                messagebox.showerror("GAS","Authentication done!")
                self.k=0
                self.R_img.destroy()
            else:
                self.R_img.destroy()
                self.k=0
                if(self.A_v.get()==1):
                    messagebox.showerror("GAS","Intruder detected!")
                    messagebox.showerror("GAS","System Shutdown Activated!")
                    self.close_window()
                elif(self.A_v.get()==2):
                    random.shuffle(self.imgs)
                    g=random.randint(0,5)
                    load = Image.open(self.imgs[g])
                    load = load.resize((594, 431), Image.ANTIALIAS)
                    render = ImageTk.PhotoImage(load)
                    self.R_img = Label(self.A_Picture_Canvas, image=render)
                    self.R_img.image = render  
                    self.R_img.place(x=3, y=3 ,width=594, height=431)
                    self.R_img.bind("<Button-1>",self.A_printcoords)

        def close_window (self): 
            app.destroy()
        
        def Forgot_Function(self):
            a=simpledialog.askstring("Forgot Password","Enter Your Email:-")
            ob1 = db.database()
            query = "select question from registration_table where email = '"+a+"'"
            ob1.datalist = ob1.universal_getdata(query)
            st=str(ob1.datalist)
            st=st[3:len(st)-4]
            if(a==st):
                b=simpledialog.askstring("Forgot Password",st+"?")
                ob2 = db.database()
                query1 = "select answer from registration_table where email = '"+a+"'"
                ob2.datalist = ob2.universal_getdata(query1)
                st=str(ob2.datalist)
                st=st[3:len(st)-4]
                if(b==st):
                   self.A_controller.show_frame("Graph_Updation")


    class Graph_Updation(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)
            self.U_controller = controller
            Graph_Functions.G_upload_image(self,"bg7.jpg",1366, 700,self,-2,0)
            U_title=tk.Label(self,text="User's Details Updation",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#006666",fg="white",)
            U_title.pack(side=TOP,fill=X)

            #=========All Variables===========================
            self.U_image_count_var=[0,0,0]
            self.U_path_list_var=["","",""]
            self.i=0
            self.U_point_count_var=0
            self.U_name_var=StringVar()
            self.U_email_var=StringVar()
            self.U_contact_var=StringVar()
            self.U_question_var=StringVar()
            self.U_answeU_var=StringVar()
            self.filename=StringVar()
            self.U_cues_var=StringVar()
            self.U_Picture_Canvas=tk.Canvas()
            self.U_Image_Canvas=tk.Canvas()
            self.U_Left_Canvas=tk.Canvas()
            self.U_img=tk.Label()    # displays image
            self.U_img1=tk.Label()
            self.U_img2=tk.Label()
            self.U_img3=tk.Label()
            self.U_mousePosition = StringVar() # displays mouse position

            try:            
                #=========Register Canvas===========================

                self.U_Left_Canvas=tk.Canvas(self,bd=0,relief=RIDGE,bg="#C79408")
                self.U_Left_Canvas.place(x=10,y=90,width=545,height=512)

                self.U_Left_Canvas.create_line(0, 3, 545, 3, width=3)  
                self.U_Left_Canvas.create_line(475, 2, 542, 70, width=3)
                self.U_Left_Canvas.create_line(541, 0, 541, 512, width=3)
                self.U_Left_Canvas.create_line(542, 369, 475, 437, width=3)
                self.U_Left_Canvas.create_line(0, 436, 545, 436, width=3)
                self.U_Left_Canvas.create_line(3, 0, 3, 512, width=3) 
                self.U_Left_Canvas.create_line(0, 508, 545, 508, width=3)

                U_Updation_title=tk.Label(self.U_Left_Canvas,text="UPDATION PROCESS",pady=0,bg="#C79408",fg="black",font=("times new roman",18,"bold"))
                U_Updation_title.place(x=9,y=8)
                
                self.U_Left_Canvas.create_line(11, 41, 311, 41, width=3) 
                self.U_Left_Canvas.create_line(12, 53, 12, 275, width=2)

                Graph_Functions.G_upload_image(self,'close_lock.jpg',127, 140,self.U_Left_Canvas,355,25)

                U_lbl_name=tk.Label(self.U_Left_Canvas,text="NAME",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_name.place(x=20,y=55,width=65,height=22)
                U_txt_name=tk.Entry(self.U_Left_Canvas,textvariable=self.U_name_var,width=25,font=("times new roman",15,""),bd=2,relief=GROOVE)
                U_txt_name.place(x=90,y=52)

                U_lbl_email=tk.Label(self.U_Left_Canvas,text="EMAIL",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_email.place(x=20,y=88,width=68,height=22)
                U_txt_email=tk.Entry(self.U_Left_Canvas,width=25,font=("times new roman",15,""),textvariable = self.U_email_var,bd=2,relief=GROOVE)
                U_txt_email.place(x=90,y=85)

                U_lbl_mob=tk.Label(self.U_Left_Canvas,text="CONTACT",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_mob.place(x=20,y=121,height=22)
                U_txt_mob=tk.Entry(self.U_Left_Canvas,width=21,font=("times new roman",15,""),textvariable = self.U_contact_var,bd=2,relief=GROOVE)
                U_txt_mob.place(x=130,y=118)

                U_lbl_pts=tk.Label(self.U_Left_Canvas,text="CUE POINTS COLLECTED",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_pts.place(x=20,y=150)
                self.U_Scroll_Frame = tk.Frame(self.U_Left_Canvas, bd=2, relief=SUNKEN)
                self.U_Scroll_Frame.place(x=20,y=175,width=400,height=100)

                self.U_xscroll = tk.Scrollbar(self.U_Scroll_Frame, orient=HORIZONTAL)
                self.U_xscroll.pack(side=BOTTOM,fill=X)
                self.U_yscroll = tk.Scrollbar(self.U_Scroll_Frame, orient=VERTICAL)
                self.U_yscroll.pack(side=RIGHT,fill=Y)
                self.U_mylist = tk.Listbox(self.U_Scroll_Frame, yscrollcommand=self.U_yscroll.set)
                
                U_forgot_title=tk.Label(self.U_Left_Canvas,text="FORGOT PASSWORD",pady=0,bg="#C79408",fg="black",font=("times new roman",18,"bold"))
                U_forgot_title.place(x=9,y=280)

                self.U_Left_Canvas.create_line(11, 313, 256, 313, width=3)
                self.U_Left_Canvas.create_line(12, 322, 12, 430, width=2)

                U_lbl_ques=tk.Label(self.U_Left_Canvas,text="CUSTOM QUESTION",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_ques.place(x=20,y=318)
                U_txt_ques=tk.Entry(self.U_Left_Canvas,textvariable = self.U_question_var,width=40,font=("times new roman",15,""),bd=2,relief=GROOVE)
                U_txt_ques.place(x=20,y=345)

                U_lbl_ans=tk.Label(self.U_Left_Canvas,text="CUSTOM ANSWER",bg="#C79408",fg="black",font=("times new roman",15,"bold"))
                U_lbl_ans.place(x=20,y=375)
                U_txt_ans=tk.Entry(self.U_Left_Canvas,textvariable = self.U_answeU_var,width=40,font=("times new roman",15,""),bd=2,relief=GROOVE)
                U_txt_ans.place(x=20,y=402)

                U_lbl_update=tk.Label(self.U_Left_Canvas,text ="UPDATE\nTO DB",bg="#C79408",fg="black",font=("Franklin Gothic Book",12,"bold"))
                U_lbl_update.place(x=29,y=452,width=104,height=44)
                U_update_btn=tk.Button(self.U_Left_Canvas,text="UPDATE",command = self.registerfn,font=("times new roman",15,"bold")).place(x=135,y=454)

                U_lbl_save=tk.Label(self.U_Left_Canvas,text ="SAVE",bg="#C79408",fg="black",font=("Franklin Gothic Book",15,"bold"))
                U_lbl_save.place(x=350,y=459,width=60)
                U_save_btn=tk.Button(self.U_Left_Canvas,text="SAVE",command=self.collection,font=("times new roman",15,"bold")).place(x=425,y=454)

                U_reset_btn=tk.Button(self,text="RESET",command=self.clear,bg="#FF6666",font=("times new roman",15,"bold")).place(x=593,y=543)
                #=========Image Canvas===========================

                self.U_Image_Canvas=tk.Canvas(self,bd=4,relief=RIDGE,bg="#B999FA")
                self.U_Image_Canvas.place(x=715,y=90,width=637,height=512)

                U_Image_title=tk.Label(self.U_Image_Canvas,text="IMAGE",bg="#B999FA",fg="black",font=("times new roman",25,"bold"))
                U_Image_title.place(x=270,y=6)

                self.U_Image_Canvas.create_line(270, 50, 390, 50, width=3)

                #=========Picture Canvas===========================

                self.U_Picture_Canvas=Canvas(self.U_Image_Canvas,bd=0,relief=RIDGE,bg="crimson")
                self.U_Picture_Canvas.place(x=18,y=60,width=600,height=437)

                for i in range(25,600,25):
                    self.U_Picture_Canvas.create_line(i,3,i,434,fill="black")
                
                for i in range(25,437,25):
                    self.U_Picture_Canvas.create_line(3,i,597,i,fill="black")

                #=========Bottom self.U_Scroll_Frame===========================

                U_Bottom_Canvas=Frame(self,bd=4,relief=RIDGE,bg="#1E90FF")
                U_Bottom_Canvas.place(x=10,y=610,width=1340,height=80)

                U_lbl_load_pic=Label(U_Bottom_Canvas,text="LOAD\nPICTURE",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                U_lbl_load_pic.place(x=70,y=15,width=75,height=44)

                U_load_pic_btn=Button(U_Bottom_Canvas,text="LOAD PIC",command=self.fileDialog,font=("times new roman",15,"bold")).place(x=155,y=17)

                U_lbl_cue=Label(U_Bottom_Canvas,text="CUE\nPOINTS",bg="#1E90FF",fg="black",font=("times new roman",13,"bold"))
                U_lbl_cue.place(x=563,y=15,width=67,height=44)

                U_lbl_points=Label(U_Bottom_Canvas,textvariable = self.U_mousePosition,bd=3,relief=RIDGE,bg="white",fg="black",font=("times new roman",18,"bold"))
                U_lbl_points.place(x=640,y=15,width=150,height=45)             
                
                U_lbl_exit=Label(U_Bottom_Canvas,text ="EXIT TO\nMAIN MENU",bg="#1E90FF",fg="white",font=("times new roman",12,"bold"))
                U_lbl_exit.place(x=1066,y=15,width=104,height=44)

                U_cancel_btn=Button(U_Bottom_Canvas,text="CANCEL",fg="black",command=lambda: controller.show_frame("Graph_Home"),bg="white",font=("times new roman",15,"bold")).place(x=1180,y=17)

            except Exception as e:
                print(e)

        #=========Image Loading function===========================
        def fileDialog(self): 
            self.filename = filedialog.askopenfilename(initialdir =  "S:/", title = "Select A File", filetype =
            (("jpeg files","*.jpg"),("all files","*.*")) )
            if(self.filename!="" and self.i<3):
                self.U_image_count_var[self.i]=1
                load = Image.open(self.filename)
                load = load.resize((594, 431), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
                self.U_img = Label(self.U_Picture_Canvas, image=render)
                self.U_img.image = render  
                self.U_img.place(x=3, y=3 ,width=594, height=431)
                self.U_img.bind("<Button-1>",self.printcoords)
                
                if(self.i==0):
                    load1 = Image.open(self.filename)
                    load1 = load1.resize((151, 110), Image.ANTIALIAS)
                    render1 = ImageTk.PhotoImage(load1)
                    self.U_img1 = Label(self, image=render1)
                    self.U_img1.image = render1
                    self.U_img1.place(x=560, y=115 ,width=151, height=110)
                elif(self.i==1):
                    load2 = Image.open(self.filename)
                    load2 = load2.resize((151, 110), Image.ANTIALIAS)
                    render2 = ImageTk.PhotoImage(load2)
                    self.U_img2 = Label(self, image=render2)
                    self.U_img2.image = render2
                    self.U_img2.place(x=560, y=255 ,width=151, height=110)
                elif(self.i==2):
                    load3 = Image.open(self.filename)
                    load3 = load3.resize((151, 110), Image.ANTIALIAS)
                    render3 = ImageTk.PhotoImage(load3)
                    self.U_img3 = Label(self, image=render3)
                    self.U_img3.image = render3
                    self.U_img3.place(x=560, y=395 ,width=151, height=110)
            elif(self.filename!="" and self.i>=3):
                messagebox.showerror("GAS","Images are over...!")    
                
        #Function to be called when mouse is clicked on the image
        def printcoords(self,event):
            self.U_point_count_var=1
            self.U_cues_var.set("[ " + str( event.x ) +  ", " + str( event.y ) + " ]")
            self.U_mousePosition.set( "[ " + str( event.x ) + ", " + str( event.y ) + " ]" )

        #Function to be called when save button is clicked
        def collection(self):   
            if(self.i<3):
                if(self.U_image_count_var[self.i]!=0) : 
                    if(self.U_point_count_var!=0) :
                        self.U_path_list_var[self.i]=self.filename +"  #"+ self.U_cues_var.get()
                        self.U_point_count_var=0  
                        self.U_mylist.insert(END, self.filename +"  #"+ self.U_cues_var.get() )  
                        self.U_mylist.pack( side = TOP ,fill=BOTH)
                        self.U_xscroll.config(command=self.U_mylist.xview)
                        self.U_yscroll.config(command=self.U_mylist.yview)
                        self.U_mousePosition.set("")
                        self.U_cues_var.set("")
                        self.U_img.destroy()
                        self.i=self.i+1
                    else:
                        self.U_mousePosition.set("")
                        self.U_cues_var.set("")
                        self.U_point_count_var=0
                        messagebox.showerror("GAS","Please Select Cue Point on the Image first...!")    
                else:
                    self.U_mousePosition.set("")
                    self.U_mousePosition.set("")
                    self.U_cues_var.set("")
                    self.U_point_count_var=0
                    messagebox.showerror("GAS","Please Upload the Image first...!")
            else:
                self.U_mousePosition.set("")
                self.U_mousePosition.set("")
                self.U_cues_var.set("")
                self.U_point_count_var=0
                messagebox.showinfo("GAS","All the Images and Cue Points\nare saved successfully...!")
        
        #Function to be called when register button is clicked !
        def registerfn(self):
            ob = db.database()
            is_success=0
            if(self.U_name_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the name")
            elif(self.U_email_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the email")
            elif(self.U_contact_var.get() == ''):
                messagebox.showinfo("GAS","Please enter the contact number")
            

            if( self.U_image_count_var[0]!=0 and self.U_image_count_var[1]!=0 and self.U_image_count_var[2]!=0 and self.U_name_var!="" and self.U_email_var!="" and self.U_question_var!="" and self.U_answeU_var!="" ):
                #query = "update registration_table set name = %s,email = %s,contact = %s, question = %s,answer = %s,p1 = %s,p2 = %s, p3 = %s"
                val = (self.U_name_var.get(),self.U_email_var.get(),self.U_contact_var.get(),self.U_question_var.get(),self.U_answeU_var.get(),self.U_path_list_var[0],self.U_path_list_var[1],self.U_path_list_var[2])
                is_success = ob.universal_Transact(query, val)
            if is_success == 1:
                messagebox.showinfo("GAS","done")
            else:
                messagebox.showinfo("GAS","not done")
            self.clear()
                
        #Function to be called when reset button is clicked...!
        def clear(self):
            if( self.U_image_count_var[0]==0 and self.U_image_count_var[1]==0 and self.U_image_count_var[2]==0 and self.i==0 and self.U_point_count_var==0 and self.U_name_var=="" and self.U_email_var=="" and self.U_contact_var=="" and self.U_question_var=="" and self.U_answeU_var=="" and self.filename=="" and self.U_cues_var=="" and self.U_mousePosition == "" ):
                messagebox.showerror("Error","All Fields are already Empty!!!")
            else:
                self.U_image_count_var[0]=0
                self.U_image_count_var[1]=0
                self.U_image_count_var[2]=0
                self.i=0
                self.U_point_count_var=0
                self.U_name_var.set("")
                self.U_email_var.set("")
                self.U_contact_var.set("")
                self.U_question_var.set("")
                self.U_answeU_var.set("")
                self.filename=""
                self.U_cues_var.set("")
                self.U_mousePosition.set("")
                self.U_img.destroy()
                self.U_img1.destroy()
                self.U_img2.destroy()
                self.U_img3.destroy()
                self.U_mylist.delete(0,END)
                self.U_path_list_var[0]=""
                self.U_path_list_var[1]=""
                self.U_path_list_var[2]=""

    class Graph_Admin(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.Am_controller = controller
            Graph_Functions.G_upload_image(self, "bg3.jpg", 1366, 700, self, -2, 0)
            title = tk.Label(self, text="Graphical Authentication System", bd=10, relief=GROOVE,
                             font=("times new roman", 40, "bold"), bg="#800000", fg="white", )
            title.pack(side=TOP, fill=X)

            # =========All Variables===========================

            self.Am_name_var = StringVar()
            self.Am_email_var = StringVar()
            self.Am_contact_var = StringVar()
            self.Am_question_var = StringVar()
            self.Am_answer_var = StringVar()
            self.Am_filename = StringVar()
            self.Am_cues_var = StringVar()
            self.Am_Picture_Canvas = tk.Canvas()
            self.Am_Image_Canvas = tk.Canvas()
            self.Am_Register_Canvas = tk.Canvas()
            self.Am_img = tk.Label()  # displays image
            self.Am_img1 = tk.Label()
            self.Am_mousePosition = StringVar()  # displays mouse position

            try:
                Graph_Functions.G_upload_image(self, 'GraphicalLogo.jpg', 600, 400, self, 90, 190)
                # =========Right Canvas===========================
                Am_lbl_username = tk.Label(self, text="Username", bg="black", fg="white",
                                      font=("times new roman", 30, "bold"))
                Am_lbl_username.place(x=820, y=318)

                Am_lbl_password = tk.Label(self, text="Password", bg="black", fg="white",
                                       font=("times new roman", 30, "bold"))
                Am_lbl_password.place(x=820, y=400)

                Am_txt_username = tk.Entry(self, width=21, font=("times new roman", 15, ""),
                                      bd=2, relief=GROOVE)
                Am_txt_username.place(x=1020, y=325)

                Am_txt_password = tk.Entry(self, width=21, font=("times new roman", 15, ""),
                                           bd=2, relief=GROOVE)
                Am_txt_password.place(x=1020, y=410)

                Am_login_btn = tk.Button(self, text="Login",
                                       font=("times new roman", 15, "bold")).place(x=930, y=500)

                Am_cancel_btn = tk.Button(self, text="Cancel",command=lambda: controller.show_frame("Graph_Home"),
                                         font=("times new roman", 15, "bold")).place(x=1020, y=500)

                Graph_Functions.G_upload_image(self, 'AdminLogo.png', 150, 152, self, 960, 115)



            except Exception as e:
                print(e)

        def Am_About_Function(self):
            messagebox.showinfo("GAS",
                                "The Graphical Authentication System Project is made by\n-MUZAMMIL AHSAN\n-IMAN ABBAS\n-PRAKHAR SINGH")

        def close_window(self):
            x = messagebox.askquestion("Confirm", "Are you sure?")
            if (x == "yes"):
                app.destroy()



            
    class Graph_Functions:
        #Image Uploading function      
        def G_upload_image(self,img,wt,ht,pos,x1,y1):
            load = Image.open(img)
            load = load.resize((wt, ht), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            self.img = Label(pos, image=render)
            self.img.image = render
            self.img.place(x=x1, y=y1)


    app = SampleApp()
    if __name__ == "__main__":
        app.mainloop()

except Exception as et:
                print(et)