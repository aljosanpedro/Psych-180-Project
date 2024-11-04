label profile_others:
    $ p_section = "looking for"

    $ section_correct = False
    while not section_correct:
        show app bg
        show kulo_slow 
        with new_screen
        label .gender_preference:
            kulo "Are there any preferences for genders you want to see here?"

            scene app bg textbox with q_fade
            menu:
                'Men':
                    $ p_temp = "Men"
                'Women':
                    $ p_temp = "Women"
                "Any's fine":
                    $ p_temp = "Men & women"
                "What was that?":
                    show kulo_slow with entrance
                    kulo "That's alright. I asked..."
                    jump profile_others.gender_preference

            $ p_gender_preference = p_temp

        show app bg
        show kulo_slow 
        with q_fade
        label .relationship_type:
            kulo "What kind of relationship are you looking for here?"

            scene app bg textbox with q_fade
            menu:
                'Love':
                    $ p_temp = "Love"
                'Friendship':
                    $ p_temp = "Friend"
                'Either':
                    $ p_temp = "Either"
                "What was that?":
                    show kulo_slow with entrance
                    kulo "That's alright. I asked..."
                    jump profile_others.relationship_type

            $ p_relationship_type = p_temp

        show app bg
        show kulo_slow 
        with q_fade
        label .future_priority:
            kulo "What's your main priority for the near future?"

            scene app bg textbox with q_fade
            menu:
                "Family":
                    $ p_temp = "Family"
                "Career":
                    $ p_temp = "Career"
                "Relax":
                    $ p_temp = "Relax"
                "What was that?":
                    show kulo_slow with entrance
                    kulo "That's alright. I asked..."
                    jump profile_others.future_priority

            $ p_future_priority = p_temp

        call profile.repeat from _call_profile_repeat_1

    return