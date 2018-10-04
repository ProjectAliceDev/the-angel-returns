image reload_bg = "#000"
image fake_reload = Text("{color=#fff}Reloading script...{/color}", size=40, style="_default")
image fake_reload2 = Text("{color=#fff}Reloading game...{/color}", size=40, style="_default")

image blackbox bg = "mod_assets/images/gui/blackbox/cc.png"
image blight complete = "mod_assets/images/gui/blackbox/c.png"
image blight start = "mod_assets/images/gui/blackbox/u.png"

image amesh = "mod_assets/images/gui/blackbox/ac.png"

image bg campus = "mod_assets/images/bg/campus.png"
image bg residential_entrance = "mod_assets/images/bg/entrance_mod.png"
image bg station = "mod_assets/images/bg/unknown by LeoDeCraprio.png"
image bg studio entrance = "mod_assets/images/bg/studio-1.png"
image bg studio inkmachine = "mod_assets/images/bg/studio-2.png"
image bg studio breakroom = "mod_assets/images/bg/studio-3.png"
image bg studio lift = "mod_assets/images/bg/studio-4.jpg"
image bg studio office = "mod_assets/images/bg/studio-7.jpg"
image bg apple = "mod_assets/images/bg/appleshop.png"

define audio.a4 = "mod_assets/music/b4g.ogg"
define audio.bt = "<loop 18.073>mod_assets/music/theme.wav"
define audio.bt3 = "mod_assets/music/theme2.wav"

## Demo Music
## This WILL be replaced in the final version of the game.
define audio.b1 = "mod_assets/music/demo/t6.mp3"
define audio.b2 = "mod_assets/music/demo/mend.mp3"
define audio.b3 = "mod_assets/music/demo/b3.mp3"
define audio.b4 = "mod_assets/music/b4.ogg"
define audio.b5 = "mod_assets/music/THA-thecakeisalie.mp3"
define audio.b6 = "mod_assets/music/demo/t7.mp3"
define audio.b7 = "mod_assets/music/demo/t8.mp3"

image yuri 3by7 = im.Composite((960, 960), (0, 0), "yuri/y7.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

define narrator = Character(ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxmc.png", xalign=0.5, yalign=1.0))
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxmc.png", xalign=0.5, yalign=1.0), who_style='say_label_mc')
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxblue.png", xalign=0.5, yalign=1.0), who_style='say_label_blue')
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxgreen.png", xalign=0.5, yalign=1.0), who_style='say_label_green')
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxpink.png", xalign=0.5, yalign=1.0), who_style='say_label_pink')
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxpurple.png", xalign=0.5, yalign=1.0), who_style='say_label_purple')
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', image='alice', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxamber.png", xalign=0.5, yalign=1.0), who_style='say_label_amber')
define sm = DynamicCharacter('sm_name', image='sayonika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxteal.png", xalign=0.5, yalign=1.0), who_style='say_label_teal')
define c = DynamicCharacter('c_name', image='craig', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("/mod_assets/images/gui/textboxapple.png", xalign=0.5, yalign=1.0), who_style='say_label_apple')