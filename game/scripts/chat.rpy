label chat:
    $ story = "chatting"

    label .setup:
        stop music fadeout 1.0
        play music "audio/music/chat.ogg"

        call tips.give from _call_tips_give

        define sim_temp = 0
        define sim_match = 3
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
            call swipe_geo.stats from _call_swipe_geo_stats
            call chat.similarity from _call_chat_similarity
            
            $ sim_geo = sim_temp
            if sim_geo >= sim_match:
                $ matches.append("Geo")
        if "pao" in rights:
            call swipe_pao.stats from _call_swipe_pao_stats
            call chat.similarity from _call_chat_similarity_1
            $ sim_pao = sim_temp
            if sim_pao >= sim_match:
                $ matches.append("Pao")
        if "lily" in rights:
            call swipe_lily.stats from _call_swipe_lily_stats
            call chat.similarity from _call_chat_similarity_2
            $ sim_lily = sim_temp
            if sim_lily >= sim_match:
                $ matches.append("Lily")
        if "bianca" in rights:
            call swipe_bianca.stats from _call_swipe_bianca_stats
            call chat.similarity from _call_chat_similarity_3
            $ sim_bianca = sim_temp
            if sim_bianca >= sim_match:
                $ matches.append("Bianca")

    label .choose:
        show kulo_slow with q_fade

        if len(matches) == 0:
            kulo "Sorry, it seems you didn't get any matches..."
            jump ending.pass

        $ matches_extracted = ", ".join(matches)
        kulo "You matched with: [matches_extracted]!"
        kulo "Awesome! Now, let's look at the specifics."

        hide kulo_slow
        show kulo_mid

        if "Geo" in matches:
            kulo "You have [sim_geo] things in common with Geo."
        if "Pao" in matches:
            kulo "You have [sim_pao] things in common with Pao."
        if "Lily" in matches:
            kulo "You have [sim_lily] things in common with Lily."
        if "Bianca" in matches:
            kulo "You have [sim_bianca] things in common with Bianca."

        hide kulo_mid

        # CURRENT END OF GAME
        jump ending.prototype

        if len(matches) == 1:
            $ to_chat = matches[0]    
        
        if len(matches) > 1:
            kulo "Who from your matches would you like to get to know the most?"

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
            call chat_geo from _call_chat_geo
        elif to_chat == "Pao":
            call chat_pao from _call_chat_pao
        elif to_chat == "Lily":
            call chat_lily from _call_chat_lily
        elif to_chat == "Bianca":
            call chat_bianca from _call_chat_bianca

        jump date
