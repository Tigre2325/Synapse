# libraires
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image as ImageModule
from PIL import ImageTk
from numpy import interp

###############################################################################


class Player():
    playerList = []
    playerName = []

    def __init__(self, parent, imagePath,
                 textColor, backgroundColor):
        self.parent = parent
        self.image = ImageModule.open(imagePath)
        self.photoImage = ImageTk.PhotoImage(self.image)
        self.textColor = textColor
        self.textColor = textColor
        self.backgroundColor = backgroundColor

        # Canvas which will contain the player settings
        self.canvasPlayer = tk.Canvas(
            self.parent,
            width=int(self.parent.winfo_reqwidth() * 22 / 100),
            height=int(self.parent.winfo_reqheight() * 40 / 100),
            borderwidth=10,
            relief=tk.RIDGE,
            background=self.backgroundColor,
            highlightthickness=0
        )
        # Scaling the setting background image
        self.xFactor = self.canvasPlayer.winfo_reqwidth() / self.photoImage.width()
        self.yFactor = self.canvasPlayer.winfo_reqheight() / self.photoImage.height()
        self.image = self.image.resize(
            (int(self.image.width * self.xFactor),
             int(self.image.height * self.yFactor)),
            ImageModule.ANTIALIAS
        )
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Image on the canvas
        self.canvasImage = self.canvasPlayer.create_image(
            int(self.canvasPlayer.winfo_reqwidth() * 50 / 100),
            int(self.canvasPlayer.winfo_reqheight() * 50 / 100),
            image=self.photoImage
        )

        ###############################
        # Name
        self.canvasNameText = self.canvasPlayer.create_text(
            int(self.canvasPlayer.winfo_reqwidth() * 50 / 100),
            int(self.canvasPlayer.winfo_reqheight() * 10 / 100),
            anchor=tk.N,
            text="Name:",
            font=("Minecraft", 16),
            fill=self.textColor,
        )
        self.nameEntry = tk.Entry(
            self.parent,
            width=15,
            justify=tk.CENTER,
            background=self.textColor,
            foreground=self.backgroundColor,
            font=("Minecraft", 16),
            highlightthickness=0
        )
        self.canvasNameWindow = self.canvasPlayer.create_window(
            int(self.canvasPlayer.winfo_reqwidth() * 50 / 100),
            int(self.canvasPlayer.winfo_reqheight() * 25 / 100),
            window=self.nameEntry,
            height=40,
        )
        ###############################
        # Playing style
        self.canvasPlayStyleText = self.canvasPlayer.create_text(
            int(self.canvasPlayer.winfo_reqwidth() * 10 / 100),
            int(self.canvasPlayer.winfo_reqheight() * 50 / 100),
            anchor=tk.W,
            text="Style:",
            font=("Minecraft", 12),
            fill=self.textColor,
        )

        self.playStyles = [
            "Mouse",
            "Keyboard"
        ]
        self.choosenStyle = tk.StringVar()
        self.choosenStyle.set(self.playStyles[0])

        self.playStyle = tk.OptionMenu(
            self.parent,
            self.choosenStyle,
            *self.playStyles,
        )
        self.playStyle.configure(
            width=9,
            font=("Minecraft", 12),
            background=self.textColor,
            foreground=self.backgroundColor,
            activebackground=self.backgroundColor,
            activeforeground=self.textColor,
            highlightthickness=0
        )
        self.playStyleWindows = self.canvasPlayer.create_window(
            int(self.canvasPlayer.winfo_reqwidth() * 40 / 100),
            int(self.canvasPlayer.winfo_reqheight() * 50 / 100),
            anchor=tk.W,
            window=self.playStyle,
        )

        Player.playerList.append(self)

    def show(cls):
        for player in Player.playerList:
            xPlace = interp(
                Player.playerList.index(player),
                [0, len(Player.playerList)-1],
                [13, 87]
            )
            player.parent.create_window(
                int(player.parent.winfo_reqwidth() * xPlace / 100),
                int(player.parent.winfo_reqheight() * 25 / 100),
                window=player.canvasPlayer
            )
    show = classmethod(show)
