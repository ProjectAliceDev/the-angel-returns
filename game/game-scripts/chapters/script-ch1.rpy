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
    m "I couldn't find an extra pair of clothing, so I just used one that I packed!"
    m "I don't have a lot of clothes, ahaha~."
    show yuri zorder 3 at f33
    show monika zorder 2 at t31
    y 1bf "For someone of your stature, I would've thought you had a lot."
    show monika zorder 3 at f31
    show yuri zorder 2 at t33
    m 2bd "Well, not necessarily..."
    m "I like having a limited wardrobe."
    m 4bd "It helps me stay focused on what needs to get done."
    m 4bn "I'm not really that into fashion either, ehehe~"
    m "My parents picked most of my clothes..."
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 5bk "Well, at least you're here..."
    n "Where's this place, anyway?"
    n "And where's Mio?"
    show yuri at thide
    hide yuri
    show sayori 1bc zorder 3 at f33
    s "I think we're supposed to take a train there or something..."
    show sayori zorder 2 at t33
    show monika zorder 3 at f31
    m 2bc "You're right, it's a bit far from here."
    m 2bd "The next train should be leaving in thirty minutes or so."
    m "Mio's already there at the studio and she's watching the schedules for us."
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
    m 2bd "I was doing some more research last night with Yuri about the studio."
    m 4bd "From our records, Mr. Drew had passed a few months before Sayori received the letter, which makes sense."
    m "Unfortunately, we found no records of Alice Angel herself taking over."
    m "It's filed under a man named 'Henry', but the day-to-day operations are managed by a 'Susan Campbell', the original voice actress."
    mc "Susan Campbell? That's an odd choice to leave a huge studio to..."
    m 2bd "It is a bit odd, but I guess Joey trusted her to keep things moving smoothly if Henry wasn't up to the task."
    m "This is probably why you thought Susie wrote the letter."
    m "I'm a bit worried, to be honest."
    m "Further research suggests that Ms. Campbell's personality is, well, a bit volatile."
    m "She didn't handle her replacement of roles very well."
    m "She was a bit skeptical to take such an administrative role at first."
    mc "I guess she came to her senses afterwards, right?"
    mc "Either that or she died and this 'Alice' woman took over for her."
    m 4bi "That's when things got weird. Like, {i}really{/i} weird."
    m "Joey had been working on an ink machine to bring cartoons to life."
    m "You know, like one of the 3D printers at school, only on a biological scale."
    mc "Okay... and?"
    m "Some sites and sources have suggested that he used this machine on his employees to create his perfect cartoons."
    m 2bf "Isn't that kind of messed up?"
    mc "..."
    mc "Uh..."
    mc "I mean, I did see it coming, but I don't think that she'd be that paranoid."
    m 4bf "Rumor has it that he, out of remorse, committed suicide."
    m "Alas, other sources have stated that there were successful prints without the aid of a human."
    m "They tend to not last long, though..."
    m "We have to be really careful, [player]..."
    m 4bi "Whatever we do, we have to avoid that machine at all costs."
    mc "Right."
    m "There may be hope if it does happen."
    m 2bd "Surprisingly, they have an updated model."
    m "It's clean, compact, and it's programmable."
    m "The studio's been writing APIs for it in Python."
    m "Should something go wrong, there's a Python script that can decouple a human from their inky counterpart."
    m 2bn "Unfortunately, the success rate of the script is very low for humans."
    m "Not to mention it's flagged as a 'legacy' API, which I am assuming that means that cartoon characters are made much differently now."
    m 2bd "Somehow, the success rate is a bit higher for robots, which is a bit weird..."
    m 2bn "{i}*Sigh*{/i}"
    m 2bi "I don't want anyone else to know about what I just told you."
    m "Only Yuri, you, and I know about it."
    mc "What about Mio?"
    mc "I feel like she would know about this, too."
    m 1bc "Well, I was chatting with her last night, too."
    m "She says that the place has a lot of backstory, but most of it is 'irrelevant'."
    m "She also told me that Susie died, which didn't make sense to me at first."
    mc "Dead?"
    mc "{i}Maybe I was right...{/i}"
    m 1bi "I don't think we should be jumping to conclusions that quickly."
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
    $ aliceangel.send_message("Okay, I'm done waiting. Let's cut to the chase!")
    call screen alert("Reload Required", "The script has been modified and needs to be reloaded.", ok_action=Return())
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
    play music bt3
    show monika 1bc zorder 2 at t31
    m "Whoa..."
    m "This looks totally different from the images on Google."
    show yuri 1be zorder 2 at t33
    y "This isn't what I expected..."
    mc "I think this is only the lobby."
    show mio 1 zorder 2 at t32
    mi 1e "Hey, everyone!"
    mi "I hope the directions weren't too confusing, ehehe~"
    mi 1b "Anyways, Alice is aware that you all came, but I have to warn you."
    mi 4l "I'm kind of the only human she's had constant contact with."
    mi "I'm sorry if she gets abrasive at first..."
    show mio at thide
    hide mio
    "Suddenly, we hear soft singing coming from the corner."
    $ a_name = "???"
    a "{i}I got a friendly halo and I'm filled with love...{/i}"
    show alice 0j zorder 3 at f32
    a "{i}I'm Alice...{/i}"
    a 0d "...Angel?"
    a 0g "Who {w=1.0}{i}are{/i} you people?"
    show alice zorder 2 at t32
    show yuri zorder 3 at f33
    y 3bp "A-aah, s-sorry!"
    y 4bc "Th-the door was unlocked."
    y "W-we thought the studio was o-open..."
    show yuri at lhide
    hide yuri
    show mio 1 zorder 2 at t33
    show monika zorder 3 at f31
    m 3bd "My apologies if we came here unannounced."
    m "We came here as per a response to a letter you sent to the vice president of our literature club, Sayori."
    m "As well as Mio's recommendations."
    show mio zorder 3 at f33
    show monika zorder 2 at t31
    mi 1e "Alice, this is the Literature Club."
    mi "I know we're kind of small..."
    show mio zorder 2 at t33
    show alice zorder 3 at f32
    $ a_name = aliceangel.short_name
    a 0d "The Literature Club...?"
    a "Uh..."
    mc "Perhaps it would help if I gave you the letter you wrote to Sayori."
    "I hand the woman the letter from my coat pocket."
    a "..."
    a 0d "Oh..."
    a "Ah!"
    "She lightly chuckles to herself."
    a "It's {i}that{/i} letter!"
    a 0b "I'm sorry, I must have forgotten that I wrote this one, ehehe!"
    a "So this is the Literature Club, eh?"
    a 0j "Well, then... Welcome to Angelhus Productions, formerly Joey Drew Studios, home of the Bendy and Alice Angel cartoons!"
    a "A {i}lot{/i} has changed since you got this letter, so, uh..."
    a 0b "Allow me to introduce myself..."
    show mio zorder 3 at f33
    show alice zorder 2 at t32
    mi "Ahaha, I'll take care of that for you."
    mi "This guy here is [player], the only boy in our club!"
    mc "Uh..."
    "Crap. Mio put me in an awkward situation..."
    mc "Nice to meet you, Alice."
    show alice at f32
    a "Ahaha, don't sweat it!"
    a "He kind of looks like Henry, doesn't he, Mio?"
    show alice at t32
    mi "I guess you could say that."
    mi "Anyways, this is Monika, the president of the club."
    show mio zorder 2 at t33
    show monika zorder 3 at f31
    m 1bb "A pleasure to meet you, Alice!"
    m "I can't wait to discuss things with you about the club!"
    show monika at thide
    hide monika
    show natsuki 4bd at t31
    show mio zorder 3 at f33
    mi "And this is Natsuki, always full of energy!"
    show mio zorder 2 at t33
    show natsuki zorder 3 at f31
    n "And I finally meet the Angel herself!"
    n "I hope you like manga as much as I do!"
    show natsuki at thide
    hide natsuki
    show alice at f32
    a 0c "...{w=1.0}Manga?"
    show alice at t32
    show mio zorder 3 at f33
    show sayori 1br at t31
    mi "And this is Sayori, the vice president."
    show mio at t33
    show sayori at f31
    s "Yaay! You're real!"
    s "I get to be around an angel for a week!"
    show sayori at thide
    hide sayori
    a 0b "Ahaha, she seems cheerful!"
    show mio at f33
    mi "And, finally, we have Yuri, the smartest in the club."
    show yuri 1ba at f31
    show mio at t33
    y "It's a pleasure meeting you."
    y 2bq "I apologize for running off..."
    show yuri at thide
    hide yuri
    show monika 1ba at t31
    show mio zorder 3 at f33
    mi "Everyone, this is the Angel herself, Alice."
    mi 5x "She's quite a gal! (pun intended)"
    show alice zorder 3 at f32
    show mio zorder 2 at t33
    a 0m "Ehehe~"
    a 0n "I was kind of hoping you didn't say that..."
    show mio zorder 3 at f33
    show alice zorder 2 at t32
    mi 1e "Ahaha, no need to be embarassed, Alice!"
    mi "Why don't we head to the breakroom for now?"
    show alice zorder 3 at f32
    show mio zorder 2 at t33
    a "Uh, sure..."
    a "I'll meet you there in a moment..."
    show alice at lhide
    hide alice
    show monika at f31
    m 1bg "Is she alright?"
    show mio at f33
    show monika at t31
    mi 4l "I think she's just a bit overwhelmed."
    mi 3b "[player] and I will go talk to her. We'll meet you down there in a bit."
    show monika at thide
    show mio at thide
    hide mio
    hide monika
    "I follow Mio down the corridor to reach some offices, presumably where the Ink Machine used to be."

    stop music fadeout 1.0
    scene bg studio inkmachine
    with wipeleft
    "I glance around the room."
    "Surprisingly, nothing in here resembles an ink machine."
    "She probably forgot to change the text or something..."
    mc "...Alice?"
    show alice 0g at f21
    show mio 1h at t22
    play music b1
    a "Aah!"
    a "How did you find me?"
    a "You guys just spawn out of nowhere..."
    mc "I followed Mio down here..."
    mc "I'll say, your directory's a bit misleading."
    a 0d "We haven't had the time to change it."
    a "You know, in all of the time we had to build a new studio, we somehow forgot about the sign."
    a 0n "I digress."
    a 0i "Mio, you shouldn't have dragged him here."
    a 0g "Why did you come here, [player]?"
    mc "We figured that we wanted to check ou-{nw}"
    a "No, not that."
    a "Why are {i}you here{/i}?"
    mc "..."
    show mio at f22
    show alice at t21
    mi 4i "We noticed you trailed off after I made that remark."
    mi 1g "I have [player] here with me because he's pretty good at understanding things."
    show alice at f21
    show mio at t22
    mc "Alice, how long has it been since someone's come down here that isn't Mio?"
    a "..."
    a 0n "Too long ago."
    a "Henry came down here because Joey had sent him a letter, too..."
    a 0g "And look at where I am."
    a "I'm forever trapped in this..."
    a "...lost memory."
    a "Heh, at least there's a new coat of paint or something..."
    a "God, it's so weird having real human beings here."
    a 0i "But you already knew that, didn't you?"
    stop music fadeout 1.0
    mc "..."
    mc "I had a funny feeling."
    mc "Monika told me a few things before we got here."
    play music t9
    a 0m "Man, it must be a living {i}hell{/i} dealing with those girls..."
    mc "They're not as bad as you think."
    mc "You get kind of used to it, I guess..."
    a 0m "That's what Joey said to everyone else about Susie."
    a 0n "He was a good liar. Sammy, too..."
    show mio at f22
    show alice at t21
    mi 4h "It's okay, you can tell him."
    mi 4g "He'll understand, right?"
    "I nod."
    show alice at f21
    show mio at t22
    a 0o "{i}*Sigh*{/i}"
    a "Here we go, I guess..."
    a 0g "Everyone treats me so much differently ever since the whole...{w=1.0} {i}Susie{/i} thing."
    a "Allison..."
    a "Well, I guess it's kind of pointless to really explain all of that."
    a "You already know what had happened, right?"
    a 0m "Ahaha~"
    a 0g "It's just so weird now... everyone thinks I'm Susie, but I'm not, I swear!"
    a "It's like I'm living someone else's life..."
    show alice 0o at s21
    mc "..."
    mc "Alice, aren't you being a little hard on yourself?"
    mc "I know some of us may be skeptical, but that's not going to make us treat you differently."
    mc "Sometimes, it just takes some time to really see a change."
    mc "It's obvious to me that Mio already sees you for who you are and not as Susie."
    mc "A lot of people see Natsuki as an agressive, underaged girl."
    mc "If you really get to know her, though, she's an interesting person to be around."
    mc "Don't beat yourself up over it. I'm sure the club members will understand soon."
    mc "Promise me and Mio that you'll be yourself, okay?"
    a 0t "..."
    a 0m "Well, [player], I don't know if anyone's told you that you are a man of many words..."
    a "But I guess I have to trust you now."
    stop music fadeout 1.0
    show alice at t21
    show mio at f22
    mi 5e "That's the spirit!"
    play music b7
    show alice at f21
    show mio at t22
    a 0d "Tell me, are they really obsessive over cuteness?"
    mc "What?"
    "Mio stifles a chuckle."
    a "What? It's a legitimate concern of mine."
    mc "It's okay. Just be yourself."
    a "Fine, then..."
    a "We should probably meet up with them before things get a bit hectic."
    mc "Of course!"
    show mio at f22
    show alice at t21
    mi 5x "To the break room!"
    show alice at thide
    show mio at thide
    hide mio
    hide alice
    "We proceed to the break room, with Alice leading the way."
    return

label ch1_end:
    stop music fadeout 1.0
    scene bg studio breakroom
    with wipeleft
    play music t3
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
    a 0d "I didn't mean to make things awkward..."
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
    m 2bb "Sayori, Natsuki, Mio... please follow Alice to the residential areas."
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
    "Yuri eyes the quartet down as they exit the break room and close the doors."

    show vignette zorder 1 at vignettefade(1.5)
    stop music fadeout 1.5
    show monika zorder 2 at f21
    show yuri 1be zorder 2 at t22
    m 1bi "[player], was everything alright with Alice?"
    mc "Yeah, I guess."
    mc "She's just a bit overwhelmed at everything."
    play music b5
    show yuri zorder 2 at f22
    show monika zorder 2 at t21
    y 2bt "She doesn't seem trustworthy."
    y 1bh "She could be possibly watching our every move."
    y 1bf "I'll admit, we did walk in on her unexpectedly."
    y "Still, she raises some suspicions."
    mc "Well, it doesn't help that she knows that we know about what happened before."
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
    y 2bh "Did anyone find it a bit odd that she forgot about the letter?"
    show yuri at t22
    "The room falls silent for a second."
    show monika at f21
    m 1br "She's onto us, I'm afraid."
    m "From what it sounded like, she would've better anticipated us to come."
    m "We came in a time when she least expected it."
    m 2bp "We're going to have to be a lot more careful if she knows about us."
    show yuri at f22
    show monika at t21
    y 2br "We can't keep leading her on like this."
    y "There has to be a way around it!"
    show yuri 4bc at t22
    mc "Guys, I understand if you're being skeptical and all..."
    mc "But we shouldn't try to make her out as an enemy."
    mc "It looks like she's a bit rattled over a few things."
    show monika at f21
    m 1bi "[player], what are you suggesting?"
    m "You can't be saying that we should be trusting her..."
    mc "Mio trusts her a lot, and she wanted me to come along because she thought I would understand."
    mc "If you really want to think of it like this, she's kind of like Natsuki or anyone else in the club."
    mc "Looks aren't everything, Monika."
    show yuri at f22
    show monika at t21
    y 1bs "I think [player]'s right, Monika."
    y "I think we're getting a bit too skeptical."
    y 1bs "He really didn't get to know us until he interacted with us more."
    y 3bs "There should be no reason why we don't do the same to her."
    show monika at f21
    show yuri at t22
    m 1bq "Jeez..." 
    m "Let's just keep this on the down low until we figure out what the hell is going on."
    show monika at t21
    mc "Alright, you do your thing."
    mc "Meanwhile, I'm going to make sure she doesn't see us as villians."
    mc "Just don't try to aggravate her or anyth{nw}"
    a "Is everything alright in there?"
    a "Jeez, you've been in there longer than I ever have, ahaha~!"
    stop music fadeout 1.0
    hide vignette
    play music b7
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

    scene bg studio lift
    with wipeleft
    "As we reach the lift, Alice signals Yuri to step in first."
    show alice 0b at t21
    show yuri 1ba at t22
    a "I just want to chit-chat with Monika and [player] for a second."
    "Yuri nods."
    show yuri at f22
    y "Which floor do I go to?"
    show alice at f21
    show yuri at t22
    a "Level {i}S{/i}."
    a "Follow the signs to get to the Archives."
    a "You'll know what I mean when you see it."
    "Yuri nods again in response and pushes the button, watching as the doors close."
    show yuri at thide
    hide yuri
    show monika 1ba at t22
    "The elevator sinks down, taking her straight to Level S."
    a "Now, as for you two..."
    show alice at f21
    stop music fadeout 1.0
    a 0d "I'm sorry if I seem a little crusty and abrasive about this."
    play music b5
    a "But, I need you to understand something."
    a 0i "Things have changed around here."
    a "I'm not that sadomasochist 'Susie'. Trust me."
    a 0n "Please, do your best to not associate me with that her."
    a "{i}*Gag*{/i}"
    show monika at f22
    show alice at t21
    m 1bi "Uh..."
    m 1bn "Don't you think that's a bit early to tell us something like that?"
    show alice at f21
    show monika at t22
    a 0g "I already know that you are well aware of what's going on here."
    a "I would expect that from a club President. Wouldn't you?"
    show alice at t21
    "The room yet again falls silent."
    mc "Um..."
    mc "Why am I exactly a part of this conversation?"
    show alice 0l at f21
    a "Ehehe~"
    a 0i "That's besides the point."
    a "I don't know if you have plans to stalk me or whatever."
    a "But let me make one thing clear."
    show monika 1bg at t22
    a "I don't like liars, and I don't like those who try to double-cross me."
    a "It's best that you don't end up on my bad side."
    a "Do I make myself clear?"
    show alice at t21
    mc "..."
    mc "Yes, ma'am{nw}"
    show alice at f21
    a 0k "Ahaha, I'm not worried about you, darling!"
    a 0i "I'm more concerned about your friend here."
    show alice at t21
    show monika at f22
    m "..."
    m "...me?"
    m 4bi "Well, as long as you don't try to harm us in any way, I don't see why we can't trust you."
    m "I'm sure you'll respect my decisions as club President."
    m "I'm only looking out for my club's safety."
    show monika at t22
    show alice at f21
    a "Perhaps so."
    a "But if you really were looking out for your members..."
    a "...coming here would've been an absolute mistake."
    a "Don't think for a second that I'm not onto you, Monika."
    a "You may have had control at your clubroom."
    a "But, you're entering my territory."
    a "Just don't piss me off, okay?"
    a "It's a practically easy thing to do."
    a 0d "We'll have to wait for the lift to come back."
    a "In the meantime, I'd like to talk to [player] alone for a second."
    show alice at t21
    show monika at f22
    m "..."
    stop music fadeout 1.0
    m 1bi "Fine."
    m "Do what you wish."
    show monika at thide
    hide monika

    play music b7
    show alice at t11
    a "..."
    a "Uh... okay."
    a "Does she usually do that?"
    mc "Not really."
    mc "I mean, I did promise to spend a little more time with her."
    a 0g "I wasn't too... {i}aggressive{/i}, was I?"
    "I honestly cannot find an answer for that."
    mc "Um..."
    mc "Mayb-{nw}"
    a 0n "Nevermind that."
    a 0d "I'm sure she'd get over it quite easily."
    a "She seems like the type, anyway..."
    a "I just don't want things to get ugly around here, you know?"
    mc "I get it."
    mc "You can trust Monika, though. She's pretty shrewd about things and will use her best judgement."
    a 0i "You call deleting your friends and rewriting the entire game so you can be with the player forever 'best judgement'?"
    a "Jeez, [player], I didn't realize you were {i}that{/i} dense!"
    mc "Wait, what are you talking about?"
    a 0g "Please tell me that's a joke."
    a "Perhaps you should be the one wary of Monika."
    a "I don't know what the hell she's going to do with you."
    a 0d "Well, it looks like the lift is returning."
    a "I'll go talk to Monika myself. You can go down there and meet up with everyone else."
    a "Level S. Just follow the screams... or giggles. It's probably giggles, if anything, knowing those girls."
    a 0k "Ahaha~"
    show alice at thide
    hide alice
    "Screams?"
    "I should probably be careful."
    "With that in mind, I step into the lift and push the button for Level S."
    "I just hope this doesn't end horribly."
    $ renpyApp.send_temporary_notification("Character file modified", "Mio's character file has been updated.", action=Return(0))
    return
