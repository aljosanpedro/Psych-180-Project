label tips:
    label .setup:
        define tips_A = []
        define tips_B = []
        define tips_C = []

        define tip = {}

        define tip_title = ""
        define part_1 = ""
        define part_2 = ""
        define part_3 = ""

        call tips.reset

    label .reset:
        python:
            tips_A = [
                {
                    "title": "Self-Presentation",
                    "part 1": "Biasing the way you present yourself is usually rewarded.",
                    "part 2": "People tend to portray themselves more positively online than in reality.",
                    "part 3": "But try not to do it with people you know like your friends and family.",
                },
                {
                    "title": "Impression Management",
                    "part 1": "Being modest—and even exposing your flaws—could make others like you more.",
                    "part 2": "Agreeing with others' images could also make them agree with yours.",
                    "part 3": "But be careful. Using these strategies too much can lead to negative reactions.",
                },
                {
                    "title": "First Impressions",
                    "part 1": "First impressions are processed quickly but have long-lasting effects.",
                    "part 2": "For some traits like fear, even impressions from little information can be accurate.",
                    "part 3": "Still, impressions are updated with new information relevant the current situation.",
                },
            ]
            tips_B = [
                {
                    "title": "Gender Differences",
                    "part 1": "There are some gender differences when forming a connection with someone.",
                    "part 2": "Women tend to emphasize intimacy by sharing emotions and experiences.",
                    "part 3": "Men tend to prefer activities like playing sports or working on projects.",
                },
                {
                    "title": "Similarity",
                    "part 1": '"Opposites attract", though popular, has weak evidence to support it.',
                    "part 2": "Instead, look to similarities in responses, attitudes, attractiveness…",
                    "part 3": "Even trivial things, like a favorite number, can go a long way!",
                },
                {
                    "title": "Persuasion Success",
                    "part 1": "Trying to get someone to like you can be tough, but there are keys to success.",
                    "part 2": "A good communicators is credible, attractive, and likable.",
                    "part 3": "Good communicators should also NOT come off as trying to persuade you.",
                },
                {
                    "title": "Resisting Persuasion",
                    "part 1": "Don't give in to others' persuasion attempts if you don't want to!",
                    "part 2": "A good way to get out of it is to give the other person direct negative reactions.",
                    "part 3": "Also, stay focused on the conversation and conserve your energy to resist.",
                },
                {
                    "title": "Balance Theory",
                    "part 1": "Liking and agreeing with another person supposedly that leads to positive emotions.",
                    "part 2": "Liking and disagreeing should lead to negative emotions and wanting an agreement.",
                    "part 3": "Disliking and disagreeing is said to just lead to indifference.",
                },
            ]
            tips_C = [
                {
                    "title": "Types of Love",
                    "part 1": "Love is more than just sexual and romantic attraction.",
                    "part 2": "Love can be as a very close friendship with caring, mutual liking, and respect.",
                    "part 3": "One theory suggests that the ideal love has passion, intimacy, and commitment.",
                },
                {
                    "title": "Need for Affiliation",
                    "part 1": "People have a natural motivation to interact with others cooperatively.",
                    "part 2": 'This is called the "need for affiliation" in social psychology.',
                    "part 3": "It seems to be the case even for those who say they don't feel it.",
                },
                {
                    "title": "Physical Attraction",
                    "part 1": 'Love can make you "blind" to seeing that others could be more attractive.',
                    "part 2": "Love can also make us see our love interest as a good person, even when they aren't.",
                    "part 3": 'Historically, "red is sexy" has shown to be true, especially for women.',
                },
                {
                    "title": "Forming Friendships",
                    "part 1": "The way you make strong friendships differs as you age.",
                    "part 2": "As an adult, it's important to take time in different situations with friends.",
                    "part 3": "Also, aim for a friendship where there's mutual support and self-disclosure.",
                },
            ]

            renpy.random.shuffle(tips_A)
            renpy.random.shuffle(tips_B)
            renpy.random.shuffle(tips_C)

            tips = []
            tip = {}

            tip_title = ""
            part_1 = ""
            part_2 = ""
            part_3 = ""

        return

    label .give:
        call tips.pick
        call tips.say

        return

    label .pick:
        if tips_A == [] or tips_B == [] or tips_C == []:
            call tips.reset

        python:
            tip = {}

            if story == "intro" or story == "profile" or story == "swipe":
                tip = renpy.random.choice(tips_A)
                tips_A.remove(tip)
            elif story == "chat" or story == "date":
                tip = renpy.random.choice(tips_B)
                tips_B.remove(tip)
            elif story == "decide" or story == "ending":
                tip = renpy.random.choice(tips_C)
                tips_C.remove(tip)

            tip_title = tip["title"].lower()
            part_1 = tip["part 1"]
            part_2 = tip["part 2"]
            part_3 = tip["part 3"]

        return
    
    label .say:
        scene app bg

        if mascot == blank:
            show blank still
        elif mascot == kulo:
            show kulo still
        elif mascot == kali:
            show kali still
        mascot "Loading...Preparing random tip on [tip_title]..."

        if mascot == blank:
            show blank_slow
        elif mascot == kulo:
            show kulo_slow
        elif mascot == kali:
            show kali_slow
        mascot "[part_1]"
        if mascot == blank:
            hide blank_slow
        elif mascot == kulo:
            hide kulo_slow
        elif mascot == kali:
            hide kali_slow

        if mascot == blank:
            show blank_mid
        elif mascot == kulo:
            show kulo_mid
        elif mascot == kali:
            show kali_mid
        mascot "[part_2]"
        if mascot == blank:
            hide blank_mid
        elif mascot == kulo:
            hide kulo_mid
        elif mascot == kali:
            hide kali_mid

        if mascot == blank:
            show blank_fast
        elif mascot == kulo:
            show kulo_fast
        elif mascot == kali:
            show kali_fast
        mascot "[part_3]"
        if mascot == blank:
            hide blank_fast
        elif mascot == kulo:
            hide kulo_fast
        elif mascot == kali:
            hide kali_fast

        return