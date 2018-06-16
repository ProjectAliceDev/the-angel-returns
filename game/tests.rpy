label gui_playground:
    stop music fadeout 1.0
    play music m1
    scene bg mojave desktop
    "I hope she doesn't ping me again."
    play sound ping
    call screen ios_notify("Alice", "I wouldn't do that if I were you!", dismiss=Return())
    $ renpy.pause(3.0)
    hide ios_notify
    "Uh, can you hear me?"
    return