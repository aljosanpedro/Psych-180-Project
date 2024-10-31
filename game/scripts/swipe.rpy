label swipe:
    stop music fadeout 1.0
    play music "audio/music/swipe.ogg"

    define rights = []
    $ swiped = False
    $ direction = ""

    jump swipe.profiles.geo

    label .choice:
        menu:
            "Left":
                $ swiped = True
                $ direction = "left"
            "Right":
                $ swiped = True
                $ direction = "right"
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
            with swipe_up

        return

    label .geo:
        $ swiped = False
        while not swiped:
            scene bus morning at bg_nora_new
            show geo casual neutral at char
            with profile_swipe
            geo ""
            show geo casual smile at char
            with dissolve
            geo ""

            scene school morning stairs at bg_nora_new
            show geo work happy at char
            with profile_swipe
            geo ""

            scene resto evening center at bg_resto_evening
            show geo date smile at char
            with profile_swipe
            geo ""

            call swipe.choice

    label .pao:
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
            with profile_swipe
            pao ""

            scene house sala table at bg_senpai
            show pao casual neutral at char
            with profile_swipe
            pao ""

            call swipe.choice

    label .lily:
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
            with profile_swipe
            lily ""

            scene train inside at bg_nora_old
            show lily work neutral at char
            with profile_swipe
            lily ""

            call swipe.choice

    label .bianca:
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
            with profile_swipe
            bianca ""

            scene house bedroom closet at bg_senpai
            show bianca casual neutral at char
            with profile_swipe
            bianca ""

            call swipe.choice

    jump chat