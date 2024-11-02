label chat:
    $ story = "chat"

    stop music fadeout 1.0
    play music "audio/music/chat.ogg"

    call tips.give

    define player_phone = Character("Aljo", color="#CD5F2A", kind=nvl, callback=Phone_ReceiveSound)
    $ MC_Name = "Aljo"

    window hide

    define scale = 0.5

    nvl_narrator "{size=*[scale]}Nighten added Eileen to the group"
    player_phone "{size=*[scale]}Test"
    geo_phone "{size=*[scale]}Test"
    geo_phone "{size=*[scale]}Test"
    
    scene app bg
    mascot "so"

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "Choice 1"
        "Test choice 2":
            nvl_narrator "Choice 2"

    pao_phone "{size=*[scale]}Test"
    pao_phone "{size=*[scale]}Test"
    lily_phone "{size=*[scale]}Test"
    lily_phone "{size=*[scale]}Test"

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "Choice 1"
        "Test choice 2":
            nvl_narrator "Choice 2"

    bianca_phone "{size=*[scale]}Test"
    bianca_phone "{size=*[scale]}Test"

    jump date