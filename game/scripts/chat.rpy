label chat:
    $ story = "chat"

    label .setup:
        stop music fadeout 1.0
        play music "audio/music/chat.ogg"

        call tips.give

        define sim_temp = 0
        define sim_match = 1
        define sim_geo = 0
        define sim_pao = 0
        define sim_lily = 0
        define sim_bianca = 0

        define matches = []
        define matches_extracted = ""
        define match_1 = ""
        define match_2 = ""
        define match_3 = ""
        define match_4 = ""

        define to_chat = ""

        define player_phone = Character("[name]", color="#CD5F2A", kind=nvl, callback=Phone_ReceiveSound)
        $ MC_Name = "name"
        define scale = 0.5

        jump chat.matches
    
    label .similarity:
        python:
            sim_temp = 0

            if p_self_presentation == c_self_presentation:
                sim_temp += 1
            if p_self_conscious_emo == c_self_conscious_emo:
                sim_temp += 1

            # gender preference doesn't count
            if p_relationship_type == c_relationship_type:
                sim_temp += 1
            if c_distance == "Very Near":
                sim_temp += 1
            elif c_distance == "Far":
                sim_temp -= 1
            if p_future_priority == c_future_priority:
                sim_temp += 1

            if p_age_range == c_age_range:
                sim_temp += 1
            if p_interests == c_interests:
                sim_temp += 1
            if p_occupation == c_occupation:
                sim_temp += 1
            if p_education == c_education:
                sim_temp += 1

            if p_social_skills == c_social_skills:
                sim_temp += 1
            if p_sociable == c_sociable:
                sim_temp += 1
            if p_belief == c_belief:
                sim_temp += 1
            if p_exercise == c_exercise:
                sim_temp += 1

        return

    label .matches:
        if "geo" in rights:
            call swipe_geo.stats
            call chat.similarity
            
            $ sim_geo = sim_temp
            if sim_geo >= sim_match:
                $ matches.append("Geo")
        if "pao" in rights:
            call swipe_pao.stats
            call chat.similarity
            $ sim_pao = sim_temp
            if sim_pao >= sim_match:
                $ matches.append("Pao")
        if "lily" in rights:
            call swipe_lily.stats
            call chat.similarity
            $ sim_lily = sim_temp
            if sim_lily >= sim_match:
                $ matches.append("Lily")
        if "bianca" in rights:
            call swipe_bianca.stats
            call chat.similarity
            $ sim_bianca = sim_temp
            if sim_bianca >= sim_match:
                $ matches.append("Bianca")

    label .choose:
        if len(matches) == 0:
            mascot "It seems you didn't get any matches..."
            jump ending.pass

        $ matches_extracted = ", ".join(matches)
        mascot "You matched with: [matches_extracted]"

        if len(matches) == 1:
            $ to_chat = matches[0]    
        
        if len(matches) > 1:
            mascot "Who from your matches would you like to get to know the most?"

            $ match_1 = matches[0]
            $ match_2 = matches[1]

            if len(matches) > 2:
                $ match_3 = matches[2]
            if len(matches) > 3:
                $ match_4 = matches[3]

            menu:
                "[match_1]":
                    $ to_chat = match_1
                "[match_2]":
                    $ to_chat = match_2
                "[match_3]" if (len(matches) > 2):
                    $ to_chat = match_3
                "[match_4]" if (len(matches) == 4):
                    $ to_chat = match_4

    label .chat:
        window hide
        scene app bg

        if to_chat == "Geo":
            call chat_geo
        elif to_chat == "Pao":
            call chat_pao
        elif to_chat == "Lily":
            call chat_lily
        elif to_chat == "Bianca":
            call chat_bianca

        jump date
