label demo_end:
    stop music fadeout 1.0
    scene default_background
    with dissolve_scene_full
    $ consolehistory = []
    call updateconsole("_alice float", "Running aliceangel.chr as tool...")
    a "Aah!"
    a "Wait, you're not supposed to see this!"
    a "{i}Jeez, I freaking hate demos...{/i}"
    show alice 0bc at t11
    a "[player]..."
    a "Well, I have some explaining to do."
    a 0bm "Ehehe~"
    a 0bd "Well, I guess there's thing called 'AliceOS'."
    a "I honestly don't know what it really is or what it can do..."
    a "But, what I do know is that I have some form of control over it."
    a "I'm required to have this control over it."
    a "So, uh..."
    a 0bm "I guess it was kind of pointless for it to ask you all those permissions."
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
    scene default_background
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
    window hide(None)
    show black
    pause 0.2
    call rsod_missing_act
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
