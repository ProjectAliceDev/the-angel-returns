image bg mojave setup = "mod_assets/images/mojave/bg-setup.png"
image bg mojave desktop = "mod_assets/images/mojave/bg-desktop.png"
image setup_feedback = "mod_assets/images/mojave/feedback.png"
image mojave_setup = "mod_assets/images/mojave/setup-window.png"
image mojave_setup_complete = "mod_assets/images/mojave/setup-window-complete.png"


image mojave setup header = Text("Alice OS Setup Assistant", font="Resources/systemfont/Medium.ttf", size=38, style="_default")

# All possible setup screens
image setup_process_files = Text("Validating beta program files...", font="Resources/systemfont/Light.ttf", size=10, style="_default")
image setup_create_accnt = Text("Please create a username for this computer. Your password will be\ncreated automatically.",font="Resources/systemfont/Regular.ttf", size=22, style="_default")
image setup_prerelease_info = Text("We've detected that you're running a pre-release version of AliceOS.\nSome features of this operating system may not work properly\non your computer.\n\nIf you wish to roll back to a stable version of AliceOS, contact your\nsystem administrator.",font="Resources/systemfont/Regular.ttf", size=22, style="_default")
image setup_send_feedback_info = Text("Your computer has been enrolled in the AliceOS Beta Program. You\ncan send feedback through the menu option on the main screen\nor in-game as seen below.",font="Resources/systemfont/Regular.ttf", size=22, style="_default")
image setup_complete_thankyou = Text("Your profile has been created and this computer is ready to be used.\n\nIf you need to enter a password, check the profiles file.\n\nThank you for choosing Alice OS.",font="Resources/systemfont/Regular.ttf", size=22, style="_default")

image loader:
    "mod_assets/images/gui/loader/1.png"
    pause 0.125
    "mod_assets/images/gui/loader/2.png"
    pause 0.125
    "mod_assets/images/gui/loader/3.png"
    pause 0.125
    "mod_assets/images/gui/loader/4.png"
    pause 0.125
    "mod_assets/images/gui/loader/5.png"
    pause 0.125
    "mod_assets/images/gui/loader/6.png"
    pause 0.125
    "mod_assets/images/gui/loader/7.png"
    pause 0.125
    repeat

label setup:
    stop music fadeout 1.0
    scene black with trueblack
    window hide(None)
    show loader at truecenter
    pause 5.0
    call hideconsole
    show bg mojave setup zorder 2 with dissolve_scene_half
    window hide(None)
    play music m1
    show mojave_setup zorder 2 at truecenter
    show mojave setup header zorder 3:
        xalign 0.5 yalign 0.15
    if "beta" in config.version:
        show setup_prerelease_info zorder 3:
            xalign 0.5 yalign 0.3
        show setup_process_files zorder 3:
            xalign 0.5 yalign 0.85
        show loader zorder 4:
            xalign 0.5 yalign 0.7
        pause 5.0
        hide setup_prerelease_info
        hide loader
    call setup_feedback_mode
    return

label setup_feedback_mode:
    if "beta" in config.version:
        show setup_feedback zorder 3 at truecenter
        show setup_send_feedback_info zorder 4:
            xalign 0.5 yalign 0.3
        $ renpy.pause(5.0)
        hide setup_process_files
        hide setup_feedback
        hide setup_send_feedback_info
    else:
        pass
    call setup_accounts
    return

label setup_accounts:
    show setup_create_accnt zorder 3:
        xalign 0.5 yalign 0.3
    python:
        if persistent.playername:
            p = persistent.playername
            SystemUIServer.send_temporary_notification("Username detected", "Press Respond to use the name '" + p + "'.", action=Jump("setup_complete"))
        player = renpy.input(' ')
        player = player.strip()
        persistent.playername = player
    show loader zorder 4:
        xalign 0.5 yalign 0.7
    $ renpy.pause(3.0)
    call setup_complete
    return

label setup_complete:
    hide setup_create_accnt
    hide bg mojave setup
    show menu_bg zorder 1
    hide mojave_setup
    show mojave_setup_complete zorder 2 at truecenter
    hide loader
    python:
        with open(config.basedir + '/game/profiles.moj', 'w+') as f:
            f.write(player + ":sierra")
    show setup_complete_thankyou zorder 3:
        xalign 0.5 yalign 0.3
    $ renpy.pause(3.0)
    return
