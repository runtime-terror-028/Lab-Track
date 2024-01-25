import socket
import customtkinter as ctk
import tkinter.messagebox as tkmb

#GUI theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
#GUI_Login--------------
login_app = ctk.CTk()
login_app.geometry("400x400")
login_app.title("Student Login")

def login():
    userName = "admin" #<--------make a data base for this
    password = "admin"

    if user_id_entry.get() == userName and user_pass_entry.get() == password:
        tkmb.showinfo(title="Login successfull", message="You have logged in Successfully")
    else:
        tkmb.showerror(title="Login Failed",message="Invalid Username and password")

#login GUI-----------------
label = ctk.CTkLabel(login_app,text="Student login portal") 
label.pack(pady=20) 

frame = ctk.CTkFrame(master=login_app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='Lab track') 
label.pack(pady=12,padx=10) 

user_id_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_id_entry.pack(pady=12,padx=10) 

user_pass_entry= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass_entry.pack(pady=12,padx=10) 


button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 


login_app.mainloop()
