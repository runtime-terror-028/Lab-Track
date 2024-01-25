import customtkinter as ctk

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text='Lab track') 
        self.label.pack(pady=12,padx=10) 
        
        self.user_id = ctk.CTkEntry(self, placeholder_text="ID") 
        self.user_id.pack(pady=12,padx=10) 

        self.user_pass= ctk.CTkEntry(self, placeholder_text="Password",show="*") 
        self.user_pass.pack(pady=12,padx=10) 

        self.button = ctk.CTkButton(self, text='Login',command=self.login) 
        self.button.pack(pady=12,padx=10)
    
    def login(self):
        print("button pressed")



class Login_window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Admin Login")
        self.geometry("400x400")
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text= "Admin login portal")
        self.label.pack(pady=20)

        self.my_frame = MyFrame(master=self)
        self.my_frame.pack(pady=20,padx=40,fill='both',expand=True) 

login_app = Login_window()
login_app.mainloop()