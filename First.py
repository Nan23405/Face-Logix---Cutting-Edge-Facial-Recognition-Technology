# from tkinter import*
# from tkinter import ttk
# from PIL import Image, ImageTk


# class Face_Recognition_System:
#     def __init__(self, root): #constructor called
#         self.root = root #root window assigned to self.root
#         self.root.geometry("1530x790+0+0") #(Width,length,x-axis,y-axis)
#         self.root.title("Face Recognition System")

#         img = Image.open(r"C:/Users/singh/Documents/Face_Rec Images/Stanford.jpg") #image path set.
        
#         img = img.resize((500, 130), Image.Resampling.LANCZOS) #image resized
#         self.photoimg = ImageTk.PhotoImage(img) #image converted to PhotoImage

#         f_lbl = Label(self.root, image=self.photoimg)
#         f_lbl.image = self.photoimg   # <-- VERY IMPORTANT
#         f_lbl.place(x=0, y=0, width=500, height=130) #image placed on window



# if __name__ == "__main__": #main":
#     root = Tk() #creating object of Tk(toolkit) class
#     obj = Face_Recognition_System(root) #object class
#     root.mainloop() #mainloop is used to run the application, and wait for an event to occur

from tkinter import *
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Stanford.jpg"
        ).convert("RGB")

        # First Image
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

        img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        self.bg = Label(self.root, image=self.photoimg3, bd=4, relief="solid", bg="white")
        self.bg.image = self.photoimg3
        self.bg.place(x=1000, y=0, width=550, height=130)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

# .\.venv\Scripts\Activate.ps1
# python First.py
