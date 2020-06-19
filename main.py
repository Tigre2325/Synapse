# libraires
import tkinter as tk
import time
from PIL import Image as ImageModule
from PIL import ImageTk

###############################################################################
# Classes
from classes.application import *
from classes.page import *
from classes.image import *
from classes.text import *
from classes.button import *

###############################################################################
# Window
app = Application()

# Application pages
home = Page(app)
register = Page(app)
game = Page(app)
settings = Page(app)
rules = Page(app)
###############################################################################
# Homepage
background = Image(home, "./images/light_theme/background.png",
                   int(app.winfo_width() / 2), int(app.winfo_height() / 2))
synapse = Text(home, "SYNAPSE",
               int(app.winfo_width() / 2), int(app.winfo_height() * 1 / 5),
               -150, "#502010")


# Buttons on the homepage
playButton = Button(home, "./images/light_theme/button_background_3-1.png",
                    "Play", app.winfo_width() / 2, app.winfo_height() * 3 / 5,
                    32, "#ceaf91", "#804030")
settingsButton = Button(home, "./images/light_theme/button_background_3-1.png",
                        "Settings",
                        app.winfo_width() / 2, app.winfo_height() * 4 / 5,
                        32, "#ceaf91", "#804030")
quitButton = Button(home, "./images/light_theme/button_background_3-1.png",
                    "Quit", app.winfo_width() * 2 / 30, app.winfo_height() * 28 / 30,
                    16, "#ceaf91", "#804030")
ruleButton = Button(home, "./images/light_theme/button_background_3-1.png",
                    "Rules", app.winfo_width() * 28 / 30, app.winfo_height() * 28 / 30,
                    16, "#ceaf91", "#804030")

background.show()
synapse.show()
# Show the homepage buttons


playButton.scale(2)
playButton.show()
settingsButton.scale(2)
settingsButton.show()
quitButton.scale(0.7, 1)
quitButton.show()
ruleButton.scale(0.7, 1)
ruleButton.show()

###############################################################################
# Open the start page
home.show(app)
# register.show(app)
# game.show(app)
# settings.show(app)
# rules.show(app)


###############################################################################
# # Scale the view
# def configure(event):
#     currentWidth, currentHeight = event.width, event.height


# home.bind("<Configure>", configure)


app.mainloop()
