"""
label .flow:
    define rights = []

    call swipe.loop("geo")
    call swipe.loop("pao")
    call swipe.loop("lily")
    call swipe.loop("bianca")

    jump chat

label .loop(character):
    define swiped = False
    define direction = "" 
    while not swiped:
        if character == "geo":
            call swipe.geo
        elif character == "pao":
            call swipe.pao(direction)
        elif character == "lily":
            call swipe.lily(direction)
        elif character == "bianca":
            call swipe.bianca(direction)

        menu:
            "Left":
                $ swiped = True
                $ direction = "left"
            "Right":
                $ rights.append(character)
                $ swiped = True
                $ direction = "right"
            "Go Over Again":
                $ swiped = False
                $ direction = ""
                pass
"""