screen ActivitiesView():
    add "Resources/systemui/overlay_confirm.png"
    use bing_top_bar

    python:
        import gc
        applets_list = []
        for obj in gc.get_objects():
            if isinstance(obj, Applet):
                applets_list.append(obj)

        for item in applets_list:
            if item.launch["show_in_launcher"] == False:
                applets_list.remove(item)

    grid len(applets_list) 1:
        xalign 0.5
        yalign 0.5

        spacing 32

        for i in range(len(applets_list) * 1):

            $ slot = i + 1

            button:
                action eval(applets_list[i].launch["action"])

                has vbox

                if applets_list[i] == None:
                    pass

                else:
                    add "Applets/" + applets_list[i].app_dir + "/Resources/icons/" + applets_list[i].icons[128] xalign 0.5

                    spacing 8

                    text _(applets_list[i].short_name):
                        style "app_name_text"
                        xalign 0.5


style app_name_text is aliceos_medium:
    color "#ffffff"
    hover_color aliceos_oem_pink[700]
    size 18