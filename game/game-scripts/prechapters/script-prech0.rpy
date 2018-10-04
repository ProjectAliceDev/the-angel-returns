## Pseudo-menu content
image ts_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image ts_intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image ts_warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image ts_splash_warning = ParameterizedText(style="ts_splash_text", xalign=0.5, yalign=0.5)

style ts_splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

image ts_menu_fade:
    "#ffffff"
    menu_fadeout

image ts_menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image ts_menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image ts_menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image ts_menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image ts_menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image ts_menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

label pre_ch0:
    stop music fadeout 1.0
    $ config.allow_skipping = False
    $ persistent.alice_desktop = True
    scene oem_background
    with dissolve_scene_full
    if not persistent.alice_activate:
        call screen bing_desktop()
        if _return != 'aliceangel':
            call screen alert("Not Initialized", "You must run Alice before you can load DDLC.", ok_action=Return(0))
            call pre_ch0
        else:
            pass
        python:
            aliceangel.ask_app_permissions()
            mscv = aliceangel.start_build()
            if mscv != 'go':
                quick_menu = False
                renpy.call_screen("ThrowASError", "ALICE_BUILD_DENIED")
                renpy.utter_restart()
            else:
                pass
            aliceangel.send_message("Wh-what?")
            aliceangel.send_message("What is this?")
            aliceangel.send_message("Where am I?")
        call screen alert("Alice Initialized", "To continue, please launch Doki Doki Literature Club from Activities.", ok_action=Return(0))
        $ persistent.alice_activate = True
        call screen bing_desktop()
    else:
        call screen bing_desktop()
    
    scene white
    with dissolve_scene_full
    
    # Start fake DDLC title screen
    python:
        persistent.ghost_menu = False
        splash_message = splash_message_default
        config.main_menu_music = audio.t1
        renpy.music.play(config.main_menu_music)
        persistent.alice_desktop = False
    show ts_intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide ts_intro with Dissolve(0.5, alpha=True)

    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show ts_splash_warning "This content is not suitable for children\nor those who are easily disturbed." with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    show ts_menu_fade
    show ts_menu_bg
    show ts_menu_art_n
    show ts_menu_art_y
    show ts_menu_art_s
    show ts_menu_art_m
    show ts_menu_nav
    show ts_menu_logo
    show menu_particles
    show ts_menu_fade
    $ renpy.pause(4.0)
    $ renpyApp.ask_app_permissions()
    $ renpy.pause(3.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    return
