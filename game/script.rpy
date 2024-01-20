# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
transform ch:
    zoom 0.6
transform bg:
    zoom 0.75


define h = Character("Haruo", color="4d474b")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg haruo_casual at bg, left

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show haruo casual at ch, truecenter

    # These display lines of dialogue.

    h "You've created a new Ren'Py game."

    h "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
