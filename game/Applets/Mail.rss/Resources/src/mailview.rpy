screen mail_view(subject, sender, message):
    modal True
    zorder 200
    style_prefix "confirm"
    use bing_top_bar

    frame:
        xalign 0.5
        yalign 0.6
        style "mail_frame"
        has vbox:
            spacing 16
            xsize 720
            ymaximum 550
            ysize 550
        
        hbox:
            add "Applets/Mail.rss/Resources/icons/48.png"
            null width 8
            label _("Mail.RSS Message"):
                style "setup_title"

        vbox:
            spacing 16
            label _(subject + " (" + sender + ")"):
                style "message_subject"

            viewport id "vp":
                draggable True
                scrollbars "vertical"
                ymaximum 400
                mousewheel True

                text _(message):
                    style "email_message_text"

        hbox:
            xalign 1.0
            yalign 1.0
            spacing 32
            textbutton _("Mark as Read") action Return(0):
                style "confirm_button_negative"

style mail_frame:
    background Frame([ "Applets/Mail.rss/Resources/emview.png", "Applets/Mail.rss/Resources/emview.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style message_subject is gui_prompt_text
style message_subject_text is aliceos_medium:
    font "Resources/systemfont/Ubuntu/Ubuntu-Medium.ttf"
    color "#000"
    outlines []
    text_align 0.0
    size 28
    layout "subtitle"

style email_message_text is aliceos_regular:
    font "Resources/systemfont/Ubuntu/Ubuntu-Regular.ttf"
    color slate[700]
    size 16
    outlines []
    # text_align 0.5
    xpadding 32
    ypadding 8
    layout "tex"