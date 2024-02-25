import tkinter as tk
from tkinter import Canvas, Text, Button, PhotoImage
import socket
import threading
import sys
import openpyxl
import login_system
import client_main_gui
from login_system import status

class Login_System():
    def __init__(self, excel_file='credentials.xlsx'):
        self.excel_file = excel_file
        self.workbook = openpyxl.load_workbook(self.excel_file)
        self.sheet = self.workbook.active

    def authenticate(self, username, password, type):
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            stored_username, stored_password, stored_type = row
            if username == stored_username and str(password) == str(stored_password) and type == stored_type:
                return True, "True"  # Return a tuple indicating success and a message
        return False, "False"

    def login(self, entered_username, entered_password, entered_type):
        success, message = self.authenticate(entered_username, entered_password, entered_type)
        if success:
            status.login_type = "client"
            status.session_status = True
            status.user_id = entered_username
            print("auth")
        return success, message  # Return authentication result and message


class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, s):
        self.text_widget.insert(tk.END, s)
        self.text_widget.see(tk.END)  # Scroll to the end

    def flush(self):
        pass  # No need to flush anything in this case

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

    def create_socket(self, port=55555):
        threading.Thread(target=self._create_socket, args=(port,)).start()

    def _create_socket(self, port):
        try:
            sys.stdout = StdoutRedirector(self.entry_2)
            # Create a socket object
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket successfully created")

            # Bind to the port
            server_socket.bind(('192.168.0.102', int(port)))
            print(f"Socket bound to port {port}")

            # Listen for incoming connections
            server_socket.listen(5)
            print("Socket is listening")

            while True:
                # Accept incoming connection
                client_socket, client_address = server_socket.accept()
                print("Connection accepted from", client_address)

                # Receive messages
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    decoded_data = data.decode()
                    print("Received data:", decoded_data)  # Print received data
                    parts = decoded_data.split(',')  # Assuming ',' is the delimiter
                    if len(parts) >= 3:
                        IDpart = parts[0]
                        PASSWORDpart = parts[1]
                        TYPEpart = parts[2]
                        # Call the login method of Login_System class
                        login_system = Login_System()
                        success, message = login_system.login(IDpart, PASSWORDpart, TYPEpart)
                        if success:
                            client_socket.sendall(message.encode())  # Send the message back to the client
                        else:
                            client_socket.sendall(b"Login failed")  # Send a failure message back to the client
                    else:
                        print("Received data does not contain three parts")
        except Exception as e:
            print("Error:", e)
        finally:
            server_socket.close()