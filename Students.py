from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Students:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

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

        dep_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering")
        dep_combo.current(0) # Will show Select Departmnet
        dep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "B.Sc", "M.Sc")
        course_combo.current(0) # Will show Select Course
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Year_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        Year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        Year_combo.current(0) # Will show Select Year
        Year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        semester_combo.current(0) # Will show Select Semester
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame,bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=8,y=260, width=750, height=295)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_student_frame, font=("times new roman", 13, "bold"), width=20)
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, font=("times new roman", 13, "bold"), width=20)
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, font=("times new roman", 13, "bold"), width=20)
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, font=("times new roman", 13, "bold"), width=20)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0) # Will show Select Gender
        gender_combo.grid(row=2,column=1,padx=2,pady=5)

        # Date of Birth
        dob_label = Label(class_student_frame,text="DOB (DD/MM/YYYY)",font=("times new roman", 13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=(5),sticky=W)

        dob_entry = ttk.Entry(class_student_frame,text="",font=("times new roman", 13,"bold"),width=(20))
        dob_entry.grid(row=2,column=3,padx=(10),pady=(5),sticky=W)

        # Email
        email_label = Label(class_student_frame,text="Email",font=("times new roman", 13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=(5),sticky=W)

        email_entry = ttk.Entry(class_student_frame,text="",font=("times new roman", 13,"bold"),width=(20))
        email_entry.grid(row=3,column=1,padx=(10),pady=(5),sticky=W)

        # Phone No.
        phone_label = Label(class_student_frame,text="Phone No.",font=("times new roman", 13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,text="",font=("times new roman", 13,"bold"),width=(20))
        phone_entry.grid(row=3,column=3,padx=10,pady=(5),sticky=W)

        # Address
        address_label = Label(class_student_frame,text="Address",font=("times new roman", 13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(class_student_frame,text="",font=("times new roman", 13,"bold"),width=(20))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Faculty Name
        faculty_label = Label(class_student_frame,text="Faculty Name",font=("times new roman", 13,"bold"),bg="white")
        faculty_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        faculty_entry = ttk.Entry(class_student_frame,text="",font=("times new roman", 13,"bold"),width=(20))
        faculty_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons
        radio_btn1 = ttk.Radiobutton(class_student_frame, text="Take Photo Sample", value="Yes")
        radio_btn1.grid(row=5, column=0, padx=10, pady=10)

        radio_btn2 = ttk.Radiobutton(class_student_frame, text="No Photo Sample", value="No")
        radio_btn2.grid(row=5, column=1, padx=10, pady=10)

        # Button Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=745, height=35) #220, 35

        save_btn = Button(btn_frame, text="Save", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=5)

        #Update Button
        update_btn = Button(btn_frame, text="Update", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=5)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # # Take Photo Sample Button
        # take_photo_btn = Button(btn_frame, text="Take Photo Sample", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        # take_photo_btn.grid(row=1, column=0)

        # # Update Photo Sample Button
        # update_photo_btn = Button(btn_frame, text="Update Photo Sample", command="", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        # update_photo_btn.grid(row=1, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780,y=10, width=660, height=580) 

        


if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()  