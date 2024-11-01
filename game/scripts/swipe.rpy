label swipe:
    stop music fadeout 1.0
    play music "audio/music/swipe.ogg"

    label .setup:
        python:
            rights = []
            swiped = False
            direction = ""
            character = ""

        jump swipe.geo

    label .choice:
        show app textbox
        kulo "So, what do you think?" 

        menu:
            "Swipe Left":
                $ swiped = True
                $ direction = "left"
            "Swipe Right":
                $ swiped = True
                $ direction = "right"

                $ rights.append(character)
            "Reread Profile":
                $ swiped = False
                $ direction = "up"

        return

    label .direction:
        if direction == "left":
            with swipe_left
        elif direction == "right":
            with swipe_right
        elif direction == "up":
            with new_screen

        return

    label .geo:
        $ character = "geo"
        $ swiped = False

        while not swiped:
            scene bus morning at bg_nora_new
            show geo casual neutral at char
            with new_screen
            geo ""
            show geo casual smile at char
            with dissolve
            geo ""

            scene school morning stairs at bg_nora_new
            show geo work happy at char
            with scroll_up
            geo ""

            scene resto evening center at bg_resto_evening
            show geo date smile at char
            with scroll_up
            geo ""

            call swipe.choice

    label .pao:
        $ character = "pao"
        $ swiped = False

        while not swiped:
            scene street afternoon store at bg_nora_new
            show pao date neutral at char
            call swipe.direction
            pao ""
            show pao date smile at char
            with dissolve
            pao ""

            scene resto inside at bg_nora_old
            show pao work happy at char
            with scroll_up
            pao ""

            scene house sala table at bg_senpai
            show pao casual neutral at char
            with scroll_up
            pao ""

            call swipe.choice

    label .lily:
        $ character = "lily"
        $ swiped = False

        while not swiped:
            scene school morning shrine at bg_nora_new
            show lily date smile at char
            call swipe.direction
            lily ""
            show lily date happy at char
            with dissolve
            lily ""

            scene playground slide at bg_senpai
            show lily casual shock at char
            with scroll_up
            lily ""

            scene train inside at bg_nora_old
            show lily work neutral at char
            with scroll_up
            lily ""

            call swipe.choice

    label .bianca:
        $ character = "bianca"
        $ swiped = False

        while not swiped:
            scene resto cake shop at bg_nora_old
            show bianca date neutral at char
            call swipe.direction
            bianca ""
            show bianca date smile at char
            with dissolve
            bianca ""

            scene house kitchen at bg_senpai
            show bianca work happy at char
            with scroll_up
            bianca ""

            scene house bedroom closet at bg_senpai
            show bianca casual neutral at char
            with scroll_up
            bianca ""

            call swipe.choice

    label .repeat:
        scene app bg
        call swipe.direction
        scene app bg textbox with dissolve
        mascot "Are you OK with your swipes?"
        menu:
            "Yup!":
                pass
                mascot "You liked [rights]"
            "Repeat":
                jump swipe.setup

    jump chat