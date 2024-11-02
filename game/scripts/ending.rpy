label ending:
    $ story = "ending"
    
    call tips.give

    label .dating:
        stop music fadeout 1.0
        play music "audio/music/endings/dating.ogg"

        label .geo:
            scene train station at bg_nora_old
            show geo casual smile at char
            with dissolve
            geo ""

        label .pao:
            scene resto inside at bg_nora_old
            show pao casual happy at char
            with dissolve
            pao ""

        label .lily:
            scene bus afternoon at bg_nora_new
            show lily work happy at char
            with dissolve
            lily ""

        label .bianca:
            scene school morning stairs at bg_nora_new
            show bianca work happy at char
            with dissolve
            lily ""

    label .friends:
        stop music fadeout 1.0
        play music "audio/music/endings/friends.ogg"

        mascot "friends"

    label .pass:
        stop music fadeout 1.0
        play music "audio/music/endings/pass.ogg"

        mascot "pass"
        
    jump end