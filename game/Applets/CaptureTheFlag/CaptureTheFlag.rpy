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
    
    ctf = CaptureTheFlag()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.
image alice_just_main = "mod_assets/images/cg/ja.png"