# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
transform ch:
    zoom 0.65
transform bg:
    zoom 0.8


# Disable help keys (i.e. Esc)
define _game_menu_screen = None
define h = Character("Haruo", color="4d474b")


# The game starts here.

label start:

    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg madoka_casual at bg

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show madoka casual at ch, center

    # These display lines of dialogue.

    h "You've created a new Ren'Py game."

    h "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
