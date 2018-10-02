label ch0_main:
    stop music fadeout 1.0
    scene bg club_day
    with dissolve_scene_half
    play music t2

    "Here we are again: another day at the Literature Club."
    "Despite the fall semester's turmoil, the club's stayed pretty consistent."
    "I look around the room to see the girls once more."

    show sayori 1a at t11
    s "Hi again, [player]!"
    mc "Hey, Sayori."
    s 4x "I'm excited to share poems today."
    s "I think you'll like mine."
    mc "Well, you do seem to have gotten a lot better since the first week of this club."
    mc "I'm looking forward to it, too."
    s 2q "I'm looking forward to spring break~"
    mc "Sayori, that's not even related."
    s 5a "Ehehe~"
    s "Well, you know... always thinking ahead..."
    mc "Yeah, in conversation, silly..."
    s 1l "I know, I know..."
    s "It's just..."
    mc "Just what?"
    s 1b "Monika and I have been planning the spring break for weeks now."
    s 4r "I'm just so excited to share today!"
    mc "..."
    mc "I have a funny feeling your poem's about that..."
    s 5a "Maybe..."
    mc "Not that it's a bad thing..."
    "I hadn't even really thought about spring break."
    "The quarter tests had been stressing me out for the past few weeks."
    "I had to study pretty hard for a few of them."
    mc "Well, hold on to your exci-{nw}"
    show sayori at thide
    hide sayori
    "Just like that, she's already sitting down, coloring in some pamphlets."
    mc "Yup..."
    "Typical Sayori."
    "I notice Natsuki and Yuri in the corner."
    "They're usually fighting about something, but today seems different."
    "I listen in for a brief moment."
    show yuri 1a at t21
    show natsuki 4j at t22
    y 1b "So, Natsuki, what did you think?"
    show natsuki at f22
    n 4k "Well, it wasn't all that bad, I guess."
    n "Now tell me how you found a novel with a manga version again..."
    "Ah, of course."
    "I forgot that Yuri found a novel that also had a manga counterpart."
    "Despite the arguments, Yuri still seems to try putting effort into being amiable with Natsuki."
    "This is probably the first time I've seen them not fighting..."
    show yuri at f21
    show natsuki at t22
    y 1f "Well, I just kind of searched Amazon and found something."
    y "I didn't quite know what to expect when getting the books."
    y 1q "I, uh..."
    y 1o "Oh, God..."
    show natsuki at f22
    show yuri at t21
    n 2m "Yuri, I'm not asking for your browser history."
    show yuri at h21
    show natsuki at t22
    y 3p "W-what? That's... not..."
    show natsuki at f22
    show yuri 3o at t21
    n 2h "Besides... I wouldn't care about what you searched, anyway."
    n 5f "Not as much as [player] over here!"
    mc "Wait, what?"
    "Shit. She caught me right in the act."
    n 1e "What the hell are you thinking eavesdropping like that?"
    mc "Jeez, you don't need to be all rude about it..."
    n 5o "Mind your own damn business next time!"
    n 1r "Come on, Yuri, we should move elsewhere..."
    show yuri at thide
    show natsuki at thide
    hide natsuki
    hide yuri
    "I stand still for a moment, trying to recollect what happened."
    "Did she just...?"
    "Wow, the dynamic's changed today..."
    "I take a look around the room again."
    "Yuri and Natsuki reseat themselves by the makeshift table."
    "Sayori's coloring more pamphlets on the side."
    "However, something felt a bit off."
    mc "Hey, guys?"
    mc "Where's Moni-{nw}"
    "Suddently, the doors near the table burst open."
    "Monika rushes through, sweat dripping down from her face."
    show monika 1 at t11
    m 1l "Hi, everyone!"
    m "Sorry that I'm a bit late..."
    show sayori 1 at t22
    show monika at t21
    s 1h "What happened, Monika?"
    s "You look like you've been running around..."
    show monika at f21
    m 1b "I'm alright, Sayori!"
    m 1n "I was just running a bit late."
    mc "Hi, Monika."
    show monika at h21
    m 5a "Oh, hi, [player]!"
    "Monika smiles sweetly."
    "For a while, we didn't say a word."
    "Sayori's eyes bounce between me and Monika repeatedly."
    "Monika locks her eyes onto mine like a target."
    "I sheepishly look back at her."
    "Sayori must have noticed me as she pipes up."
    show sayori at f22
    s 2x "Today's the day, Monika!"
    s 4r "Spring break plans!"
    show monika at f21
    show sayori at t22
    m 1b "Ah! Yes, that's right..."
    m "I almost forgot about that..."
    
    
    call showletter(letter_1)
    $ poemsread = 4
    mc "..."
    mc "Well, Sayori's claims and Mio's claims are valid."
    mc "It looks like she does have interest."
    mc "Suffice to say, Natsuki's claims are also valid."
    mc "I don't think I've seen the word 'beautiful' pop up any more times than in this letter."
    mc "We should be careful."
    mc "Any wrong move could cost us big time."
    mc "Sayori, I'm sure that whoever wrote the letter to you must like you or tolerate you enough to not hurt you."
    mc "Natsuki, consider this a getaway from troubles at home."
    show monika zorder 3 at f41
    m 5a "Then it's settled!"
    m 1a "Be sure to pack your bags and any safety equipment!"
    m 4b "We're going on an adventure."
    show sayori zorder 3 at f44
    show monika zorder 2 at t41
    s 2r "Okay!"
    show yuri zorder 3 at f43
    show mio at thide
    hide mio
    show sayori zorder 2 at t44
    y 3d "This'll be thrilling!"
    show natsuki zorder 3 at f42
    show yuri zorder 2 at t43
    n 5s "..."
    n 5h "Alright, if you say so..."
    show natsuki at thide
    show yuri at thide
    show sayori at thide
    hide natsuki
    hide yuri
    hide sayori
    show monika zorder 2 at t11
    m 1b "Remember to stay safe, everyone!"
    m "We'll go over a few things in the morning before we venture off."
    m 4b "Let's meet in front of campus tomorrow morning to take inventory!"
    m "I look forward to having another adventure with you, [player]..."
    m 5a "Ehehe~"
    mc "You too, Monika..."
    show sayori 2b zorder 3 at f33
    s "Before I forget!"
    s "I'll be coming home a bit later, [player]."
    s 2a "I'm shopping with Natsuki for supplies and stuff."
    mc "Okay, let me know if you need anything."
    s 1j "Wait! I'm supposed to say that!"
    s 1x "You goof!"
    mc "Well, some things don't go as planned."
    mc "Just stay safe, alright?"
    s "No problemo!"
    show sayori at thide
    hide sayori
    m 2b "You're such a dynamic pair!"
    mc "Just watching out for each other, that's all."
    m "I shall see you in the morning, then."

    scene bg residential_day
    with wipeleft_scene

    "With that, I walk home, checking my phone once in a while to see if Sayori texted me."
    "Spending a solid week in a cartoon studio with:"
    show sayori 1 zorder 2 at t11
    "Sayori,"
    show sayori at thide
    hide sayori
    show natsuki 4 zorder 2 at t11
    "Natsuki,"
    show natsuki at thide
    hide natsuki
    show yuri 1 zorder 2 at t11
    "Yuri,"
    show yuri at thide
    hide yuri
    show mio 1 zorder 2 at t11
    "Mio,"
    show mio at thide
    hide mio
    show monika 1 zorder 2 at t11
    "and, of course, Monika."
    "This could totally work out and bring us closer to each other."
    "However, this could also be the end of us..."
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I just need to grab a few things and I should be ready for the morning."
    "It's the beginning of a wild adventure..."
    return
    