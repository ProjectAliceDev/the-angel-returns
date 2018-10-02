screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"
    
    add "menu_fade"
    add "menu_bg"
    # add "menu_art_n"
    # add "menu_art_s"
    # add "menu_art_y"
    add "menu_art_m"
    add "menu_art_mi"
    add "menu_art_a"
    frame:
        pass

## The use statement includes another screen inside this one. The actual
## contents of the main menu are in the navigation screen.
    use navigation

#    add "menu_particles"
#    add "menu_particles"
#    add "menu_particles"
#    add "menu_logo"
#    add "menu_particles"
#    add "menu_fade"
    text "[config.name!t]":
        style "info_title"

    if gui.show_name:
        vbox:
            text "v. [config.version]":
                style "hl3_version_text"
            if persistent.ctf_mode:
                text "For evaluation purposes only. CTF mode enabled.":
                    style "hl3_version_text"
            else:
                text "For evaluation purposes only.":
                    style "hl3_version_text"
                


    key "K_ESCAPE" action Quit(confirm=False)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size

init -1 style info_title:
    size gui.title_text_size
    xpos gui.navigation_xpos
    yalign 0.48
    font "mod_assets/gui/font/generic.ttf"
    color "#ffffffE6"
    outlines [(1, "#33333380", 0, 0), (1, "#33333300", 1, 1)]

init -1 style hl3_version_text:
    color "#d4d4d4"
    size 16
    font "Resources/systemfont/Regular.ttf"
    outlines [(1, "#33333380", 0, 0), (1, "#33333300", 1, 1)]
    xalign 1.0
