# libraires
import tkinter as tk

###############################################################################


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("SYNAPSE")
        self.setupWindowSize()
        self.update()
        self.width = self.winfo_width()
        self.height = self.winfo_height()

    def setupWindowSize(self):
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.baseWidth = 1280
        self.baseHeight = 720
        self.minsize(self.baseWidth, self.baseHeight)

        x = (screenWidth // 2) - (self.baseWidth // 2)
        y = (screenHeight // 2) - (self.baseHeight // 2)

        self.geometry(
            "{}x{}+{}+{}".format(self.baseWidth, self.baseHeight, x, y))
