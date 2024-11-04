label profile_bio:
    $ p_section = "bio"

    $ section_correct = False
    while not section_correct:  # looped for uniformity, but will only run once
        show app bg kulo text with new_screen
        label .self_presentation_1:
            kulo "When talking to someone you'd like to know better, how would you do it?"
            
            scene app bg textbox with q_fade
            menu:
                "Sell my strengths":
                    $ p_temp = "Self-promotion"
                "Self-criticize":
                    $ p_temp = "Self-deprecation"
                "Adjust to them":
                    $ p_temp = "Ingratiation"
                "What was that?":
                    show kulo still with entrance
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_presentation_1

            $ p_self_presentation = p_temp

        show app bg kulo text with q_fade
        label .self_presentation_2:
            kulo "How accurate would you make your profile be to your actual self?"
            
            scene app bg textbox with q_fade
            menu:
                "Like a mirror":
                    pass
                "Close enough":
                    pass
                "Another me":
                    $ p_self_presentation = "Too much"
                "What was that?":
                    show kulo still with entrance
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_presentation_2

        show app bg kulo text with q_fade
        label .self_conscious_emo_1:
            kulo "How do you feel about other people?"

            scene app bg textbox with q_fade
            menu:
                "Where? I'll join!":
                    $ p_temp = "Guilt"
                "Leave me alone":
                    $ p_temp = "Shame"
                "They're alright":
                    show app bg kulo text with q_fade
                    call profile_bio.self_conscious_emo_2 from _call_profile_bio_self_conscious_emo_2   
                "What was that?":
                    show kulo still with entrance
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_conscious_emo_1

            $ p_self_conscious_emo = p_temp
            
            jump profile_bio.end

        label .self_conscious_emo_2:
            kulo "How do you feel about yourself?"

            scene app bg textbox with q_fade
            menu:
                "I'm good enough":
                    $ p_temp = "Authentic pride"
                "I'm the best":
                    $ p_temp = "Hubristic pride"
                "I'm not much":
                    pass
                "What was that?":
                    show kulo still with entrance
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_conscious_emo_2

            $ p_self_conscious_emo = p_temp

            return

        label .end:
            $ section_correct = True
            # call profile.repeat

    return