label ch1_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    $ renpy.music.set_volume(0.75)
    play music t2

    s "Yaay!"
    "Sayori runs towards me, being yet again oblivious to the attention she's drawing to herself."
    show sayori 4br zorder 2 at t11
    s "Are you excited, [player]?"
    s 1ba "See, I have my stuff here!"
    "Sayori beams while holding a duffel bag."
    mc "Glad to see you're prepared this time."
    s 2bh "Heey!"
    s "I do prepare!"
    s 2bl "I just forget to bring the bag, ehehe~"
    mc "Okay, then..."
    mc "You made sure to grab everything you needed from the sto{nw}"
    n "Ay! Sayori!!!"
    "Natsuki tries to rush out of Sayori's house, clutching another duffel bag."
    "The weight of the bag seems to be slowing her down."
    show sayori zorder 2 at t21
    show natsuki 1be zorder 3 at f22
    n "You forgot the toothbrushes, dummy!"
    show sayori 2bp zorder 3 at f21
    show natsuki zorder 2 at t22
    s "Uwaa~!"
    s "Sorry! I didn't think about that."
    show natsuki zorder 3 at f22
    show sayori zorder 2 at t21
    n 2ba "Don't make a fuss about it, dummy!"
    n "I have them in my bag."
    mc "Ah, Natsuki!"
    mc "I see you slept over..."
    n 5bk "Yeah..."
    n "It just made it easier because you and Sayori are that much closer to school."
    n 5bq "It's not like I was trying to stay away or anything, if you're so worried about it..."
    mc "It's fine!"
    mc "I sometimes sleep on her couch unannounced when I can't get into my house."
    n 5bk "Wait, what?"
    show sayori zorder 3 at f21
    show natsuki zorder 2 at t22
    s 2bl "Ehehe~"
    s 1bx "You know, you can always just ask for my key!"
    "Natsuki giggles."
    show natsuki 5bz zorder 3 at f22
    show sayori zorder 2 at t21
    n "Aren't you quite a couple!"
    mc "Natsuki, can you please stop shipping me with others?"
    mc "You said the same thing with Monika, too!"
    n 5bl "I'm just teasing, baka!"
    n 2bc "We should probably go before Monika gets worried."
    mc "Let me take your bag, then."
    mc "It looked like you were struggling with it."
    "Nastuki attempts to hand me the bag."
    "My arm twitches as I grab it."
    mc "Wow, this is heavy!"
    mc "What do you have in here?"
    show natsuki zorder 2 at t22
    show sayori zorder 3 at f21
    s 4br "The entire kitchen! Ehehe~"
    mc "Wait, what?"
    s 1bx "I have all of the clothes and stuff."
    s "She didn't know if there were any tools in the kitchen there, so she has some stuff in hers."
    show natsuki 5bs zorder 3 at f22
    show sayori zorder 2 at t21
    n "..."
    n "No comment."
    show natsuki zorder 2 at t22
    mc "Um..."
    mc "Okay then."
    mc "Let's get there before it's too late."
    show sayori at lhide
    show natsuki at lhide
    hide sayori
    hide natsuki
    "Natsuki and Sayori proceed in front of me."
    "Holding on to Natsuki's bag, I trudge behind."

    scene bg campus
    with wipeleft
    mc "Hmm..."
    "I scan the scene, looking for Monika."
    show yuri 1ba zorder 2 at t11
    y "[player]!"
    y "I see you brought Nastuki and Sayori with you."
    show natsuki 1bc zorder 2 at f21
    show yuri zorder 2 at t22
    n "Where's Monika?"
    show yuri zorder 3 at f22
    show natsuki zorder 2 at t21
    y 2be "That's funny, I was just about to ask you the same thing."
    y "I hope she didn't forget!"
    show natsuki zorder 3 at f21
    show yuri zorder 2 at t22
    n 5bf "She'd better not have!"
    n "She practically set this whole thing up!"
    show monika 4bl zorder 3 at f31
    show natsuki zorder 2 at t32
    show yuri zorder 2 at f33
    m "Sorry, everyone!"
    m "I couldn't find an extra pair of clothing, so I just used on that I packed!"
    m "I don't have a lot of clothes, ahaha~."
    show yuri zorder 3 at f33
    show monika zorder 2 at t31
    y 1bf "For someone of your stature, I wouldv'e thought you had a lot."
    show monika zorder 3 at f31
    show yuri zorder 2 at t33
    m 2bd "Well, not necessarily..."
    m "I like living simply."
    m 4bd "It helps me stay focused on what needs to get done."
    m 4bn "I'm not really that into fashion either, ehehe~"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 5bk "Well, at least you're here..."
    n "Where's this place, anyway?"
    show yuri at thide
    hide yuri
    show sayori 1bc zorder 3 at f33
    s "I think we're supposed to take a train there or something..."
    show sayori zorder 2 at t33
    show monika zorder 3 at f31
    m 2bc "You're right, it's a bit far from here."
    m 2bd "The next train should be leaving in thirty minutes or so."
    m "At least that's what Apple Maps says."
    m 4bb "Don't worry, though!"
    m "I know we have a lot of bags, so I can drive us over to the station."
    show yuri 1bb zorder 3 at f41
    show monika 2bb zorder 2 at t42
    show natsuki zorder 2 at t43
    show sayori zorder 2 at t44
    y "Yes, and I have already paid for all of our tickets."
    y "Monika and I were discussing transportation last night."
    show yuri zorder 2 at t41
    show monika zorder 3 at f42
    m 2bk "Don't worry! We got this."
    show monika zorder 2 at t42
    show natsuki zorder 3 at f43
    n "Wow, this was really planned out..."
    n 2bd "I guess bring 'the kitchen' wasn't a bad idea after all!"
    show sayori zorder 3 at f44
    show natsuki zorder 2 at t43
    s 4br "Yay! This is going to be so much fun!"
    show sayori zorder 2 at t44
    mc "Well, we've got quite the trip ahead."
    mc "We should probably get moving before we miss the train."
    show monika zorder 3 at f42
    m 2ba "Ah, yes, we should!"
    m 4bb "Okay, everyone! You can go ahead and place everything in the trunk."
    show monika zorder 2 at t42
    show sayori at thide
    show yuri at thide
    show natsuki at thide
    hide sayori
    hide natsuki
    hide yuri
    show monika zorder 2 at t11
    m 2bb "Don't worry, [player], I can take those bags for you."
    mc "Uh, I think you should take this one, then..."
    m 2bg "Why so?"
    mc "Trust me."
    "Monika takes my bag from me."
    m 4bi "I was hoping to take the heavier one from you, actually."
    mc "Why that all of a sudden?"
    m 4bg "[player], your face is turning a bit red."
    m "Are you sure you're able to carry that?"
    mc "I got it, Monika."
    m "..."
    "Monika take Natsuki's bag from my hands and gives me mine back."
    "I sigh in relief."
    m 1bk "I don't want you collapsing before we get there, ahaha~!"
    m 1bb "I'm a lot stronger than I look, you know."
    "I sometimes wonder how Monika knows what I think sometimes."
    mc "It's not that..."
    m 2bk "Ahaha!"
    m "You're so cute when you're humble. You know that, right?"
    m "Let's go before the other girls get worried."
    show monika at lhide
    hide monika
    "Monika races to the trunk and places the bag in."
    "I do the same and soundly close the trunk."
    "As everyone else appears to have filld up the back seats, I reluctantly sit right next to Monika in the front."

    scene bg station
    with wipeleft
    stop music fadeout 1.0
    play music t3
    "We arrive to the station in ten minutes."
    show monika 1bb zorder 2 at t21
    show sayori 1ba zorder 2 at t22
    m "Okay, everyone! Now we wait for the train."
    show sayori zorder 3 at f22
    s 2br "Ehehe, I can't wait..."
    "Sayori rushes off join Yuri and Natsuki on the bench."
    show sayori at thide
    hide sayori
    show monika zorder 2 at t11
    m "So, [player], a lot will probably be taking place."
    mc "I suppose so. I'm just hoping we can all stay safe."
    m 4bk "Of course, [player]!"
    m 4bb "That's why we have you to look out for us."
    mc "Don't forget to exclude yourself, Miss President."
    m 2bj "Ahaha, you're funny..."
    m 2ba "I won't rest from my duties just yet."
    m "Anyways, I have a feeling that we'll be all over the place."
    m 2bd "I was doing some research last night with Yuri about the studio."
    m 4bd "Unfortunately, it seems as if Mr.Drew had passed after Sayori received the letter."
    mc "So who runs the studio now?"
    m "It's filed under a man named 'Henry', but the day-to-day operations are managed by a 'Susan Campbell', the original voice actress for Alice Angel."
    mc "Susan Campbell? That's an odd choice to leave a huge studio to..."
    m 2bd "It is a bit odd, but I guess Joey trusted her to keep things moving smoothly if Henry wasn't up to the task."
    m "I'm a bit worried, to be honest."
    m "Further research suggests that Ms. Campbell's personality is, well, a bit volatile."
    m "She didn't handle her replacement of roles very well."
    m "She was a bit skeptical to take such an administrative role at first."
    mc "I guess she came to her senses afterwards, right?"
    m 4bi "That's when things got weird. Like, {i}really{/i} weird."
    m "Joey had been working on an ink machine to bring cartoons to life."
    m "You know, like one of the 3D printers at school, only on a biological scale."
    mc "Okay... and?"
    m "Some sites and sources have suggested that he used this machine on his employees to create his perfect cartoons."
    m 2bf "Isn't that kind of messed up?"
    mc "..."
    mc "Uh..."
    m 4bf "Rumor has it that he even did it to himself."
    m "We have to be really careful, [player]..."
    m 4bi "Whatever we do, we have to avoid the ink at all costs."
    mc "Right."
    m "I don't want anyone else to know about this."
    m "Only Yuri, you, and I know about it."
    m "I think it's best that we bunk with each other to discuss plans."
    m 1bg "I certainly wouldn't want to get Sayori's and Natsuki's hopes down."
    mc "I understand."
    mc "Say, the train's about to arrive in a few seconds."
    m 1be "Ah, that it is!"
    show monika zorder 2 at t21
    m 1bb "Okay, everyone! Let's grab our bags and board the train!"
    show sayori 2br zorder 2 at t22
    s "Yaay!"
    show sayori at thide
    hide sayori
    show yuri 2bf zorder 3 at f22
    y "Monika, I think [player] should sit with you and me."
    y 4bb "You know, to discuss things..."
    show monika zorder 3 at f21
    show yuri zorder 2 at t22
    m 3bb "What a great idea, Yuri!"
    m "That way, we can all be on the same page!"
    mc "Sure, whatever works..."
    show monika at thide
    show yuri at thide
    hide monika
    hide yuri
    "Monika, Yuri, and I head onto the train."
    "Natsuki and Sayori wave, showing us where to go."
    "We take the three seats perpendicular from them."
    "The train starts to move as we head to the studio."
    return
