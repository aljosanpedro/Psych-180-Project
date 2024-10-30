# SET-UP

# Disable help keys (i.e. Esc)
define _game_menu_screen = None

# Image Transforms
"""
transform ch:
    zoom 0.65
transform bg:
    zoom 0.8
"""

# Characters
# Boys
define geo = Character("Geo", color="#609AD2")
define pao = Character("Pao", color="#212630")
# Girls
define lily = Character("Lily", color="#61575A")
define bianca = Character("Bianca", color="#C3A393")

# Inputs
define name = ""
define player = Character("[name]")

# START

label start:

    stop music fadeout 1.0

    scene bg school morning stairs
    show geo date smile

    geo "You've created a new Ren'Py game."

    while not name:
        $ name = renpy.input("Name:", length=10)
        $ name = name.strip().title()

    geo "Hi, my name is [name]!"

    geo "Once you add a story, pictures, and music, you can release it to the world!"

# END

    return
