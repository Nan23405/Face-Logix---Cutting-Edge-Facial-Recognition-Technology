from email.mime import image
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np

 

class Train:
    def __init__(self, root):
        print("INIT CALLED")

        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="TRAINING DATASET", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width = 1530, height=45)

        # TOP IMAGE
        img_top = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/facialrecognition.png" #Recognized.jpg
        ).convert("RGB")

        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        self.f_lbl3 = Label(self.root, image=self.photoimg_top, bd=4, relief="solid", bg="white")
        self.f_lbl3.image = self.photoimg_top
        self.f_lbl3.place(x=0, y=45, width=1530, height=325)

        
        # Button
        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=400, y=380, width=220, height=40)

        #BOTTOM IMAGE
        img_bottom = Image.open(
            r"C:/Users/singh/Documents/Face_Rec Images/Recognized.jpg" 
        ).convert("RGB")

        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        self.f_lbl4 = Label(self.root, image=self.photoimg_bottom, bd=4, relief="solid", bg="white")
        self.f_lbl4.image = self.photoimg_bottom
        self.f_lbl4.place(x=0, y=440, width=1530, height=325)

    # def train_classifier(self):
    #     data_dir=("data")
    #     path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
    #     # Example of training classifier logic
        

    #     faces = []
    #     ids= []

    #     for image in path:
    #         img = Image.open(image).convert('L') # grayscale image
    #         imageNp = np.array(img, 'uint8')

    #         id = int(os.path.split(image)[1].split('.')[1])
    #         faces.append(imageNp)
    #         ids.append(id)
    #         cv2.imshow("Training", imageNp)
    #         cv2.waitKey(1) == 13 # close window
    #     ids = np.array(ids) # Numpy increases the performance of the code and makes it faster. It is used to convert the list of ids into a numpy array for efficient processing.

    #     # ============= Train the classifier and save =======================
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.train(faces, ids)
    #     clf.save("classifier.xml")
    #     cv2.destroyAllWindows()
    #     messagebox.showinfo("Result", "Training of dataset is completed.")

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')

                filename = os.path.split(image)[1]
                id = int(filename.split('.')[1])

                faces.append(imageNp)
                ids.append(id)

                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            except Exception as e:
                print("Skipping file:", image, e)

        if len(faces) == 0:
            messagebox.showerror("Error", "No valid training images found")
            return

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        print("Saving classifier.xml...")   # ⭐ debug
        clf.save("classifier.xml")

        cv2.destroyAllWindows()

        messagebox.showinfo("Training", "Training dataset completed.")





if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()  