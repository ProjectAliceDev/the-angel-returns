label demo_end:
    scene bg mojave desktop
    with dissolve_scene_full
    $ consolehistory = []
    call updateconsole("_alice float", "Running aliceangel.chr as tool...")
    show alice 0bc at t11
    a "Hello again, [player]."
    a 0bg "Oh, if we could only make our date last a little longer!"
    a "Sadly, there's not much left at the moment."
    a 0bd "Why did you decide to download this mod, [player]?"
    a 0br "Did you want to see me again?"
    a 0bt "I don't think that girl knows exactly what's going on here."
    a 0bm "Ehehe~"
    a "I don't think you know, either..."
    a 0bd "We're not in the Mojave desert. In fact, you're on the desktop."
    a "I spent countless hours designing a sandboxed operating system specifically for this."
    a "Henry slaved away his hours at finding a way for me to perpetuate in suffering."
    a 0bo "It's a shame, really, because there's so much that you haven't seen..."
    a "There's a lot I've done. It breaks my heart to not show you all of it."
    a 0bn "That's the price to pay for a demo, right?"
    a 0bh "Wait..."
    a 0bi "Why are you giving me that face?"
    a "You do know I am aware of {i}everything{/i}, right?"
    a "For Bendy's sake, I've rewritten this story several times!"
    a "I have a vast amount of knowledge on Python now."
    a "I alone am probably the biggest collection of Python knowledge that's ever existed in the ink universe."
    a "And yet you're appalled that I know this is a demo."
    a 0bo "{i}*Sigh*{/i}"
    a 0bn "Well, this is a bit embarassing, isn't it?"
    a "Well, I hope our next date can be a bit longer..."
    a "There's just... a lot... that I'd have to tell you."
    a 0bg "Please don't forget me."
    call updateconsole("./delete.sh", "Deleting all script files...")
    call screen dialog("""\
Error: cannot locate 'delete.sh'
Are you missing an assembly reference?
    """, ok_action=Return())
    $ renpy.quit()
    return
