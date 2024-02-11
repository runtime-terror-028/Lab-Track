import tkinter as tk
from tkinter import messagebox
import openpyxl
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

#note- remove registor option from client after asking suggestion from teacher
class login_system:#<---------Login database using ms exel
    def __init__(self, excel_file='credentials.xlsx'):
        self.excel_file = excel_file

        # Create the Excel file if it doesn't exist
        try:
            self.workbook = openpyxl.load_workbook(self.excel_file)
            self.sheet = self.workbook.active
        except FileNotFoundError:
            self.create_excel_file()

    def create_excel_file(self):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet['A1'] = 'Username'
        self.sheet['B1'] = 'Password'
        self.workbook.save(self.excel_file)

    def authenticate(self, username, password):
        for row in self.sheet.iter_rows(min_row=2, values_only=True):
            stored_username, stored_password = row
            if username == stored_username and password == stored_password:
                return True
        return False

    def register(self, username, password):
        self.sheet.append([username, password])
        self.workbook.save(self.excel_file)
        messagebox.showinfo("Registration Successful", "Account registered successfully!")

    def login(self, entered_username, entered_password):
        if self.authenticate(entered_username, entered_password):
            messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def register_user(self, entered_username, entered_password):
        if entered_username and entered_password:
            self.register(entered_username, entered_password)
        else:
            messagebox.showerror("Registration Failed", "Username and password are required.")
#------------------------------------------------------------------------------
class login(login_system):#<---------Login GUI
    def __init__(self):
        super().__init__()

        self.window_ask = tk.Tk()
        self.window_ask.title("ask")

        label = tk.Label(self.window_ask, text="Choose User Type:")
        label.pack(pady=10)

        option1_button = tk.Button(self.window_ask, text="Student", command=self.login_kill_client)
        option1_button.pack(pady=5)

        option2_button = tk.Button(self.window_ask, text="Admin", command=self.login_kill_admin)
        option2_button.pack(pady=5)

        self.window_ask.mainloop()

    def login_admin(self):#<------------admin login window
        window_admin_login = tk.Tk()
        window_admin_login.title("Admin")
        window_admin_login.geometry("496x433")
        window_admin_login.configure(bg = "#FFFFFF")

        canvas = Canvas(
            window_admin_login,
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
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
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
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
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
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=207.0,
            y=314.0,
            width=82.0,
            height=38.0
        )
        window_admin_login.resizable(False, False)
        window_admin_login.mainloop()

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

    def login_client(self):#<--------client login window
        window_client_login = tk.Tk()
        window_client_login.title("Client")
        window_client_login.geometry("744x457")
        window_client_login.configure(bg = "#FFFFFF")

        canvas = Canvas(
            window_client_login,
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
            command=lambda: print("button_1 clicked"),
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
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
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
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
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
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
        x=517.0,
        y=354.0,
        width=101.0,
        height=38.0
        )
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
        window_client_login.resizable(False, False)
        window_client_login.mainloop()

    def login_kill_admin(self):#<---kill ask window and show admin login
        self.window_ask.destroy()
        self.login_admin()

    def login_kill_client(self):#<---kill ask window and show client login
        self.window_ask.destroy()
        self.login_client()
#-------------------------------------------------------
class main_window():#<-------------Main GUI window
    def client_window():
        window_client = tk.Tk()
    def server_window():
        window_server = tk.Tk()
#-------------------------------------------------------
login_instance = login()
