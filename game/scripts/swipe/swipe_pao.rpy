label swipe_pao:
    label .stats:
        python:
            character = "geo"

            c_bio = "sabi ng mga tropa ko subukan ko daw 'to. eh wala naman sigurong mawala, kaya ayon."
            c_self_presentation = "Ingratiation"
            c_self_conscious_emo = "Guilt"

            c_gender_preference = "Women"
            c_relationship_type = "Love"
            c_distance = "Very near"
            c_future_priority = "Family"

            c_age_range = "21 to 23"
            c_interests = "Social"
            c_interests_specific = "Games!"
            c_occupation = "Service"
            c_occupation_specific = "Waiter"
            c_education = "Finished HS"

            c_social_skills = "Just right"
            c_sociable = "Extrovert"
            c_belief = "Fate & choice"
            c_exercise = "Sometimes"

    label .profile:
        $ swiped = False
        while not swiped:
            scene street afternoon store at bg_nora_new
            show pao date neutral at char
            call swipe.direction
            pao "[c_bio]"
            show pao date smile at char
            with dissolve
            pao "Prefers: [c_gender_preference]\nFriends or Love: [c_relationship_type]\nDistance: [c_distance]\nFuture Priority: [c_future_priority]"

            scene resto inside at bg_nora_old
            show pao work happy at char
            with scroll_up
            pao "Age: [c_age_range]\nInterests: [c_interests_specific]\nOccupation: [c_occupation_specific]\nEducation: [c_education]"

            scene house sala table at bg_senpai
            show pao casual neutral at char
            with scroll_up
            pao "Social Skills: [c_social_skills]\nSociable: [c_sociable]\nBelief: [c_belief]\nExercise: [c_exercise]"

            call swipe.choice

    return