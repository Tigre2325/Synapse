import tkinter as tk
from PIL import Image as ImageModule
from PIL import ImageTk


class Image():
    def __init__(self, parent, imagePath, x=0, y=0):
        self.parent = parent
        self.image = ImageModule.open(imagePath)
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.x = x
        self.y = y
        self.canvasImage = self.parent.create_image(self.x, self.y,
                                                    image=self.photoImage, state=tk.HIDDEN)

    def show(self):
        self.parent.itemconfigure(self.canvasImage, state=tk.NORMAL)

    def hide(self):
        self.parent.itemconfigure(self.canvasImage, state=tk.HIDDEN)

    def scale(self, factor):
        self.image = self.image.resize(
            (self.image.width * factor, self.image.height * factor), ImageModule.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(self.image)
