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

###############################################################################
# Graphical elements
#######################################
# Homepage
homeBackground = Image(
    home, "./images/light_theme/background.png",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 50 / 100)
)

synapse = Text(
    home,
    "SYNAPSE",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 20 / 100),
    -150,
    "#502010"
)


# Buttons on the homepage
playButton = Button(
    home,
    "./images/light_theme/button_background_3-1.png",
    "Play",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 60 / 100),
    32,
    "#ceaf91",
    "#804030"
)

settingsButton = Button(
    home,
    "./images/light_theme/button_background_3-1.png",
    "Settings",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 80 / 100),
    32,
    "#ceaf91",
    "#804030"
)

quitAppButton = Button(
    home,
    "./images/light_theme/button_background_3-1.png",
    "Quit",
    int(app.winfo_width() * 7 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#ceaf91",
    "#804030"
)

ruleButton = Button(
    home,
    "./images/light_theme/button_background_3-1.png",
    "Rules",
    int(app.winfo_width() * 93 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#ceaf91",
    "#804030"
)

# Show all the objects on the home page canvas
homeBackground.show()

synapse.show()

playButton.scale(2)
playButton.show()

settingsButton.scale(2)
settingsButton.show()

quitAppButton.scale(0.8, 0.7)
quitAppButton.show()

ruleButton.scale(0.8, 0.7)
ruleButton.show()


#######################################
# Register page


#######################################
# Game page
gameBackground = Image(
    game,
    "./images/light_theme/background.png",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 50 / 100)
)

board = Image(
    game,
    "./images/light_theme/board.png",
    int(app.winfo_width() * 50 / 100),
    int(app.winfo_height() * 50 / 100)
)

# Left side
quitGameButton = Button(
    game,
    "./images/light_theme/button_background_3-1.png",
    "Quit",
    int(app.winfo_width() * 7 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#ceaf91",
    "#804030"
)

# Right side
onePieceButton = Button(
    game,
    "./images/light_theme/number_piece.png",
    "1",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#ceaf91",
    "#804030"
)

twoPieceButton = Button(
    game,
    "./images/light_theme/number_piece.png",
    "2",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#ceaf91",
    "#804030"
)

threePieceButton = Button(
    game,
    "./images/light_theme/number_piece.png",
    "3",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#ceaf91",
    "#804030"
)

arrowUpButton = Button(
    game,
    "./images/light_theme/arrow_up.png",
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 43 / 100),
    1,
    "#ceaf91",
    "#804030"
)

arrowDownButton = Button(
    game,
    "./images/light_theme/arrow_down.png",
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 61 / 100),
    1,
    "#ceaf91",
    "#804030"
)

arrowRightButton = Button(
    game,
    "./images/light_theme/arrow_right.png",
    "",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#ceaf91",
    "#804030"
)

arrowLeftButton = Button(
    game,
    "./images/light_theme/arrow_left.png",
    "",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#ceaf91",
    "#804030"
)

confirmButton = Button(
    game,
    "./images/light_theme/button_background_3-1.png",
    "Confirm",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 73 / 100),
    20,
    "#ceaf91",
    "#804030"
)

# Show all the objects on the home page canvas
gameBackground.show()

board.show()

quitGameButton.scale(0.8, 0.7)
quitGameButton.show()

confirmButton.scale(1.2, 0.8)
confirmButton.show()

onePieceButton.show()
twoPieceButton.show()
threePieceButton.show()

arrowUpButton.show()
arrowDownButton.show()
arrowRightButton.show()
arrowLeftButton.show()

#######################################
# Settings page


#######################################
# Rule page


#######################################
# Open the start page
# home.show(app)
# register.show(app)
game.show(app)
# settings.show(app)
# rules.show(app)
###############################################################################

###############################################################################
# Logical elements
#######################################
# # Scale the view
# def configure(event):
#     currentWidth, currentHeight = event.width, event.height


# home.bind("<Configure>", configure)


app.mainloop()
