label pre_ch1:
    stop music fadeout 1.0
    scene bg bedroom_night
    with dissolve_scene_full
    "It's midnight."
    "And I have randomly awoken."
    "And I have no clue why."
    "Well, I guess I could probably check to see if I have any new emails."
    "Sayonika did mention something about emailing us before the trip about some 'critical information'."
    "Maybe she sent it already?"
    scene mc_desktop
    with dissolve_scene_half
    python:
        mailApp.ask_app_permissions()
        get_mail_input = mailApp.send_temporary_notification("New Mail from Sayonika", "Please open Mail.RSS to view the message.", action=Return('get_mail'))

        if get_mail_input == 'get_mail':
            renpy.call_screen("mail_view", "About the trip", "Sayonika <sayonika@maidcafe.me>", emailmsg[0])
        else:
            pass
        
    call pre_ch1_loop

    scene bg bedroom_night
    with dissolve_scene_half
    "Well, I certainly didn't see that coming."
    "How is Mio everywhere?"
    "And why is she... horrible?"
    "I can only hope she doesn't rain on our parade for the next week."
    "Otherwise, we're being sentenced to hell..."
    return

label pre_ch1_loop:
    call screen bing_desktop()
    if _return == "ready":
        call screen mail_view("About the trip", "Sayonika <sayonika@maidcafe.me>", emailmsg[0])
        pass
    else:
        call pre_ch1_loop
    return