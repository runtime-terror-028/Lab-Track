import tkinter as tk
from tkinter import messagebox
import openpyxl
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time
import socket
import login_system
import login_gui
import login_system

class Client_Main():#<---------main admin window
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Admin")
        self.window.geometry("744x457")
        self.window.configure(bg = "#FFFFFF")
        self.window.overrideredirect(True)  # Remove the title bar
        # Set window position to the right side of the screen
        screen_width = self.window.winfo_screenwidth()
        self.window.geometry(f"455x768+{screen_width - 455}+0")
        # Set window level to below all other windows
        self.window.attributes('-topmost', 0)
        # def lower_window(self):
        # self.window.lower()
        # self.window.bind('<FocusIn>', lower_window)

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 768,
            width = 455,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("assets/client_main_bg.png"))
        image_1 = canvas.create_image(
            341.0,
            384.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("assets/kiit.png"))
        image_2 = canvas.create_image(
            225.0,
            68.0,
            image=image_image_2
        )

        canvas.create_text(
            148.0,
            134.0,
            anchor="nw",
            text="Lab Track",
            fill="#1E1E1E",
            font=("Inter Bold", 32 * -1)
        )

        canvas.create_rectangle(
            36.0,
            215.0,
            429.0,
            742.0,
            fill="#8D8D8D",
            outline="")

        canvas.create_rectangle(
            58.0,
            473.0,
            407.0,
            721.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_rectangle(
            58.0,
            234.0,
            407.0,
            339.0,
            fill="#DEDADA",
            outline="")

        canvas.create_text(
            183.0,
            298.0,
            anchor="nw",
            text="Null3",#<---student name
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            183.0,
            273.0,
            anchor="nw",
            text=login_system.status.user_id,
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            61.0,
            298.0,
            anchor="nw",
            text="Student name:",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            78.0,
            274.0,
            anchor="nw",
            text="  Student ID:",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            71.0,
            248.0,
            anchor="nw",
            text="Computer ID:",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            183.0,
            248.0,
            anchor="nw",
            text=Client_Main.get_ip(),
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_rectangle(
            58.0,
            358.0,
            407.0,
            454.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            183.0,
            404.0,
            anchor="nw",
            text="Online",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            66.0,
            404.0,
            anchor="nw",
            text="Server Status:",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            183.0,
            369.0,
            anchor="nw",
            text="Null5",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        canvas.create_text(
            110.0,
            369.0,
            anchor="nw",
            text="Session:",
            fill="#000000",
            font=("Inter Medium", 16 * -1)
        )

        button_image_1 = PhotoImage(
            file=("assets/client_main_endsession.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.close_client_main,
            relief="flat"
        )
        button_1.place(
            x=243.0,
            y=650.0,
            width=146.0,
            height=42.0
        )

        canvas.create_text(
            78.0,
            530.0,
            anchor="nw",
            text="Remember to shutdown the\n computer properly :>",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )
        self.window.resizable(False, False)
        # Create a label for session time
        self.session_time_label = tk.Label(
            self.window,
            text="00:00:00",
            font=("Inter Medium", 16 * -1),
            fg="#000000"
        )
        self.session_time_label.place(x=183.0, y=369.0, anchor="nw")

        # Start the session timer
        self.session_start_time = time.time()

        self.update_session_time()
        self.window.mainloop()

    def create_canvas_elements(self):
        image_image_1 = PhotoImage(file=("assets/client_main_bg.png"))
        self.image_1 = self.canvas.create_image(341.0, 384.0, image=image_image_1)


    def update_session_time(self):
        elapsed_time = time.time() - self.session_start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
        self.session_time_label.config(text="Session Time: " + time_string)
        self.session_time_label.update()  # Force update of label
        self.window.after(1000, self.update_session_time)

    def get_ip():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address

    def close_client_main(self):
        self.window.destroy()