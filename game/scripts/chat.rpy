label chat:
    stop music fadeout 1.0
    play music "audio/music/chat.ogg"

    $ correct_name = False
    while not correct_name:
        $ name = ""
        while not name:
            $ name = renpy.input("Name:", length=10)
            $ name = name.strip().title()
        kulo "Your name is [name]?"
        menu:
            "Yes":
                $ correct_name = True
            "No":
                $ correct_name = False

    define player_phone = Character("[name]", color="#CD5F2A", kind=nvl, callback=Phone_ReceiveSound)
    $ MC_Name = "[name]"

    window hide

    define scale = 0.5

    nvl_narrator "{size=*[scale]}Nighten added Eileen to the group"
    player_phone "{size=*[scale]}Test"
    geo_phone "{size=*[scale]}Test"
    geo_phone "{size=*[scale]}Test"
    pao_phone "{size=*[scale]}Test"
    pao_phone "{size=*[scale]}Test"
    lily_phone "{size=*[scale]}Test"
    lily_phone "{size=*[scale]}Test"
    bianca_phone "{size=*[scale]}Test"
    bianca_phone "{size=*[scale]}Test"
    
    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "Choice 1"
            pass
        "Test choice 2":
            nvl_narrator "Choice 2"
            pass
        "Test choice 3":
            nvl_narrator "Choice 3"
            pass
        "Test choice 4":
            nvl_narrator "Choice 4"
            pass

    jump date