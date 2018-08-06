label GOBFADUTestLock:
    scene rsod_bg
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_search_error_text:
        xpos 0.1
        yalign 0.75
    show rsod_gobfadu_test_lock_message:
        xpos 0.1
        yalign 0.8
    pause 10.0
    $ renpy.utter_restart()
    return
