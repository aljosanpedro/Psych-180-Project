label ending:
    $ story = "ending"
    
    call tips.give from _call_tips_give_3

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

        kulo "friends"

    label .pass:
        stop music fadeout 1.0
        play music "audio/music/endings/pass.ogg"
        
        scene app bg
        show kulo_slow
        with new_screen

        kulo "Thanks for trying out Simmer!"
        kulo "Look forward to our future updates soon!"

    label .prototype:
        stop music fadeout 1.0
        play music "audio/music/endings/friends.ogg"

        scene app bg
        show kulo_slow
        with new_screen

        kulo "That's all we've got at the moment."
        kulo "Thank you for testing out the prototype for Simmer:"
        kulo "a dating app simulator with social psychology elements!"
        kulo "Please look forward to our future updates!"
        kulo "Until then, keep the spice simmering!"
        
    jump end