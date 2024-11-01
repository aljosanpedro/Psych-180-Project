label tips:
    label .setup:
        define tips_original = [
            {
                "title": "Tip 1",
                "part 1": "Tip 1 Part 1",
                "part 2": "Tip 1 Part 2",
                "part 3": "Tip 1 Part 3",
            },
            {
                "title": "Tip 2",
                "part 1": "Tip 2 Part 1",
                "part 2": "Tip 2 Part 2",
                "part 3": "Tip 2 Part 3",
            },
            {
                "title": "Tip 3",
                "part 1": "Tip 3 Part 1",
                "part 2": "Tip 3 Part 2",
                "part 3": "Tip 3 Part 3",
            },
        ]
        define tips = tips_original
        define tip = []

        define part_1 = ""
        define part_2 = ""
        define part_3 = ""

        jump tips.pick

    label .reset:
        python:
            tips_original = [
                {
                    "title": "Tip 1",
                    "part 1": "Tip 1 Part 1",
                    "part 2": "Tip 1 Part 2",
                    "part 3": "Tip 1 Part 3",
                },
                {
                    "title": "Tip 2",
                    "part 1": "Tip 2 Part 1",
                    "part 2": "Tip 2 Part 2",
                    "part 3": "Tip 2 Part 3",
                },
                {
                    "title": "Tip 3",
                    "part 1": "Tip 3 Part 1",
                    "part 2": "Tip 3 Part 2",
                    "part 3": "Tip 3 Part 3",
                },
            ]
            tips = tips_original
            tip = []

            part_1 = ""
            part_2 = ""
            part_3 = ""

        return

    label .pick:
        if tips == []:
            call tips.reset

        python:
            renpy.random.shuffle(tips)
            tip = renpy.random.choice(tips)
            tips.remove(tip)

            part_1 = tip["part 1"]
            part_2 = tip["part 2"]
            part_3 = tip["part 3"]

        call tips.give

        return
    
    label .give:
        if mascot == kulo:
            show kulo_slow
        elif mascot == kali:
            show kali_slow
        mascot "Loading..."
        mascot "[part_1]"
        if mascot == kulo:
            hide kulo_slow
        elif mascot == kali:
            hide kali_slow

        if mascot == kulo:
            show kulo_mid
        elif mascot == kali:
            show kali_mid
        mascot "[part_2]"
        if mascot == kulo:
            hide kulo_mid
        elif mascot == kali:
            hide kali_mid

        if mascot == kulo:
            show kulo_fast
        elif mascot == kali:
            show kali_fast
        mascot "[part_3]"
        if mascot == kulo:
            hide kulo_fast
        elif mascot == kali:
            hide kali_fast

        return