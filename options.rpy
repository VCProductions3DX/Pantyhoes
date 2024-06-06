

define config.name = _("Pantyhoes")
define gui.show_name = False

define config.version = "1.0.12"


define gui.about = _p("""
Stockings/Pantyhoes is copyrighted 2019-2021 to VC Productions.
A Big thank you to our supporters for helping us with this release!

""")



define build.name = "PantyhoesOfficial"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.has_quicksave = True
define config.has_autosave = True

define config.sample_sound = "sfx/click3.ogg"
define config.main_menu_music = "music/track5.ogg"



define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

define config.window = "auto"



define config.window_show_transition = Dissolve(.05)
define config.window_hide_transition = Dissolve(.05)

default preferences.text_cps = 0


default preferences.afm_time = 20



define config.save_directory = "SPHOfficial-1584128527"




define config.window_icon = "gui/icon.ico"


## Build configuration #########################################################


init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.archive("01system", "all")
    build.classify('game/01system/**.**', '01system')

    build.archive("bonus", "all")
    build.classify('game/bonus/**.**', 'bonus')

    build.archive("images", "all")
    build.classify('game/images/**.**', 'images')

    build.archive("music", "all")
    build.classify('game/music/**.**', 'music')

    build.archive("sfx", "all")
    build.classify('game/sfx/**.**', 'sfx')

    build.archive("story", "all")
    build.classify('game/story/**.**', 'story')

    build.archive("xxx", "all")
    build.classify('game/xxx/**.**', 'xxx')



    build.documentation('*.html')
    build.documentation('*.txt')
