from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    NORMAL,
    END,
    Button,
    PhotoImage,
    Text,
    Scrollbar,
    filedialog,
)
from PIL import Image, ImageTk
from _tkinter import *
from prediction_script import XRayPrediction

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets_2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class GUI:
    def __init__(self, window):
        self.window = window
        self.setup_ui()

    def setup_ui(self):
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
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(45.0, 356.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(600.0, 50.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(45.0, 643.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(620.0, 240.0, image=self.image_image_4)

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

        self.text_widget.place(height=580, width=1080, rely=0.08, x=110, y=60)
        self.text_widget.configure(
            cursor="arrow", state=NORMAL
        )  # Set state to NORMAL to insert image

        # Insert image into text widget
        self.text_widget.image_create("end", image=self.image_image_4)
        self.text_widget.image = []

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side="right", fill="y")
        scrollbar.config(command=self.text_widget.yview)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        def open_file_dialog():
            filepath = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.png")]
            )
            print(filepath)
            label = XRayPrediction.predict(filepath)
            print(label)

            if filepath:
                # Check if a file was selected
                image = Image.open(filepath)
                photo = ImageTk.PhotoImage(image)
                self.text_widget.image_create("end", image=photo)
                self.text_widget.insert("end", "\n")
                self.text_widget.image.append(photo)

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        self.button_5 = Button(
            image=self.image_image_5,
            bg="#202225",
            borderwidth=0,
            highlightthickness=0,
            command=open_file_dialog,
        )
        self.button_5.place(x=890.0, y=250.0)

        self.window.resizable(False, False)


if __name__ == "__main__":
    window = Tk()
    gui = GUI(window)
    window.mainloop()
