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
        scene app bg
        show kulo still
        with new_screen

        kulo "Here's what that set of answers will look like on your profile:"

        if p_section == "looking for":
            player "Prefers: [p_gender_preference]\nFriends or Love: [p_relationship_type]\nFuture Priority: [p_future_priority]"
        elif p_section == "basics":
            player "Age: [p_age_range]\nInterests: [p_interests]\nOccupation: [p_occupation]\nEducation: [p_education]"
        elif p_section == "personality":
            player "Social Skills: [p_social_skills]\nSociable: [p_sociable]\nBelief: [p_belief]\nExercise: [p_exercise]"

        kulo "Is that right?"
        
        scene app bg textbox with q_fade
        menu:
            "Yes":
                $ section_correct = True
            "No":
                show kulo_slow with q_fade
                kulo "That's alright. Let's go over that section again."
                $ section_correct = False

        return

    label .check:
        scene app bg
        show kulo_slow
        with new_screen

        kulo "Here's what your profile will look like:"

        hide kulo_slow

        player "Prefers: [p_gender_preference]\nFriends or Love: [p_relationship_type]\nFuture Priority: [p_future_priority]"
        player "Age: [p_age_range]\nInterests: [p_interests]\nOccupation: [p_occupation]\nEducation: [p_education]"
        player "Social Skills: [p_social_skills]\nSociable: [p_sociable]\nBelief: [p_belief]\nExercise: [p_exercise]"
        
        show kulo_slow with q_fade
        kulo "Is that right?"

        scene app bg textbox with q_fade
        menu:
            "Yes":
                pass
            "No":
                show kulo_slow with entrance
                kulo "That's alright. We can start over again..."
                call tips.reset
                jump profile

        return

    label .flow:
        call tips.give

        show kulo still with entrance
        kulo "First, I'll throw you some practice questions, [name]."
        kulo "Just to make sure you get what's going on."
        kulo "First up..."
        call profile_bio

        scene app bg kulo text with q_fade
        kulo "Alright, I think you got that."
        kulo "Now, let's get on with the real questions"
        kulo "This first set will be about what you're looking for."
        call profile_others
        hide kulo_slow

        scene app bg
        show kulo_mid
        with q_fade
        kulo "Let's keep cooking up your profile, [name]."
        kulo "Next, let's go over your basic info."
        call profile_basics
        hide kulo_mid

        scene app bg
        show kulo_fast
        with q_fade
        kulo "Whew, I can feel it. Things are getting spicy now!"
        kulo "Last, tell me more about your personality and attitudes."
        call profile_personality
        hide kulo_fast

        call profile.check

        jump swipe

