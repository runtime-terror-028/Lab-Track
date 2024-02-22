import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import time
import socket
import sys
from io import StringIO

class Admin_Main():#<---------main admin window
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Admin")
        self.window.geometry("848x610")
        self.window.configure(bg = "#FFFFFF")

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 610,
            width = 848,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("assets/admin_bg.png"))
        image_1 = canvas.create_image(
            424.0,
            305.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("assets/kiit.png"))
        image_2 = canvas.create_image(
            424.0,
            44.0,
            image=image_image_2
        )

        canvas.create_text(
            366.0,
            92.0,
            anchor="nw",
            text="Lab Track",
            fill="#FFFFFF",
            font=("Inter Bold", 24 * -1)
        )

        entry_1 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=336.0,
            y=145.0,
            width=494.0,
            height=443.0
        )

        self.entry_2 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=21.0,
            y=266.0,
            width=286.0,
            height=322.0
        )

        canvas.create_rectangle(
            21.0,
            145.0,
            307.0,
            238.0,
            fill="#D9D9D9",
            outline="")

        canvas.create_text(
            34.0,
            155.0,
            anchor="nw",
            text="default port: 55555",
            fill="#000000",
            font=("Inter Bold", 13 * -1)
        )

        entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=134.0,
            y=185.0,
            width=154.0,
            height=31.0
        )

        button_image_1 = PhotoImage(
            file=("assets/change_port_button.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_port(),
            relief="flat"
        )
        button_1.place(
            x=40.0,
            y=185.0,
            width=77.0,
            height=33.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def change_port(self):
        # Redirect standard output
        sys.stdout = mystdout = StringIO()

        # Your port changing code goes here
        print("change port clicked")  # This will be redirected to mystdout

        # Get the output and display in entry_2
        output = mystdout.getvalue()
        self.entry_2.insert(tk.END, output)

# Instantiate the Admin_Main class
Admin_Main()
