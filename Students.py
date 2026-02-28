from email.mime import image
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

 

class Students:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #========= variables ==========

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentId=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_faculty=StringVar()


        # First Image
        img = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/student1_1.jpg"
        ).convert("RGB")

        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.f_lbl1 = Label(self.root, image=self.photoimg, bd=4, relief="solid", bg="yellow")
        self.f_lbl1.image = self.photoimg
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/students_2.jpg"
        ).convert("RGB")

        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl2 = Label(self.root, image=self.photoimg1, bd=4, relief="solid", bg="yellow")
        self.f_lbl2.image = self.photoimg1
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/st_1.jpg"
        ).convert("RGB")

        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl3 = Label(self.root, image=self.photoimg2, bd=4, relief="solid", bg="white")
        self.f_lbl3.image = self.photoimg2
        self.f_lbl3.place(x=1000, y=0, width=550, height=130)

        # bg Image
        img3 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/bg_future.webp"
        ).convert("RGB")

        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg = Label(self.root, image=self.photoimg3, bd=4, relief="solid", bg="white")
        self.bg.image = self.photoimg3
        self.bg.place(x=0, y=130, width=1530, height=710)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width = 1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1490, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10,y=10, width=760, height=580)

        # Left Image
        img_left = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/facial-recognition_0.jpg"
        ).convert("RGB")

        img_left = img_left.resize((750, 150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        self.f_lbl3 = Label(Left_frame, image=self.photoimg_left, bd=4, relief="solid", bg="white")
        self.f_lbl3.image = self.photoimg_left
        self.f_lbl3.place(x=8, y=0, width=750, height=150)

        # Current Course
        current_course_frame = LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=8,y=150, width=750, height=110)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering")
        dep_combo.current(0) # Will show Select Departmnet
        dep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "B.Sc", "M.Sc")
        course_combo.current(0) # Will show Select Course
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        Year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27")
        Year_combo.current(0) # Will show Select Year
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        semester_combo.current(0) # Will show Select Semester
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=8,y=260, width=750, height=295)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_studentId, font=("times new roman", 13, "bold"), width=20)
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, font=("times new roman", 13, "bold"), width=20)
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), width=20)
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        division_combo = ttk.Combobox(current_course_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
        division_combo["values"] = ("Division", "A", "B", "C", "D")
        division_combo.current(0) # Will show Select Division
        division_combo.grid(row=1, column=1, padx=1, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll_no, font=("times new roman", 13, "bold"), width=20)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0) # Will show Select Gender
        gender_combo.grid(row=2,column=1,padx=2,pady=5)

        # Date of Birth
        dob_label = Label(class_student_frame,text="DOB (DD/MM/YYYY)",font=("times new roman", 13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=(5),sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, font=("times new roman", 13,"bold"),width=(20))
        dob_entry.grid(row=2,column=3,padx=(10),pady=(5),sticky=W)

        # Email
        email_label = Label(class_student_frame,text="Email",font=("times new roman", 13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=(5),sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=("times new roman", 13,"bold"),width=(20))
        email_entry.grid(row=3,column=1,padx=(10),pady=(5),sticky=W)

        # Phone No.
        phone_label = Label(class_student_frame,text="Phone No.",font=("times new roman", 13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, font=("times new roman", 13,"bold"),width=(20))
        phone_entry.grid(row=3,column=3,padx=10,pady=(5),sticky=W)

        # Address
        address_label = Label(class_student_frame,text="Address",font=("times new roman", 13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, font=("times new roman", 13,"bold"),width=(20))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Faculty Name
        faculty_label = Label(class_student_frame,text="Faculty Name",font=("times new roman", 13,"bold"),bg="white")
        faculty_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        faculty_entry = ttk.Entry(class_student_frame, textvariable=self.var_faculty, font=("times new roman", 13,"bold"),width=(20))
        faculty_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", value="Yes", variable=self.var_radio1)
        radio_btn1.grid(row=5, column=0, padx=10, pady=10)

        # self.var_radio2 = StringVar()
        radio_btn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", value="No", variable=self.var_radio1)
        radio_btn2.grid(row=5, column=1, padx=10, pady=10)

        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=745, height=30) #220, 35

        # Save Button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5)

        #Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # button frame 2
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=245, width=745, height=30)

        # Take Photo Sample Button
        take_photo_btn = Button(btn_frame1, command=self.genertate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=5)

        # Update Photo Sample Button
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", command="", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=5)



        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780,y=10, width=700, height=580) # 780,660

        img_right = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/sty1.jpg"
        ).convert("RGB")

        img_right = img_right.resize((750, 150), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        self.f_lbl4 = Label(Right_frame, image=self.photoimg_right, bd=4, relief="solid", bg="white")
        self.f_lbl4.image = self.photoimg_right
        self.f_lbl4.place(x=5, y=0, width=750, height=150)

        #=========Search System ==================
        Search_frame = LabelFrame(Right_frame,bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5,y=150, width=690, height=70) #260,295

        # Search By Label
        search_label = Label(Search_frame,text="Search By:",font=("times new roman", 13,"bold"), bg="sky blue", width=14) #15
        search_label.grid(row=0,column=0,padx=6,pady=5,sticky=W) 

        # SEarch combo box
        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=12) #20
        search_combo["values"] = ("Select", "Roll_No", "Phone_No", "ID")
        search_combo.current(0) # Will show Select Semester
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Search Entry
        search_entry = ttk.Entry(Search_frame,text="",font=("times new roman", 13,"bold"),width=12)
        search_entry.grid(row=0,column=2,padx=10,pady=(5),sticky=W)

        # Search Button
        search_btn = Button(Search_frame, text="Search", command="", width=11, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5)

        # showAll Button
        showAll_btn = Button(Search_frame, text="Show All", command="", width=11, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5)

        #=========Table Frame ==================
        # table_frame = LabelFrame(Right_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        # table_frame.place(x=5,y=220, width=690, height=150) 

        table_frame = Frame(Right_frame,bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5,y=220, width=690, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        # Use 'columns' (plural) and hide the implicit tree column ('#0')
        # so the headings line up exactly with the columns and no extra empty
        # column appears at the left. Department will be the first visible column.
        self.student_table = ttk.Treeview(
            table_frame,
            columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "faculty", "photo"),
            show='headings',
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("faculty", text="Faculty Name")
        self.student_table.heading("photo", text="Photo Sample Status")


        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("faculty", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    
    # ==================== Function Delclaration ==================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentId.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll_no.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="Root@1234", database="face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_studentId.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll_no.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_faculty.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    # ======================= fetch data ==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="Root@1234", database="face_recog")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ======================= get cursor ==================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_studentId.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll_no.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_faculty.set(data[13])
        self.var_radio1.set(data[14])

    # ======================= update function ==================
    
    # def update_data(self):
    #     if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentId.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll_no.get() == "":
    #         messagebox.showerror("Error", "All Fields are required", parent=self.root)
    #     else:
    #         try:
    #             update=messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
    #             if update>0:
    #                 conn=mysql.connector.connect(host="localhost", username="root", password="Root@1234", database="face_recog")
    #                 my_cursor=conn.cursor()
    #                 my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Faculty=%s, PhotoSample=%s where Student_id=%s", (
    #                       self.var_dep.get(),
    #                       self.var_course.get(),
    #                       self.var_year.get(),
    #                       self.var_semester.get(),
    #                       self.var_std_name.get(),
    #                       self.var_div.get(),
    #                       self.var_roll_no.get(),
    #                       self.var_gender.get(),
    #                       self.var_dob.get(),
    #                       self.var_email.get(),
    #                       self.var_phone.get(),
    #                       self.var_address.get(),
    #                       self.var_faculty.get(),
    #                       self.var_radio1.get(),
    #                       self.var_studentId.get()
    #                 ))
    #             else:
    #                 if not update:
    #                     return
    #             messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentId.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll_no.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return

        Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
        if not Update:
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Root@1234",
                database="face_recog"
            )

            my_cursor = conn.cursor()

            

            my_cursor.execute("""
                UPDATE student SET
                Dep=%s, course=%s, Year=%s, Semester=%s,
                Name=%s, Division=%s, Roll=%s, Gender=%s,
                Dob=%s, Email=%s, Phone=%s, Address=%s,
                Faculty=%s, PhotoSample=%s
                WHERE `Student id`=%s

            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_faculty.get(),
                self.var_radio1.get(),
                self.var_studentId.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)


    # =========================delete function ==================

    def delete_data(self):
        if self.var_studentId.get() =="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Student", "Do you want to delete this student?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="Root@1234", database="face_recog")
                    my_cursor=conn.cursor()
                    sql="delete from student where `Student id`=%s"
                    val=(self.var_studentId.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)


    # ========================= reset function ==================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentId.set("")
        self.var_std_name.set("")
        self.var_div.set("Division")
        self.var_roll_no.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("No")

    # ==================== Generate data set or take photo sample ==================
    def genertate_dataset(self):
         
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_studentId.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll_no.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return

            # Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            # if not Update:
            #     return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Root@1234",
                database="face_recog"
            )

            my_cursor = conn.cursor()
            my_cursor.execute(" select * from student")
            myresult = my_cursor.fetchall()
            id = 0
            for x in myresult:
                id += 1
            my_cursor.execute("""
                UPDATE student SET
                Dep=%s, course=%s, Year=%s, Semester=%s,
                Name=%s, Division=%s, Roll=%s, Gender=%s,
                Dob=%s, Email=%s, Phone=%s, Address=%s,
                Faculty=%s, PhotoSample=%s
                WHERE `Student id`=%s

            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll_no.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_faculty.get(),
                self.var_radio1.get(),
                self.var_studentId.get()== id+1
            ))

            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            #=================== Load predifined data on face frontals from opencv ==============================
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray, 1.3, 5)
                # scalling factor = 1.3
                # Minimum neighbor = 5
                for (x,y,w,h) in faces:
                    face_cropped=img[y:y+h, x:x+w]
                    return face_cropped
                
            cap=cv2.VideoCapture(0)
            image_id=0
            while True:
                ret, my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                    image_id+=1
                    face=cv2.resize(face_cropped(my_frame), (450, 450))
                    face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(image_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1)==13 or int(image_id)==100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Result", "Generating data set completed!!!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                
if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()  