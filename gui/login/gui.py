from pathlib import Path

from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, Frame
from controller import *
from ..main_window.main import mainWindow
from gui.login.FaceLogin.main import LoginByFace
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def loginWindow():
    Login()


class Login(Toplevel):

    global user
    # Login check function
    def loginFunc(self):
        global user
        if checkUser(self.username.get().lower(), self.password.get()):
            user = self.username.get().lower()
            self.destroy()
            mainWindow()
            return
        else:
            messagebox.showerror(
                title="Invalid Credentials",
                message="The username and self.password don't match",
            )
            
    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed - where to display each frame
        self.windows[name].place(x=529.0, y=0, width=1012.0, height=506.0)
        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Login - UITrainer")

        self.geometry("1012x506")
        self.configure(bg="#5E95FF")
        
        #FACE LONGIN INDICATOR
        self.sidebar_indicator = Frame(self, background="#FFFFFF")
        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)



        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )
        
        #curent name forr pressbuton functions
        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="FaceLogin",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        #LOGIN SESSSION
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(736.0, 331.0, image=entry_image_1)
        entry_1 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_1.place(x=568.0, y=294.0, width=336.0, height=0)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(736.0, 229.0, image=entry_image_2)
        entry_2 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_2.place(x=568.0, y=192.0, width=336.0, height=0)

        self.canvas.create_text(
            573.0,
            306.0,
            anchor="nw",
            text="Password",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.canvas.create_text(
            573.0,
            204.0,
            anchor="nw",
            text="Username",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.canvas.create_text(
            553.0,
            38.0,
            anchor="nw",
            text="Enter your login details",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )
        
        self.canvas.create_text(
            553.0,
            77.0,
            anchor="nw",
            text="Enter the credentials that the admin gave",
            fill="#CCCCCC",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            553.0,
            98.0,
            anchor="nw",
            text="you while signing up for the program",
            fill="#CCCCCC",
            font=("Montserrat Bold", 16 * -1),
        )
        
        entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(736.0, 241.0, image=entry_image_3)
        self.username = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
        )
        self.username.place(x=573.0, y=229.0, width=326.0, height=22.0)

        entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(736.0, 342.0, image=entry_image_4)
        self.password = Entry(
            self.canvas,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 16 * -1),
            foreground="#777777",
            show="???",
        )
        self.password.place(x=573.0, y=330.0, width=326.0, height=22.0)
        
        self.canvas.create_text(
            791.0,
            384.0,
            anchor="nw",
            text="Forget password?",
            fill="#5E95FF",
            font=("Montserrat SemiBold", 13 * -1)
        )

        #STUDET ID LOGIN MODULE
        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginFunc,
            relief="flat",
        )
        button_1.place(x=631.0,y=423.0, width=190.0, height=48.0)
        
                
        #FACE LOGIN MODULE
        face_login = PhotoImage(file=relative_to_assets("button_2.png"))
        self.facelogin_btn = Button(
            self.canvas,
            image=face_login,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.facelogin_btn, "face"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.facelogin_btn.place( x=553.0,y=137.0, width=130.625,height=33.0)
        self.windows = {
            "face": LoginByFace(self),
        }
        
        #Logo and animation Image
        image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(469.0, 289.0, image=image_image_1)
        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(38.0,41.0,image=image_image_2)
        
        
        #Description
        self.canvas.create_text(
            85.0,
            77.0,
            anchor="nw",
            text="UIT TRAINER",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1),
        )
        
        self.canvas.create_text(
            90.0,
            150.0,
            anchor="nw",
            text="The application is designed",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            179.0,
            anchor="nw",
            text="to support and encourage",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            208.0,
            anchor="nw",
            text="UIT students to do more exercises",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            237.0,
            anchor="nw",
            text="and to join in more sporty activities",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            266.0,
            anchor="nw",
            text="using a well-engineered solution.",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            295.0,
            anchor="nw",
            text="Login to have a look for",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            90.0,
            324.0,
            anchor="nw",
            text="yourself and enjoy it!",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )   
        
        
        self.canvas.create_text(
            90.0,
            431.0,
            anchor="nw",
            text="?? UIT & LCT, 2022",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1),
        )     

        # Bind enter to form submit
        self.username.bind("<Return>", lambda x: self.loginFunc())
        self.password.bind("<Return>", lambda x: self.loginFunc())

        self.resizable(False, False)
        self.mainloop()
