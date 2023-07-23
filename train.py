from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set ", font=(
            "times new roman ", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        img_top = Image.open(
            "Images\Images19.jpg")
        img_top = img_top.resize((1540, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=52, width=1540, height=325)

        # Buttons

        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier,  cursor="hand2", font=(
            "times new roman", 30, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=0, y=375, width=1540, height=90)

        img_bottom = Image.open(
            "Images\Images20.jpg")
        img_bottom = img_bottom.resize((1540, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=470, width=1540, height=325)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray Scale Image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        #============Train Claassifier=============#

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Results", "Training data set completed Successfully!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop(
    )
