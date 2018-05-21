init python:
    waittime = renpy.random.randint(4, 8)

label start_blackbox_puzzle:
    window hide(None)
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music b3
    $ consolehistory = []
    call updateconsole("r.file(\"blackbox.chr\")", "Loading blackbox.chr...")
    call updateconsole("box.init(_alice)", "Initialized.")
    window show(None)
    "Welcome to Doki Doki: The Angel Returns."
    "This mod's minigames are slightly different from what you might expect."
    "These games are intended to think about how you use Doki Doki Literature Club! and your computer."
    show blight start zorder 2 at t11
    "This is a light."
    "To advance further in the story, you must activate this light."
    "There are subtle hints in dialogue that may help you, but you may have to do things that you didn't think about before."
    "For now, we will make this easy."
    $ consolehistory = []
    call updateconsole("call _alice", "Loading into scene...")
    $ a_name = "???"
    a "..."
    a "Oh, God..."
    a "How... how did I get here?"
    a "No, I can't be alive..."
    a "You'd better have a damn good reason as to why I'm here, [player]."
    a "You know, sometimes I wonder I'll take the big screen again..."
    a "{i}...or if I am forever trapped in a darkened window.{/i}"
    window hide(config.window_hide_transition)
    jump start_blackbox_puzzle_loop
    return

label start_blackbox_puzzle_loop:
    if preferences.fullscreen == True:
        jump start_blackbox_puzzle_success
    else:
        window show(config.window_show_transition)
        a "{i}...or if I am forever trapped in a darkened window.{/i}"
        window hide(config.window_hide_transition)
        $ waittime -= 1
        $ pause(5)
        if waittime > 0:
            jump start_blackbox_puzzle_loop
    return

label start_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    a "I don't understand this at all..."
    a "I didn't want this..."
    a "I guess it's now time for me to get what was promised."
    $ style.say_dialogue = style.edited
    a "And I won't let you stop me."
    $ style.say_dialogue = style.normal
    return

label ch0_blackbox_puzzle:
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music b3
    show blight start zorder 2 at t11
    a "[player]..."
    a "[player]..."
    a "Why am I here?"
    a "Why are you here?"
    a "Why am I still alive?"
    a "I don't understand, [player]..."
    a "I don't deserve this."
    a "No..."
    a "This can't be..."
    a "Why did you save me?"
    window hide(config.window_hide_transition)
    $ renpy.jump("ch0_blackbox_puzzle_loop")
    return

label ch0_blackbox_puzzle_loop:
    python:
        import os

        default = config.savedir
        renpy.list_saved_games()
        if renpy.can_load("1-3") == True:
            renpy.jump("ch0_blackbox_puzzle_success")

    window show(config.window_show_transition)
    a "{i}Why did you save me?{/i}"
    window hide(config.window_hide_transition)

    $ waittime -= 1
    $ pause(5)
    if waittime > 0:
        jump ch0_blackbox_puzzle_loop
    return

label ch0_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    a "Why?"
    return
