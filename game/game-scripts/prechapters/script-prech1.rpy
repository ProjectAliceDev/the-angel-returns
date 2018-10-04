label pre_ch1:
    stop music fadeout 1.0
    scene mc_desktop
    python:
        mailApp.ask_app_permissions()
        get_mail_input = mailApp.send_temporary_notification("New Mail from Sayonika", "Please open Mail.RSS to view the message.", action=Return('get_mail'))

        if get_mail_input == 'get_mail':
            renpy.call_screen("mail_view", "About the trip", "Sayonika <sayonika@maidcafe.me>", emailmsg[0])
        else:
            pass
        
    call pre_ch1_loop
    return

label pre_ch1_loop:
    call screen bing_desktop()
    if _return == "ready":
        call screen mail_view("About the trip", "Sayonika <sayonika@maidcafe.me>", emailmsg[0])
        pass
    else:
        call pre_ch1_loop
    return