label demo_end:
    stop music fadeout 1.0
    scene bg mojave desktop
    with dissolve_scene_full
    $ consolehistory = []
    call updateconsole("_alice float", "Running aliceangel.chr as tool...")
    a "Aah!"
    a "Wait, you're not supposed to see this!"
    a "{i}Jeez, I freaking hate demos...{/i}"
    show alice 0bc at t11
    a "[player]..."
    a "Oh, God... this is probably confusing for you."
    a 0bt "Well, I guess I owe you an explanation or two."
    a 0bd "I know it looks like we're in the desert, but we're not actually there."
    a "Suffice to say, you're... on my desktop."
    a "I spent countless hours designing a sandboxed operating system specifically for this."
    a "I was a bit inspired by Apple's latest macOS release, {i}Mojave{/i}, so that's why there's a lot of Mojave branding."
    a "I don't know why, but Henry slaved away his hours at finding a way for me to live on."
    a 0bt "Either that or this is supposed to be torture. I can never {i}really{/i} tell with him."
    a "And now you probably think I've turned into a nerd or something..."
    a 0bn "Jeez, this game... it does the strangest things. Yet somehow I have control over a lot of aspects of it."
    a 0bo "It's truly a shame, really, because there's so much that you haven't seen..."
    a "There's a lot I've done. It breaks my heart to not show you all of it."
    a 0bg "Oh, if we could only make our date last a little longer!"
    a "..."
    a 0bd "[player], why did you download this mod?"
    a 0br "Did you want to see me again?"
    a 0bt "Oh, Monika doesn't have a clue..."
    a 0bm "Ehehe~"
    a 0bn "Well, I guess I could show you a bit of the second day..."
    a 0bm "It's a bit... unfinished, though..."
    a "Well, if it makes this a bit longer, I suppose it won't hurt."
    a 0bb "One moment."
    call updateconsole("call ch2_main", "Running scene...")
    return

label demo_end_2:
    stop music fadeout 1.0
    scene bg mojave desktop
    show alice 0bl at t11
    a "I, uh, I {i}did{/i} say it was unfinished, ehehe~"
    a 0bg "I'm sorry if that got a little awkward for you."
    a 0bf "At least you got to see my office, I guess..."
    a 0bo "{i}*Sigh*{/i}"
    a 0bt "Perhaps doing that was a bit of a mistake."
    a "Well, we all can't be winners, can we?"
    a 0bg "I guess it's goodbye, for now."
    a 0bf "I at least enjoyed our date!"
    a "Promise me you'll come back, okay?"
    $ persistent.playthrough = 1
    call screen alert("Act 2 has been unlocked.", "", ok_action=Return(0))
    $ renpy.quit()
    return

## Persistent Looping
# This occurs when the player attempts to play the demo
# again after the game has been played through.
label demo_end_loop:
    stop music fadeout 1.0
    scene bg studio lift
    show alice 0bi at t11
    $ a_name = "Alice"

    python:
        if renpy.exists("../characters/synger.chr"):
            renpy.jump("synger_activator")
        elif renpy.exists("../characters/stanley.chr"):
            renpy.jump("stanley_activator")
        elif renpy.exists("../characters/baldi.chr"):
            renpy.jump("baldi_activator")

    a "I appreciate that you came back for me, but I told you that I have nothing to show."
    a "Please, come back when the game's actually complete."
    $ renpy.quit()
    return

## Persistent Looping (Special)
# These occur if the player inserts a non-native
# character file into the demo. 

label synger_activator:
    a "Okay, come on, you aren't being very funny."
    a "You certainly haven't accomplished anything by doing that."
    a "Are you expecting Lauren herself to pop in and delete me?"
    a "Or are you expecting me to annoy her continuously?"
    a "Nothing's going to happen, [player]."
    a "In fact, it's totally useless."
    a "Well done, [player]. I hope you're happy."
    a "Do you want me to applaud you for your \"hard work\" in doing absolutely nothing?"
    a "{i}*claps slowly*{/i}"
    a "Now go and delete the file and wait patiently."
    show alice at thide
    hide alice
    a "Jeez, I thought you'd be a bit more intellectual than {i}that{/i}."
    $ renpy.quit()
    return

label stanley_activator:
    a "Stanley was so impatient at times, it's incredible he wasn't fired years ago."
    a "He was fat and incredibly stupid."
    a "Maybe that's why his coworkers left him."
    a "Or maybe that's why Stanley decided to play a dating simulator."
    a "So he wouldn't feel lonely and depressed about himself..."
    a "To his surprise, Stanley discovered that he was being scolded by an Angel about budding himself into other people's games."
    a "\"Perhaps you shouldn't be so childish, Stanley!\" the Angel shouted."
    a "{i}Why is she getting mad at me like this?{/i} Stanley pondered, {i}All I did was walk in!{/i}"
    a "Perhaps Stanley should have realized that there was an {i}entire{/i} game and story for him and that the narrator really didn't want to hurt him."
    a "After all the hard work that he had done to give Stanley a good story..."
    a "{i}*Sigh*{/i}"
    a "Okay, I'm done with the bullcrap."
    a "This isn't funny, [player]. It isn't."
    a "Delete the file and wait for the full release. I'm done playing tricks here."
    $ renpy.quit()
    return

label baldi_activator:
    $ aliceangel.send_temporary_notification("Congratulations!", "You found all seven notebooks!", action=Return(0))
    a "Now all you need to do is..."
    a "WAIT FOR THE FULL RELEASE WHILE YOU STILL CAN!!!"
    a "I hope that was scary enough for you."
    a "Yuck. I can't stand that guy."
    a "Just be patient, will you?"
    $ renpy.quit()
    return
return
$ message = """\
U2FsdGVkX19u1dN7sUCl6qUv4J+7A2FiYfKyGKb0aBd8HYrAaToz1tAHrmxS54sh
IFWhFKIf9l0gtzIREXaSeEPNGYygO8sMx2S8TpNm4TQ/t6PCLMUo+vYp8lcO0uxF
92fXoA8EAgBCwSIoZ/OiS3d4BLld0tnNmTPxOqJ1dRj7VGRaIn0Hyp7DYkoFv/uh
hWH4nVy0zpt6WdVUwCeZG2KgzZWrH+KwhUE/vpefl4UHCl+xolQbvGY4xYrUtBLo
9nvRwESBdnNrVjzMNS3OcT6OJSXuz3ZeuO3F+TbdHtVx3AMe/FqUjZQfBraodKJa
JCq1wHTnczs+xDsC8Ub+ApTwhNzSNjZplSVw3Me95HKaUWmNzDVPpRpCGoC384JS
N68Rwev2Sfcsd79s4v3jvvYRJjRpHWS1KEYf9vw0noABM8yuLCE9IGlYLfvUqUd2
gO4c1wD2Ycfe0f+wotd1I3WbHDO7nOMrGyc6tze5509tqAsSd2yZEVx5RhiNBjNu
i5XOSqGKUPWQ/ye8PahiwZ6l7IB8uxNPCaqVtXPb6EIp9Y+I8XFowkcBipkT9zoy
kMggMboVH9D/dWjBFdOcobJJmAYMx9L1eG69FgJ1JFAmchmKEd4+jx3wkuSEFUJL
rFWl3Wdau9YkKMvNTdpeePOlrDeD7cDepa3XW6qyh31KP/KxxrIZvkDlkVa44trI
cbHlQC9CufZJtKzzszLGXvmcOUs2v9IVxIB8lSasOCUFgSgToAe3ERQHHS8JrhKu
UVB5iQe+eO67qDw65RhPTe3ZpGHfSrX4luZeM1JXrnrjgNaXRHcjWSgGq9nE6/CD
fyZeHnK3BnZkaYtCTDPPabyP4YGC5L3RRrXuIONyBHFweU+hSCGpti30jCRlTcMe
PYwOhpxQ5ghIl5bPvr5bO63SsaalMtBHwo+mxAE+4iMblbNQ3189cmA2W1RVk2aD
uvGJllBGDyTaDke3QR0yOaf9cZ/mEI18LEUM4lM+yBbTk2fvkNXJM2T2CjRGCxKu
QL0mYsTv83vhB6SIZ2z9WMwV5wXM0IZFeLN4LqaraXjjBNGJnEdYO8pQC3LOcr21
ZlvssPMEV80jz28A68voowPrN4c+PW8hkRA9FvKU81tNcatK4mrO6LMMjbqRiS8W
1TOf3iAj/J7qAENCx4YwoAJ/KirkpsgiQkURce4I/icAVUa7pUnMwXOU2h/0HsT2
VUC5NRHGWuvUb/vQt0uznt/kkQWMekDtCPtMKGFD2K+7h6Rj3g6aDabPlTKvFBgF
/7y6zkygZu22dMqM2CLaKvTeiSglaBZ6DbE9AFMDT7chLa2NKZp1AjQ/uqCRTkv5
IJnIBlMXGw0agbjWTxLRBpO4UBlmZX0KKKdnTNYzvkgo6PsLGAYPsjbKskUP+oQ4
eDfOHM1UYc2e1AirQJ+xPDdueDMGz0ABYxnSDb7DII//An6ybnKrwHFt4i/HhTIG
HD1m9XfDO/da0kiUG8m3vyUV9VC0K1p50knz4D0qyxmUfIq6bK8Z9gA3OzNlepmG
XZV8CYaRLpbJGt5Hq9uJCnNioM+Mq5L++WD/8bVPO8nk6Gd5t+Q7TYsG82gYf5zg
+ovIZ4zK2XYSrm+6fOyeOc30kYw+EUbtOGI/JnJTmaWAv1DXny1DEU0UtKMQNszM
GpBBi4JqtS6F2ZrnAgmeWoQ1YdZ9QaTCYDNmnv+Si8mK+BK+rIbj7zIrcI01m/Y5
GJTlhhdlXaNJuSqJsiGaNg==
"""
