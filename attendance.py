from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images27.jpg")
        img = img.resize((800, 230), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=230)

        img1 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images28.jpg")
        img1 = img1.resize((800, 230), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=230)

        img3 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images29.jpg")
        img3 = img3.resize((1550, 750), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=230, width=1550, height=750)

        title_lbl = Label(bg_img, text="Attendance Managment System ", font=(
            "times new roman ", 35, "bold"), bg="NavyBlue", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=53)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=15, y=55, width=1500, height=580)

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=550)

        img_left = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images30.jpg")
        img_left = img_left.resize((750, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=2, y=0, width=755, height=150)

        left_inside_frame = Frame(Left_frame, relief=RIDGE, bd=2)
        left_inside_frame.place(x=2, y=155, width=752, height=300)

        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=(
            "times new roman", 13, "bold"))
        attendanceId_label.grid(row=0, column=0, padx=10, sticky=W)

        attendanceId_entry = ttk.Entry(
            left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, sticky=W)

        rollLabel = Label(left_inside_frame, text="Roll :",
                          font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=22,
                               font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        nameLabel = Label(left_inside_frame, text="Name:           ",
                          font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22,
                               font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        depLabel = Label(left_inside_frame, text="Department:",
                         font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=22,
                              font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        timeLabel = Label(
            left_inside_frame, text="Time :            ", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=22,
                               font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        dateLabel = Label(left_inside_frame, text="Date:",
                          font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=22,
                               font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        attendanceLabel = Label(
            left_inside_frame, text="Attendance :", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(
            left_inside_frame, font="comicsansns 11 bold", width=20, state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons Frame

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=190, width=750, height=38)

        # Save_BTN
        save_btn = Button(btn_frame, text="Import CSV", width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # Update_Btn
        update_btn = Button(btn_frame, text="Export CSV", width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # Delete_btn
        delete_btn = Button(btn_frame, text="Update", width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # Reset_btn
        reset_btn = Button(btn_frame, text="Reset", width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=800, y=10, width=685, height=550)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=670, height=450)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReport = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "Time", "Date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReport.xview)
        scroll_y.config(command=self.AttendanceReport.yview)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
