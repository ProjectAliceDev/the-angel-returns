label scotia_test:
    stop music fadeout 1.0
    scene bg studio lift
    show alice 1sd at t11
    a 1sd "Have you ever wondered what Heaven is like?" 
    a 1sa "I like to dream that it's quite beautiful." 
    a 1sf "A soft valley of green grass, blanketed by a warm sun." 
    a 1sg "I don't think I'll ever get to see it." 
    a 1sb "Are you ready to ascend, my little errand boy? The heavens are waiting."
    a 1se "{i}*sigh*{/i}"
    $ timeleft = 0 - get_pos()
    show noise at noisefade(8 + timeleft) zorder 3
    show vignette as flicker at vignetteflicker(timeleft) zorder 4
    show vignette at vignettefade(timeleft) zorder 4
    show layer master at layerflicker(timeleft)
    show alice layer master zorder 5
    a 1sa "Ahaha~"
    a 1sb "AHAHAHAHAHA"
    $ style.say_dialogue = style.edited
    a 1sy4 "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA"
    a 1sl "Did you really think I'd let you steal from me?!" 
    a "Did you really think I'd just let you go?!" 
    a 1sy2 "No, Henry!" 
    a 1sy5 "I know who you are! And I know why you're here!" 
    a 1sy1 "And you will not stop what needs to be done!" 
    a 1sy5 "Now come down and bring me back my Boris!" 
    a 1sy4 "It's the most perfect Boris I've ever seen, and I want it! I need it." 
    a 1sy2 "I need it's insides so that I can be beautiful again!" 
    a "Don't you understand? Don't you get it?!" 
    a 1sy5 "Give him to me!!" 
    a 1sy4 "Or better yet, I'll take him!"
    a 1sy5 "Once...{w=0.5} you\'re...{w=0.5} dead!!"
    $ style.say_dialogue = style.normal
    return
