label profile_basics:
    $ p_section = "basics"

    $ section_correct = False
    while not section_correct:
        label .age_range:
            kulo "Where does your age fit?"

            scene app bg textbox
            menu:
                "Above 24":
                    $ p_temp = "Above 24"
                "21 to 23":
                    $ p_temp = "21 to 23"
                "Below 21":
                    $ p_temp = "Below 21"
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_basics.age_range

            $ p_age_range = p_temp

        label .interests_1:
            kulo "What are your interests like?"

            scene app bg textbox
            menu:
                "Physical":
                    $ p_temp = "Physical"
                "Social":
                    $ p_temp = "Social"
                "Technical":
                    $ p_temp = "Technical"
                    call profile_basics.interests_2
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_basics.interests_1

            $ p_interests = p_temp

            jump profile_basics.occupation_1

        label .interests_2:
            kulo "Would you rather..."

            scene app bg textbox
            menu:
                "Consume":
                    $ p_interests = "Consume"
                "Make":
                    pass
                "Learn":
                    pass
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_basics.interests_2

            return

        label .occupation_1:
            kulo "Are you employed?"

            scene app bg textbox
            menu:
                "Yes":
                    call profile_basics.occupation_2
                "No":
                    $ p_temp = "None"
                "I'm a student":
                    $ p_temp = "Student"
                "What was that?":
                    kulo "That's alright. I asked..."
                    call profile_basics.occupation_1

            $ p_occupation = p_temp

            jump profile_basics.education_1

        label .occupation_2:
            kulo "What best describes your occupation?"

            scene app bg textbox
            menu:
                "Service":
                    $ p_temp = "Service"
                "Technical":
                    $ p_temp = "Technical"
                "Business":
                    $ p_temp = "Business"
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_basics.occupation_2

            $ p_occupation = p_temp

            return

        label .education_1:
            kulo "Are you in college?"

            scene app bg textbox
            menu:
                "Yes":
                    $ p_education = "In college"
                "No":
                    call profile_basics.education_2
                "What was that?":
                    jump profile_basics.education_1

            jump profile_basics.repeat

        label .education_2:
            kulo "What's your highest level of schooling?"

            scene app bg textbox
            menu:
                "Grade School":
                    $ p_temp = "Finished GS"
                "High School":
                    $ p_temp = "Finished HS"
                "College":
                    $ p_temp = "College Grad."
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_basics.education_2

            $ p_education = p_temp

            return

        label .repeat:
            call profile.repeat

    return