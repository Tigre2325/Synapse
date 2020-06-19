import tkinter as tk


class Page(tk.Canvas):
    pageNumber = 0
    pageList = []

    def __init__(self, parent):
        self.parent = parent
        tk.Canvas.__init__(self, self.parent, width=self.parent.width,
                           height=self.parent.height, borderwidth=0)
        self.pack()  # fill=tk.BOTH, expand=True)  # Make the window resizable
        self.hide(self.parent)

        Page.pageNumber += 1
        Page.pageList.append(self)

        self.parent.update()

    def show(self, parent):
        self.pack()  # fill=tk.BOTH, expand=True)
        self.parent = parent
        self.parent.update()

    def hide(self, parent):
        self.pack_forget()
        self.parent = parent
        self.parent.update()
