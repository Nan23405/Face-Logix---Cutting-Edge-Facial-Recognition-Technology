from email.mime import image
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np




 

class Face_Recognizing:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width = 1530, height=45)


        # Image 1
        img_bottom = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Recognized.jpg" 
        ).convert("RGB")

        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        self.f_lbl4 = Label(self.root, image=self.photoimg_bottom, bd=4, relief="solid", bg="white")
        self.f_lbl4.image = self.photoimg_bottom
        self.f_lbl4.place(x=0, y=440, width=1530, height=325)


        # # Image 2
        # img_bottom = Image.open(
        #     r"C:/Users/singh/Documents/Face_Rec Images/face_detector2.jpg" 
        # ).convert("RGB")

        # img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        # self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # self.f_lbl4 = Label(self.root, image=self.photoimg_bottom, bd=4, relief="solid", bg="white")
        # self.f_lbl4.image = self.photoimg_bottom
        # self.f_lbl4.place(x=600, y=55, width=950, height=700)
        




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognizing(root)
    root.mainloop()