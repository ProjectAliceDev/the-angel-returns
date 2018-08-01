image rsod_bg = "#c6262e"
image rsod_face = Text(":(", font="Resources/systemfont/Regular.ttf", size=128, color="#ffffff", style="_default")
image rsod_generic_message = Text("AliceOS ran into an error it couldn't handle and\nneeds to restart.", font="Resources/systemfont/Regular.ttf", size=48, color="#ffffff", style="_default")

image rsod_gobfadu_lock_message = Text("You can search online for this error: ERR_GOBFADU_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_applet_lock_message = Text("You can search online for this error: ERR_GOBFADU_APPLET_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_frame_lock_message = Text("You can search online for this error: ERR_GOBFADU_FRAME_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_os_lock_message = Text("You can search online for this error: ERR_GOBFADU_OS_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_gui_lock_message = Text("You can search online for this error: ERR_GOBFADU_GUI_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_resource_lock_message = Text("You can search online for this error: ERR_GOBFADU_RESOURCE_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_test_lock_message = Text("You can search online for this error: ERR_GOBFADU_TEST_LOCK", font="Resources/systemfont/Light.ttf", size=24, color="#ffffff", style="_default")

label GOBFADULock:
    scene rsod_bg
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_gobfadu_lock_message:
        xpos 0.1
        yalign 0.75
    pause 10.0
    $ renpy.utter_restart()
    return
