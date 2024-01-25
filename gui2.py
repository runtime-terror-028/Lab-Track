import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("455x239")

        #------------
        self.label = customtkinter.CTkLabel(self, text="Enter Roll No", fg_color="transparent")
        self.label.grid(row=0, column=0, padx=49, pady=(59, 0)) 
        self.label = customtkinter.CTkLabel(self, text="Enter Password", fg_color="transparent")
        self.label.grid(row=1, column=0, padx=49, pady=(35, 0)) 

        self.entry = customtkinter.CTkEntry(self, placeholder_text="roll no")
        self.entry.grid(row=0, column=1, padx=10, pady=(59, 0))
        self.entry = customtkinter.CTkEntry(self, placeholder_text="password")
        self.entry.grid(row=1, column=1, padx=10, pady=(35, 0))
        #------------


app = App()
app.mainloop()