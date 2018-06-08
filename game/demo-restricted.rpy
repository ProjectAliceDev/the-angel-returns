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
    a 0bg "I'm sorry if that got a little emotional for you."
    a 0bf "At least you got to see my office, I guess..."
    a 0bo "{i}*Sigh*{/i}"
    a 0bt "Perhaps doing that was a bit of a mistake."
    a "Well, we all can't be winners, can we?"
    a 0bg "I guess its' goodbye, for now."
    a 0bf "I at least enjoyed our date!"
    a "Promise me you'll come back, okay?"
    $ renpy.quit()
    return

## Persistent Looping
# This occurs when the player attempts to play the demo
# again after the game has been played through.
label demo_end_loop:
    stop music fadeout 1.0
    scene bg mojave desktop
    show alice 0bi at t11
    a "I appreciate that you came back for me, but I told you that I have nothing to show."
    a "Please, come back when the game's actually complete."
    $ renpy.quit()
    return
