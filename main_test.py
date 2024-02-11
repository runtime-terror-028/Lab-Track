from . import login
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
