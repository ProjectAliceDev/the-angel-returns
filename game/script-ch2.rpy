label ch2_main:
    stop music fadeout 1.0
    scene bg studio breakroom
    play music t2
    "It was a little weird sleeping in the same room as Monika and Yuri."
    "The conversations in there got a bit awkward."
    "That fact that Monika even knew then the sun rose without a window or her phone was even more awkward."
    "Nonetheless, we all decided to head to the breakroom and set ourselves up for some form of breakfast."
    "As expected, Natsuki pushed one of the tables and set up all of her equipment for baking."
    "Sayori's helping her with some of the baking."
    "Yuri enthusiastically is already working on making the tea."
    "Meanwhile, Monika checks the breakroom for any utensils."
    show monika 3bd at t11
    m "[player], do you see any utensils in here?"
    mc "I guess it's in another breakroom or something."
    m 3bb "I hope Alice isn't hiding them from us, ahaha~!"
    mc "Nah, I don't think she'd do that."
    a "Hey, you folks looking for these?"
    "To my surprise, Alice walks into the room with a box."
    "She sets the box down onto the table and then turns towards us."
    show alice 0b at f22
    show monika at t21
    a "I had a funny feeling you'd need some utensils."
    a "So, I grabbed the set we have in the lower levels."
    a 0k "I'm surprised you set up over here instead of down there!"
    
    return

label ch2_end:
    return
