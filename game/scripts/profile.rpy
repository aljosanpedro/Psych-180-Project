label profile:
    $ story = "profile"
    
    label .setup:
        define player_profile = {}

        define section_correct = False
        define section_stats = {}
        define section_stat = {}

        jump profile.part_1

    label .add_stat:
        $ section_stats.update(section_stat)
        $ section_stat = {}

        return

    label .repeat:
        $ section_stats_extracted = ', '.join(section_stats.values())
        mascot "So, you're [section_stats_extracted]..."

        mascot "Correct?"
        menu:
            "Yes":
                $ section_correct = True
                $ player_profile.update(section_stats)
            "No":
                $ section_correct = False

        $ section_stats = {}

        return

    label .part_1:
        call tips.give

        while not section_correct:
            mascot "Part 1"

            mascot "Choice 1"
            menu:
                "Option 1":
                    mascot "Option 1"
                    $ section_stat = {"Choice 1": "Option 1"}
                "Option 2":
                    mascot "Option 2"
                    $ section_stat = {"Choice 1": "Option 2"}
            call profile.add_stat

            mascot "Choice 2"
            menu:
                "Option 1":
                    mascot "Option 1"
                    $ section_stat = {"Choice 2": "Option 1"}
                "Option 2":
                    mascot "Option 2"
                    $ section_stat = {"Choice 2": "Option 2"}
            call profile.add_stat

            call profile.repeat
            
    label .part_2:
        while not section_correct:
            mascot "Part 2"

            mascot "Choice 1"
            menu:
                "Option 1":
                    mascot "Option 1"
                    $ section_stat = {"Choice 1": "Option 1"}
                "Option 2":
                    mascot "Option 2"
                    $ section_stat = {"Choice 1": "Option 2"}
            call profile.add_stat

            mascot "Choice 2"
            menu:
                "Option 1":
                    mascot "Option 1"
                    $ section_stat = {"Choice 1": "Option 1"}
                "Option 2":
                    mascot "Option 2"
                    $ section_stat = {"Choice 1": "Option 2"}
            call profile.add_stat

            call profile.repeat

    jump swipe