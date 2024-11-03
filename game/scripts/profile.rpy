label profile:
    $ story = "profile"
    
    label .setup:
        define p_temp = ""
        define p_section = ""
        define section_correct = False
        define question_answered = False

        define p_bio = ""
        define p_self_presentation = ""
        define p_self_conscious_emo = ""

        define p_gender_preference = ""
        define p_relationship_type = ""
        define p_distance = ""
        define p_future_priority = ""

        define p_age_range = ""
        define p_interests = ""
        define p_occupation = ""
        define p_education = ""

        define p_social_skills = ""
        define p_sociable = ""
        define p_belief = ""
        define p_exercise = ""

        jump profile.flow

    label .repeat:
        if p_section != "bio":
            mascot "Here's what your choices will look like:"
        if p_section == "others":
            player "Prefers: [p_gender_preference]\nFriends or Love: [p_relationship_type]\nFuture Priority: [p_future_priority]"
        elif p_section == "basics":
            player "Age: [p_age_range]\nInterests: [p_interests]\nOccupation: [p_occupation]\nEducation: [p_education]"
        elif p_section == "personality":
            player "Social Skills: [p_social_skills]\nSociable: [p_sociable]\nBelief: [p_belief]\nExercise: [p_exercise]"

        mascot "Is that right?"
        menu:
            "Yes":
                $ section_correct = True
            "No":
                mascot "That's alright. Let's go over that section again."
                $ section_correct = False

        return

    label .flow:
        call tips.give

        call profile_bio
        call profile_others
        call profile_basics
        call profile_personality

        jump swipe