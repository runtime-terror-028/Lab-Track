import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage
import login_system
from tkinter import messagebox
import socket
import login_system


class login(login_system.Login_System):#<---------Login GUI

    def __init__(self):#<-----Client login
        super().__init__()
        self.window_client_login = tk.Tk()
        self.window_client_login.title("Client")
        self.window_client_login.geometry("744x457")
        self.window_client_login.configure(bg = "#FFFFFF")

        canvas = Canvas(
            self.window_client_login,
            bg = "#FFFFFF",
            height = 457,
            width = 744,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("assets/login_bg.png"))
        image_1 = canvas.create_image(
            189.0,
            228.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("assets/kiit.png"))
        image_2 = canvas.create_image(
            189.0,
            58.0,
            image=image_image_2
        )

        canvas.create_text(
            140.0,
            120.0,
            anchor="nw",
            text="Lab Track",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        canvas.create_text(
            67.0,
            167.0,
            anchor="nw",
            text="A computer lab monitoring tool",
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        button_image_1 = PhotoImage(
                file=("assets/login_as_admin_button.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login_kill_client,
            relief="flat"
        )
        button_1.place(
            x=75.0,
            y=398.0,
            width=213.0,
            height=35.0
        )

        canvas.create_text(
            495.0,
            48.0,
            anchor="nw",
            text="Student Login",
            fill="#000000",
            font=("Inter Medium", 20 * -1)
        )

        image_image_3 = PhotoImage(
            file=("assets/dp.png"))
        image_3 = canvas.create_image(
            563.0,
            129.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=("assets/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            561.5,
            298.0,
            image=entry_image_1
        )
        password_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        password_entry.place(
            x=443.0,
            y=274.0,
            width=237.0,
            height=46.0
        )

        entry_image_2 = PhotoImage(
            file=("assets/entry_2.png"))
        entry_bg_2 = canvas.create_image(
            561.5,
            218.0,
            image=entry_image_2
        )
        username_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        username_entry.place(
            x=443.0,
            y=194.0,
            width=237.0,
            height=46.0
        )

        button_image_2 = PhotoImage(
            file=("assets/login_button.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (request_server.make_data(username_entry.get(),password_entry.get(),"client"), self.kill_login_client()),
            relief="flat"
        )
        button_2.place(
        x=517.0,
        y=354.0,
        width=101.0,
        height=38.0
        )

        self.window_client_login.resizable(False, False)
        self.window_client_login.mainloop()
#-----------------------------------------------------------------------------------------
    def login_admin(self):#<-------------------admin login
        self.window_admin_login = tk.Tk()
        self.window_admin_login.title("Admin")
        self.window_admin_login.geometry("496x433")
        self.window_admin_login.configure(bg = "#FFFFFF")

        canvas = Canvas(
            self.window_admin_login,
            bg = "#FFFFFF",
            height = 433,
            width = 496,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("assets/kiit.png"))
        image_1 = canvas.create_image(
            248.0,
            52.0,
            image=image_image_1
        )

        canvas.create_text(
            172.0,
            113.0,
            anchor="nw",
            text="Admin Login",
            fill="#000000",
            font=("Inter Medium", 24 * -1)
        )

        entry_image_1 = PhotoImage(
            file=("assets/entry_1.png"))
        entry_bg_1 = canvas.create_image(
            248.5,
            191.0,
            image=entry_image_1
        )
        username_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        username_entry.place(
            x=144.0,
            y=172.0,
            width=209.0,
            height=36.0
        )

        entry_image_2 = PhotoImage(
            file=("assets/entry_2.png"))
        entry_bg_2 = canvas.create_image(
            248.5,
            252.0,
            image=entry_image_2
        )
        password_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        password_entry.place(
            x=144.0,
            y=233.0,
            width=209.0,
            height=36.0
        )

        button_image_1 = PhotoImage(
            file=("assets/admin_login_button.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.login(username_entry.get(), password_entry.get(), "admin"), self.kill_login_admin()),
            relief="flat"
        )
        button_1.place(
            x=207.0,
            y=314.0,
            width=82.0,
            height=38.0
        )
        self.window_admin_login.resizable(False, False)
        self.window_admin_login.mainloop()

        # username_label = tk.Label(window_admin_login, text="Username:")
        # username_label.grid(row=0, column=0, sticky="e", pady=5)
        # username_entry = tk.Entry(window_admin_login)
        # username_entry.grid(row=0, column=1, pady=5)

        # password_label = tk.Label(window_admin_login, text="Password:")
        # password_label.grid(row=1, column=0, sticky="e", pady=5)
        # password_entry = tk.Entry(window_admin_login, show="*")
        # password_entry.grid(row=1, column=1, pady=5)

        # login_button = tk.Button(window_admin_login, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        # login_button.grid(row=2, column=0, pady=10)

        # register_button = tk.Button(window_admin_login, text="Register", command=lambda: self.register_user(username_entry.get(), password_entry.get()))
        # register_button.grid(row=2, column=1, pady=10)

        # window_admin_login.mainloop()
        #---------------------------------------------------------
        # username_label = tk.Label(window_client_login, text="Username:")
        # username_label.grid(row=0, column=0, sticky="e", pady=5)
        # username_entry = tk.Entry(window_client_login)
        # username_entry.grid(row=0, column=1, pady=5)

        # password_label = tk.Label(window_client_login, text="Password:")
        # password_label.grid(row=1, column=0, sticky="e", pady=5)
        # password_entry = tk.Entry(window_client_login, show="*")
        # password_entry.grid(row=1, column=1, pady=5)

        # login_button = tk.Button(window_client_login, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        # login_button.grid(row=2, column=0, pady=10)

        # register_button = tk.Button(window_client_login, text="Register", command=lambda: self.register_user(username_entry.get(), password_entry.get()))
        # register_button.grid(row=2, column=1, pady=10)

        # window_client_login.mainloop()
        # window_client_login.resizable(False, False)
        # window_client_login.mainloop()

    def login_kill_client(self):#<---kill login window && open admin login window
        self.window_client_login.destroy()
        self.login_admin()
    def kill_login_client(self):#<---kill login window
        self.window_client_login.destroy()
    def kill_login_admin(self):#<---kill login window
        self.window_admin_login.destroy()

class request_server(login):
    def Auth(value):
        if (value == "True"):
            print("working")
            login_system.status.session_status = True
            login_system.status.login_type = "client"
        else:
            login_system.status.session_status = False

    def send_data_to_server(data):
        HOST = '192.168.0.102'  # Server IP address
        PORT = 55555            # Server port

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(data.encode())
            data1 = client_socket.recv(1024)
            if (data1):
                decode_data1 = data1.decode()
                request_server.Auth(decode_data1)

    def make_data(Id, Password, Type):
        fdata = Id+","+Password+","+Type
        request_server.send_data_to_server(fdata)
        login_system.status.user_id = Id
#-------------------------------------------------------
if __name__ == "__main__":
    messagebox.showinfo("This is not a entry point, please start from main.py")
    login_instance = login()#<------------------------------Start here
#-------------------------------------------------------