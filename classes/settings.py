# libraires
import tkinter as tk
from PIL import Image as ImageModule
from PIL import ImageTk
from numpy import interp

###############################################################################


class Settings(tk.OptionMenu):
    settingsList = []

    def __init__(self, parent, imagePath, text, optionList,
                 textColor, backgroundColor):
        self.parent = parent
        self.image = ImageModule.open(imagePath)
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.text = text
        self.optionList = optionList
        self.textColor = textColor
        self.backgroundColor = backgroundColor

        # Canvas which will contain the setting
        self.canvasSetting = tk.Canvas(
            self.parent,
            width=int(self.parent.winfo_reqwidth() * 60 / 100),
            height=int(self.parent.winfo_reqheight() * 10 / 100),
            borderwidth=10,
            relief=tk.RIDGE,
            background=self.backgroundColor,
            highlightthickness=0
        )

        # Scaling the setting background image
        self.xFactor = self.canvasSetting.winfo_reqwidth() / self.photoImage.width()
        self.yFactor = self.canvasSetting.winfo_reqheight() / self.photoImage.height()
        self.image = self.image.resize(
            (int(self.image.width * self.xFactor),
             int(self.image.height * self.yFactor)),
            ImageModule.ANTIALIAS
        )
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Image on the canvas
        self.canvasImage = self.canvasSetting.create_image(
            int(self.canvasSetting.winfo_reqwidth() * 50 / 100),
            int(self.canvasSetting.winfo_reqheight() * 50 / 100),
            image=self.photoImage
        )
        # Text
        self.canvasText = self.canvasSetting.create_text(
            int(self.canvasSetting.winfo_reqwidth() * 25 / 100),
            int(self.canvasSetting.winfo_reqheight() * 50 / 100),
            text=self.text,
            font=("Minecraft", 22),
            fill=self.textColor,
            justify=tk.CENTER
        )

        # Widget
        self.variable = tk.StringVar()
        self.variable.set(self.optionList[0])

        tk.OptionMenu.__init__(
            self,
            self.parent,
            self.variable,
            *self.optionList,
        )
        self.configure(
            width=12,
            height=2,
            background=self.textColor,
            foreground=self.backgroundColor,
            activebackground=self.backgroundColor,
            activeforeground=self.textColor,
            highlightthickness=0,
            font=("Minecraft", 16),
        )
        self.canvasWidget = self.canvasSetting.create_window(
            int(self.canvasSetting.winfo_reqwidth() * 75 / 100),
            int(self.canvasSetting.winfo_reqheight() * 50 / 100),
            window=self,
        )

        Settings.settingsList.append(self)

    def show(cls):
        for setting in Settings.settingsList:
            yPlace = interp(
                Settings.settingsList.index(setting),
                [0, len(Settings.settingsList)],
                [10, 100]
            )
            setting.parent.create_window(
                int(setting.parent.winfo_reqwidth() * 60 / 100),
                int(setting.parent.winfo_reqheight() * yPlace / 100),
                window=setting.canvasSetting
            )
    show = classmethod(show)
