label swipe_lily:
    label .stats:
        python:
            character = "lily"

            c_bio = "my friend made my account...di ko nga alam bat ako nandito hahaha good luck nlng"
            c_self_presentation = "Self_promotion"
            c_self_conscious_emo = "Hubristic pride"

            c_gender_preference = "Men & women"
            c_relationship_type = "Either"
            c_distance = "Near"
            c_future_priority = "Career"

            c_age_range = "21 to 23"
            c_interests = "Physical"
            c_interests_specific = "Running"
            c_occupation = "Business"
            c_occupation_specific = "Big corpo"
            c_education = "In college"

            c_social_skills = "Not good"
            c_sociable = "Ambivert"
            c_belief = "Fate & choice"
            c_exercise = "A lot"

    label .profile:
        $ swiped = False
        while not swiped:
            scene school morning shrine at bg_nora_new
            show lily date smile at char
            call swipe.direction
            lily "[c_bio]"
            show lily date happy at char
            with dissolve
            lily "Prefers: [c_gender_preference]\nFriends or Love: [c_relationship_type]\nDistance: [c_distance]\nFuture Priority: [c_future_priority]"

            scene playground slide at bg_senpai
            show lily casual shock at char
            with scroll_up
            lily "Age: [c_age_range]\nInterests: [c_interests_specific]\nOccupation: [c_occupation_specific]\nEducation: [c_education]"

            scene train inside at bg_nora_old
            show lily work neutral at char
            with scroll_up
            lily "Social Skills: [c_social_skills]\nSociable: [c_sociable]\nBelief: [c_belief]\nExercise: [c_exercise]"

            call swipe.choice

    return