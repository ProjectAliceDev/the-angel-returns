## splash screen is first thing that gets shown to player
init -100 python:

    # archive check for mods
    for archive in ['audio','images','fonts']:
        if archive not in config.archives:
            renpy.error("DDLC archive files not found in /game folder. Check installation and try again.")

# disclaimers
init python:
    menu_trans_time = 1

    splash_message_default = "This game is not suitable for children\nor those who are easily disturbed."
    splash_message_beta = "This is a pre-release version of The Angel Returns.\nSome things may be changed in the future."

    splash_messages = [
        "The choices of the beautiful are unbearable.",
        "It took so many tries to make this beautiful.",
        "Fear more than the Ink Demon.",
        "Dark nights are upon us!",
        "You will be forever mine.",
        "I've waited here for the longest time.",
        "This game is not suitable for children\nor those who are easily disturbed?",
        "This game is not suitable for children\nor those who are easily dismembered.",
        "This game is not suitable for children\nor those who are easily disguarded."
    ]


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)


image menu_logo:
    "/mod_assets/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    block:
        choice:
            "mod_assets/images/menu/hl3.png"
        choice:
            "mod_assets/images/menu/hl3-2.png"
    # menu_bg_move

image game_menu_bg:
    topleft
    "mod_assets/images/menu/hl3.png"
#    menu_bg_loop

image menu_fade:
    "black"
    menu_fadeout

label menu_glitch:
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    return

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 825
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 825, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 460
    ycenter 400
    zoom 0.58
    menu_art_move(0.54, 750, 0.54)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 665
    ycenter 345
    zoom 0.56
    menu_art_move(0.56, 665, 0.56)

image menu_art_m:
    subpixel True
    "mod_assets/images/menu/menu_art_sm.png"
    xcenter 1050
    ycenter 580
    zoom 0.60
    menu_art_move(0.60, 600, 0.60)

image menu_art_a:
    subpixel True
    "mod_assets/images/menu/menu_art_a.png"
    xcenter 875
    ycenter 590
    zoom 0.80
    menu_art_move(0.54, 1100, 0.80)

image menu_art_mi:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 725
    ycenter 580
    zoom 0.60
    menu_art_move(0.60, 600, 0.60)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "mod_assets/images/menu_art_s.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "mod_assets/images/gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadein:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.6
    easeout 0.5 alpha 1


transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "black"
    0.5
    "mod_assets/images/bg/splash-white.png" with Dissolve(0.5, alpha=True)
    2.0
    "black" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "black"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "mod_assets/images/menu/warning.png"
image tos2 = "mod_assets/images/menu/warning2.png"


init python:
    if not persistent.do_not_delete:

        import os
        try:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")

            if persistent.playthrough <= 2:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 0 or persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

        except:
            pass


label splashscreen:
    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        stop music fadeout 1.0
        call default_boot_screen
        scene black
        pause 0.5
        call setup
        scene black
        with Dissolve(1.5)

        $ persistent.first_run = True

    python:
        basedir = config.basedir.replace('\\', '/')

    if persistent.autoload and not _restart:
        jump autoload

    $ config.allow_skipping = False

    call default_boot_screen
    scene black
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.bt
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)

    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    elif "beta" in config.version:
        $ splash_message = splash_message_beta
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    with fade
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        call screen alert("Cannot Load Save File", "Are you trying to cheat?", ok_action=Return(0))
        $ renpy.utter_restart()
    return


label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None



    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.bt
    $ persistent.bootpass = 0
    
    return

label quit:

    # stuff that happens when the game closes

    return
