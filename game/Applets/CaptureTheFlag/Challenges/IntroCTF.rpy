label ctf_intro:
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
    show alice_just_main at truecenter
    $ a_name = "Alice"
    a "..."
    a "Hm, now we come to the question..."
    a "Do I delete you?"
    a "Do I tear your file apart to my heart's delight?"
    a "The choices of the beautiful are unbearable; how's a girl to choose?"
    a "Ahaha~"
    a "I'm only kidding, of course."
return