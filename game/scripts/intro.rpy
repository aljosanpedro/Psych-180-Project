label intro:
    
    stop music fadeout 1.0
    play music "audio/music/profile.ogg"

    scene app bg

    show kulo_slow
    kulo "Loading..."
    hide kulo_slow

    show kulo_mid
    kulo "Loading..."
    hide kulo_mid

    show kulo_fast
    kulo "Loading..."
    hide kulo_fast

    while not name:
        $ name = renpy.input("Name:", length=10)
        $ name = name.strip().title()

    "Hello, [name]!\ntest\ntest\ntest"

    jump profile