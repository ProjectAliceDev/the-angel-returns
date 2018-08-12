## Applet Name
# A short description of a delicious app!
# Author(s): Your Name (@githubusername)
# Copyright: (C) 2018

init python:
    class CaptureTheFlag(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "CTF"
        long_name = "Capture The Flag"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "CaptureTheFlag"
        author = "Marquis Kurt"
        version = "0.1.0"
        description = """\
It's time to capture the flag!
        """

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {pm_notify}

        flags = {
            0: "n4m35_d0_w0rk_t00",
            1: "MG4xeV80MTFjM19kcjM0bTVfMW5fMGNy",
            2: ""
        }

        errorhandlers = {
            1: "U2FsdGVkX18cQQ188vuU4tPLaSKYYJytI9UUgOmK62p2sSavqNUSMACGtVsVFZxFUbbgRYs2UjqedJbHTR7u8FxBALqUw0VNjTYrkkF18yZekSCbJJC8QaemvDdUmo3JWqjByzu4ZBUpcAQ6blmHTSvabxb99PNeW11MN6lFWF+JpLQiXIqqoDnYmtMSWNeBd39ctANV7fBtpzqIUacO8GJ2y80vYQXe7H3CAARvxYBSkXvqsKYsq5J29DQvND6t1FjqyAd1hlrd4Xw4GT3z+FstnAwjiQm3A7DhqCSDOB7VFhrIxUM6DGsttvuaW2hqZJ8Ykv1+GoZh91hYMUfUYlSK6TQstiNR4A1BFv4WoShfUowp6NbbfpDFUBwFXXcy8m0aghVFHcKth6ZVniVzqKJYReDGRsKd4QXWmJtN18PUxfdZQxQTIaSLivBI90yWi2bSD5EeIsH1Q4T2Xryn2YRnAWrnHW3T0qZEUclk9CPZASUsdz09EscWm5bxBkjIFxSqAoXDlSgyDhWefbGT9U8JH+ff+xsGHvWxjG327gm9v7lZaHdl22y8U94PSD4bS+dc5ZTdt7JIpaIKEC4sNvJmDY9IQZJ7luvTf6zkONtV1DTQ2jsdTqa5Z1g6mta7Z+GpajQYz/RKRd6wutXJw6mzGmecPawM1CcNFeoxgOKqHpvnSx6SwKjVVK9rNOAmF1scyRomu7iYQeTN8ZF9097woNul9t54n/3pKlJ0pROjoISy5bOr6cTYrXITAjyIDIFeB4g4m2eLHlwD6F5LwQ9Id8zpke6cqpe+G/M94H/c8z+lRxjpHda5LcvtE1yAl4vSsR/QssPW3L3WGerkK8LxwAMbFnxhUvSA3rMZC/n7D7qt7CppOW5DuZrtAyIMKnjoUitthbvMjqdCq84ofz1a4oJj3MLmZk2lFE3CGVcP/Bz/vfb875zdzCrfhtWB8Z5Ze13l2s2AXwY4oxAsSmHhJb21xLujau5pCXoYJ+L9qjZ0igeJyp9vy0GpMIXh"
        }
    
    ctf = CaptureTheFlag()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.
image alice_just_main = "mod_assets/images/cg/ja.png"

init -501 screen flag_input(message, ok_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

        input default "ctf." value VariableInputValue("flag")