from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import Face_Recognizing
from Students import Students
import os

from train import Train

class Face_Recognition_System:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Stanford.jpg"
        ).convert("RGB")

        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.f_lbl1 = Label(self.root, image=self.photoimg, bd=4, relief="solid", bg="yellow")
        self.f_lbl1.image = self.photoimg
        self.f_lbl1.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/facialrecognition.png"
        ).convert("RGB")

        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        self.f_lbl2 = Label(self.root, image=self.photoimg1, bd=4, relief="solid", bg="yellow")
        self.f_lbl2.image = self.photoimg1
        self.f_lbl2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/u.jpg"
        ).convert("RGB")

        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl3 = Label(self.root, image=self.photoimg2, bd=4, relief="solid", bg="white")
        self.f_lbl3.image = self.photoimg2
        self.f_lbl3.place(x=1000, y=0, width=550, height=130)

        # bg Image
        img3 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/bgimg.jpg"
        ).convert("RGB")

        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg = Label(self.root, image=self.photoimg3, bd=4, relief="solid", bg="white")
        self.bg.image = self.photoimg3
        self.bg.place(x=0, y=130, width=1530, height=710)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width = 1530, height=45)

        # Student Button
        img3 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/gettyimages.jpg"
        ).convert("RGB")
        img4 = img3.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Face Detection Button
        img5 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/face_detector1.jpg"
        ).convert("RGB")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance Button
        img6 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Attendance_1.jpg"
        ).convert("RGB")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help Desk Button
        img7 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Help Desk_0.png"
        ).convert("RGB")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)


        # Train Face Button
        img8 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Train data.jpg"
        ).convert("RGB")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)


        # Photos
        img9 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Photos_1.jpg"
        ).convert("RGB")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        
        # Developer Button
        img10 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Developer_1.jpg"
        ).convert("RGB")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)
        
        
        # Exit Button
        img11 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/exit.jpg"  # r"C:/Users/singh/Documents/Face_Rec Images/exit.jpg"
        ).convert("RGB")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    # ===================Function Buttons=====================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Students(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    #================= Train Data Function =================

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognizing(self.new_window)

    


if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition_System(root)
    root.mainloop()

# .\.venv\Scripts\Activate.ps1
# python First.py
