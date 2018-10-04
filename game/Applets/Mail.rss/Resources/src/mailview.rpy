screen mail_view(subject, sender, message):
    modal True
    zorder 200
    style_prefix "confirm"

    frame:
        xalign 0.5
        yalign 0.5
        style "confirm_setup_frame"
        has vbox:
            spacing 16
            xsize 656
            ymaximum 600
            ysize 600
            
        vbox:
            spacing 16
            style_prefix "setup"
            label _(subject):
                style "setup_title"

            label _(sender):
                style "setup_details"

            viewport id "vp":
                draggable True
                scrollbars "vertical"
                ymaximum 400
                mousewheel True

                text _(message):
                    style "setup_mute_text"

        hbox:
            xalign 1.0
            yalign 1.0
            spacing 32
            textbutton _("Mark as Read") action Return(0):
                style "confirm_button_negative"