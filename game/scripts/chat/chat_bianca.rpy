label chat_bianca:
    nvl_narrator "{size=*[scale]}Bianca sent you a message."

    bianca_phone "{size=*[scale]}Hi [name]!"
    bianca_phone "{size=*[scale]}I'm Bianca, we matched just now"

    menu (nvl=True):
        "Test choice 1":
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            nvl_narrator "{size=*[scale]}Choice 2"

    show app_bg_anim
    menu:
        "Test choice 1":
            hide app_bg_anim
            nvl_narrator "{size=*[scale]}Choice 1"
        "Test choice 2":
            hide app_bg_anim
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