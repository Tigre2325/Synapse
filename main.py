# libraires
import tkinter as tk
import time
from PIL import Image as ImageModule
from PIL import ImageTk

###############################################################################
# Classes
from classes.application import *
from classes.button import *
from classes.image import *
from classes.page import *
from classes.player import *
from classes.settings import *
from classes.text import *


###############################################################################
# Window
app = Application()
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
# Application pages
homePage = Page(app, "./images/{}/background.png".format(currentTheme))
registerPage = Page(app, "./images/{}/background.png".format(currentTheme))
gamePage = Page(app, "./images/{}/background.png".format(currentTheme))
settingsPage = Page(app, "./images/{}/background.png".format(currentTheme))
rulesPage = Page(app, "./images/{}/background.png".format(currentTheme))

#######################################
# Homepage
synapse = Text(
    homePage,
    "SYNAPSE",
    centerWidth,
    int(app.winfo_height() * 20 / 100),
    -150,
    "#502010"
)
synapse.show()

authors = Text(
    homePage,
    "Made by Tigre2325 in 2020,\n\n with the participation of Fukuro and CaptainRommel,\n\n and based on LARBROJEUX's Synapse game",
    centerWidth,
    int(app.winfo_height() * 93 / 100),
    12
)
authors.show()

# Buttons on the homepage
playButton = Button(
    homePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Play",
    centerWidth,
    int(app.winfo_height() * 50 / 100),
    32,
    "#f0d0a0",
    "#804030"
)
playButton.scale(2)
playButton.show()

settingsButton = Button(
    homePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Settings",
    centerWidth,
    int(app.winfo_height() * 70 / 100),
    32,
    "#f0d0a0",
    "#804030"
)
settingsButton.scale(2)
settingsButton.show()

quitAppButton = Button(
    homePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Quit",
    int(app.winfo_width() * 7 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#f0d0a0",
    "#804030"
)
quitAppButton.scale(0.8, 0.7)
quitAppButton.show()

ruleHomeButton = Button(
    homePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    int(app.winfo_width() * 93 / 100),
    int(app.winfo_height() * 95 / 100),
    16,
    "#f0d0a0",
    "#804030"
)
ruleHomeButton.scale(0.8, 0.7)
ruleHomeButton.show()

#######################################
# Register page
player1 = Player(
    registerPage,
    "./images/dark_wood_plank.png",
    "#f0d0a0",
    "#804030"
)

player2 = Player(
    registerPage,
    "./images/dark_wood_plank.png",
    "#f0d0a0",
    "#804030"
)

# player3 = Player(
#     registerPage,
#     "./images/dark_wood_plank.png",
#     "#f0d0a0",
#     "#804030"
# )

# player4 = Player(
#     registerPage,
#     "./images/dark_wood_plank.png",
#     "#f0d0a0",
#     "#804030"
# )
Player.show()

addPlayerButton = Button(
    registerPage,
    "./images/dark_wood_plank.png",
    "New player",
    int(app.winfo_width() * (len(Player.playerList) * 24.5 + 13) / 100),
    int(app.winfo_height() * 25 / 100),
    22,
    "#f0d0a0",
    "#804030"
)
addPlayerButton.scale(1.2, 1.22)
addPlayerButton.show()

backRegisterButton = Button(
    registerPage,
    "./images/{}/button_back_background_165x55.png".format(currentTheme),
    "            Back",
    int(app.winfo_width() * 8 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
backRegisterButton.scale(1, 0.7)
backRegisterButton.show()

ruleRegisterButton = Button(
    registerPage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    centerWidth,
    int(app.winfo_height() * 95 / 100),
    20,
    "#f0d0a0",
    "#804030"
)
ruleRegisterButton.scale(1, 0.7)
ruleRegisterButton.show()

startButton = Button(
    registerPage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Play",
    int(app.winfo_width() * 92 / 100),
    int(app.winfo_height() * 95 / 100),
    20,
    "#f0d0a0",
    "#804030"
)
startButton.scale(1, 0.7)
startButton.show()

#######################################
# Game page
board = Image(
    gamePage,
    "./images/{}/board.png".format(currentTheme),
    centerWidth,
    centerHeight
)
board.show()

# Left side
backGameButton = Button(
    gamePage,
    "./images/{}/button_back_background_165x55.png".format(currentTheme),
    "            Back",
    int(app.winfo_width() * 7 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
backGameButton.show()
backGameButton.scale(0.9, 0.7)

ruleGameButton = Button(
    gamePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    int(app.winfo_width() * 18 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
ruleGameButton.show()
ruleGameButton.scale(0.5, 0.7)

# Right side
currentPlayer = Text(
    gamePage,
    # TODO: creer methode dans la classe Brain qui retourne le joueur actuel
    "{}'s turn".format("Anthony"),
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 6 / 100),
    24,
)
currentPlayer.set(width=280)
currentPlayer.show()

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
    # TODO: terminer l'ecriture des instructions
]

instruction = Text(
    gamePage,
    instructions[0],
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 16 / 100)
)
instruction.set(width=280)
instruction.show()

onePieceButton = Button(
    gamePage,
    "./images/{}/background_55x55.png".format(currentTheme),
    "1",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)
onePieceButton.show()

twoPieceButton = Button(
    gamePage,
    "./images/{}/background_55x55.png".format(currentTheme),
    "2",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)
twoPieceButton.show()

threePieceButton = Button(
    gamePage,
    "./images/{}/background_55x55.png".format(currentTheme),
    "3",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 30 / 100),
    22,
    "#f0d0a0",
    "#804030"
)
threePieceButton.show()

arrowUpButton = Button(
    gamePage,
    "./images/{}/arrow_up.png".format(currentTheme),
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 43 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)
arrowUpButton.show()

arrowDownButton = Button(
    gamePage,
    "./images/{}/arrow_down.png".format(currentTheme),
    "",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 61 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)
arrowDownButton.show()

arrowRightButton = Button(
    gamePage,
    "./images/{}/arrow_right.png".format(currentTheme),
    "",
    int(app.winfo_width() * 96 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)
arrowRightButton.show()

arrowLeftButton = Button(
    gamePage,
    "./images/{}/arrow_left.png".format(currentTheme),
    "",
    int(app.winfo_width() * 82 / 100),
    int(app.winfo_height() * 52 / 100),
    1,
    "#f0d0a0",
    "#f0d0a0"
)
arrowLeftButton.show()

confirmButton = Button(
    gamePage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Confirm",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 73 / 100),
    20,
    "#f0d0a0",
    "#804030"
)
confirmButton.scale(1.2, 0.8)
confirmButton.show()

piecesRemainingText = Text(
    gamePage,
    "Number of pieces remaining:",
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 83 / 100),
    20
)
piecesRemainingText.set(width=280)
piecesRemainingText.show()

# TODO: nombre de piece à creer avec le lancement de la partie
piecesRemaining = 0

piecesRemainingNumber = Text(
    gamePage,
    "{}".format(piecesRemaining),
    int(app.winfo_width() * 89 / 100),
    int(app.winfo_height() * 93 / 100),
    50
)
piecesRemainingNumber.show()

#######################################
# Settings page
backSettingsButton = Button(
    settingsPage,
    "./images/{}/button_back_background_165x55.png".format(currentTheme),
    "            Back",
    int(app.winfo_width() * 10 / 100),
    int(app.winfo_height() * 95 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
backSettingsButton.scale(1, 0.7)
backSettingsButton.show()

ruleSettingsButton = Button(
    settingsPage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "Rules",
    int(app.winfo_width() * 10 / 100),
    int(app.winfo_height() * 15 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
ruleSettingsButton.scale(1, 0.7)
ruleSettingsButton.show()

codeButton = Button(
    settingsPage,
    "./images/{}/button_background_165x55.png".format(currentTheme),
    "See the code",
    int(app.winfo_width() * 10 / 100),
    int(app.winfo_height() * 55 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
codeButton.scale(1, 0.7)
codeButton.show()

# Settings
languageSetting = Settings(
    settingsPage,
    "./images/dark_wood_plank.png".format(currentTheme),
    "Language",
    language,
    "#f0d0a0",
    "#804030"
)

themeSetting = Settings(
    settingsPage,
    "./images/dark_wood_plank.png".format(currentTheme),
    "Theme",
    theme,
    "#f0d0a0",
    "#804030"
)

Settings.show()
#######################################
# Rule page
backRulesButton = Button(
    rulesPage,
    "./images/{}/button_back_background_165x55.png".format(currentTheme),
    "            Back",
    int(app.winfo_width() * 10 / 100),
    int(app.winfo_height() * 5 / 100),
    14,
    "#f0d0a0",
    "#804030"
)
backRulesButton.scale(1, 0.7)
backRulesButton.show()

rulesText = [
    "Synapse is a turn-based strategy game (like chess) which is originally played by 2 players.",
    "The aim of the game is to cause your opponent to lose the ability to play.",
    "The 1st player is randomly chosen. He can put 1, 2 or 3 pieces on the case he wants (the pieces must have the same orientation). These pieces indicate where the next player have to play its turn.",
    "The winner is the player who manage to cause its opponent to lose the ability to play either by lack of pieces, or by lack of empty case : the player who is stuck win the game.\nTo simplify, the looser is the player who take the last piece or the player who put its piece on the last case of the board."
]

rulesTextFormat = ""
for li in rulesText:
    rulesTextFormat += li + "\n\n\n\n\n"

rules = Text(
    rulesPage,
    rulesTextFormat,
    int(app.winfo_width() * 22 / 100),
    int(app.winfo_height() * 9 / 100),
    14,
    "#502010"
)
rules.set(
    anchor=tk.NW,
    justify=tk.LEFT,
    width=int(app.winfo_width() * 75 / 100)
)
rules.show()

introduction = Text(
    rulesPage,
    "Introduction",
    int(app.winfo_width() * 20 / 100),
    int(app.winfo_height() * 3 / 100),
    20,
    "#502010"
)
introduction.set(
    anchor=tk.NW,
    justify=tk.LEFT,
    width=int(app.winfo_width() * 75 / 100),
    font=("Minecraft", 20, "bold")
)
introduction.show()

aim = Text(
    rulesPage,
    "Aim of the game",
    int(app.winfo_width() * 20 / 100),
    int(app.winfo_height() * 19 / 100),
    20,
    "#502010"
)
aim.set(
    anchor=tk.NW,
    justify=tk.LEFT,
    width=int(app.winfo_width() * 75 / 100),
    font=("Minecraft", 20, "bold")
)
aim.show()

proceedings = Text(
    rulesPage,
    "Game proceedings",
    int(app.winfo_width() * 20 / 100),
    int(app.winfo_height() * 32 / 100),
    20,
    "#502010"
)
proceedings.set(
    anchor=tk.NW,
    justify=tk.LEFT,
    width=int(app.winfo_width() * 75 / 100),
    font=("Minecraft", 20, "bold")
)
proceedings.show()

winCondition = Text(
    rulesPage,
    "Winner",
    int(app.winfo_width() * 20 / 100),
    int(app.winfo_height() * 50 / 100),
    20,
    "#502010"
)
winCondition.set(
    anchor=tk.NW,
    justify=tk.LEFT,
    width=int(app.winfo_width() * 75 / 100),
    font=("Minecraft", 20, "bold")
)
winCondition.show()

#######################################
# Open the start page
# homePage.show()
# registerPage.show()
# gamePage.show()
# settingsPage.show()
rulesPage.show()
###############################################################################

###############################################################################
# Logical elements
#######################################
# # Scale the view
# def configure(event):
#     currentWidth, currentHeight = event.width, event.height

# homePage.bind("<Configure>", configure)

"""
TODO: faire une classe Brain qui sera une classe utilitaire
    avec que des methodes statiques dedans
"""

app.mainloop()
