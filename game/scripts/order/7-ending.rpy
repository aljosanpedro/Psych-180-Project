label ending:
    stop music fadeout 1.0
    
    label .dating:
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
        play music "audio/music/endings/friends.ogg"

    label .pass:
        play music "audio/music/endings/pass.ogg"
        
    jump end