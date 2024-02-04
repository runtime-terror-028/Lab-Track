import server
import client
import tkinter as tk
from tkinter import messagebox

class login():
    def login_admin():
        window_admin = tk.Tk()
        window_admin.title("Admin")

        username_label = tk.Label(text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry()
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(text="Login")
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        window_admin.mainloop()
    
    def login_client():
        window_admin = tk.Tk()
        window_admin.title("Admin")
        
        username_label = tk.Label(text="Username:")
        username_label.grid(row=0, column=0, sticky="e", pady=5)
        username_entry = tk.Entry()
        username_entry.grid(row=0, column=1, pady=5)

        password_label = tk.Label(text="Password:")
        password_label.grid(row=1, column=0, sticky="e", pady=5)
        password_entry = tk.Entry(show="*")
        password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(text="Login")
        login_button.grid(row=2, column=0, columnspan=2, pady=10)

        window_admin.mainloop()
    
    def login_ask():
        window_ask = tk.Tk()
        window_ask.title("ask")

        label = tk.Label(text="Choose User Type:")
        label.pack(pady=10)

        option1_button = tk.Button(text="Student")
        option1_button.pack(pady=5)

        option2_button = tk.Button(text="Admin", command = login.login_admin())
        option2_button.pack(pady=5)

        window_ask.mainloop()

user_session= False
user_type = "Admin"

if user_session == True and user_type == "Admin":
    login.login_admin()
elif user_session == True and user_type == "Client":
    login.login_client()
elif user_session == False:
    login.login_ask()
else:
    print("session error")