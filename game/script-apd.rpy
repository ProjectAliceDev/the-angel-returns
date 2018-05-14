label alice_poem_demos:
    image aa = "mod_assets/wtflol.png"
    scene black
    play music t3
    # show yuri 4b zorder 2 at t11
    $ y_name = "Yuri"
    y "Did... did you w-want to read this b-book with me?"

    # scene black
    # show monika 1g zorder 2 at t11
    # $ m_name = "Monika"
    # m "I had to do it. {i}She{/i} made me."

    scene bg club_day
    with wipeleft_scene
    play music t5

    show alice a zorder 2 at f11
    a b "Hi, [player]!"
    a "This is just a developer script to see all of my poems and intricate scenes."
    a g "If you are still seeing this, then the developers probably didn't do a good job of cleaning up the release, ahaha~!"
    show alice a zorder 2 at t11
    a k "I can't wait to show you my poetry, ahaha~!"
    call showpoem (poem_a1)
    a b "And here's the next one..."
    call showpoem (poem_a2)
    a j "This one... I hold it dear to me."

    # Parameters must be exact for intended effect
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_a3, img="alice eyes", track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", where=truecenter)

    a "Do you like it?"
    a "I wrote it for you, my darling!"
    a "And finally..."
    play sound "sfx/glitch2.ogg"
    $ pause(0.2)
    stop sound
    show alice a at i11
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    call showpoem (poem_a4)
    $ style.say_dialogue = style.edited
    a j "Just Alice."
    $ style.say_dialogue = style.normal
    scene white
    with Dissolve(1.0)
    return
