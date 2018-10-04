init python:
    class MailRSS(Applet):
        short_name = "Mail.RSS"
        long_name = "Chrysalis Mail RSS Services"
        app_dir = "Mail.rss"
        author = "Chrysalis Systems LLC."
        version = "12.1.2"
        description = """\
Quickly get messages without managing a mailbox through RSS. Note: Requires Chrysalis RSC or Chrysalis RSS tools to properly function. Run sudo apt install chrysalis-rsc to install these packages.
        """
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }
        permissions = {
            pm_notify, 
        }

        launch = {
            "action": "[Hide('ActivitiesView'), Return('ready')]",
            "show_in_launcher": True
        }

        def __init__(self):
            pass    
    
    mailApp = MailRSS()