from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images15.png")
        img = img.resize((500, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=150)

        img1 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images14.png")
        img1 = img1.resize((500, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=150)

        img2 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images13.png")
        img2 = img2.resize((550, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=150)

        img3 = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images16.png")
        img3 = img3.resize((1550, 750), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1550, height=750)

        title_lbl = Label(bg_img, text="Student Managment System ", font=(
            "times new roman ", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=50)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=55, width=1500, height=580)

        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=550)

        img_left = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images17.png")
        img_left = img_left.resize((750, 150), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=150)

        current_course_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=135, width=760, height=150)

        dep_label = Label(current_course_frame, text="Department",
                          font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=3)

        # Department

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department ", "Computer", "IT", "Mechanical", "Civil", "BioTech",
                               "BlockChain", "Ai", "Cyber-Security", "Electrical", "E&C", "Robotics", "Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # Courses

        course_label = Label(current_course_frame, text="Course",
                             font=("times new roman", 13, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Years

        year_label = Label(current_course_frame, text="Years",
                           font=("times new roman", 13, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        year_combo["values"] = ("Select Years", "2020",
                                "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

      # Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 13, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2 ", "Semester 3 ",
                                    "Semester 4 ", "Semester 5 ", "Semester 6 ", " Semester 7 ", "Semester 8 ")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Labels

        class_student_frame = LabelFrame(
            main_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=10, y=250, width=760, height=310)

       # Student_ID

        studentId_label = Label(class_student_frame, text="StudentID:", font=(
            "times new roman", 13, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_frame, textvariable=self.va_std_id, width=20, font=("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student_Name

        studentName_label = Label(class_student_frame, text="Student Name:", font=(
            "times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Student_division

        class_div_label = Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 13, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        class_div_combo["values"] = ("Select Division", "1A11",
                                     "2A11", "3A11", "4A11", "5A11")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Student_Roll.No

        roll_no_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 13, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender

        gender_label = Label(class_student_frame, text="Gender:", font=(
            "times neww roman", 13, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB

        dob_label = Label(class_student_frame, text="DOB:",
                          font=("times new roman ", 13, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20,
                              font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email

        email_label = Label(class_student_frame, text="Email:",
                            font=("times new roman", 13, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

       # Phone No

        phone_label = Label(class_student_frame, text="Phone No:",
                            font=("times new roman", 13, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, pady=5, padx=10, sticky=W)

        # Address

        address_label = Label(class_student_frame, text="Address:", font=(
            "times new roman", 13, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

    # Teacher Name

        teacher_label = Label(class_student_frame, text="Teacher Name:", font=(
            "times new roman", 13, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

      # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take a Photo Sample", value="Yes")
        radiobtn1.grid(row=5, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

       # Buttons Frame

        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=210, width=755, height=40)

        # Save_BTN
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

       # Update_Btn
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

      # Delete_btn
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)


# Reset_btn
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=250, width=755, height=35)


# Take Photo_btn
        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset, width=37, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)


# Update Photo_btn
        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=37, font=(
            "times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


# Right_Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=800, y=10, width=660, height=550)

        img_right = Image.open(
            r"C:\Users\agarw\OneDrive\Desktop\harsh project\Face Recogintion System\Images\Images18.png")
        img_right = img_right.resize((750, 105), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=650, height=105)

     #==============Search System==============#
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=110, width=650, height=70)

      # Search Bar
        search_label = Label(search_frame, text="Search By:", font=(
            "times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)


# Search_Btn
        search_btn = Button(search_frame, text="Search", width=10, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=3)

# Show_All_Btn
        showAll_btn = Button(search_frame, text="Show All", width=9, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=3)

# Table_Frame
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=190, width=650, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("Department", "Course", "Year", "Semester", "ID", "Name", "Division", "Roll",
                                          "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll", text="Roll")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="H@rsh2810", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.va_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="H@rsh2810", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
        for i in data:
            self.student_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Field Are Required", parent=self.root
            )
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do You Want To Update This Data?", parent=self.root
                )
                if update:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="H@rsh2810", database="face_recognition"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        f'UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s,'
                        f'Gender=%s,dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s', (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.va_std_id.get()
                        ),
                    )
                    conn.commit()
                    messagebox.showinfo(
                        "Success", "Student Details Update Successfully", parent=self.root)

                else:
                    return
            except Exception as e:
                messagebox.showerror(
                    "Error", f"Due To: {str(e)}", parent=self.root)

    def delete_data(self):
        if self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student Id Must Be Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Data", "Do you Want To Delete This Data", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="H@rsh2810", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Delete", "Successfully Delete Student  Details", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Years")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #============================= Generate Data Set ===================#


    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="H@rsh2810", database="face_recognition"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()

                id = len(myresult) + 1

                my_cursor.execute(
                    "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s,"
                    "Gender=%s, dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        id
                    ),
                )
                conn.commit()

                # Load Predefined data from system
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # Scaling Factor=1.3
                    # Minimum Neighbor = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{id}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:
                            break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating Data Sets Completed Successfully!!!")

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To: {str(es)}", parent=self.root)

            conn.close()
            self.fetch_data()
            self.reset_data()


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop(
    )
