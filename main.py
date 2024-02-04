import tkinter as tk
from tkinter import messagebox
import openpyxl

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

        username_label = tk.Label(window_admin_login, text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry(window_admin_login)
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(window_admin_login, text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(window_admin_login, show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(window_admin_login, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.grid(row=2, column=0, pady=10)

        register_button = tk.Button(window_admin_login, text="Register", command=lambda: self.register_user(username_entry.get(), password_entry.get()))
        register_button.grid(row=2, column=1, pady=10)

        window_admin_login.mainloop()

    def login_client(self):#<--------client login window
        window_client_login = tk.Tk()
        window_client_login.title("Client")
        
        username_label = tk.Label(window_client_login, text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry(window_client_login)
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(window_client_login, text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(window_client_login, show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(window_client_login, text="Login", command=lambda: self.login(username_entry.get(), password_entry.get()))
        login_button.grid(row=2, column=0, pady=10)

        register_button = tk.Button(window_client_login, text="Register", command=lambda: self.register_user(username_entry.get(), password_entry.get()))
        register_button.grid(row=2, column=1, pady=10)

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
