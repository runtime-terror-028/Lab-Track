from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/client_main")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("455x768")
window.configure(bg = "#FFFFFF")
window.overrideredirect(True)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 455,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    341.0,
    384.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    225.0,
    68.0,
    image=image_image_2
)

canvas.create_text(
    148.0,
    134.0,
    anchor="nw",
    text="Lab Track",
    fill="#1E1E1E",
    font=("Inter Bold", 32 * -1)
)

canvas.create_rectangle(
    36.0,
    215.0,
    429.0,
    742.0,
    fill="#8D8D8D",
    outline="")

canvas.create_rectangle(
    53.0,
    232.0,
    402.0,
    337.0,
    fill="#DEDADA",
    outline="")

canvas.create_text(
    183.0,
    298.0,
    anchor="nw",
    text="Null",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    183.0,
    273.0,
    anchor="nw",
    text="Null",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    57.0,
    298.0,
    anchor="nw",
    text="Student name:",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    72.0,
    273.0,
    anchor="nw",
    text="  Student ID:",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    65.0,
    248.0,
    anchor="nw",
    text="Computer ID:",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    183.0,
    248.0,
    anchor="nw",
    text="Null",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_rectangle(
    53.0,
    356.0,
    402.0,
    452.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    183.0,
    404.0,
    anchor="nw",
    text="Null",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    57.0,
    404.0,
    anchor="nw",
    text="Server Status:",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    183.0,
    369.0,
    anchor="nw",
    text="Null",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)

canvas.create_text(
    102.0,
    369.0,
    anchor="nw",
    text="Session:",
    fill="#000000",
    font=("Inter Medium", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
