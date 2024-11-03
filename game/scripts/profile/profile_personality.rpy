label profile_personality:
    $ p_section = "personality"

    $ section_correct = False
    while not section_correct:
        
        label .social_skills:
            mascot "How would you rate your social skills?"
            mascot "A: I can handle anything\nB: I just need some prep time\nC: Can't someone else do it?"

            scene app bg textbox
            menu:
                'A':
                    $ p_temp = "Confident"
                'B':
                    $ p_temp = "Just right"
                'C':
                    $ p_temp = "Not good"
                "What was that?":
                    mascot "That's alright. I asked..."
                    jump profile_personality.social_skills

            $ p_social_skills = p_temp

        label .sociable:
            mascot "How do you like to recharge after a long day?"
            mascot "A: Hang out with friends\nB: Do my own thing\nC: A bit of both"

            scene app bg textbox
            menu:
                'A':
                    $ p_temp = "Extrovert"
                'B':
                    $ p_temp = "Introvert"
                'C':
                    $ p_temp = "Ambivert"
                "What was that?":
                    mascot "That's alright. I asked..."
                    jump profile_personality.sociable

            $ p_sociable = p_temp

        label .belief:
            mascot "Do you believe in destiny?"

            scene app bg textbox
            menu:
                'Yes':
                    $ p_temp = "Fate"
                'No':
                    $ p_temp = "Choice"
                'Not exactly':
                    $ p_temp = "Fate & choice"
                "What was that?":
                    mascot "That's alright. I asked..."
                    jump profile_personality.belief

            $ p_belief = p_temp

        label .exercise:
            mascot "Do you exercise?"

            scene app bg textbox
            menu:
                'Yes':
                    $ p_temp = "A lot"
                'No':
                    $ p_temp = "Not much"
                'Not really':
                    $ p_temp = "Sometimes"
                "What was that?":
                    mascot "That's alright. I asked..."
                    jump profile_personality.exercise

            $ p_exercise = p_temp

        call profile.repeat

    return