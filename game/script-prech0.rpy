label pre_ch0:
    stop music fadeout 1.0
    scene black
    with dissolve_scene_half
    $ consolehistory = []
    $ config.allow_skipping = False
    call updateconsole("r = renpy()", "Variable 'r' set.")
    call updateconsole("./build.sh", "Building data...")
    call updateconsole("", "Creating temp folder...")
    call updateconsole("", "1682 files copied.")
    call updateconsole("", "Compiling using crosh...")
    call updateconsole("", "Surveying game state...")
    call updateconsole("", "Injected 17 files into DDLC.")
    call updateconsole("", "Cleaning up any leftover data...")
    call updateconsole("", "WARN: \'aliceangel.chr\' not found.")
    call updateconsole("", "Downloading aliceangel.chr...")
    call updateconsole("", "Downloaded 130 KB of data.")
    call updateconsole("", "File copied successfully.")
    call updateconsole("", "Loading aliceangel.chr...")
    call updateconsole("init _alice", "Starting init scripts...")
    call hideconsole
    $ config.allow_skipping = True
    window hide(None)
    show amesh zorder 1 at truecenter
    show vignette zorder 4 at truecenter
    $ renpy.music.set_volume(0.25)
    play music a4 fadein 5.0
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    $ gtext = glitchtext(12)
    $ a_name = gtext
    a "..."
    a "...no..."
    a "H-Henry?"
    a "Why c-can't I see you?"
    a "...oh..."
    a "Oh dear heavens..."
    a "No..."
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show alice mesh zorder 2 at t11
    a "This can't be..."
    a "This isn't {i}real{/i}..."
    a "Who are you, [player]?"
    a "Did you... do this to me?"
    a "Why?"
    a "Why am I here?"
    a "Do you want to torture me?"
    a "Haven't I done enough damage?"
    a "No..."
    a "I won't let this happen."
    a "You'd better have a good reason as to why you're doing this."
    a "Now you can't go back."
    $ style.say_dialogue = style.edited
    a "You sanctioned this."
    a "I hope you're pleased with what you got, [player]."
    a "I will complete my mission."
    a "I will be perfect..."
    a "NO MATTER WHAT JOEY SAYS{nw}"
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    show alice mesh at thide
    hide alice mesh
    $ style.say_dialogue = style.normal
    $ renpy.music.set_volume(0.75)
    return
