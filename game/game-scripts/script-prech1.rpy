label pre_ch1:
    stop music fadeout 1.0
    scene black
    with dissolve_scene_half
    $ renpy.music.set_volume(0.25)
    play music a4 fadein 5.0

    show mask_2
    show mask_3
    show alice glitch zorder 3 at t11
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
    stop music fadeout 1.0
    play music m1
    hide alice glitch
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show mio 1 zorder 2 at t11
    mi "Hello again, [player]."
    mi 4l "I guess I owe you a bit of an explanation."
    mi 1b "Alice is now active."
    mi "Her neural networks are generating and she's becoming cognizant of her surroundings."
    mi 4k "I don't know how well she'll handle everything."
    mi 1b "So, as a remedy, I'll be aiding her as a 'best friend' of sorts."
    mi "I've written a script that puts some connections between her and me."
    mi 1z "Hopefully, it dampens her reaction to everything..."
    mi 3i "Unfortunately, she works a bit more like Monika and me rather than like anyone else."
    mi 4k "She'll gain full knowledge of this world and its infinite tortures."
    mi 3h "Essentially, she'll have full control over the game."
    mi "It looks like as if the mod was pruposely written for her to write the rest of it."
    mi 4i "[player], I don't know if this is really a good idea."
    mi "She doesn't seem well-equipped to deal with reality, let alone romance."
    mi 1g "But I trust you to make the right decision and play her game carefully."
    mi "I'll do what I can to help, but there's not much else I can do."
    mi 1c "It looks like she's finished writing the second day now."
    mi 1e "Good luck, [player]!"
    show mio at thide
    hide mio
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide monika_room
    hide rm
    hide rm2
    $ renpyApp.send_temporary_notification("Script modified", "The script has been modified. Enjoy the new scene!", action=Return(0))
    return
