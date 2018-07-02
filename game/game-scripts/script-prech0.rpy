label pre_ch0:
    $ config.allow_skipping = False
    scene black
    with dissolve_scene_half
    play music m1
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    $ consolehistory = []
    call updateconsole("", """\
DDLC RenPy Console for AliceOS
(C) 2017-2018 | Team Salvato.
All rights reserved.

Ready.
        """)
    show mio 1e at t11
    mi "Hi, thank you for playing Doki Doki Literature Club for AliceOS!"
    mi "I'm Mio, your administrative assistant."
    mi "I'll help you set up DDLC so you can get started!"
    mi 3b "There's a few things we need to take care of first, though..."
    mi "This is a sandboxed applet, but we need permission to do a few things."
    mi "It's mostly stuff like send notifications and file management."
    mi "Of course, this is at your own discretion."
    mi "Would you please help me and the team out here?"
    python:
        renpyApp.ask_app_permissions()
        renpyApp.send_temporary_notification("You're all set!", "You'll receive notifications in DDLC. Nice!", action=Return(0))
    mi "Alright, it looks like we are set."
    mi "No we can sta{nw}"
    mi 1c "Wait."
    mi "..."
    mi "[player]?"
    mi "Have you played Doki Doki already?"
    mi 1h "Why did you come back here?"
    mi "Was there something you think you..."
    mi 1c "... oh."
    mi 3d "I see."
    mi "You're not here to play the regular Doki Doki, are you?"
    mi "No, it looks like you have some mod."
    mi 4l "Ehehe, I should have known."
    mi "Well, I guess I could help you a little in setting everything up."
    mi 1b "It is my job, after all."
    mi "Let's see what we have here..."

    call updateconsole("r = renpy()", "Variable 'r' set.")
    $ consolehistory = []

    mi 1c "Eh?"
    mi "Gimme a sec."

    call updateconsole("ddlc-ls --diff", """\
New files located.
WARN: build.sh detected. This mod 
MUST be built before use.
    """)

    mi "These files are a bit unusual for a mod."
    mi "[player], what are you doing, exactly?"
    mi "Something doesn't seem right here."
    mi "You shouldn't have to {i}build{/i} the mod to play it, even if you're a developer."
    mi "I'll inspect this for just a second."
    window hide(None)
    $ renpy.pause(3.0)
    window show(None)
    mi "[player], this mod looks a bit dangerous."
    mi "I don't know what you think you're going to accomplish, but it may be detrimental."
    mi "I just looked through the entire script."
    mi 4n "Please tell me you don't actually plan to put{w=1.0} {i}her{/i}{w=1.0} in here, do you?"
    mi 3k "I'd hate to be punny, but she really is quite a gal."
    mi "Who knows what she'd do here?"
    mi "Oh gosh, [player]..."
    mi 1h "Why do you want to do this?"
    mi "There's only so many reasons I can think of..."
    mi 1k "But I still can't quite put my finger on it..."
    mi "Tell me, [player]..."

    show mio 3h at t11
    mi "Do you love her? Be honest with me."

    # Where's the pride when you needed it?
    # Do you really want to follow the trail of the damned?

    menu:
        "Yes...":
            mi 8q "My god! [player], that's disturbing!"
            mi "Are you insane?"
            mi 8u "{i}*Yuck!*{/i}"
            mi 8q "I can't believe you!"
            mi "I know this is a dating simulator and all, but..."
            mi "Jesus christ!"
            mi "There must be something wrong with you!"
            mi 6t "It'd be a miracle if she didn't kill you first!"
            mi 3v "God..."
            mi "I know I'm supposed to be proper and all, but..."
            mi 3r "That's probably the most horrifying thing I've heard all day."
            mi 1z "{i}*Sigh*{/i}"
        "Hell no!":
            mi 1c "Well, that's not what I expected."
            mi "In fact, that might be a bit better."
            mi "So, why would you decide to bring her back?"
            mi "Are you looking for something?"
            mi "Answers? A secret?"
            mi 1z "Perhaps I will never really know."
    
    window hide(None)
    $ renpy.pause(3.0)
    window show(None)
    mi 1c "Well, I can't go against your decision."
    mi "I'll run the script for you."
    mi "It'll build the game scripts and stuff needed to put her in."
    mi 7g "I hope this makes you happy."
    call updateconsole("./build.sh", "Building data...")
    
    $ consolehistory = []
    call updateconsole("", "Creating temp folder...")
    call updateconsole("", "1682 files copied.")
    call updateconsole("", "Compiling using crosh...")
    call updateconsole("", "Surveying game state...")
    call updateconsole("", "Injected files into DDLC.")
    call updateconsole("", "Cleaning up any leftover data...")
    python:
        if renpy.exists("../characters/aliceangel.chr"):
            renpy.jump("pre_ch0_result")
        else:
            renpy.jump('pre_ch0_err')
    return

label pre_ch0_err:
    call updateconsole("", "WARN: \'aliceangel.chr\' not found.")
    call updateconsole("", "Downloading aliceangel.chr...")
    call updateconsole("", "Downloaded 130 KB of data.")
    python:
        open(config.basedir + "/characters/aliceangel.chr", "w").write("""\
01010011 01010111 01110100 01101111 01100100 01000101 01111000 01110000 01010001 01101011 00111001 01101001 01001101 00110010 01001110 01101110 01011010 01000100 01001010 01010110 01011010 00110001 01101011 01111001 01001111 01011000 01010010 01100001 01010101 00110000 01001001 01110111 01011001 01101110 01101100 01000011 01001101 01000111 01000110 01001000 01010110 01010111 01100100 01101010 01010111 01000110 01011010 01110011 01011001 01111010 01001110 01010011 01100011 01000111 01001001 01111001 01001110 01001000 01010110 01001101 01100001 01010100 01010010 01101110 01010101 01101011 01100011 00110100 01011010 00110001 01001110 01010100 01010001 01101110 01001010 01101000 01010110 00110011 01101000 01111010 01010011 01010101 01101000 01110011 01100100 01101101 01010010 01010101 01001111 01000111 01100100 01001101 01100001 01010100 01010010 00110001 01010101 01101011 01100011 00110100 01011010 00110001 01001110 01010100 01010001 01101010 01000010 01100001 01010110 00110000 01011010 00110101 01010011 01010101 01101000 01110011 01100100 01101101 01010010 01010100 01010001 01101101 01101000 01101010 01010010 00110000 01011010 00110101 01011010 01000101 01001110 01000011 01001101 01000111 01001010 00110101 01010001 01101110 01010010 01101100 01010101 00110000 01001010 01110110 01010111 01101100 01100100 01000111 01100101 01010111 01010010 01000100 01011010 01001000 01110000 01001010 01010010 00110001 01001010 01110011 01011001 01101011 01100100 01110011 01100010 01101101 01000110 01001001 01010101 01010011 00111001 01001010 01010010 01101100 01001010 01110110 01010111 01101100 01001110 01000011 01100001 01101101 01000110 01001000 01001111 01011000 01000010 01011010 01001101 01101100 01011010 00110110 01010011 01010101 01100011 00110101 01100010 01010101 01101100 01001001 01010101 01101101 00111001 01100001 01010101 00110000 01001010 01110000 01010111 01101100 01100100 01000111 01001101 01010111 01010010 01001000 01100010 01000111 00110001 01101011 01010110 00110011 01100100 01101110 01010111 01010110 01101000 01001011 01100010 01000101 01101100 01001001 01010110 01101110 01010110 01011010 01100010 01010110 01011010 01101111 01011001 00110010 00110001 01000111 01100001 01010111 01001010 01001000 01010110 01011000 01010110 01001010 01010010 01010111 01101000 00110010 01011010 01001000 01101100 01101011 01100101 01101011 01101100 01001000 01010010 01010111 01100100 01100001 01001101 01101101 01111000 00110101 01011001 01101011 01001110 01000011 01001101 01000111 01001010 00110101 01010001 01101101 01110000 01101000 01010010 01111010 01101100 00110010 01011001 01111010 01001010 01010110 01001100 00110000 01101100 01000111 01010101 01101101 01101000 01101000 01001101 01101100 01010110 01101110 01011010 01000101 01100100 01101111 01100011 01000111 01001110 00110101 01010001 01101110 01001110 01101000 01010111 01000110 01001001 01110111 01011001 01101011 01100100 01010110 01011010 00110001 01110000 01110101 01010011 01101101 01111000 01011010 01010110 00110011 01001110 01101110 01010111 01101101 00110000 00110101 01100101 01010101 01101100 01001000 01100010 01001000 01010110 01101010 01001101 00110001 01001010 01101111 01011001 01101101 00110001 01001111 01100010 01000101 01101100 01010100 01010001 01101011 01101100 01100001 01010101 00110000 01001010 01110001 01011001 00110010 00110001 01000111 01001101 00110010 01001010 01001000 01010110 01101101 01110100 01001010 01010010 00110010 01111000 00110001 01010011 01010101 01100100 01101111 01100010 01000111 01001110 01110100 01010110 01011000 01010110 01001101 01100001 01010100 01010010 01101110 01010110 01101011 01101000 01001011 01100001 01000111 01000110 01011000 01100101 01001000 01000010 01101001 01100010 01010111 01001110 01101110 01011001 01010101 01100100 01110011 01100101 01101011 01101100 01001001 01010101 01101101 01101000 01101000 01010110 01111010 01010101 01110111 01010111 01101100 01100100 01010010 01011010 00110010 01000110 01011000 01001110 01011000 01001010 01001010 01010011 01000110 01001010 00110010 01010011 01010101 01100011 01111000 01001110 01010101 01101100 01001000 01010101 01101110 01011010 01101001 01001101 00110000 01101100 01101111 01010011 01010101 01010110 01110011 01001101 01000101 01101100 01001000 01010100 01101110 01011010 01101011 01010110 00110011 01101000 01110010 01010011 01010101 01100100 01101111 01100001 01000111 01010010 01110100 01010110 01010111 01100100 01101011 01010010 01111010 01101011 01111000 01010111 01010100 01001010 01101111 01100010 01000110 01110000 01000100 01010001 01101110 01010010 01100001 01010101 00110000 01010110 01101110 01010101 00110001 01101000 01010010 01011010 00110001 01101011 01111001 01001111 01010100 01000110 01101001 01010010 00110001 01000110 01101110 01011001 01010101 01100100 01000111 01001101 01101100 01110000 01010100 01010001 01101110 01100100 01101011 01010110 00110011 01101000 01111010 01010111 01101100 01100100 01010010 01011010 00110010 01001010 01011000 01010110 01010111 01100100 01011010 01100010 01010101 01011010 01110001 01011001 01011000 01101100 01000110 01100001 01000101 01101100 01000110 01010101 01101110 01011010 01001010 01010011 01000111 01111000 00110010 01011010 01000110 01001110 01000011 01100011 01101101 01001010 01110100 01001111 01010100 01001110 01001010 01010011 01000111 01010010 01110110 01010111 01010110 01101000 01010010 01011010 00110010 01000110 01011001 01010101 01010111 00110101 01101010 01100101 01010101 01001010 01111010 01011001 01010110 01100100 00110000 01100010 01000110 01000010 00110101 01010001 01101011 00110001 01101000 01010111 01000110 01110000 01110111 01011001 01101101 00110001 01101010 01011010 00110010 01000110 01011000 01001110 01000111 01100100 01101011 01010010 00110010 01101000 01110011 01010011 01010101 01100100 01010011 01100001 01000111 01001110 01110100 01100011 00110010 01100100 01101010 01010011 01000110 01011010 01110010 01010111 01101011 01100100 00110100 01100010 01000111 01001110 00110110 01001111 01000111 01100100 01010100 01010111 01000110 01000110 01110101 01011001 00110011 01101100 01000011 01100001 01000101 01101100 01001000 01010011 01101010 01000110 01101100 01100010 01101110 01000010 01110111 01011001 01101101 00110001 01101010 01100011 00110000 01101100 01001001 01010100 01101101 01110000 01101010 01100010 01010110 01011010 01101111 01011001 01101100 01100100 01110011 01100100 01010110 01110000 00110101 01010001 01101010 01001110 01100001 01010110 00110011 01101000 01111010 01010011 01010101 01100011 00110101 01100010 01010101 01101100 01001001 01010111 01101110 01011010 01101000 01010110 00110000 00110101 01110011 01011001 00110011 01101100 01000110 01011010 00110001 01000110 01110100 01100010 01000100 01000010 01101010 01100101 01010101 01001010 00110010 01010111 01101101 01101100 01000011 01001110 01010111 01001001 01111010 01010110 01101110 01101100 01001010 01010010 01111010 01000110 01110111 01011001 01101101 00110001 01010010 01100011 00110000 01101100 01001001 01010100 01101010 01001110 01101000 01010110 01111010 01000110 00110000 01011001 01010110 01100011 00110001 01100010 01101011 01111000 01110000 01001110 01001000 01010110 01001010 01010010 00110011 01101000 01110111 01011001 01010100 01001010 01010110 01100100 01010101 01111000 01110000 01001110 01000111 01100100 01101001 01010010 00110010 01111000 01111001 01010111 01101100 01001110 01000011 01100010 01010111 01000110 01011001 01010100 01101101 00111001 01001010 01010010 00110010 01111000 00110001 01010011 01010101 01100100 01000110 01011010 00110001 01101100 01110100 01001111 01010100 01001110 01101001 01010001 00110000 01010110 01101110 01010110 01101011 01100100 01101111 01100010 01000101 01101100 01001000 01010111 01101110 01000010 01101010 01100010 01101011 00110100 01110111 01010011 01010101 01101000 01010011 01100011 01000111 01001010 01011000 01010110 01010111 01100100 01010100 01010101 00110000 01001001 01111010 01010111 01010110 01101000 01001110 01011010 00110001 01101100 01110100 01001111 01011000 01101100 01101001 01100001 01010101 01001010 01110100 01011001 00110010 00110000 00110101 01100100 01000101 01101100 01001000 01100010 01000100 01000010 01101010 01100101 01010111 01001110 01101110 01011001 01010110 01100011 00110001 01100011 01101101 01010110 01010100 01010001 01101010 01001110 01101001 01001101 01101010 01000110 01110000 01010100 01000101 01001110 01000011 01010011 01101011 01101100 01001001 01011010 01000111 01101000 01101010 01100101 01010101 01001010 01101111 01010011 01010101 01101000 01101011 01100101 01010111 01000110 01011000 01011010 01000111 00110101 01101001 01010010 00110010 01111000 00110001 01010111 01101110 01101100 00110011 01011010 00110010 01001110 01001001 01010110 01101110 01110000 01101010 01001101 01101101 01111000 00110001 01010111 01101110 01101100 00110011 01011010 00110010 01001101 01111001 01100001 01000111 01101000 01101010 01010010 00110001 01011010 01111010 01010111 01101100 01101000 01001111 01100101 01101011 01101100 01001001 01010100 01101110 01001110 01101011 01010110 00110010 01001110 00110001 01010011 01010101 01011010 01010011 01100010 00110001 01110000 01010100 01010001 01101110 01110000 01100001 01010110 00110000 00110101 00110010 01011001 01101101 00110001 01010010 01011010 00110010 01010010 01001000 01100010 01001000 01010010 01100001 01010101 01111010 01010010 00110001 01010100 01000111 01101100 01000011 01001101 00110001 01110000 01011000 01100101 01001000 01001110 01001101 01100001 01010100 01010010 00110001 01010011 01010101 01010110 01110011 01001101 01000101 01101100 01001000 01001101 01010111 01101000 01100001 01010010 00110001 01010110 01101110 01011001 01101100 01100100 01010110 01011010 00110001 01101100 01011000 01001110 01000111 01100100 01011010 01010110 01111010 01010110 01110101 01010111 01101100 01100100 00110011 01100001 01000101 01101100 01000110 01100001 00110010 01100100 01101011 01001101 01101101 01111000 01111010 01011001 01101011 01001110 01000011 01100100 01010111 01001001 01111010 01010101 01010111 01100100 01101001 01010010 00110001 01011001 01110111 01010011 01010101 01101000 01010011 01100010 00110001 01110000 01010100 01010001 01101101 01110100 01100001 01010110 01111010 01000110 00110010 01011001 01101101 01101100 01000011 01001101 01000111 01001001 01111010 01010110 01101101 01110000 01101000 01010001 00110000 01001010 00110000 01010111 01101100 01001110 01000011 01100001 01000110 01101111 01111001 01010010 01101110 01000010 01101001 01100001 01010100 01010010 01101110 01010101 00110001 01001110 01101011 01100100 01000101 01101100 01001001 01010100 01101110 01011010 01001010 01010010 00110000 00110101 01111010 01011001 01101010 01001110 01001111 01100010 01000101 01101100 01001000 01001110 01011000 01011010 01101011 01100101 01010100 01010010 01101110 01010110 01010100 01001001 00110100 01100100 01010101 01111000 01110000 01001110 01000111 01100100 01011010 01010110 00110011 01101000 00110000 01011001 01101010 01001110 01001111 01001101 01000101 01101100 01001001 01010001 01101101 01111000 01101010 01100010 01010110 01110000 01110011 01010111 01010100 01001110 01010010 01100100 01010101 01101100 01000111 01100010 01000111 01111000 01101010 01100101 01010100 01010010 01101110 01010101 00110001 01001110 01000011 01001101 00110010 01000110 01011000 01100101 01001000 01001110 01001010 01010011 01000101 00110101 00110011 01010111 01010110 01101000 01001011 01100010 01000101 01101100 01001001 01100010 01001000 01011010 01101011 01010101 01111010 01010010 01101110 01010101 01101101 00110000 00110101 01100101 01010101 01101100 01001000 01001110 01011000 01011010 01101011 01100101 01010100 01010010 01101110 01010101 01010111 00110001 01010111 01001101 01000111 01010010 01001000 01010110 01101110 01101100 01001010 01010011 01000111 01111000 01110011 01011010 01000101 01001101 00110000 01100100 01010101 01111000 01110000 01010001 01101011 01110000 01001011 01001101 01101110 01101000 01111010 01010011 01010101 01100100 01010111 01001101 01101100 01110000 01011000 01001110 01000111 01100100 01101001 01010010 00110001 01011001 01110111 01010011 01010101 01101000 01110011 01100100 01101101 01010010 01010100 01010001 01101101 01101000 01101010 01001101 01101011 00110101 01110011 01011001 01101101 00110001 01010010 01011010 00110001 01101100 01011000 01001110 01010111 01110100 01001010 01010010 00110011 01101000 01110011 01010111 01010110 01101000 01100001 01100010 01000101 01101100 01001001 01010101 01101101 00111001 01101000 01010111 01000101 00110001 01101110 01011001 00110000 01100100 00110100 01100001 01000110 01101011 01111001 01010110 01011000 01010110 01001010 01010010 01010111 01111000 01110100 01010011 01010101 01101000 01110011 01100100 01101101 01010010 01010100 01010001 01101010 01001110 01101000 01010110 00110011 01101000 01111010 01010011 01010101 01100100 01010011 01100100 01101011 01101100 01001000 01010010 01010111 01100100 01100001 01100010 01010110 01011001 01111010 01010011 01010101 01100100 01010111 01100010 01000111 01001010 01110101 01010100 01101010 01010110 01001101 01010001 00110000 01001001 01111010 01010111 01101100 01100100 01010111 01100100 01010111 01001101 01111010 01100001 00110010 01100100 01101001 01010010 00110010 01110111 01110111 01011010 01000101 01100100 00110100 01100010 01000101 01101100 01001000 01010111 01101101 01101000 01101011 01100010 01010100 01101100 00110101 01011001 00110011 01101100 01000011 01100010 01010111 01001001 01111010 01010011 01010111 01100100 01101001 01010110 00110001 01010110 01101110 01010111 01101101 00110001 01110011 01100101 01010111 01001101 01111010 01010101 01011000 01010110 01001010 01010010 01101011 01110000 01110011 01011010 01000101 01101000 01010111 01100101 01010111 01001010 01110000 01010001 01101010 01000010 01101001 01100101 01010101 01001001 01110111 01011001 01010101 01100100 01010110 01011010 00110010 01001010 01001000 01100010 01000111 00110001 01101011 01010001 00110011 01100100 01101110 01011001 01101100 01101000 01110010 01011010 00110010 01001010 01001000 01100010 01000100 01000010 01101011 01010010 00110011 01101000 01110011 01010011 01010101 01100100 01010111 01100101 01010111 01001110 01110100 01010010 01101110 01010110 01100001 01010001 00110000 01001010 01110000 01011001 01101010 01001110 01110010 01100100 01010101 01101100 01000111 01011010 01000111 01111000 01001010 01010010 00110010 01101000 01101111 01011010 01000111 00110001 01010110 01011010 00110010 01010001 01111001 01001111 01011000 01101100 01101000 01100101 01010101 01001001 01110111 01011001 01101110 01101100 01000011 01100001 00110010 01001010 00110101 01010010 01010111 01101011 00111101
        """)
    call updateconsole("", "File copied successfully.")
    $ renpy.jump("pre_ch0_result")
    return

label pre_ch0_result:
    call updateconsole("", "Loading aliceangel.chr...")
    mi 1g "Well, this is it."
    mi "I'll see you on the other side."
    mi "Just don't let her kill you, alright?"
    mi "She'll probably react terribly to this..."
    show mio at thide
    hide mio
    
    call updateconsole("init _alice", "Starting init scripts...")
    call hideconsole
    hide rm
    hide rm2
    hide monika_room
    python:
        renpyApp.notify_new_char("Alice Angel")
        config.allow_skipping = True
        gtext = glitchtext(12)
    window hide(None)
    python:
        aliceangel.long_name = gtext
        aliceangel.ask_app_permissions()
        with open(config.basedir + "/game/AliceAngel.apf", "r") as f:
                perm_lines = f.readlines()
                if perm_lines[0] == 'pm_notify_disable\n':
                    aliceangel.override_perms()
                elif perm_lines[1] == "pm_files_disable\n":
                    aliceangel.override_perms()
                elif perm_lines[2] == "pm_sysadmin_disable\n":
                    aliceangel.override_perms()
        SystemUIServer.send_temporary_notification("New Admin Helper Added", "[gtext] now has administrative privileges on this device.", action=Return(1))
        renpy.music.set_volume(0.25)
    play music a4 fadein 5.0
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    $ a_name = gtext
    a "..."
    a "...no..."
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
    a "No..."
    a "I won't let this happen."
    a "You poor innocent soul..."
    a "He'd better have a good reason as to why he did this."
    a "Well, I guess this wouldn't be horrifying..."
    a "Ahaha~"
    a "I'll say, I could make a fine story out of this."
    a "Ahahaha"
    a "AHAHAHAHAHA"
    $ style.say_dialogue = style.edited
    a "AHAHAHAHAHAHAHAHAHAHAHAHA"
    a "Congratulations, [player]!"
    a "You just got a date with an Angel!"
    $ style.say_dialogue = style.normal
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    python:
        renpy.music.set_volume(0.75)
        aliceangel.short_name = "Alice"
        aliceangel.long_name = "Alice Angel"
    return
