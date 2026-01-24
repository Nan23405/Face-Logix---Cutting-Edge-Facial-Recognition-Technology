from tkinter import *
from PIL import Image, ImageTk

class Students:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/students_1.jpg"
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
            r"C:/Users/singh/Documents/Face_Rec Images/students_3.jpg"
        ).convert("RGB")

        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        self.f_lbl3 = Label(self.root, image=self.photoimg2, bd=4, relief="solid", bg="white")
        self.f_lbl3.image = self.photoimg2
        self.f_lbl3.place(x=1000, y=0, width=550, height=130)

        # bg Image
        img3 = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/bgimg1.jpg"
        ).convert("RGB")

        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg = Label(self.root, image=self.photoimg3, bd=4, relief="solid", bg="white")
        self.bg.image = self.photoimg3
        self.bg.place(x=0, y=130, width=1530, height=710)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Students Management SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width = 1530, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()