from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Login_Client_Window():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("744x457")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=457,
            width=744,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("assets/client_login")
        self.images = {}  # Store references to PhotoImage objects

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_widgets(self):
        self.create_images()
        self.create_texts()
        self.create_entries()
        self.create_buttons()

    def create_images(self):
        self.images["image_1"] = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(189.0, 228.0, image=self.images["image_1"])

        self.images["image_2"] = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(189.0, 58.0, image=self.images["image_2"])

        self.images["image_3"] = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(563.0, 129.0, image=self.images["image_3"])

    def create_texts(self):
        self.canvas.create_text(140.0, 120.0, anchor="nw", text="Lab Track", fill="#000000", font=("Inter Medium", 20 * -1))
        self.canvas.create_text(67.0, 167.0, anchor="nw", text="A computer lab monitoring tool", fill="#000000",
                                font=("Inter", 16 * -1))
        self.canvas.create_text(495.0, 48.0, anchor="nw", text="Student Login", fill="#000000",
                                font=("Inter Medium", 20 * -1))

    def create_entries(self):
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.images["entry_1"] = entry_image_1
        self.entry_bg_1 = self.canvas.create_image(561.5, 298.0, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=443.0, y=274.0, width=237.0, height=46.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.images["entry_2"] = entry_image_2
        self.entry_bg_2 = self.canvas.create_image(561.5, 218.0, image=entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=443.0, y=194.0, width=237.0, height=46.0)

    def create_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.images["button_1"] = button_image_1
        self.button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                               command=print(), relief="flat")#<---------------
        self.button_1.place(x=75.0, y=398.0, width=213.0, height=35.0)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.images["button_2"] = button_image_2
        self.button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_2 clicked"), relief="flat")
        self.button_2.place(x=517.0, y=354.0, width=101.0, height=38.0)

    def run(self):
        self.create_widgets()
        self.window.resizable(False, False)
        self.window.mainloop()

    def open_login_admin(self):
        self.master.destroy()

abc = Login_Client_Window()
abc.run()