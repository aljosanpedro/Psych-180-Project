label date:
    stop music fadeout 1.0

    label .player:
        label .geo:
            scene house bedroom desk
            player ""
        
            scene house sala couch black
            player ""
        
        label .pao:
            scene house sala couch brown
            player ""
        
            scene house sala table
            player ""
        
        label .lily:
            scene school classroom
            player ""
        
            scene school canteen
            player ""
        
        label .bianca:
            scene house bedroom bed regular
            player ""
        
            scene house bedroom closet
            player ""

    label .char:
        label .geo:
            play music "audio/music/dates/geo.ogg"

            label .station:
                scene bus afternoon at bg_nora_new
                show geo date neutral at char 
                with dissolve
                geo ""

            label .street_enter:
                scene street evening resto at bg_nora_new
                show geo date happy at char
                with dissolve
                geo ""

            label .resto:
                scene resto evening left at bg_senpai
                show geo date neutral at char
                with dissolve
                geo ""

                scene resto evening right at bg_senpai
                show geo date smile at char
                with dissolve
                geo ""

            label .street_exit:
                scene street evening resto at bg_nora_new
                show geo date happy at char
                with dissolve
                geo ""

        label .pao:
            play music "audio/music/dates/pao.ogg"

            label .resto:
                scene resto inside at bg_nora_old
                show pao work shock at char
                with dissolve
                pao ""

            label .street:
                scene street afternoon resto at bg_nora_new
                show pao date happy at char
                with dissolve
                pao ""

            label .cafe:
                scene resto cafe at bg_nora_old
                show pao date neutral at char
                with dissolve
                pao ""

            label .station:
                scene bus evening at bg_nora_new
                show pao date smile at char
                with dissolve
                pao ""

        label .lily:
            play music "audio/music/dates/lily.ogg"

            label .station:
                scene train station at bg_nora_old
                show lily date shock at char
                with dissolve
                lily ""

            label .street:
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

            label school:
                scene school afternoon stairs at bg_nora_new
                show bianca date neutral at char
                with dissolve
                bianca ""

            label shop:
                scene resto cake shop at bg_nora_old
                show bianca date smile at char
                with dissolve
                bianca ""

            label street:
                scene street evening store at bg_nora_new
                show bianca date happy at char
                with dissolve
                bianca ""

            label grocery:
                scene grocery at bg_senpai
                show bianca date neutral at char
                with dissolve
                bianca ""

    jump decide