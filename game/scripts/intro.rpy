label intro:
    
    stop music fadeout 1.0
    play music "audio/music/profile.ogg"

    scene app bg

    show simon_slow
    simon "Loading..."
    hide simon_slow

    show simon_mid
    simon "Loading..."
    hide simon_mid

    show simon_fast
    simon "Loading..."
    hide simon_fast

    while not name:
        $ name = renpy.input("Name:", length=10)
        $ name = name.strip().title()

    "Hello, [name]!\ntest\ntest\ntest"

    jump profile