label decide:
    $ story = "deciding"

    stop music fadeout 1.0
    play music "audio/music/decide.ogg"

    call tips.give from _call_tips_give_2

    """
    back to chats?
    try to ask someone for another date?
    """

    jump ending