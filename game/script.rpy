# Entry point
label start:
    python:
        anticheat = persistent.anticheat

        chapter = 0

        _dismiss_pause = config.developer

        s_name = "Sayori"
        m_name = "Monika"
        n_name = "Natsuki"
        y_name = "Yuri"
        mi_name = "Mio"
        sm_name = "Sayonika"
        c_name = "Craig"
        a_name = "Alice"

        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = True

    if persistent.playthrough == 0:
        call pre_ch0
        call ch0_main
        call ch0_end
        

        $ chapter = 1
        call pre_ch1
        call ch1_main
        call ch1_end
        call ch0_puzzle

        $ chapter = 2

        ## Disable this segment if it isn't the demo.
        call demo_end
        call ch2_main
        call ch2_cg
        call demo_end_2
        call ch1_puzzle

    if persistent.playthrough == 1:
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
