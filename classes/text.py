# libraires
import tkinter as tk

###############################################################################


class Text():
    def __init__(self, parent, text, x, y,
                 textSize=16, textColor="#000000"):
        self.parent = parent
        self.text = text
        self.textSize = textSize
        self.textColor = textColor
        self.x = x
        self.y = y
        self.canvasText = self.parent.create_text(
            self.x,
            self.y,
            text=self.text,
            font=("Minecraft", self.textSize),
            fill=self.textColor,
            justify=tk.CENTER,
            state=tk.HIDDEN
        )

    def set(self, **kwargs):
        self.parent.itemconfigure(self.canvasText, **kwargs)

    def show(self):
        self.parent.itemconfigure(self.canvasText, state=tk.NORMAL)

    def hide(self):
        self.parent.itemconfigure(self.canvasText, state=tk.HIDDEN)
