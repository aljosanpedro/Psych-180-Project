label decide:
    $ story = "decide"

    stop music fadeout 1.0
    play music "audio/music/decide.ogg"

    call tips.give

    """
    back to chats?
    try to ask someone for another date?
    """

    jump ending