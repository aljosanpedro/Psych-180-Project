label intro:
    $ story = "welcome" #  used for tips
    
    label .welcome:
        stop music fadeout 1.0
        play music "audio/music/profile.ogg"

        call tips.give

        show kulo still
        with entrance
        kulo "Welcome to Simmer!"
        kulo "I'm Kulo, ang kumukulong kaldero!"
        kulo "Simmer is a dating app simulator."
        kulo "Yes, I acknowledge that I'm in a simulation. Scary, I know."
        kulo "What Simmer does differently is add elements of social psychology"
        kulo "to the process of dating via dating apps."
        kulo "In this prototype version, I'll be walking you through a few steps."

        show kulo_slow
        kulo "First, we'll make your profile."
        kulo "I'll be asking you a bunch of questions."
        kulo "Some of it is the usual stuff we know and love."
        kulo "While the rest are based on social psychology concepts."
        kulo "In particular: the self, social perception, and attraction."
        hide kulo_slow

        show kulo_mid
        kulo "Next, you'll be swiping others' profiles."
        kulo "Since there's a limited user base at the moment"
        kulo "I'll be showing you all the profiles we have, regardless of gender."
        kulo "Don't worry, there'll no mis-swiping from mixing lefts and rights."
        kulo "Just tell me what you think, and I'll remember it for you."
        kulo "These profiles will also be based on the things I asked you."
        kulo "The other Kulos in the other Simmers asked them the same things."
        kulo "Again, scary for me, I know. I'm used to it now though..."
        hide kulo_mid

        show kulo_fast
        kulo "Woo, I'm getting excited for this last part. Turn up the heat!"
        kulo "The last thing I'll be guiding your through today is matching."
        kulo "Here on Simmer, we do the matching for you."
        kulo "We base our matches on how similar two profiles are."
        hide kulo_fast

        show kulo_slow
        kulo "In the future, there will be features to chat and meet with matches."
        kulo "I heard the developer's also preparing another mascot, and she's a girl!"
        hide kulo_slow
        show kulo_fast
        kulo "Ooh, I wonder what she's like. Maybe she's in the market for another pot..."
        hide kulo_fast
        show kulo_slow
        kulo "Ahem, anyway..."
        kulo "We do all the math and logic in the background and {i}voila{/i}!"
        kulo "The matches are ready to serve, {i}bon appetit{/i}"
        kulo "Careful though, they're sizzling hot!"
        hide kulo_slow

        show kulo_fast
        kulo "Oh, and as you noticed at the start there, we have random tips for you."
        kulo "These are based on psychological concepts relevant to the current section."
        kulo "So, they switch up depending on if you're swiping, chatting, etc."
        hide kulo_fast

        show kulo_mid
        kulo "Ah! How rude of me."
        kulo "I've been simmering with excitement and going on and on..."
        kulo "I don't even know who you are!"

    label .name:
        kulo "So, what's your name?"

        scene app bg textbox 
        with Dissolve(0.1)
        $ name = ""
        while not name:
            $ name = renpy.input("Name:", length=10)
            $ name = name.strip().title()

        show kulo_mid
        kulo "Your name is [name]?"

        scene app bg textbox with q_fade
        menu:
            "Yes":
                pass
            "No":
                show kulo still
                kulo "It's not? I see..."
                
                jump intro.name
            "Wait, what?":
                show kulo still
                kulo "That's alright. Let me repeat that..."

                jump intro.name

        show kulo_fast
        kulo "Hello, [name]! Again, I'm Kulo, your kaldero on-demand."
        kulo "Now, let's see what kind of profile we can stir up!"
        hide kulo_fast

    jump profile

