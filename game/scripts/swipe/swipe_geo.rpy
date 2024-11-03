label swipe_geo:

    call swipe_geo.stats
    jump swipe_geo.profile

    label .stats:
        python:
            character = "geo"

            c_bio = "hi! i'm a fil-am and can speak some tagalog. i'm here for a much-deserved vacation 😇"
            c_self_presentation = "Self-promotion"
            c_self_conscious_emo = "Hubristic pride"

            c_gender_preference = "Women"
            c_relationship_type = "Either"
            c_distance = "Far"
            c_future_priority = "Relax"

            c_age_range = "Above 24"
            c_interests = "Technical"
            c_interests_specific = "Nerd culture"
            c_occupation = "Technical"
            c_occupation_specific = "Software"
            c_education = "College"

            c_social_skills = "Confident"
            c_sociable = "Ambivert"
            c_belief = "Choices"
            c_exercise = "Not much"

        return

    label .profile:
        $ swiped = False
        while not swiped:
            scene bus morning at bg_nora_new
            show geo casual neutral at char
            call swipe.direction
            geo "[c_bio]"
            show geo casual smile at char
            with dissolve
            geo "Prefers: [c_gender_preference]\nFriends or Love: [c_relationship_type]\nDistance: [c_distance]\nFuture Priority: [c_future_priority]"

            scene school morning stairs at bg_nora_new
            show geo work happy at char
            with scroll_up
            geo "Age: [c_age_range]\nInterests: [c_interests_specific]\nOccupation: [c_occupation_specific]\nEducation: [c_education]"

            scene resto evening center at bg_resto_evening
            show geo date smile at char
            with scroll_up
            geo "Social Skills: [c_social_skills]\nSociable: [c_sociable]\nBelief: [c_belief]\nExercise: [c_exercise]"

            call swipe.choice

    return