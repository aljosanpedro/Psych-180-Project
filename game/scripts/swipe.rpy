label swipe:
    $ story = "swiping"

    stop music fadeout 1.0
    play music "audio/music/swipe.ogg"

    label .setup:
        define rights = []
        define swiped = False
        define direction = "up"
        define character = ""
        define characters = ["geo", "pao", "lily", "bianca"]
        define profile = ""

        define c_bio = ""
        define c_self_presentation = ""
        define c_self_conscious_emo = ""

        define c_gender_preference = ""
        define c_relationship_type = ""
        define c_distance = ""
        define c_future_priority = ""

        define c_age_range = ""
        define c_interests = ""
        define c_interests_specific = ""
        define c_occupation = ""
        define c_occupation_specific = ""
        define c_education = ""

        define c_social_skills = ""
        define c_sociable = ""
        define c_belief = ""
        define c_exercise = ""

    label .dialog:
        show kulo_slow
        kulo "Your profile's looking good, [name]."
        kulo "I've got some profiles incoming for you."
        kulo "Tell me at the end of each what you think."
        kulo "You can also choose to go over it again."
        hide kulo_slow
        show kulo_fast
        kulo "Here comes the {i}entree{/i}!"

    label .flow:
        $ renpy.random.shuffle(characters)
        while len(characters) > 0:
            python:
                profile = renpy.random.choice(characters)
                characters.remove(profile)

            if profile == "geo":
                call swipe_geo from _call_swipe_geo
            elif profile == "pao":
                call swipe_pao from _call_swipe_pao
            elif profile == "lily":
                call swipe_lily from _call_swipe_lily
            elif profile == "bianca":
                call swipe_bianca from _call_swipe_bianca

        jump swipe.repeat

    label .reset:
        $ rights = []
        $ swiped = False
        $ direction = "up"
        $ character = ""
        $ characters = ["geo", "pao", "lily", "bianca"]
        $ renpy.random.shuffle(characters)
        $ profile = ""

        return

    label .repeat:
        scene app bg
        call swipe.direction from _call_swipe_direction
        scene app bg textbox with q_fade
        show kulo_slow

        kulo "How was that? Now, let see here..."

        if len(rights) == 0:
            kulo "You liked...no one!"
        else:
            $ rights_extracted = ', '.join(rights).title()
            kulo "You liked: [rights_extracted]"

        hide kulo_slow

        show kulo_mid
        kulo "Are you OK with your swipes?"

        scene app bg textbox with q_fade
        menu:
            "Yup!":
                if len(rights) == 0:
                    jump ending.pass       
                else:
                    jump chat
            "No...":
                show kulo_slow
                kulo "That's alright! Let me get another serving for you..."
                call swipe.reset from _call_swipe_reset
                call tips.reset from _call_tips_reset_2
                call tips.give from _call_tips_give_6
                jump swipe.flow

    label .choice:
        show app textbox
        kulo "So, what do you think?"

        menu:
            "No thanks.":
                $ swiped = True
                $ direction = "left"
            "I like them!":
                $ swiped = True
                $ direction = "right"

                $ rights.append(character)
            "Wait...":
                $ swiped = False
                $ direction = "up"

                kulo "Alright, let me scroll that back up for you."

        return

    label .direction:
        if direction == "left":
            with swipe_left
        elif direction == "right":
            with swipe_right
        elif direction == "up":
            with new_screen

        return
