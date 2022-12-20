from pathlib import Path

from tkinter import Frame, Canvas,Label, Entry, Text, Button, PhotoImage, messagebox
from controller import *
from PIL import Image, ImageTk
import cv2
import imutils

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def FaceLogin():
    LoginByFace()


class LoginByFace(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        #Background
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=506,
            width=543,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)
        

        
        self.label = Label(self, width=450, height=350, bg="#FFFFFF")
        self.label.frame_num = 0
        self.label.grid(row=3, column=0)
        global video 
        video = None
        #LOGIN BUTTON
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.video_stream,
            relief="flat",
        )
        button_1.place(x=10.0, y=437.0, width=190.0, height=48.0)
        
        self.canvas.create_rectangle(
            56.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_rectangle(
            418.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        )
        
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.end_capture,
            relief="flat",
        )
        button_2.place(x=250.0, y=437.0, width=190.0, height=48.0)
        


    def video_stream(self):
        global video
        video = cv2.VideoCapture(0)
        self.start_capture()
    
    def start_capture(self):
        global video
        ret, frame = video.read()
        if ret:
            frame = imutils.resize(frame, width = 640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            image = ImageTk.PhotoImage(image=img)
            self.label.configure(image=image)
            self.label.image = image
            self.label.imgtk = image
            self.label.after(10,self.start_capture)
        else:
            video.release()
            

    
    def end_capture(self):
        global video
        imagetk = self.label.imgtk
        imgpil = ImageTk.getimage( imagetk )
        print(imgpil)
        self.label.place_forget()
        video.release()


