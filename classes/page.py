import tkinter as tk
from PIL import Image as ImageModule
from PIL import ImageTk


class Page(tk.Canvas):
    pageList = []

    def __init__(self, parent, background):
        self.parent = parent

        self.frame = tk.Frame(
            self.parent
        )
        tk.Canvas.__init__(
            self,
            self.frame,
            width=self.parent.width,
            height=self.parent.height,
            borderwidth=0,
            highlightthickness=0
        )

        if "#" in background:
            self.configure(background=background)
        else:
            self.image = ImageModule.open(background)
            self.photoImage = ImageTk.PhotoImage(self.image)

            self.create_image(
                int(self.parent.winfo_width() * 50 / 100),
                int(self.parent.winfo_height() * 50 / 100),
                image=self.photoImage,
            )

        self.frame.pack(fill=tk.BOTH, expand=True)  # Make the window resizable
        self.pack(expand=True)
        self.hide()

        Page.pageList.append(self)

        self.parent.update()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)  # Make the window resizable
        self.parent.update()

    def hide(self):
        self.frame.pack_forget()
        self.parent.update()
