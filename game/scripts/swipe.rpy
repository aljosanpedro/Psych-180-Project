label swipe:
    $ story = "swipe"

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

    label .flow:
        call tips.give

        $ renpy.random.shuffle(characters)
        while len(characters) > 0:
            python:
                profile = renpy.random.choice(characters)
                characters.remove(profile)

            if profile == "geo":
                call swipe_geo
            elif profile == "pao":
                call swipe_pao
            elif profile == "lily":
                call swipe_lily
            elif profile == "bianca":
                call swipe_bianca

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
        call swipe.direction
        scene app bg textbox with dissolve

        if len(rights) == 0:
            kulo "You liked...no one!"
        else:
            $ rights_extracted = ', '.join(rights).title()
            kulo "You liked: [rights_extracted]"

        kulo "Are you OK with your swipes?"
        menu:
            "Yup!":
                if len(rights) == 0:
                    jump ending.pass       
                else:
                    jump chat
            "Repeat":
                call swipe.reset
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
