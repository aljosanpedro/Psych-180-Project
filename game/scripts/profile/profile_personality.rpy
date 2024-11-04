label profile_personality:
    $ p_section = "personality"

    $ section_correct = False
    while not section_correct:
        show app bg
        show kulo_fast
        with new_screen
        label .social_skills:
            kulo "How would you rate your social skills?"
            
            scene app bg textbox with q_fade
            menu:
                "I can handle it!":
                    $ p_temp = "Confident"
                "Give me some time":
                    $ p_temp = "Just right"
                "Why me?":
                    $ p_temp = "Not good"
                "What was that?":
                    show kulo_mid with entrance
                    kulo "That's alright. I asked..."
                    jump profile_personality.social_skills

            $ p_social_skills = p_temp

        show app bg
        show kulo_fast
        with q_fade
        label .sociable:
            kulo "How do you like to recharge after a long day?"

            scene app bg textbox with q_fade
            menu:
                "Friendship time":
                    $ p_temp = "Extrovert"
                "Do my own thing":
                    $ p_temp = "Introvert"
                "A bit of both":
                    $ p_temp = "Ambivert"
                "What was that?":
                    show kulo_mid with entrance
                    kulo "That's alright. I asked..."
                    jump profile_personality.sociable

            $ p_sociable = p_temp

        show app bg
        show kulo_fast
        with q_fade
        label .belief:
            kulo "Do you believe in destiny?"

            scene app bg textbox with q_fade
            menu:
                "Totally":
                    $ p_temp = "Fate"
                "Not at all":
                    $ p_temp = "Choice"
                'Not exactly...':
                    $ p_temp = "Fate & choice"
                "What was that?":
                    show kulo_mid with entrance
                    kulo "That's alright. I asked..."
                    jump profile_personality.belief

            $ p_belief = p_temp

        show app bg
        show kulo_fast
        with q_fade
        label .exercise:
            kulo "Do you exercise?"

            scene app bg textbox with q_fade
            menu:
                "A lot":
                    $ p_temp = "A lot"
                "Not much":
                    $ p_temp = "Not much"
                "Sometimes":
                    $ p_temp = "Sometimes"
                "What was that?":
                    show kulo_mid with entrance
                    kulo "That's alright. I asked..."
                    jump profile_personality.exercise

            $ p_exercise = p_temp

        call profile.repeat from _call_profile_repeat_2

    return