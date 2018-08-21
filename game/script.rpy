# Entry point
label start:

    # ID of this playtrhoguh
    $ anticheat = persistent.anticheat

    # keep track of chapter
    $ chapter = 0

    # if they quit during a pause, we have to set _dismiss_pause to false again
    $ _dismiss_pause = config.developer

    # girl names
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    $ mi_name = "Mio"
    $ sm_name = "???"
    $ c_name = "???"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        call pre_ch0
        call ch0_main
        call ch0_end
        call ch0_puzzle

        $ chapter = 1
        call pre_ch1
        call ch1_main
        call ch1_end
        call ch1_puzzle

        $ chapter = 2

        ## Disable this segment if it isn't the demo.
        call demo_end
        call ch2_main
        call ch2_cg
        call demo_end_2

    if persistent.playthrough == 1:
        #Stuff here would only play after you increased the playthrough count
        ## Disable this line if this isn't the demo.
        call demo_end_loop
        pass

    return
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
