label chat_bianca:
    nvl_narrator "{size=*[scale]}Bianca sent you a message."

    bianca_phone "{size=*[scale]}Hi [name]!"
    bianca_phone "{size=*[scale]}I'm Bianca, we matched just now"

    player_phone "{size=*[scale]}Hi Bianca!"
    player_phone "{size=*[scale]}I found your profile interesting"  

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            nvl_narrator "{size=*[scale]}Choice 2"

    scene app bg
    show kulo_slow
    with q_fade
    menu:
        "Test choice 1":
            hide kulo_slow
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            hide kulo_slow
            nvl_narrator "{size=*[scale]}Choice 2"

    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"
    bianca_phone "{size=*[scale]}Test!"

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            nvl_narrator "{size=*[scale]}Choice 2"

    menu:
        "Test choice 1":
            hide window
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            hide window
            nvl_narrator "{size=*[scale]}Choice 2"

    return