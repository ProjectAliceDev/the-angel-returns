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