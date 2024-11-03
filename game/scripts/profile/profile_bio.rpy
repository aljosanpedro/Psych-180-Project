label profile_bio:
    $ p_section = "bio"

    $ section_correct = False
    while not section_correct:
        
        label .self_presentation_1:
            kulo "When talking to someone you'd like to know better, how would you do it?"
            kulo "A: Sell my strengths\nB: Be self-critical\nC: Adjust to them"

            scene app bg textbox
            menu:
                'A':
                    $ p_temp = "Self-promotion"
                'B':
                    $ p_temp = "Self-deprecation"
                'C':
                    $ p_temp = "Ingratiation"
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_presentation_1

            $ p_self_presentation = p_temp

        label .self_presentation_2:
            kulo "How accurate would you make your profile be to your actual self?"
            kulo "A: A perfect reflection\nB: With a few changes\nC: Completely different"

            scene app bg textbox
            menu:
                'A':
                    pass
                'B':
                    pass
                'C':
                    $ p_self_presentation = "Too much"
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_presentation_2

        label .self_conscious_emo_1:
            kulo "How do you feel about other people?"
            kulo "A: I want to help out\nB: I'd rather not bother anyone\nC: They're alright"

            scene app bg textbox
            menu:
                'A':
                    $ p_temp = "Guilt"
                'B':
                    $ p_temp = "Shame"
                'C':
                    jump profile_bio.self_conscious_emo_2   
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_conscious_emo_1

            $ p_self_conscious_emo = p_temp

        label .self_conscious_emo_2:
            kulo "How do you feel about yourself?"
            kulo "A: I'm good enough\nB: I'm the best\nC: I'm not much"

            scene app bg textbox
            menu:
                'A':
                    $ p_temp = "Authentic pride"
                'B':
                    $ p_temp = "Hubristic pride"
                'C':
                    pass
                "What was that?":
                    kulo "That's alright. I asked..."
                    jump profile_bio.self_conscious_emo_2

            $ p_self_conscious_emo = p_temp

        call profile.repeat

    return