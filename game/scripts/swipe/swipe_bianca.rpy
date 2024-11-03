label swipe_bianca:
    label .stats:
        python:
            character = "bianca"

            c_bio = "you deserve good things in life, kaya you deserve me 😉\nchar lang! unless...🫣"
            c_self_presentation = "Too much"
            c_self_conscious_emo = "Authentic pride"

            c_gender_preference = "Men"
            c_relationship_type = "Love"
            c_distance = "Far"
            c_future_priority = "Career"

            c_age_range = "Below 21"
            c_interests = "Consuption"
            c_interests_specific = "Food!"
            c_occupation = "None"
            c_occupation_specific = "Student"
            c_education = "In college"

            c_social_skills = "Just right"
            c_sociable = "Introvert"
            c_belief = "Fate"
            c_exercise = "A lot"

    label .profile:
        $ swiped = False
        while not swiped:
            scene resto cake shop at bg_nora_old
            show bianca date neutral at char
            call swipe.direction
            bianca "[c_bio]"
            show bianca date smile at char
            with dissolve
            bianca "Prefers: [c_gender_preference]\nFriends or Love: [c_relationship_type]\nDistance: [c_distance]\nFuture Priority: [c_future_priority]"

            scene house kitchen at bg_senpai
            show bianca work happy at char
            with scroll_up
            bianca "Age: [c_age_range]\nInterests: [c_interests_specific]\nOccupation: [c_occupation_specific]\nEducation: [c_education]"

            scene house bedroom closet at bg_senpai
            show bianca casual neutral at char
            with scroll_up
            bianca "Social Skills: [c_social_skills]\nSociable: [c_sociable]\nBelief: [c_belief]\nExercise: [c_exercise]"

            call swipe.choice


    return