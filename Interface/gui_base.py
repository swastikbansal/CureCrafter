from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
from tkinter import *
from gui_1 import GUI as GUI1
from gui_2 import GUI as GUI2

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets_base")


class GUI:
    def __init__(self, window=None):

        if window is None:
            self.window = Tk()
        else:
            self.window = window

        self.setup_window()
        self.create_canvas()
        self.load_images()
        self.window.mainloop()

    def setup_window(self):
        self.window.geometry("1200x700")
        self.window.configure(bg="#202225")
        self.window.resizable(False, False)

    def create_canvas(self):
        self.canvas = Canvas(
            self.window,
            bg="#202225",
            height=700,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

    def open_new_interface_1(self):
        self.window.destroy()
        new_window = Tk()
        GUI1(new_window)
        new_window.mainloop()

    def open_new_interface_2(self):
        self.window.destroy()
        new_window = Tk()
        GUI2(new_window)
        new_window.mainloop()

    def load_images(self):
        self.image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(592.0, 350.0, image=self.image_1)

        self.image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(601.0, 64.0, image=self.image_2)

        self.image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.button_3 = Button(
            self.window,
            image=self.image_3,
            bg="#2f3235",
            borderwidth=0,
            highlightthickness=0,
            command=self.open_new_interface_1,
        )
        self.button_3.place(x=-46, y=290.0)

        self.image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.button_4 = Button(
            self.window,
            image=self.image_4,
            bg="#2f3235",
            borderwidth=0,
            highlightthickness=0,
            command=self.open_new_interface_2,
        )
        self.button_4.place(x=20, y=520.0)

        self.image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        self.canvas.create_image(90.0, 215.0, image=self.image_5)

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


if __name__ == "__main__":
    GUI()
