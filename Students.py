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
        current_course_frame.place(x=8,y=150, width=750, height=150)

        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering")
        dep_combo.current(0) # Will show Select Departmnet
        dep_combo.grid(row=0, column=1, padx=2, pady=5)

        # Right label frame
        Right_frame = LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=780,y=10, width=660, height=580)
if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()