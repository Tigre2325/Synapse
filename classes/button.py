# libraires
import tkinter as tk
from PIL import Image as ImageModule
from PIL import ImageTk

###############################################################################


class Button(tk.Button):
    def __init__(self, parent, imagePath, text, x, y,
                 textSize, textColor, backgroundColor):
        self.parent = parent
        self.image = ImageModule.open(imagePath)
        self.photoImage = ImageTk.PhotoImage(file=imagePath)
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        self.x = x
        self.y = y
        self.backgroundColor = backgroundColor
        self.borderWidth = 5
        tk.Button.__init__(self, self.parent, compound=tk.CENTER,
                           text=self.text, image=self.photoImage,
                           font=("Minecraft", self.textSize),
                           foreground=self.textColor, activeforeground=self.textColor,
                           background=self.backgroundColor, activebackground=self.backgroundColor,
                           borderwidth=self.borderWidth)
        self.canvasButton = self.parent.create_window(
            self.x, self.y, window=self, state=tk.HIDDEN)

    def show(self):
        self.parent.itemconfigure(self.canvasButton, state=tk.NORMAL)

    def hide(self):
        self.parent.itemconfigure(self.canvasButton, state=tk.HIDDEN)

    def scale(self, xFactor, yFactor=-1):
        if yFactor == -1:
            yFactor = xFactor

        newWidth = int(self.image.width * xFactor)
        newHeight = int(self.image.height * yFactor)
        self.image = self.image.resize(
            (newWidth, newHeight), ImageModule.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.configure(image=self.photoImage)
