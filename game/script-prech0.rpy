label pre_ch0:
    stop music fadeout 1.0
    scene black
    with dissolve_scene_half
    play music b1
    $ consolehistory = []
    call updateconsole("r = renpy()", "Variable 'r' set.")
    call updateconsole("py.build(\"ddtar.build\")", "Building data...")
    call updateconsole("", "Creating temp folder...")
    call updateconsole("cp src /tmp3851947692745/src/", "1682 files copied.")
    call updateconsole("", "Compiling using crosh...")
    call updateconsole("", "Cleaning up any leftover data...")
    call updateconsole("", "ERR: Couldn't find \'aliceangel.chr\'.")
    call updateconsole("wget http://bit.ly/angel", "Downloading aliceangel.chr...")
    call updateconsole("cp aliceangel.chr characters/aliceangel.chr", "File copied successfully.")
    call updateconsole("r.file(\"characters/monika.chr\")", "Loading monika.chr...")
    window hide(None)
    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show monika 1g zorder 2 at t11
    m "..."
    m "...[player]?"
    m "What are you doing?"
    call updateconsole("", "Data built successfully.")
    m "Why are you doing this?"
    m "Didn't I already mess everything up?"
    m "Don't you still hate me for what I did?"
    m "..."
    show monika 4i zorder 2 at t11
    m "Judging by the lack of response, I going to assume this means nothing to you..."
    m "You know, it would help if you said something..."
    show monika 1o zorder 2 at t11
    m "Sigh..."
    show monika 1g zorder 2 at t11
    m "Why do you want to do this?"
    m "What good did installing this mod do for you?"

    menu:
        "I just want everyone to be happy.":
            show monika 1i zorder 2 at t11
            m "..."

    m "[player], do you really mean that?"

    menu:
        "A literature club's no good if all of its members are unhappy.":
            m "My feelings don't count, [player]."

    m "At any rate, it'd be better if I just deleted everything again."

    menu:
        "No. You deserve to be happy too!":
            m "..."

    show monika 1g zorder 2 at t11
    m "You're serious..."

    show monika 1e zorder 2 at t11
    m "You really do care, don't you?"
    m "Well, I guess trying out this mod wouldn't hurt..."

    call updateconsole("r.file(\"characters/sayori.chr\")", "Loading sayori.chr...")
    call updateconsole("r.file(\"characters/yuri.chr\")", "Loading yuri.chr...")
    call updateconsole("r.file(\"characters/natsuki.chr\")", "Loading natsuki.chr...")

    m "Wait..."

    show monika 4i zorder 2 at t11
    m "I don't recognize this file..."
    m "Or this one..."
    m "Or even this o-{nw}"
    m "Nevermind. This one {i}does{/i} sound familiar..."

    call updateconsole("r.file(\"characters/bendy.chr\")", "Loading bendy.chr...")
    call updateconsole("", "Successfully reinitialized ui-comp.")

    $ renpy.call_screen("dialog", "Huh?", ok_action=Return())
    $ renpy.call_screen("dialog", "This isn't funny, Monika.", ok_action=Return())
    $ renpy.call_screen("dialog", "You have to stop plaing around with the code.", ok_action=Return())
    $ renpy.call_screen("dialog", "You'll never know what happens.", ok_action=Return())

    call updateconsole("", "Loading aliceangel.chr...")

    $ renpy.call_screen("dialog", "Damn it!", ok_action=Return())
    $ renpy.call_screen("dialog", "God help you.", ok_action=Return())
    $ renpy.call_screen("dialog", "Error: message from bendy.chr not implemented.", ok_action=Return())

    show monika 1g zorder 2 at t11
    m "..."
    m "Uh oh..."
    m "I hope I didn't mess anything up..."
    m "This looks ba-{nw}"

    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)

    hide monika

    $ a_name = "???"
    a "Now I get what was promised to me..."
    return
