label intro:
    $ story = "intro"
    
    label .welcome:
        stop music fadeout 1.0
        play music "audio/music/profile.ogg"

        scene app bg

        call tips.give

    label .gender:
        scene app bg textbox
        blank "Boy or girl?"
        menu:
            "Boy":
                $ gender = "boy"
                $ mascot = kulo
            "Girl":
                $ gender = "girl"
                $ mascot = kali
        
        if mascot == kulo:
            show kulo_slow
        elif mascot == kali:
            show kali_slow
        mascot "Loading..."
        if mascot == kulo:
            hide kulo_slow
        elif mascot == kali:
            hide kali_slow

        if mascot == kulo:
            show kulo_mid
        elif mascot == kali:
            show kali_mid
        mascot "Loading..."
        if mascot == kulo:
            hide kulo_mid
        elif mascot == kali:
            hide kali_mid

        if mascot == kulo:
            show kulo_fast
        elif mascot == kali:
            show kali_fast
        mascot "Loading..."
        if mascot == kulo:
            hide kulo_fast
        elif mascot == kali:
            hide kali_fast

        mascot "You are a [gender], right?"
        menu:
            "Yes":
                pass
            "No":
                jump intro.gender
                
    label .name:
        $ correct_name = False
        while not correct_name:
            $ name = ""
            while not name:
                $ name = renpy.input("Name:", length=10)
                $ name = name.strip()
            scene app bg textbox
            mascot "Your name is [name]?"
            menu:
                "Yes":
                    $ correct_name = True
                "No":
                    $ correct_name = False

        "Hello, [name]!\ntest\ntest\ntest"

    jump profile