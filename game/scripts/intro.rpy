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

    $ correct_name = False
    while not correct_name:
        $ name = ""
        while not name:
            $ name = renpy.input("Name:", length=10)
            $ name = name.strip().title()
        kulo "Your name is [name]?"
        menu:
            "Yes":
                $ correct_name = True
            "No":
                $ correct_name = False

    "Hello, [name]!\ntest\ntest\ntest"

    jump profile