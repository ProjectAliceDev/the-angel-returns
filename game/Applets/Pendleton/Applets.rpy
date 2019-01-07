init -501 screen applets() tag menu:

    use game_menu(_("Applets"), scroll="viewport"):

        style_prefix "applets"

        vbox:
            python:
                import gc
                required_applets_list = []
                system_applets_list = []
                applets_list = []
                for obj in gc.get_objects():
                    if isinstance(obj, Applet):
                        if obj.author == "AliceOS Developers":
                            system_applets_list.append(obj)
                        elif obj.author == "Project Alice" or obj.author == "Dan Salvato":
                            required_applets_list.append(obj)
                        else:
                            applets_list.append(obj)
        
            textbutton "‹ Settings" action ShowMenu("preferences")
            null height 8
            label "Installed Applets":
                style "applets_title"

            text "AliceOS comes with several Applets preinstalled to enhance and improve the experience."
                        
            null height 8
            
            label "System Applets"
            text "These applets come with every installation of AliceOS and are required."
            vbox:
            
                spacing 4
                            
                for i in range(len(system_applets_list) * 1):
                    hbox:
                        spacing 8
                        add "Applets/" + system_applets_list[i].app_dir + "/Resources/icons/" + system_applets_list[i].icons[64] xalign 0.5
                        
                        null height 4
                        
                        vbox:
                        
                            $ appname = system_applets_list[i].long_name
                            text "[appname]":
                                style "applets_app_text"
                                xalign 0.0
                                
                            $ appauth = "Version " + system_applets_list[i].version + " | " + system_applets_list[i].author
                            text "[appauth]":
                                style "applets_app_description_text"
                                xalign 0.0
                                
                            python:
                                appdesc = system_applets_list[i].description.strip()
                                if appdesc == "":
                                    appdesc = "Information not found."
                            text "[appdesc]":
                                style "applets_app_description_text"
                                xalign 0.0
                                
            null height 8
            
            label "Required Third-Party Applets"
            text "These applets were developed or installed by the developer and cannot be removed."
            vbox:
            
                spacing 4
                            
                for i in range(len(required_applets_list) * 1):
                    hbox:
                        spacing 8
                        add "Applets/" + required_applets_list[i].app_dir + "/Resources/icons/" + required_applets_list[i].icons[64] xalign 0.5
                        
                        null height 4
                        
                        vbox:
                        
                            $ appname = required_applets_list[i].long_name
                            text "[appname]":
                                style "applets_app_text"
                                xalign 0.0
                                
                            $ appauth = "Version " + required_applets_list[i].version + " | " + required_applets_list[i].author
                            text "[appauth]":
                                style "applets_app_description_text"
                                xalign 0.0
                                
                            python:
                                appdesc = required_applets_list[i].description.strip()
                                if appdesc == "":
                                    appdesc = "Information not found."
                            text "[appdesc]":
                                style "applets_app_description_text"
                                xalign 0.0
            null height 8                   
            label "Other Applets"
            text "These applets were added on top of the required applets and may be developed by a mod author user-installed.\nTo uninstall these applets, remove the applet's folder from the Applets directory."
            vbox:
            
                spacing 4
                
                python:
                    if applets_list != []:
                        empty_set = False
                    else:
                        empty_set = True
                
                if not empty_set:           
                    for i in range(len(applets_list) * 1):
                        hbox:
                            spacing 8
                            add "Applets/" + applets_list[i].app_dir + "/Resources/icons/" + applets_list[i].icons[64] xalign 0.5
                            
                            null height 4
                            
                            vbox:
                            
                                $ appname = applets_list[i].long_name
                                text "[appname]":
                                    style "applets_app_text"
                                    xalign 0.0
                                    
                                $ appauth = "Version " + applets_list[i].version + " | " + applets_list[i].author
                                text "[appauth]":
                                    style "applets_app_description_text"
                                    xalign 0.0
                                    
                                python:
                                    appdesc = applets_list[i].description.strip()
                                    if appdesc == "":
                                        appdesc = "Information not found."
                                text "[appdesc]":
                                    style "applets_app_description_text"
                                    xalign 0.0
                else:
                    null height 4
                    text "There are no applets installed in this category.":
                        style "applets_sub_text"


style applets_title is gui_label

style applets_title_text is gui_label_text:
    size gui.label_text_size
    font "Resources/systemfont/Bold.ttf"
    color "#fff"
    outlines [(1, aliceos_oem_pink[500])]

style applets_label_text:
    font "Resources/systemfont/Medium.ttf"
    size 20

style applets_text is gui_text:
    color "#fff"
    outlines [(1, aliceos_oem_pink[700])]
    size 18
    
style applets_sub_text is gui_text:
    size 14
    color "#fff"
    outlines [(1, silver[500])]

style applets_app_text is gui_text:
    color "#fff"
    outlines [(1, aliceos_oem_pink[500])]
    size 20
    
style applets_app_description_text is gui_text:
    color "#fff"
    outlines [(1, silver[500])]
    size 14
    
style applets_button_text is aliceos_medium:
    size 22
    color "#fff"
    outlines [(1, aliceos_oem_pink[500])]
    hover_outlines [(1, aliceos_oem_pink[100])]