label ch0_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2

    "Well, it's another day at the Literature Club."
    "We've managed to stay as our humble group of five for the past few months."

    show sayori 1a zorder 2 at t11
    s "Heey [player]!"
    mc "You seem in a good mood."
    s "I always am, you goof!"
    show sayori zorder 2 at thide
    hide sayori
    "Sayori's kooky, as usual."

    show yuri 1a zorder 2 at t11
    y "[player], it's good to see you again."
    mc "Yuri, did you dye your hair?"
    y 3n "D-does it look bad?"
    mc "What? No, it's fine!"
    mc "I'm just not used to it."
    mc "It kind of adds a bit more sophistication to you..."
    y 4b "Uu..."
    "We've gotten to know each other quite well, but she's still a little shy."
    mc "It looks nice."
    y 4a "Y-you really think so?"
    y 3f "I-I wanted to try something new."
    y 1a "I should proabbly make some tea."
    show yuri at thide
    hide yuri
    "Yuri walks over to the closet to grab the tea set, as usual."

    show natsuki 1c zorder 2 at t11
    n "You, uh, just going to stare off like that?"
    mc "What? No, I was just thinking..."
    n 2d "Probably should at least blink or something."
    "Aggressive and playful. Not a single thing changed."
    n 5g "You going to keep looking at me like that?"
    mc "..."
    mc "Err, no."
    n 2y "I didn't say you had to stop, dummy."
    show natsuki at thide
    hide natsuki
    "At least I can count on her for contradictions."

    show monika 1b zorder 2 at t11
    m "Hi, [player]!"
    m "It's good to see you again."
    mc "Ah, it's good to see you, too, Monika..."

    show monika 5a at hop
    "Monika smiles sweetly."
    mc "You seem awfully cheerful today."
    m 3b "Of course I am!"
    m "You've been committed to this club since we started!"
    mc "I feel like there's a little more to that..."
    m 5a "Ahaha~"
    m "What makes you think that?"
    "There was no doubt that Monika would always go out of her way to make sure I was okay."
    "But I'm getting a funny feeling that she likes me."
    "She's completely out of my league, but still..."
    mc "A hunch, I guess..."
    m 3b "Don't be so shy about it, [player]! You can trust me, you know..."

    show yuri 1a zorder 3 at f22
    show monika zorder 2 at t21
    y "Anyone want some tea?"
    y "The kettle finished brewing."
    "Slick."
    mc "Sure, I'll take a cup."
    show monika zorder 3 at f21
    show yuri zorder 2 at t22
    m "I'd love to have a cup, too, if you don't mind."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3d "Sure."
    show yuri at thide
    hide yuri
    show monika zorder 2 at t11
    "Yuri walks towards the set and begins to pour out the tea."
    m 1l "You know, [player], I don't think we got to spend much time together..."
    mc "Uh..."
    mc "Come to think of it, you're right..."
    $ consolehistory = []
    call updateconsole("game.setroute(_monika)", "Route set to Monika.")
    call hideconsole
    m 2b "Why don't we do something today, then? Just the both of us..."

    show monika 1g zorder 2 at t21
    show natsuki 5e zorder 3 at f22
    n "Whoa there, Monika!"
    n "You're going to just call the shots like that without a consensus?"
    mc "Natsuki, take it easy."
    mc "It's not fair if I spend time with only you, Yuri, and Sayori."
    show monika zorder 2 at t31
    show natsuki zorder 2 at t32
    show yuri 2f zorder 3 at f33
    y "Uh, the tea is ready..."
    y "Is everything alright over here?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 1e "Hey, don't bud in like that!"
    n 1f "This isn't your concern."
    show monika zorder 3 at f31
    show natsuki zorder 2 at t32
    m 3l "Okay, let's not start a cat fight here..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "Eh?"
    y "I... I just came over to see if you two were ready..."
    show yuri 2f zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "..."
    stop music fadeout 1.0
    "She's pondering again..."
    play music t7
    n 3y "Preparing some tea for the couple, eh?"
    show natsuki zorder 2 at t32
    show yuri zorder 3 at f33
    y 3n "E-Eh?"
    y "N-Natsuki! It's not what you think!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1g "What do you mean by 'the couple', Natsuki?"
    m "We aren't in a relationship."
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 2k "That's funny..."
    n "You seemed pretty chummy with [player] a few moments ago."
    n "Aren't you a bit quick to assume things, Monika?"
    show monika zorder 3 at f31
    show natsuki zorder 2 at t32
    m 2i "Please drop this."
    m "This isn't helping your case."
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 3g "Ha! You're just too embarassed to admit it."
    show monika 1o zorder 2 at t31
    show natsuki 5s zorder 2 at t32
    show yuri 4b zorder 2 at t33
    stop music fadeout 1.0
    "The room falls silent for a second."
    "It's up to me to remedy the situation."
    mc "Natsuki, there isn't a relationship between me or Monika that's beyond this clubroom."

    play music t8
    mc "We're just friends, just like how I am with you, Yuri, and Sayori."
    mc "Well, Sayori's a bit of an exception...{nw}"
    mc "Still, as a friend, you should respect that."
    mc "I've spent a fair amount of time with you three. It's not really that fair if I put Monika out of the picture."
    mc "She may be the President, but she still is a member of the club that deserves the same respect and treatment as everyone else."
    show natsuki zorder 3 at f32
    n 1n "I... I guess so..."
    n 1m "It still isn't fair, though, that she gets to decide that sort of thing."
    mc "She isn't exercising control; she's just making a suggestion."
    mc "I still have the final say."
    mc "As the decider in this conversation, I accept the suggestion."
    mc "Please respect that."
    n 5s "..."
    n 5q "Whatever."
    show natsuki at thide
    hide natsuki
    "Natsuki proceeds to the closet to grab her manga."
    show monika zorder 2 at t21
    show yuri zorder 2 at t22
    mc "As for you, Yuri..."
    mc "I apologize for letting you get caught up in our discussion."
    mc "I hope that you also respect my decision."
    show yuri zorder 3 at f22
    y 1a "Of course. I'll get the tea for you."
    show yuri at thide
    hide yuri

    show monika zorder 2 at t11
    mc "Monika, I'm sorry if..."
    m 1p "I'm fine."
    m "I didn't expect things to get a little out of hand."
    m 1q "I probably shouldn't have asked in the first place..."
    mc "No, no, no,{fast} Monika, it's totally fine!"
    mc "We can still hang out together today."
    mc "I'm not objecting."
    mc "Let's just pretend nothing happened, okay?"
    m 1g "[player], it's a little more complicated than that..."
    m "I..."
    m 1q "Nevermind."
    mc "Do you want me to give you some time to breathe?"
    "Almost instantly, Monika changes her expression, like as if nothing disturbed her."
    m 3b "So, [player]..."
    m "What should we do?"

    mc "Uh..."
    mc "Well, what do you usually do?"
    m 1a "I usually talk to Sayori about future events or prepare things."
    m 5a "But I'm open to any suggestions you have, ahaha~!"
    mc "Well..."
    mc "Usually, I read whatever Yuri or Natsuki are reading with them."
    mc "Do you have a book you're reading yourself?"
    m 1n "Ahaha, well..."
    m "I am reading a book, but it's not really literature..."
    mc "Oh?"
    mc "What are you reading?"
    show monika 1m zorder 2 at t11
    "Monika hands me her book."
    "In inspect the cover and quickly flip through the pages."
    mc "Huh. {i}Python for Dummies{/i}."
    mc "I didn't know you were into programming..."
    m 5a "Ahaha~"
    m "I'm just taking a gander, that's all."
    mc "Back in middle school, I took a class for this exact language."
    mc "Monika, is this Python 2 or Python 3?"
    m 4i "Wait, there's a difference?"
    mc "A huge one at that."
    mc "It's like looking at the vast differences between Susan Campbell and Allison Pendle."
    mc "Yes, both of them did play as Alice Angel from the Bendy cartoons."
    mc "But, their voice styles and mannerisms are pretty different from each other."
    m 1i "I didn't know there were two actresses for that role."
    m "I guess there must have been a change or something."
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    call screen dialog("What the heck just happened?", ok_action=Return())
    m "..."
    m 3g "Tell me you saw that."
    m 4i "It may look like I did something, but I swear I didn't do that."
    m "Something's up with the code..."
    call screen dialog("Yeah, something's up...", ok_action=Return())
    call screen dialog("Looks like she's derailing your conversation.", ok_action=Return())
    m "..."
    m "Who?{nw}"
    call updateconsole("r.cache.clear()", "Clearing cache...")
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/8.ogg"
        renpy.music.play(track, loop=True)
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    call hideconsole
    stop music
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
    play music t3
    m 4i "Wait, there's a difference?{fast}"
    mc "A huge one at that."
    mc "It's like looking at Windows 7 and Windows 8."
    mc "They may perform the same, but they have completely different interfaces."
    m 2i "..."
    m "Did you just seriously bring up Windows 8?"
    m 5b "God, that was the most confusing thing on the planet!"
    mc "You don't need to shout like that, Monika."
    m 1p "Sorry..."
    m "I got a little carried away."
    m 1i "But, seriously, please do {i}not{/i} bring Windows 8 up ever again."
    mc "Uh, okay..."
    mc "Anyway..."
    m 1a "Yes, carry on..."
    mc "There's a huge difference between the two."
    mc "I could tell you everything, but I wouldn't want you to get too horribly confused."
    mc "Monika, have you made your own program yet?"
    m 5a "Ehehe~"
    m "I've been working on something..."
    mc "Wow. I'm surprised you have a lot of time."
    m 1l "Ahaha! I'm not just a student, you know..."
    m 1b "I do a lot of things to keep me occupied."
    m "Sometimes, I like to think to myself that code can be literature."
    mc "I guess that works...?"
    mc "In theory, it's all just written in a different language."
    mc "Doesn't that apply to a niche audience, though?"
    m 5a "Well, I guess you're a part of that audience."
    mc "I guess you're right on that."
    mc "I wouldn't want to write a poem in Python, though..."
    m 1d "Oh! That reminds me..."
    m "We need to start sharing our poems soon!"
    m 1a "Hold on, let me get everyone together..."

    show monika zorder 2 at t21
    m 1b "Okay, everyone!"
    m "It's time to share your poems!"
    show sayori 1a zorder 2 at f22
    s 4r "Yaay!"
    s 1a "I can't wait to read your poem, [player]!"
    "Sayori enthusiastically pulls out her poem from the binder."
    "Monika takes the book from my hands and pulls out her poem from the cover."
    "I walk towards my bag to grab mine, getting ready to share my poem{nw}"
    $ pause(1.25)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.50)
    stop sound
    hide screen tear
    stop music
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
    return

label ch0_end:
    play music t3
    show monika zorder 3 at t41
    show sayori zorder 2 at t42
    show yuri 1a zorder 2 at t43
    show natsuki 1a zorder 2 at t44
    m 4b "Well, that went wonderful today!"
    show monika zorder 2 at t41
    show yuri zorder 3 at f43
    y "Yes, the poems were absolutely exquisite today."
    show yuri zorder 2 at t43
    show sayori zorder 3 at f42
    s 3r "We keep getting better!"
    show sayori zorder 2 at t42
    show natsuki zorder 3 at f44
    n "..."
    n 5q "No comment."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f41
    m "Alright, everyone!"
    m "There's just one more thing we need to address."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 1o "Oh shoots! Spring break!"
    s 1a "Have we decided on what we'll be doing this week?"
    s 2r "I hope it'll be fun!"
    show sayori zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2m "Wait, we didn't decide anything..."
    show natsuki zorder 2 at t44
    show yuri zorder 3 at f43
    y 2e "I don't think we've had the proper time to discuss it..."
    show yuri zorder 2 at t43
    show monika zorder 3 at f41
    m 3i "You're right, we really didn't discuss that."
    m 3g "Sayori, please tell me you have a backup plan for this..."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 2o "Wait."
    "Sayori thinks for a moment, making various faces."
    s 1h "Well, I do have {i}something{/i}..."
    s 1k "I don't know how well it'd work, though."
    s 5a "I forgot to do research on it, ehehe~"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 4i "Wait. You had something..."
    m "But you didn't look into it?"
    m "It's kind of late now to do anything about it, but what is it?"
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 1l "So, uh... I got a letter in the mail..."
    s "And I opened it and read the letter..."
    s 5a "And there may or may not be someone willing to support the club?"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "..."
    m 1g "Sayori, why didn't you say something?"
    m "I could've looked into it myself..."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s "Ehehe~"
    s 5b "It's kind of personal..."
    s "It was, uh, written for me, you know?"
    mc "Sayori, you don't need to give us all of the details."
    mc "You're not supposed to tell us that kind of thing, anyway."
    s 5c "Meanie."
    show sayori zorder 2 at t42
    show yuri zorder 3 at f43
    y 1f "It sounds like an opporunity."
    y "I'm a bit surprised that someone sent you a letter and knew about our literature club."
    y "Who's the letter from?"
    show yuri zorder 2 at t43
    show sayori zorder 3 at f42
    s 1l "Ehehe..."
    s "J-Joey Drew?"
    show sayori zorder 2 at t42
    "An awkward silence occurs."
    show natsuki zorder 3 at f44
    n 2p "Oh, hell no!"
    "Natsuki steps out of the conversation."
    show natsuki at thide
    hide natsuki
    show yuri zorder 3 at f43
    y "Joey Drew?"
    y 1g "The name sounds familiar, but I can't recall it..."
    show yuri zorder 2 at t33
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1g "Joey Drew?"
    m 4g "As in Joey Drew Studios?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 5a "Yeah..."
    show monika zorder 3 at f31
    show sayori zorder 2 at t32
    m 1i "..."
    m 1d "How does a cartoon studio know about you and this club?"
    m "I'm a bit flattered, but this seems skeptical."
    m "I now understand why you wanted to do more research."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 3f "How interesting..."
    y "What did he say in the letter?"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1c "Well, he said some stuff about being interested in literature and that sort of thing."
    s "And then he went on a splurge about animations."
    s "And then he talked about formally inviting us to check out the studio for a week..."
    s 1k "But it sounded fishy..."
    s "It sounded like it was written from a girl."
    mc "Sayori, how would you know that?"
    mc "You practically just appreciate every poem I throw at you, regardless of its quality."
    s 5c "Hey!"
    s "That has nothing to do with it!"
    s "I like reading your poems!"
    s 1j "But, anyway..."
    s "I wanted us to be safe."
    s 1h "So that's why I didn't say anything about it."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "Sayori, I appreciate you looking out for our welfare."
    m "Personally, I'd like to take a look. Do you have a copy of the letter on you?"
    "Sayori hastily grabs the letter from her bag between her math notebook and her English textbook."
    "Monika carefully uncrumples the envelope and pulls the letter out."
    mc "Sayori, you got to be a little more careful with your stuff..."
    show sayori zorder 3 at f32
    show monika zorder 2 at t31
    s 1j "I was in a rush!"
    s 5d "I overslept again this morning, you know..."
    show monika zorder 3 at f31
    show sayori zorder 2 at t32
    "Monika scans through the letter."
    m 1i "Mhm..."
    m "I see why you're concerned."
    m 4i "There is some questionable language in here that suggests that this might be a trap."
    m "I, for one, am not able to understand the condition of the studio at this time."
    m "Furthermore, there's a few ink splatters on the corners of the letter."
    m "Something tells me that it's a mess..."
    m 1i "Nonetheless, Sayori, it doesn't appear to be written by a girl."
    m 5a "Rather, I just think Joey likes you, ehehe~"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 4p "Uwaa~!"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3d "Aww, how cute!"
    call screen dialog("Uh...", ok_action=Return())
    call screen dialog("Does she know?", ok_action=Return())
    call screen dialog("Oh, God...", ok_action=Return())
    y "I didn't realize that that kind of a spiritual figure would like you..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1i "Wait, what do you mean by that?"
    show sayori zorder 3 at f32
    show monika zorder 2 at t31
    s 2w "How can a dead person like me?"
    s "That's not fair!"
    mc "Sayori, are you..."
    s 1g "I'm fine..."
    show monika zorder 2 at t41
    show sayori zorder 2 at t42
    show natsuki 2c zorder 2 at f43
    show yuri 3f zorder 2 at t44
    n "No wonder you're skeptical!"
    n "Good thing you didn't speak of this... until now."
    n "Sayori, that's hella freaky."
    n "Maybe you're right..."
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m "Is he really dead?"
    m "It's hard to say with this letter..."
    show natsuki zorder 3 at f43
    show monika zorder 2 at t41
    n 4f "Gimme that."
    "Natsuki snatches the letter from Monika and scrutinizes the contents."
    n 5s "..."
    n 5h "Not gonna lie here, it really {i}does{/i} sound like a girl wrote it."
    n "Joey would have more substance in his letters."
    n "This?"
    n 4e "Absolute garbage."
    n "I don't think I've ever read a paragraph more infested with the word 'dream' than anything else."
    n "It's too cute to come from a guy."
    show yuri zorder 3 at f44
    show natsuki zorder 2 at t43
    y "Like you?"
    show natsuki zorder 3 at f43
    show yuri zorder 2 at t44
    n 1v "{i}I'm not cute!{/i}"
    n 5e "That's beside the point, anyway!"
    n 5c "Sayori could be onto something here."
    n "This doesn't sound at all like something from him."
    n "There's absolutely no way!"
    show yuri zorder 3 at f44
    show natsuki zorder 2 at t43
    y 2h "How would you know, Natsuki?"
    y "It's not typical of you to read literature like {i}The Illusion of Living{/i}."
    show natsuki zorder 3 at f43
    show yuri zorder 2 at t44
    n 5e "Whoa, slow down there!"
    n "Mind you, there's a manga version of that book!"
    n "It's a literal reproduction of the book!"
    n 5r "I read that one."
    n 5y "And I liked it!"
    n 2c "Point is, we shouldn't trust this guy-gal-thing."
    n "It's too dangerous to be meddling with that, anyway."
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1i "I'm glad we could have your expertise on board with this."
    m "To be honest, I'm a bit skeptical myself."
    m 4e "But, I'm sure this mysterious author has his or her reasons."
    m "I'm kind of a but curious to see this place, anyway."
    m 1b "We pass by it all the time but never stop in."
    show natsuki zorder 3 at f43
    show monika zorder 2 at t41
    n 5p "No way!"
    n "This is too risky!"
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 4b "As long as we're careful, I don't possibly see what could go wrong."
    show natsuki zorder 3 at f43
    show monika zorder 2 at t41
    n 5p "Did a rock hit your head or something?"
    show yuri zorder 3 at f44
    show natsuki zorder 2 at t43
    y 2b "I'm sure there won't be a problem if we stick together and use common sense."
    y "It adds a bit of mystery to our spring break."
    show yuri zorder 2 at t44
    show sayori zorder 3 at f42
    s "Guys, doesn't this concern you?"
    s "I don't want us getting hurt!"
    show sayori zorder 2 at t42
    mc "Let me take a look."
    "Natsuki hands me the letter."
    call showletter(letter_1)
    mc "If you girls really want to do this, we have to be careful."
    mc "Any wrong move could cost us big time."
    mc "Sayori, I'm sure that whoever wrote the letter to you must like you or tolerate you enough to not hurt you."
    mc "Natsuki, consider this a getaway from troubles at home."
    show monika zorder 3 at f41
    m 5a "Then it's settled!"
    m 1a "Be sure to pack your bags and any safety equipment!"
    m 4b "We're going on an adventure."
    show sayori zorder 3 at f42
    show monika zorder 2 at t41
    s 2r "Okay!"
    show yuri zorder 3 at f44
    show sayori zorder 2 at t42
    y 3d "This'll be thrilling!"
    show natsuki zorder 3 at f43
    show yuri zorder 2 at t44
    n 5s "..."
    n 5h "Alright, if you say so..."
    return
