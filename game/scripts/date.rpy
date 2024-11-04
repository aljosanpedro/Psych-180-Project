label date:
    $ story = "date"

    stop music fadeout 1.0
    # TODO: date music

    call tips.give from _call_tips_give_1

    label .player:
        label .boy_1:
            scene house bedroom desk at bg_nora_old
            player ""
        
            scene house sala couch black at bg_senpai
            player ""
        
        label .boy_2:
            scene house sala couch brown at bg_senpai
            player ""
        
            scene house sala table at bg_senpai
            player ""
        
        label .girl_1:
            scene school classroom at bg_nora_old
            player ""
        
            scene school canteen at bg_nora_old
            player ""
        
        label .girl_2:
            scene house bedroom bed regular at bg_senpai
            player ""
        
            scene house bedroom closet at bg_senpai
            player ""

    label .char:
        label .geo:
            play music "audio/music/dates/geo.ogg"

            label .bus_station_afternoon:
                scene bus afternoon at bg_nora_new
                show geo date neutral at char 
                with dissolve
                geo ""

            label .street_evening_resto_enter:
                scene street evening resto at bg_nora_new
                show geo date happy at char
                with dissolve
                geo ""

            label .resto_evening:
                scene resto evening left at bg_resto_evening
                show geo date neutral at char
                with dissolve
                geo ""

                scene resto evening right at bg_resto_evening
                show geo date smile at char
                with dissolve
                geo ""

            label .street_evening_resto_exit:
                scene street evening resto at bg_nora_new
                show geo date happy at char
                with dissolve
                geo ""

        label .pao:
            play music "audio/music/dates/pao.ogg"

            label .resto_inside:
                scene resto inside at bg_nora_old
                show pao work shock at char
                with dissolve
                pao ""

            label .street_afternoon_resto:
                scene street afternoon resto at bg_nora_new
                show pao date happy at char
                with dissolve
                pao ""

            label .resto_cafe:
                scene resto cafe at bg_resto_cafe
                show pao date neutral at char
                with dissolve
                pao ""

            label .bus_station_evening:
                scene bus evening at bg_nora_new
                show pao date smile at char
                with dissolve
                pao ""

        label .lily:
            play music "audio/music/dates/lily.ogg"

            label .train_station:
                scene train station at bg_nora_old
                show lily date shock at char
                with dissolve
                lily ""

            label .street_morning_resto:
                scene street morning resto at bg_nora_new
                show lily date neutral at char
                with dissolve
                lily ""

            label .playground:
                scene playground slide at bg_senpai
                show lily date smile at char
                with dissolve
                lily ""

                scene playground tunnel at bg_senpai
                show lily date happy at char
                with dissolve
                lily ""
            
        label .bianca:
            play music "audio/music/dates/bianca.ogg"

            label .school:
                scene school afternoon stairs at bg_nora_new
                show bianca date neutral at char
                with dissolve
                bianca ""

            label .shop:
                scene resto cake shop at bg_nora_old
                show bianca date smile at char
                with dissolve
                bianca ""

            label .street_evening_store:
                scene street evening store at bg_nora_new
                show bianca date happy at char
                with dissolve
                bianca ""

            label .grocery:
                scene grocery at bg_senpai
                show bianca date neutral at char
                with dissolve
                bianca ""

    jump decide