# SET-UP

# Disable help keys (i.e. Esc)
define _game_menu_screen = None

# Image Transforms
transform ch:
    zoom 0.65
transform bg:
    zoom 0.8

# Characters
# Boys
define h = Character("Haruo", color="#4D474B")
define k = Character("Kioshi", color="#516CA9")
define t = Character("Taishiro", color="#FF848B")
# Girls
define m = Character("Madoka", color="#AB6F45")
define n = Character("Nozomi", color="#474144")
define r = Character("Ryoko", color="#F6B37E")

# Inputs
define name = ""
define p = Character("[name]")

# START

label start:

    stop music fadeout 1.0

    scene bg ryoko_casual at bg
    show ryoko casual at ch, center

    r "You've created a new Ren'Py game."

    while not name:
        $ name = renpy.input("Name:", length=10)
        $ name = name.strip().title()

    p "Hi, my name is [name]!"

    r "Once you add a story, pictures, and music, you can release it to the world!"

# END

    return
