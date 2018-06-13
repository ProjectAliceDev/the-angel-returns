# This is used for top-level game strucutre.
# Should not include any actual events or scripting; only logic and calling other labels.

label start:

    # Set the ID of this playthrough
    $ anticheat = persistent.anticheat

    # We'll keep track of the chapter we're on for poem response logic and other stuff
    $ chapter = 0

    #If they quit during a pause, we have to set _dismiss_pause to false again (I hate this hack)
    $ _dismiss_pause = config.developer

    # Each of the girls' names before the MC learns their name throughout ch0.
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True

    #This section detemines the "Act Structure" for the game.
    # persistent.playthrough variable marks each of the major game events (Sayori hanging, etc.)
    #Here is an example of how you might do that
    if persistent.playthrough == 0:
        #Call example script
        #call alice_poem_demos
        call setup
        call pre_ch0
        call ch0_main
        call ch0_end
        call ch0_blackbox_puzzle

        $ chapter = 1
        call pre_ch1
        call ch1_main
        call ch1_end
        call ch1_blackbox_puzzle

        ## Extra Content
        # This probably won't be finished, so I am commenting it out.
        $ chapter = 2
        # No script for any prologue; Alice has been already introduced. For now.
        # call ch2_main
        # call ch2_end

        ## Disable this segment if it isn't the demo.
        call demo_end
        call ch2_main
        call demo_end_2

    if persistent.playthrough == 1:
        #Stuff here would only play after you increased the playthrough count

        ## Disable this line if this isn't the demo.
        call screen dialog_alert("Script Change Detected", "It appears the script has been modified. The story may appear differently than expected.", ok_action=Return())
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
