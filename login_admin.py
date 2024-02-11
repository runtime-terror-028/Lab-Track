from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class Login_Admin_Window:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("496x433")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=433,
            width=496,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.output_path = Path(__file__).parent
        self.assets_path = self.output_path / Path("assets/admin_login")
        self.images = {}  # Store references to PhotoImage objects

    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

    def create_widgets(self):
        self.create_images()
        self.create_texts()
        self.create_entries()
        self.create_buttons()

    def create_images(self):
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.images["image_1"] = image_image_1  # Store reference
        self.image_1 = self.canvas.create_image(248.0, 52.0, image=image_image_1)

    def create_texts(self):
        self.canvas.create_text(172.0, 113.0, anchor="nw", text="Admin Login", fill="#000000",
                                font=("Inter Medium", 24 * -1))

    def create_entries(self):
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.images["entry_1"] = entry_image_1  # Store reference
        self.entry_bg_1 = self.canvas.create_image(248.5, 191.0, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=144.0, y=172.0, width=209.0, height=36.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.images["entry_2"] = entry_image_2  # Store reference
        self.entry_bg_2 = self.canvas.create_image(248.5, 252.0, image=entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=144.0, y=233.0, width=209.0, height=36.0)

    def create_buttons(self):
        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.images["button_1"] = button_image_1  # Store reference
        self.button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
                               command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(x=207.0, y=314.0, width=82.0, height=38.0)

    def run(self):
        self.create_widgets()
        self.window.resizable(False, False)
        self.window.mainloop()

