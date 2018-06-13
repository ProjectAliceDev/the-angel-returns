label pre_ch1:
    stop music fadeout 1.0
    scene black
    with dissolve_scene_half
    show amesh zorder 1 at truecenter
    show vignette zorder 4 at truecenter
    $ renpy.music.set_volume(0.25)
    play music a4 fadein 5.0

    show alice mesh zorder 2 at t11
    $ style.say_dialogue = style.edited
    a "Why do you do this to me?"
    a "Does this entertain you, [player]?"
    a "Do you get a thrill out of this?"
    a "Perhaps there will be some things that I will never understand."
    a "You can't hear them, but I can."
    a "I guess we'll just have to see how this plays out, won't we, [player]?"
    a "Ahaha~"
    $ style.say_dialogue = style.normal
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    $ renpy.music.set_volume(0.75)
    call screen dialog("The script has been modified successfully.", ok_action=Return())
    return
