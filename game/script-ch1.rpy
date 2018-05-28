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
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    stop music fadeout 0.0
    show reload_bg zorder 2
    show fake_reload zorder 2 at truecenter
    $ renpy.pause(3.0)
    hide fake_reload
    $ renpy.pause(0.1)
    window hide(None)
    show fake_reload2 zorder 2 at truecenter
    $ renpy.pause(3.0)
    hide reload_bg
    hide fake_reload2
    window show(None)

    scene black
    n "Are you sure this is it?"
    n "It looks kind of run down..."
    y "This is the only location that Apple Maps brought up."
    m "Yeah, I'm pretty sure this is the studio."
    s "Can we go inside already?"
    mc "We'll go inside soon. We just have to figure out what's going on."
    y "I don't suppose we can just walk in..."
    y "The door's unlocked."
    m "Well, this is a cartoon studio."
    m "I guess we have no other choice."
    "Monika gently opens the door."
    scene bg studio entrance
    play music m1
    show monika 1bc zorder 2 at t31
    m "Whoa..."
    show yuri 1be zorder 2 at t33
    y "This isn't what I expected..."
    mc "I think this is only the lobby."
    "Suddenly, we hear soft singing coming from the corner."
    a "{i}I got a friendly halo and I'm filled with love...{/i}"
    show alice 0j zorder 3 at f32
    a "{i}I'm Alice...{/i}"
    a 0d "...Angel?"
    a 0g "How... did you get in here?"
    show alice zorder 2 at t32
    show yuri zorder 3 at f33
    y 3bp "A-aah!"
    y 4bc "Th-the door was unlocked."
    y "W-we thought the studio was o-open..."
    show yuri at lhide
    hide yuri
    show sayori 1bb zorder 2 at t33
    show monika zorder 3 at f31
    m 3bd "My apologies if we came here unannounced."
    m "We came here as per a response to a letter Mr. Joey Drew sent to the vice president of our literature club, Sayori."
    show sayori zorder 3 at f33
    show monika zorder 2 at t31
    s 4br "That's me!"
    show sayori 1ba zorder 2 at t33
    show alice zorder 3 at f32
    a 0d "A letter?"
    a "From Mr. Drew?"
    a 0i "That's interesting, he never confided with me about that."
    a "May I please see a copy of this letter?"
    "I hand the woman the letter from my coat pocket."
    a "..."
    a 0d "Oh..."
    a "Ah!"
    a 0b "I'm sorry, I guess I was misinformed."
    a 0j "Welcome to Joey Drew Studios, home of the Bendy and Alice Angel cartoons!"
    a 0b "Allow me to introduce myself..."
    n "Wait a second."
    show monika zorder 2 at t41
    show alice zorder 2 at t42
    show natsuki 5bc zorder 3 at f43
    show sayori zorder 2 at t44
    n "You look familiar."
    "The room falls silent."
    show monika 1bc zorder 2 at t41
    show alice 0c zorder 2 at t42
    n 5bs "..."
    "Natsuki's pondering again..."
    n 5bd "You're Alice Angel, aren't you?"
    show alice zorder 3 at f42
    show natsuki zorder 2 at t43
    a "..."
    $ a_name = "Alice"
    a 0d "Well, that was rather depressing."
    mc "Natsuki, I think she was..."
    a 0g "You could've at least let me properly introduce myself to you..."
    a 0o "It's been a while since I sang for a crowd of people like this..."
    show natsuki zorder 3 at f43
    show alice zorder 2 at t42
    n 5bs "..."
    n "Sorry, I didn't mean to spoil the thunder like th{nw}"
    show sayori zorder 3 at f44
    show natsuki zorder 2 at t43
    s 4br "Do it anyway!"
    show alice zorder 3 at f42
    show sayori zorder 2 at t44
    a 0g "W-what?"
    mc "Don't mind Sayori, she just really loves hea{nw}"
    show sayori zorder 3 at f44
    show alice zorder 2 at t42
    s 2be "Please?"
    s "I want to hear you sing..."
    s 1ba "I bet it sounds nice..."
    show monika zorder 3 at f41
    show sayori zorder 2 at t44
    m 2be "I'm sure the club doesn't mind hearing it anyway, even though the surprise has been spoiled."
    m 4bb "We're all about self-expression, anyway!"
    m 4bk "That's why we write poems, after all!"
    show monika 1ba zorder 2 at t41
    stop music fadeout 1.0
    play music mend
    show alice zorder 3 at f42
    a 0c "Look, I appreciate the concern and your enthusiasm about it."
    a 0g "It's just that it doesn't have the same effect now."
    a "I've been doing this for over twenty years."
    a 0o "I know when something gets too old."
    show alice zorder 2 at f42
    s 2bu "B-but..."
    show sayori at s44
    m 1bo "You can't beat yourself up like this..."
    show monika at s41
    n 5bm "You can't just call it quits like that..."
    show natsuki at s43
    show alice zorder 3 at f42
    a "..."
    a "It appears you've given me a difficult choice."
    a "I'm sorry..."
    a 0g "You can use the directory to find the break room."
    a "Situate yourselves in there for now."
    a 0o "I need some time to think..."
    show alice at lhide
    hide alice
    show monika at t31
    show natsuki at t32
    show sayori at t33
    s "..."
    s 2bw "We scared her away!"
    show natsuki zorder 3 at f32
    n 5bn "I'm sorry, guys..."
    n "I didn't mean for the first day to turn out like this."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m "Natsuki, it's not your fault."
    m 3bp "I guess she got a little bit overwhelmed..."
    m 1bp "We might've pushed her a little too much..."
    show monika zorder 2 at t31
    mc "Guys, you can't be beating yourselves up."
    mc "It sounds like not a lot of people have seen her or this studio for a while."
    mc "I bet you she's just unsure of how to handle this because she's been lonely for a long while."
    mc "Monika, take the girls to the break room."
    mc "I'm going to try finding Alice and taling to her."
    show monika zorder 3 at f31
    m 1bg "If you say so, [player]..."
    show monika zorder 2 at t31
    mc "It's going to be okay."
    mc "We'll still make this fun."
    "The girls rest the bags on the long table and start looking around for the break room."
    show monika at thide
    show sayori at thide
    show natsuki at thide
    hide monika
    hide natsuki
    hide sayori
    "I look at the directory on the wall and head to where this so-called 'Ink Machine' is."

    scene bg studio inkmachine
    with dissolve_scene_full
    mc "...Alice?"
    show alice 0g at t11
    a "How did you find me?"
    mc "I had a hunch, I guess..."
    a 0i "You shouldn't have tried to find me, ..."
    mc "[player]."
    a "[player]..."
    a 0o "That name sounds so familiar."
    a 0g "Why did you come here, [player]?"
    mc "We figured that we wanted to check ou-{nw}"
    a "No, not that."
    a "Why are {i}you here{/i}?"
    mc "..."
    mc "Alice, how long has it been since someone's come down here?"
    a "..."
    a 0n "Too long ago."
    a "Henry came down here because Joey had sent him a letter, too..."
    a 0g "And look at where I am."
    a "I'm forever trapped in this..."
    a "...lost memory."
    a "God, it's so weird having real human beings here."
    a 0i "But you already knew that, didn't you?"
    stop music fadeout 1.0
    mc "..."
    mc "I had a funny feeling."
    mc "Monika told me a few things before we got here."
    play music t9
    a 0t "That girl..."
    a 0m "Ahaha~"
    a "She's probably the smart one in your little club, yes?"
    mc "She's actually the club President. Yuri's the smart one."
    a 0d "And is Yuri the purple-haired one?"
    mc "Yeah, ehehe~"
    "I chuckle sadly."
    mc "She's a bit shy..."
    a "I can tell."
    a "Man, it must be a living {i}hell{/i} dealing with those girls..."
    mc "They're not as bad as you think."
    mc "You get kind of used to it, I guess..."
    a 0m "That's what Joey said to everyone else about me."
    a 0n "He was a good liar. Sammy, too..."
    a 0t "I'm sorry for the lackluster first impression."
    a "This... it just feels so alien."
    a "Here are you all hoping to see something exciting and I let everyone down."
    show alice at s11
    mc "..."
    mc "Alice, aren't you being a little hard on yourself?"
    mc "I know you were big in the entertainment industry and all, but..."
    mc "You can't always go about everything in that kind of light."
    mc "We're just a bunch of seniors that happen to like poetry, literature, cupcakes..."
    mc "We're not expecting a grand entrance, you know."
    a 0g "But [player]..."
    a "That's the whole point."
    a "I'm {i}Alice Angel{/i}, for goodness sake!"
    a "I'm supposed to be like this."
    a 0t "And I've given you a bad first impression."
    mc "Look, I'm sure the girls have looked past that already."
    mc "I bet they're probably blaming themselves for this."
    mc "I just want everyone to be happy."
    mc "You don't have to sing for them or anything..."
    mc "All I ask that you freely present yourself and at least give it a shot."
    a "..."
    a 0m "Well, [player], I don't know if anyone's told you that you are a man of many words..."
    a "But I guess I have to trust you now."
    stop music fadeout 1.0
    show alice at t11
    play music t8 fadein 3.0
    $ renpy.pause(2.0)
    a 0d "Tell me, are they really obsessive over cuteness?"
    mc "Ahaha~"
    a "What? It's a legitimate concern of mine."
    mc "It's okay. Just be yourself."
    a "Fine, then..."
    a "We should probably meet up with them before things get a bit{nw}"
    m "[player]?"
    show monika 1bg zorder 2 at t33
    m "Is everything alright over here?"
    mc "Uh, yeah..."
    mc "We were just chatting for a bit so that we were on the same page."
    mc "It's fine now."
    m 2be "Alright, I trust you."
    m "Alice, I'm sorry if we overwhelmed you."
    show alice at f11
    a 0k "No, no, not at all!"
    a 0b "I guess I was just caught off-guard, you know?"
    show alice at t11
    m "Well, we should get going."
    show monika at thide
    hide monika
    mc "Ehehe~"
    mc "I told you so."
    a 0r "Mhm..."
    mc "Uh..."
    mc "Okay then..."
    show alice at thide
    hide alice
    "We proceed to the break room, with Alice leading the way."
    return

label ch1_end:
    scene bg studio breakroom
    with wipeleft
    show alice 0b at t42
    a "Sorry to have kept you waiting, everyone!"
    show yuri 3bf at t43
    y "I'm sorry if we overwhelmed you at first."
    show sayori 1be at t44
    s "Yeah..."
    s "I thought that we scared you!"
    show alice zorder 3 at f42
    a 0k "It's totally fine!"
    a "I just wasn't expecting it, that's all!"
    a 0d "I didn't mean to be a party-pooper or anything..."
    show monika 4bb zorder 3 at f41
    show alice zorder 2 at t42
    m "Ahaha, it's alright!"
    m "We did kind of throw a curveball at you."
    show alice zorder 3 at f42
    show monika zorder 2 at t41
    a 0b "Well, I imagine that you all must be a bit tired from the travel over here!"
    a "We have a few residential areas downstairs that you can use."
    a 0d "Trust me, the studio's a lot bigger than it looks!"
    show sayori zorder 3 at f44
    show alice zorder 2 at t42
    s 1bc "Do you happen to have a kitchen around here?"
    s "Natsuki brought some equipment and would probably want them in there."
    n "Hey! I could've asked myself, you know..."
    show alice zordre 2 at f42
    show sayori zorder 2 at t44
    a 0k "Ahaha, no need to worry."
    a 0b "We have a recreational lounge downstairs with a kitchen."
    a "I can help bring down some of the stuff with you, if you'd like..."
    a 0j "Ehehe~"
    show yuri zorder 3 at f43
    show alice zorder 2 at t42
    y 1bb "I'm sure Natsuki would appreciate that very much."
    y 1be "You don't happen to have a tea set in there, do you?"
    show alice zorder 3 at f42
    show yuri zorder 2 at t43
    a 0b "Of course we do!"
    a "It's how my colleagues usually like to calm down, so I always make sure we keep a set around."
    a "They're almost as ubiquitous as our Bendy cutouts, ahaha~!"
    show yuri zorder 3 at f43
    show alice zorder 2 at t42
    y 1bc "Wonderful!"
    show monika zorder 3 at f41
    show yuri zorder 2 at t43
    m 4bb "With that settled, I think this week will run smoothly!"
    m 2bb "Sayori, Natsuki... please follow Alice to the residential areas."
    m 1ba "I'd like to have a word with Yuri and [player] before we get completely settled in."
    show sayori zorder 3 at f44
    show monika zorder 2 at t41
    s "Okay! We'll get you when you're ready."
    show sayori at thide
    hide sayori
    show alice zorder 3 at f42
    a 0b "Alright, Monika."
    a "I shall see you downstairs soon."
    show alice at thide
    hide alice
    show monika zorder 2 at t21
    show yuri zorder 2 at t22
    "Monika watches as Alice guides Natsuki and Sayori upstairs, clutching onto some of our bags."
    a "Come on, girls! We've got a ways to go."
    "Yuri eyes the trio down as they exit the break room and close the doors."

    show vignette zorder 1 at vignettefade(1.5)
    stop music fadeout 1.5
    show monika zorder 2 at f21
    show yuri 1be zorder 2 at t22
    m 1bi "[player], was everything alright with Alice?"
    mc "Yeah, I guess."
    mc "She was a bit overwhelemed and got a bit nostalgic."
    play music b5
    show yuri zorder 2 at f22
    show monika zorder 2 at t21
    y 2bt "She doesn't seem trustworthy."
    y 1bh "She could be possibly watching our every move."
    y 1bf "I'll admit, we did walk in on her unexpectedly."
    y "Still, she raises some suspicions."
    mc "It doesn't help that she knows that we know about what happened before."
    show monika at f21
    show yuri at t22
    m "What?"
    m "How could she possibly know?"
    mc "I don't know..."
    mc "It's almost like as if she read me like a book."
    m 4bi "Well, you were looking at her a bit funny."
    m "Maybe she got the idea that we knew about it from that."
    show yuri at f22
    show monika at t21
    y "She was scrutinizing the letter pretty hard, too."
    y 2bh "Did anyone find it a bit odd that she knew about the letter?"
    show yuri at t22
    "The room falls silent for a second."
    show monika at f21
    m 1br "She's onto us, I'm afraid."
    m 3bi "I surmise that she's the one that wrote the letter in the first place."
    m "From what it sounded like, she would've better anticipated us to come."
    m "We came in a time when she least expected it."
    m 2bp "We're going to have to be a lot more careful if she knows about us."
    show yuri at f22
    show monika at t21
    y 2br "We can't keep leading her on like this."
    y "There has to be a way around it!"
    mc "Wait a second."
    show yuri 4bc at t22
    mc "If everything holds true..."
    mc "Then that should mean that the Ink Demon still exists."
    show monika at f21
    m 1bi "[player], what are you suggesting?"
    m "You can't be saying that we're being watched by two ink creatures at the same time..."
    mc "I skimmed through your notes from the train."
    mc "Rumor has it that he hears everything."
    mc "Every door creak, every rustle of paper..."
    mc "Even this very conversation."
    m "What are you implying?"
    show yuri at f22
    show monika at t21
    y 4bd "Surely you're not suggesting that Bendy already knows about what could happen, right?"
    mc "More or less. Perhaps if we can befriend him, we can get to the bottom of this."
    y 1br "Are you insane?"
    y "He could have the potential of killing us!"
    mc "Then why didn't he kill Henry?"
    show yuri 4bb at s22
    show monika at f21
    m 4bi "[player], the relationship between him and Henry and ours is completely different."
    m "He may not be that willing to cooperate."
    call screen dialog("That's what they all say...", ok_action=Return())
    m 4bg "..."
    m "Eh?"
    m 1bi "Forget I said anything."
    m 1bq "Let's just keep this on the down low until we figure out what the hell is going on."
    show monika at t21
    mc "That seems reasonable."
    mc "I don't suppose that she{nw}"
    a "Is everything alright in there?"
    a "Jeez, you've been in there longer than I ever have, ahaha~!"
    stop music fadeout 1.0
    hide vignette
    play music t8
    show monika at f21
    m 4bi "You don't suppose she heard anything, right?"
    mc "I think we're fine."
    "I turn towards the door."
    mc "We'll be there in just a second!"
    "To our surprise, Alice invites herself in, anyway."
    show monika 1bm at t31
    show alice 0b at t32
    show yuri at t33
    a "You got me worried there!"
    a 0d "Is everyone okay? I hope I didn't upset you or anything..."
    show monika at f31
    m 1bn "No, no..."
    m "I just had to clarify a few things."
    m 1bb "We should be alright, now!"
    show alice at f32
    show monika at t31
    a 0b "Perfect!"
    a "I take it we're ready to head down to the residential areas, then..."
    show alice 0j at hop
    "Alice smiles sweetly."
    show yuri at f33
    y 1bb "Yes, we should be alright."
    y "On your lead, Alice..."
    show monika at thide
    show yuri at thide
    hide yuri
    hide monika
    "We huddle behind Alice as she takes us out of the room."
    return
