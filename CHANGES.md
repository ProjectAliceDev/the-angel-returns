# Developer Changes
This document outlines the changes made to extend DDLC to accomodate for **The Angel Returns**.

## `dialog_alert(title, subtitle, ok_action)`
This screen is an extension to the DDLC screen `dialog`. This offers a more detailed version of an alert that has similar functionality to iOS.

* `title` - Provides a main message
* `subtitle` - Provides the details to a message
* `ok_action` - Provides function that occurs when user hits OK button to dismiss message

```renpy
call screen dialog_alert("Packages not found.","Please install the packages from ddlc.moe to continue.",ok_action=Return())
```

## `confirm_alert(title, subtitle, no_action_message, no_action, yes_action_message, yes_action)`
This screen is an extension to the DDLC screen `confirm`. This offers a more detailed version of an confirm dialog that has similar functionality to iOS.

* `title` - Provides a main message
* `subtitle` - Provides the details to a message
* `no_action_message` - The text displayed on the No button
* `yes_action_message` - The text displayed on the Yes button
* `no_action` - Provides function that occurs when user hits No button
* `yes_action` - Provides function that occurs when user hits Yes button

```renpy
call screen confirm_alert("Pages Would Like To Send You Notifications", "Notifications may include alerts, sounds, and icon badges.\nThese can be configured in Settings.", no_action_message="Don't Allow", no_action=Quit(), yes_action_message="OK", yes_action=(Return()))
```