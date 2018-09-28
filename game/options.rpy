init python:
    import json
    with open(config.basedir + '/version', 'r') as f:
        release_version = json.load(f)init python: 
    import json 
    with open(config.basedir + '/version', 'r') as f: 
        release_version = json.load(f) 
# human readable name of this game 
# _() marks strings eligable for translation 
define config.name = "Doki Doki: The Angel Returns" 
 
# True shows the name on main menu, False hides it 
define gui.show_name = True 
 
# Version of the game 
define config.version = "0.1.2beta2" 
define nightlydate = release_version["version"] 
define snapshottime = "nightly_b" + nightlydate 
 
# text placed on about screen 
define gui.about = _("") 
 
# short name used in executables and dirs. 
# ASCII-only, no spaces, no colons, no semis 
define build.name = "TheAngelReturns" 
 
# Controls which sound / music mixers are available 
define config.has_sound = True 
define config.has_music = True 
define config.has_voice = False 
 
# main menu music 
define config.main_menu_music = audio.t1 
 
# enter / exiting game menu transitions 
define config.enter_transition = Dissolve(.2) 
define config.exit_transition = Dissolve(.2) 
 
# transition used when the game has been loaded 
define config.after_load_transition = None 
 
# transition used when teh game has ended 
define config.end_game_transition = Dissolve(.5) 
 
# Controls when dialogue window is displayed: 
#   show - always displayed 
#   hide - only displayed if dialogue is present 
#   auto - hidden before scene statements and shown when dialogue is shown 
# 
# this can be changed with "window <type>" statements 
define config.window = "auto" 
 
# transitions used to show / hide the dialogue window 
define config.window_show_transition = Dissolve(.2) 
define config.window_hide_transition = Dissolve(.2) 
 
# default text speed 
# 0 is infinite 
# > 0 is number of characters per second 
default preferences.text_cps = 50 
 
# default auto-forward delay. 0 - 30. 
default preferences.afm_time = 15 
 
# default volumes 
default preferences.music_volume = 0.75 
default preferences.sfx_volume = 0.75 
 
# persistent data save directory 
# this is different per platform: 
#   Windows: %AAPDATA%\RenPy\ 
#   Mac: $HOME/Libary/RenPy/ 
#   Linux: $HOME/.renpy/ 
# 
# must be a literal string 
define config.save_directory = "Doki_Doki_Alice" 
 
# icon displayed on taskbar / dock 
define config.window_icon = "mod_assets/logo.png" 
 
# True means we allow skipping, False means not 
define config.allow_skipping = True 
 
# True means we can autosave, false means not 
define config.has_autosave = False 
 
# True means autosave when we quit, False means not 
define config.autosave_on_quit = False 
 
# Number of autosave slots to use 
define config.autosave_slots = 0 
 
# layers that screens / images / anything can be displayed on. Best not to 
# mess with this 
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ] 
 
# Other things to not mess with 
define config.image_cache_size = 64 
define config.predict_statements = 50 
define config.rollback_enabled = config.developer 
define config.menu_clear_layers = ["front"] 
define config.gl_test_image = "white" 
# define config.developer = True 
 
 
init python: 
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1]) 
    renpy.game.preferences.pad_enabled = False 
# human readable name of this game
# _() marks strings eligable for translation
define config.name = "Doki Doki: The Angel Returns"

# True shows the name on main menu, False hides it
define gui.show_name = True

# Version of the game
define config.version = "0.1.2beta2"
define nightlydate = release_version["version"]
define snapshottime = "nightly_pht-" + nightlydate

# text placed on about screen
define gui.about = _("")

# short name used in executables and dirs.
# ASCII-only, no spaces, no colons, no semis
define build.name = "TheAngelReturns"

# Controls which sound / music mixers are available
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# main menu music
define config.main_menu_music = audio.t1

# enter / exiting game menu transitions
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# transition used when the game has been loaded
define config.after_load_transition = None

# transition used when teh game has ended
define config.end_game_transition = Dissolve(.5)

# Controls when dialogue window is displayed:
#   show - always displayed
#   hide - only displayed if dialogue is present
#   auto - hidden before scene statements and shown when dialogue is shown
#
# this can be changed with "window <type>" statements
define config.window = "auto"

# transitions used to show / hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# default text speed
# 0 is infinite
# > 0 is number of characters per second
default preferences.text_cps = 50

# default auto-forward delay. 0 - 30.
default preferences.afm_time = 15

# default volumes
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# persistent data save directory
# this is different per platform:
#   Windows: %AAPDATA%\RenPy\
#   Mac: $HOME/Libary/RenPy/
#   Linux: $HOME/.renpy/
#
# must be a literal string
define config.save_directory = "Doki_Doki_Alice"

# icon displayed on taskbar / dock
define config.window_icon = "mod_assets/logo.png"

# True means we allow skipping, False means not
define config.allow_skipping = True

# True means we can autosave, false means not
define config.has_autosave = False

# True means autosave when we quit, False means not
define config.autosave_on_quit = False

# Number of autosave slots to use
define config.autosave_slots = 0

# layers that screens / images / anything can be displayed on. Best not to
# mess with this
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# Other things to not mess with
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"
# define config.developer = True


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)



# BUILD CONFIG

init python:

    # the following functions take file pattersn:
    # file patterns are case-insensitive and matched against the path relative to the 
    # base directory, with and without a leading /. If multiple patterns match
    # the first is used.
    #
    # / is directory separator
    # * matches all characters, exxcept directory separator
    # ** matches all characters, including directory separator
    #
    # EXAMPLES
    # *.txt - - matches txt files in base directory
    # game/**.ogg - mathces ogg files in game directory or subdirs of game
    # **.psd - matches psd files anywhere in project
    #
    # Classify files as None to exclusde them from the built distributions
    #

    # packaged ZIP for distibution
    build.package(build.directory_name + "Mod",'zip',build.name,description='DDLC Compatible Mod')

    # archives to create
    build.archive("scripts",build.name)
    build.archive("mod_assets",build.name)
    build.archive("submods",build.name)
    build.archive("aliceos",build.name) # Create AliceOS RPA

    # folder / files to put in archives
    build.classify("game/mod_assets/**","mod_assets")
    build.classify("game/submods/**","submods")
    build.classify('game/**.rpyc',"scripts")
    build.classify('game/advanced_scripts/**',"scripts")
    build.classify('game/original_story_scripts/**',"scripts")
    build.classify("game/Applets/**", "aliceos")
    build.classify("game/CoreServices/**", "aliceos")
    build.classify("game/Frameworks/**", "aliceos")
    build.classify("game/Resources/**", "aliceos")
    build.classify("game/gui/**", "aliceos")

    # stuff to ignore
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('**.apf', None)
    build.classify('**.moj', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa',None)

    # stuff not in archive
    build.classify('README.html',build.name)
    build.classify("characters/mio.chr",build.name)
    build.classify("characters/aliceangel.chr",build.name)
    build.classify("feedback.html",build.name)
    build.classify("credits.txt",build.name)
    build.classify("libitina.cfg",build.name)
    build.classify("mod.json",build.name)
    build.classify("version", build.name)

    # Beta stuff if necessary:
    if "beta" in config.version:
        build.classify("betanotes.txt",build.name)

    # mark as documentation
    build.documentation('README.html')
    build.documentation('feedback.html')
    build.documentation('credits.txt')
    build.documentation('betanotes.txt')

    build.include_old_themes = False
