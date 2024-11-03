label intro:
    $ story = "intro"
    
    label .welcome:
        stop music fadeout 1.0
        play music "audio/music/profile.ogg"

        scene app bg

        call tips.give
                
    label .name:
        $ correct_name = False
        while not correct_name:
            $ name = ""
            while not name:
                $ name = renpy.input("Name:", length=10)
                $ name = name.strip()
            scene app bg textbox
            kulo "Your name is [name]?"
            menu:
                "Yes":
                    $ correct_name = True
                "No":
                    $ correct_name = False

        "Hello, [name]!\ntest\ntest\ntest"

    jump profile