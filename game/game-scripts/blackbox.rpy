init -1000 python:
    blackbox_message = """\
It's time to get your brain working! Each minigame has a unique puzzle. Sometimes, this may require changing the game's settings or selecting the right path.

If you get stuck, don't worry; Alice may say something to you as a hint! Good luck.
    """
    
init -501 screen blackbox_alert:
    modal True
    style_prefix "consent"
    zorder 2000
    add "gui/overlay/confirm.png"


    frame:
        xsize 600
        ysize 592
        style "confirm_frame"
        
        has vbox:
            xalign .5
            yalign .5
            spacing 16
            

        add "mod_assets/images/gui/puzzle.png":
            xalign 0.5
        label _("Puzzle Time"):
            style "consent_title"
            xalign 0.5

        label _(blackbox_message):
            style "consent_message"
            xalign 0.5

        frame:
            xalign 0.5
            xsize 568
            style "consent_button_frame"

            hbox:
                xalign 0.5
                spacing 32

                textbutton _("Get started") action Return(0):
                    style "consent_button"

init python:
    u_did_load = 0.0

label ch0_blackbox_puzzle:
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music t4
    show blight start zorder 2 at t11
    call screen blackbox_alert
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
    a "Why did you {i}save{/i} me?"
    a "{i}Why did you save me?{/i}"
    window hide(config.window_hide_transition)
    $ renpy.jump("ch0_blackbox_puzzle_loop")
    return

label ch0_blackbox_puzzle_loop:
    python:
        import os
        waittime = renpy.random.randint(4, 8)

        default = config.savedir
        renpy.list_saved_games()
        if renpy.can_load("1-3") == True:
            renpy.jump("ch0_blackbox_puzzle_success")

    window show(config.window_show_transition)
    a "{i}Why did you save me?{/i}"
    window hide(config.window_hide_transition)

    $ waittime -= 1
    $ u_did_load += 0.5
    $ pause(5)
    if u_did_load == 50.0:
        jump ch0_blackbox_puzzle_failure
    if waittime > 0:
        jump ch0_blackbox_puzzle_loop
    return

label ch0_blackbox_puzzle_failure:
    $ sweartext = glitchtext(8)
    window show(config.window_show_transition)
    $ style.say_dialogue = style.edited
    a "How can you be this clueless?"
    a "Is this your first time playing a visual novel or something?"
    a "Do you know how to play video games?"
    a "Just save in the third slot of the first page already, damn it!"
    a "It's not that [sweartext] hard!"
    $ style.say_dialogue = style.normal
    jump ch0_blackbox_puzzle_loop
    return

label ch0_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    $ renpyApp.send_temporary_notification("Chapter unlocked", "Good job on solving the puzzle!", action=Return(0))
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    return

label ch1_blackbox_puzzle:
    window hide(None)
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    show blight start zorder 2 at t11
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music b3
    a "Well, at least we met each other."
    a "I'm no longer some obscure mystery to you, ahaha~"
    a "You probably already knew that from the start, didn't you?"
    a "You know, sometimes I wonder I'll take the big screen again..."
    a "{i}...or if I am forever trapped in a darkened window.{/i}"
    window hide(config.window_hide_transition)
    jump ch1_blackbox_puzzle_loop
    return

label ch1_blackbox_puzzle_loop:
    $ waittime = renpy.random.randint(4, 8)
    if preferences.fullscreen == True:
        jump ch1_blackbox_puzzle_success
    else:
        window show(config.window_show_transition)
        a "{i}...or if I am forever trapped in a darkened window.{/i}"
        window hide(config.window_hide_transition)
        $ waittime -= 1
        $ pause(5)
        if waittime > 0:
            jump ch1_blackbox_puzzle_loop
    return

label ch1_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    $ renpyApp.send_temporary_notification("Chapter unlocked", "Good job on solving the puzzle!", action=Return(0))
    a "I don't understand this at all."
    a "I didn't want this."
    a "Why would I want to be in somebody else's universe?"
    a "For what, more control?"
    a "For pure torture because of how imperfect I really am?"
    a "Jeez, he really couldn't think of something more horrifying, could he?"
    a "Well, he's absolutely made a heavenly mistake."
    $ style.say_dialogue = style.edited
    a "Such a shame you have to pay that price."
    $ style.say_dialogue = style.normal
    return
