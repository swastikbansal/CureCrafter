from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets_2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x700")
window.configure(bg="#202225")


canvas = Canvas(
    window,
    bg="#202225",
    height=700,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(45.0, 356.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(600.0, 50.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(45.0, 643.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(620.0, 240.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
button_5 = Button(
    image=image_image_5, bg="#202225", borderwidth=0, highlightthickness=0, command=None
)
button_5.place(x=890.0, y=250.0)

window.resizable(False, False)
window.mainloop()
