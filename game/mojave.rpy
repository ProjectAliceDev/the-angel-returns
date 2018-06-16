image bg mojave setup = "mod_assets/images/mojave/bg-setup.png"
image bg mojave desktop = "mod_assets/images/mojave/bg-desktop.png"

## Init Images
image bg mojave initial = Text("{color=#fff}Loading setup assistant...{/color}", font="mod_assets/gui/font/mojave.ttf", size=28, style="_default")

## Setup Images
image mojave_setup = "mod_assets/images/mojave/setup-window.png"
image mojave_setup_complete = "mod_assets/images/mojave/setup-window-complete.png"

image mojave setup header = Text("Alice OS Mojave Setup Assistant", font="mod_assets/gui/font/mojave-header.ttf", size=38, style="_default")
image mojave_ddlc_header = Text("Alice OS Mojave Setup Assistant", font="gui/font/RifficFree-Bold.ttf", size=38, style="_default")

image mojave_setup_details = Text("Welcome to Alice OS Mojave. Your administrator, {font=mod_assets/gui/font/mojave-bold.ttf}Dan Salvato{/font}, has \nrequested you to create an account name before continuing.\n\nPlease create a username for this computer. Your password will be \ncreated and logged automatically. Press ENTER when you have \nfinished.",font="mod_assets/gui/font/mojave.ttf", size=22, style="_default")
image mojave_setup_process = Text("Processing...", font="mod_assets/gui/font/mojave-bold.ttf", size=32, style="_default")
image mojave_setup_theming = Text("Applying policy theme...", font="mod_assets/gui/font/mojave-bold.ttf", size=32, style="_default")
image mojave_setup_thankyou = Text("Your profile has been created and this computer is ready to\nbe used.\n\nYour profile data is saved in profiles.moj.\n\nThank you for choosing Alice OS. Your computer will now finish setup\nand prepare your desktop for you.",font="mod_assets/gui/font/generic2.ttf", size=22, style="_default")

## Run DDLC Images
image bg mojave ddlcinit = Text("{color=#fff}Running DDLC Console...{/color}", font="mod_assets/gui/font/mojave.ttf", size=28, style="_default")

## Mojave Sounds
define audio.ping = "mod_assets/sfx/note.mp3"

## Notifications
image notify_ddlc = "mod_assets/images/gui/frame_notify_default.png"
image notify_message = "mod_assets/images/gui/frame_notify_message.png"
image notify_system = "mod_assets/images/gui/frame_notify_system.png"


label setup:
    stop music fadeout 1.0
    scene black with trueblack
    show bg mojave initial zorder 2 at truecenter
    $ renpy.pause(0.75)
    hide bg mojave initial
    show bg mojave setup zorder 2 with dissolve_scene_full
    play music m1
    show mojave_setup zorder 2 at truecenter
    show mojave setup header zorder 3:
        xalign 0.5 ypos 0.15
    show mojave_setup_details zorder 3:
        xalign 0.5 ypos 0.25
    window hide(None)
    python:
        if persistent.playername:
            renpy.jump('setup_name_detect')
    python:
        player = renpy.input(' ')
        player = player.strip()
    show mojave_setup_process zorder 3:
        xalign 0.5 yalign 0.6
    python:
        with open(config.basedir + "/game/invalid", "r+") as invalid:
            for line in iter(invalid):
                testcase = line.strip()
                if player == testcase:
                    renpy.jump("setup_error_name")
        persistent.playername = player
        renpy.jump('setup_name_configured')
    return

label setup_error_name:
    call screen dialog_alert("Invalid Username", "You cannot use this username on this computer.\n\nThe setup assistant will be restarted.", ok_action=Return())
    jump setup
    return

label setup_name_detect:
    play sound ping
    call screen ios_notify(2, "Account detected", "Press Dismiss to use your existing name.", dismiss=Return())
    $ renpy.jump('setup_name_configured')
    return

label setup_name_configured:
    $ renpy.pause(3.0)
    hide mojave_setup_process
    show mojave_setup_theming zorder 3:
        xalign 0.5 yalign 0.6
    $renpy.pause(1.0)
    hide mojave setup header
    show mojave_ddlc_header zorder 3:
        xpos 0.26 ypos 0.15
    $ renpy.pause(1.5)
    hide mojave_setup
    show mojave_setup_complete zorder 2 at truecenter
    $ renpy.pause(2.0)
    hide mojave_setup_theming
    hide mojave_setup_details
    python:
        with open(config.basedir + '/game/profiles.moj', 'w+') as f:
            f.write(player + ":sierra")
    show mojave_setup_thankyou zorder 3:
        xpos 0.24 ypos 0.25
    $ renpy.pause(3.0)
    hide mojave_setup_details
    hide mojave_setup_thankyou
    hide mojave_ddlc_header
    hide mojave_setup_complete
    $ renpy.pause(1.5)
    call screen dialog_alert("System Policy Applied", "Your administrator has enforced a system \npolicy that does the following:\n\n \"Automatically launch DDLC and prevent desktop access\"\n\nYour computer may function differently.", ok_action=Return()) 
    stop music fadeout 1.0
    return

label init_desktop_load:
    scene bg mojave desktop with Dissolve(3.0)
    $ consolehistory = []
    $ config.allow_skipping = False
    call screen dialog_alert("No Desktop Environment", "Please install a desktop environment to use\nyour computer regularly.\n\nWe recommend installing GNOME Shell.", ok_action=Return())
    $ renpy.pause(1.0)

    scene black
    show bg mojave ddlcinit at truecenter
    $ renpy.pause(1.5)
    return