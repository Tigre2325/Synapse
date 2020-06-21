import tkinter as tk


class Page(tk.Canvas):
    pageList = []

    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(
            self.parent
        )
        tk.Canvas.__init__(
            self,
            self.frame,
            width=self.parent.width,
            height=self.parent.height,
            borderwidth=0
        )
        self.frame.pack(fill=tk.BOTH, expand=True)  # Make the window resizable
        self.pack(expand=True)
        self.hide()

        Page.pageList.append(self.frame)

        self.parent.update()

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)  # Make the window resizable
        self.parent.update()

    def hide(self):
        self.frame.pack_forget()
        self.parent.update()
