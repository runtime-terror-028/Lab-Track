import customtkinter as ctk
import socket

#Login GUI (frame)
class Login_window_frame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text='Lab track') 
        self.label.pack(pady=12,padx=10) 
        
        self.user_id = ctk.CTkEntry(self, placeholder_text="Roll Number") 
        self.user_id.pack(pady=12,padx=10) 

        self.user_pass= ctk.CTkEntry(self, placeholder_text="Password",show="*") 
        self.user_pass.pack(pady=12,padx=10) 

        self.button = ctk.CTkButton(self, text='Login',command=self.login) 
        self.button.pack(pady=12,padx=10)

        self.button = ctk.CTkButton(self, text='Registor',command=self.registor) 
        self.button.pack(pady=12,padx=10)
    
    def login(self):
        print("login button working")

    def registor(self):
        print("signup button working")


#login GUI (main)
class Login_window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Student Login")
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text= "Student login portal")
        self.label.pack(pady=20)

        self.login_window_frame = Login_window_frame(master=self)
        self.login_window_frame.pack(pady=20,padx=40,fill='both',expand=True) 

login_window = Login_window()
login_window.mainloop()