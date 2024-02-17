from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    Entry,
    Button,
    PhotoImage,
    Text,
    DISABLED,
    END,
    Scrollbar,
)
from tkinter import *
import tkinter as tk


class GUI:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1200x700")
        self.window.configure(bg="#202225")
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
        self.create_images_and_buttons()
        self.window.resizable(False, False)
        self.window.mainloop()

    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return GUI.ASSETS_PATH / Path(path)

    def create_image(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        self.canvas.create_image(x, y, image=image)
        return image

    def create_button(self, image_path, x, y):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            image=image,
            bd=0,
            highlightthickness=0,
            bg="#202225",
            command=lambda: self._on_enter_pressed(
                None
            ),  # Replace "your_command_function" with the actual command function
        )
        button.place(x=x, y=y)
        return image, button

    def create_entry(self, image_path, x, y, width, height):
        image = PhotoImage(file=self.relative_to_assets(image_path))
        entry_bg = self.canvas.create_image(x + width / 2, y + height / 2, image=image)
        entry = Entry(
            bd=0, bg="#2F3235", fg="#FFFFFF", highlightthickness=0, font=("Magra", 20)
        )
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus()
        entry.bind("<Return>", self._on_enter_pressed)
        return image, entry

    def create_images_and_buttons(self):

        self.image_1 = self.create_image(
            "image_1.png", 604.4124145507812, 56.13761901855469
        )

        self.text_widget = Text(
            self.window,
            width=0,
            height=0,
            bg="#202225",
            fg="#FFFFFF",
            font=("Helvetica", 16),
            bd=0,
            highlightthickness=0,
        )
        self.text_widget.place(height=450, width=1070, rely=0.08, x=140, y=60)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        self.image_2, self.button_2 = self.create_button("image_4.png", 1010.0, 595.0)
        self.image_3, self.entry_1 = self.create_entry(
            "entry_1.png", 210.0, 570.0, 645.0, 100.0
        )
        self.image_4, self.button_3 = self.create_button("image_3.png", 1075.0, 570.0)

        self.image_5 = self.create_image("image_2.png", 58.0, 350.0)
        self.image_6, self.button_4 = self.create_button("image_5.png", 930.0, 590.0)
        self.image_7 = self.create_image("image_6.png", 55.0, 49.0)
        self.image_8 = self.create_image("image_7.png", 55.0, 152.0)

        self.image_9 = self.create_image("image_8.png", 55.0, 620.0)

        self.image_10 = self.create_image("image_9.png", 650.0, 300.0)

        self.text_widget.image_create(tk.END, image=self.image_10, padx=25, pady=25)

    def _on_enter_pressed(self, event):
        msg = self.entry_1.get()
        self._insert_message(msg, "You ")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.entry_1.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # msg2 = f"{bot_name}: {get_response(msg)}\n\n"

        self.text_widget.configure(state=NORMAL)

        # self.text_widget.insert(END, msg2)

        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    gui = GUI()
