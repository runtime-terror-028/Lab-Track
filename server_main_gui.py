import tkinter as tk
from tkinter import Canvas, Text, Button, PhotoImage
import socket
import sys
from io import StringIO

class Admin_Main():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Admin")
        self.window.geometry("848x610")
        self.window.configure(bg="#FFFFFF")

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=610,
            width=848,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=("assets/admin_bg.png"))
        image_1 = canvas.create_image(
            424.0,
            305.0,
            image=image_image_1
        )
        image_image_2 = PhotoImage(file=("assets/kiit.png"))
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
            text="choose any port between 49152-65535",
            fill="#000000",
            font=("Inter Bold", 13 * -1)
        )
        entry_3 = tk.Entry(
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
        button_image_1 = PhotoImage(file=("assets/change_port_button.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.create_socket(entry_3.get()),
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

    # def change_port(self):
    #     # Redirect standard output
    #     sys.stdout = mystdout = StringIO()

    #     # Your port changing code goes here
    #     print("change port clicked")  # This will be redirected to mystdout

    #     # Get the output and display in entry_2
    #     output = mystdout.getvalue()
    #     self.entry_2.insert(tk.END, output)

    def create_socket(self, port=55555):
        try:
            port = int(port)
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.entry_2.insert(tk.END, "Socket successfully created\n")

            # Bind to the port
            s.bind(('localhost', port))
            self.entry_2.insert(tk.END, f"Socket bound to port {port}\n")

            # Listen for incoming connections
            s.listen(5)
            self.entry_2.insert(tk.END, "Socket is listening\n")

            return s

        except ValueError:
            self.entry_2.insert(tk.END, "Invalid port value. Please enter a valid integer port.\n")
        except socket.error as err:
            self.entry_2.insert(tk.END, f"Socket creation failed with error: {err}\n")

abc = Admin_Main()
