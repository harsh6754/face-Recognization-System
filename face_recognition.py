

# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import cv2
# import mysql.connector
# import os
# import numpy as np


# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         # ==================Title=========================
#         title_lbl = tk.Label(self.root, text="Face Recognition", font=(
#             "times new roman ", 35, "bold"), bg="black", fg="white")
#         title_lbl.place(x=0, y=0, width=1550, height=52)

#         # ==================Image========================
#         img_top = Image.open("Images\Images23.jpg")
#         img_top = img_top.resize((650, 750), Image.ANTIALIAS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)

#         f_lbl = tk.Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=52, width=650, height=750)

#         # =================Image2=======================
#         img_bottom = Image.open("Images/Images26.jpg")
#         img_bottom = img_bottom.resize((950, 750), Image.ANTIALIAS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

#         f_lbl2 = tk.Label(self.root, image=self.photoimg_bottom)
#         f_lbl2.place(x=650, y=52, width=950, height=750)

#         # ===================Button==================
#         b1_1 = ttk.Button(f_lbl2, text="Face Detection", cursor="hand2",
#                           command=self.face_recog, style='my.TButton')
#         b1_1.place(x=370, y=660, width=200, height=40)

    

#     # =============Face Recognition Function ==========

#     def face_recog(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(
#                 gray_image, scaleFactor, minNeighbors)

#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
#                 id, predict = clf.predict(gray_image[y:y+h, x:x+w])
#                 confidence = int((100*(1-predict/300)))

#                 conn = mysql.connector.connect(
#                     host="localhost", user="root", password="H@rsh2810", database="face_recognition")
#                 my_cursor = conn.cursor()

#                 my_cursor.execute(
#                     "select Name from student where Student_id="+str(id))
#                 n = my_cursor.fetchone()
#                 n = n[0] if n else "Unknown"

#                 my_cursor.execute(
#                     "select Roll from student where Student_id="+str(id))
#                 r = my_cursor.fetchone()
#                 r = r[0] if r else "Unknown"

#                 my_cursor.execute(
#                     "select Dep from student where Student_id="+str(id))
#                 d = my_cursor.fetchone()
#                 d = d[0] if d else "Unknown"

                

#                 if confidence > 77:
#                     cv2.putText(
#                         img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
#                     cv2.putText(
#                         img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
#                     cv2.putText(
#                         img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
#                 else:
#                     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Face", (x, y-55),
#                                 cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

#         def recognize(img, clf, faceCascade):
#             draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
#             return img

#         faceCascade = cv2.CascadeClassifier(
#             "haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")

#         video_cap = cv2.VideoCapture(0)

#         while True:
#             ret, img = video_cap.read()
#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Welcome To Face Recognition", img)

#             if cv2.waitKey(1) == 13:  # Press Enter to exit the loop
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.config(bg="white")
#     obj = Face_Recognition(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #================Title=========================#
        title_lbl = Label(self.root, text="Face Recognition ", font=(
            "times new roman ", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=52)

        #================Image========================#
        img_top = Image.open(
            "Images\Images23.jpg")
        img_top = img_top.resize((650, 750), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=52, width=650, height=750)

        #===============Image2=======================#
        img_bottom = Image.open("Images/Images26.jpg")
        img_bottom = img_bottom.resize((950, 750), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=52, width=950, height=750)

        #==================Botton==================#
        b1_1 = Button(f_lbl, text="Face Detection",  cursor="hand2", command=self.face_recog, font=(
            "times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=370, y=660, width=200, height=40)
        
    #=============Attendance ========================#
    def mark_attendance(self,r,n,d):
        with open("harsh.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and ( d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")

    #=============Face Recognition Function ==========#

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", user="******", password="******", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 3)
                    self.mark_attendance(r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown Face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10,
                          (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1)==13:     #Press "Enter " to exit 
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop(
    )
