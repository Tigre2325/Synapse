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
# Global application settings
centerWidth = int(app.winfo_width() * 50 / 100)
centerHeight = int(app.winfo_height() * 50 / 100)

# TODO: creer un objet Theme qui permet plus facilement de changer de theme
theme = [
    "light_theme",
    "dark_theme"
]
currentTheme = theme[0]

# TODO: fichier contenant tous les textes dans un ordre precis pour ajouter des langues
language = [
    "English",
    "Français"
]

#######################################
# Homepage
homeBackground = Image(
    home,
    "./images/{}/background.png".format(currentTheme),
    centerWidth,
    centerHeight
)

synapse = Text(
    home,
    "SYNAPSE",
    centerWidth,
    int(app.winfo_height() * 20 / 100),
    -150,
    "#502010"
)

authors = Text(
    home,
    "Made by Tigre2325,\n\n with the participation of Fukuro and CaptainRommel,\n\n and based on LARBROJEUX's Synapse game",
    centerWidth,
    int(app.winfo_height() * 93 / 100),
    12
)

# Buttons on the homepage
playButton = Button(
    home,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Play",
    centerWidth,
    int(app.winfo_height() * 50 / 100),
    32,
    "#f0d0a0",
    "#804030"
)

settingsButton = Button(
    home,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Settings",
    centerWidth,
    int(app.winfo_height() * 70 / 100),
    32,
    "#f0d0a0",
    "#804030"
)

quitAppButton = Button(
    home,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Quit",
    int(app.winfo_width() * 7 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#f0d0a0",
    "#804030"
)

ruleButton = Button(
    home,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    int(app.winfo_width() * 93 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#f0d0a0",
    "#804030"
)

# Show all the objects on the home page canvas
homeBackground.show()
synapse.show()
authors.show()

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
    "./images/{}/background.png".format(currentTheme),
    centerWidth,
    centerHeight
)

board = Image(
    game,
    "./images/{}/board.png".format(currentTheme),
    centerWidth,
    centerHeight
)

# Left side
quitGameButton = Button(
    game,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Quit",
    int(app.winfo_width() * 6 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)

ruleGameButton = Button(
    game,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    int(app.winfo_width() * 16 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)

# Right side
currentPlayer = Text(
    game,
    # TODO: creer un objet joueur avec une méthode de classe qui retourne le joueur actuel
    "{}'s turn".format("Anthony"),
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 6 / 100),
    24,
)
currentPlayer.set(width=280)

instructions = [
    # Cliquez sur une des cases du plateau afin de placer vos pièces
    # Sélectionnez le nombre de pièce à placer
    # Sélectionnez l'orientation des pièces à placer
    # Validez le tour
    # Choisissez un nombre de pièces !
    # Choisissez moins de pièces !
    # Choisissez une orientation pour vos pièces !
    # Votre choix n'est pas valide, les pièces se chevauchent !
    # Votre choix n'est pas valide, les pièces seraient en dehors du plateau !
    # Cliquez sur le bouton de validation pour continuer à jouer ou sur quitter pour arrêter
    "Click on one of the board cases to position your pieces",
    "Select the number of pieces you want to play",
    "Select the orientation of your pieces",
    # TODO: terminer l'écriture des instructions
]

instruction = Text(
    game,
    instructions[0],
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 16 / 100)
)
instruction.set(width=280)

onePieceButton = Button(
    game,
    "./images/{}/background_55x55.png".format(currentTheme),
    "1",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)

twoPieceButton = Button(
    game,
    "./images/{}/background_55x55.png".format(currentTheme),
    "2",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)

threePieceButton = Button(
    game,
    "./images/{}/background_55x55.png".format(currentTheme),
    "3",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)

arrowUpButton = Button(
    game,
    "./images/{}/arrow_up.png".format(currentTheme),
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 43 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)

arrowDownButton = Button(
    game,
    "./images/{}/arrow_down.png".format(currentTheme),
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 61 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)

arrowRightButton = Button(
    game,
    "./images/{}/arrow_right.png".format(currentTheme),
    "",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)

arrowLeftButton = Button(
    game,
    "./images/{}/arrow_left.png".format(currentTheme),
    "",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)

confirmButton = Button(
    game,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Confirm",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 73 / 100),
    20,
    "#f0d0a0",
    "#804030"
)

piecesRemainingText = Text(
    game,
    "Number of pieces remaining:",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 83 / 100),
    20
)
piecesRemainingText.set(width=280)

# TODO: nombre de pièce à créer avec le lancement de la partie
piecesRemaining = 0

piecesRemainingNumber = Text(
    game,
    "{}".format(piecesRemaining),
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 93 / 100),
    50
)

# Show all the objects on the home page canvas
quitGameButton.show()
quitGameButton.scale(0.6, 0.7)

ruleGameButton.show()
ruleGameButton.scale(0.6, 0.7)


gameBackground.show()
board.show()


currentPlayer.show()

instruction.show()

onePieceButton.show()
twoPieceButton.show()
threePieceButton.show()

arrowUpButton.show()
arrowDownButton.show()
arrowRightButton.show()
arrowLeftButton.show()

confirmButton.scale(1.2, 0.8)
confirmButton.show()

piecesRemainingText.show()
piecesRemainingNumber.show()

#######################################
# Settings page


#######################################
# Rule page


#######################################
# Open the start page
# home.show()
# register.show()
game.show()
# settings.show()
# rules.show()
###############################################################################

###############################################################################
# Logical elements
#######################################
# # Scale the view
# def configure(event):
#     currentWidth, currentHeight = event.width, event.height


# home.bind("<Configure>", configure)


app.mainloop()
