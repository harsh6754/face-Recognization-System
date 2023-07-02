from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os

class Face_Recognition_System:
    def __init__(self, root):  
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    
        
        img = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images1.jpg")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        img1 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images2.jpg")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

        img2 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images1.jpg")
        img2 = img2.resize((550, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=150)

        img3 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images4.png")
        img3 = img3.resize((1550, 750), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1550, height=750)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE ", font=(
            "times new roman ", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        img4 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images5.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,command=self.student_details, image=self.photoimg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img,command=self.student_details, text="Student Details" ,  cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        img5 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images6.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        img6 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images7.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        img7 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images8.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        img8 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images10.png")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        img9 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images9.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,command=self.open_img, cursor="hand2")
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos",command=self.open_img, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        img10 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images11.png")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        img11 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images12.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)
        
    def open_img(self):
        os.startfile("data")
    
     
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
           
        
        
        
      
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
