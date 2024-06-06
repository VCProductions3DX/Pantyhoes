init offset = -2

image ctc:
    xpos 10
    ypos 15
    alpha 0.0
    pause 0.05
    linear 0.5 alpha 1.0
    "gui/ctc_white.png"
    repeat

image disclaimer = "gui/Disclaimer.png"
image charmup = "gui/charm_up.png"
image charmdown = "gui/charm_down.png"
image authorityup = "gui/authority_up.png"
image authoritydown = "gui/authority_down.png"
image moraleup = "gui/morale_up.png"
image moraledown = "gui/morale_down.png"

image chapter1title = "gui/chapter1title.png"
image chapter1titleend = "gui/chapter1title_end.png"
image chapter2title = "gui/chapter2title.png"
image chapter2titleend = "gui/chapter2title_end.png"
image chapter3title = "gui/chapter3title.png"
image chapter3titleend = "gui/chapter3title_end.png"
image chapter4title = "gui/chapter4title.png"
image chapter4titleend = "gui/chapter4title_end.png"
image chapter5title = "gui/chapter5title.png"
image chapter5titleend = "gui/chapter5title_end.png"
image chapter6title = "gui/chapter6title.png"
image chapter6titleend = "gui/chapter6title_end.png"
image chapter7title = "gui/chapter7title.png"
image epiloguetitle = "gui/epilogue.png"
image epiloguetitleend = "gui/epilogue_end.png"
image disclaimer = "gui/Disclaimer.png"
image vclogo = "gui/vclogo.png"
image lockedthumb = MinScale("gui/lockbutton.png", maxthumbx, maxthumby)
image fakeincomestatement = "images/fakeincomestatement.png"
image realincomestatement = "images/realincomestatement.png"


image eyeopen:
    "gui/eye.png"
    alpha 1.0
    linear 3.0 alpha 0.0
    repeat

image eyeclose:
    "gui/eye.png"
    alpha 0.0
    linear 3.0 alpha 1.0
    repeat

transform attributeup:
    xalign 0.7
    ypos 475
    alpha 1.0
    linear 3.0 alpha 0.0 ypos 430

transform attributedown:
    xalign 0.7
    ypos 475
    alpha 1.0
    linear 2.0 alpha 0.0

transform fromtheleft:
    xalign 1.0
    yalign 0.5
    linear 0.5 xalign 0.5



screen eyeopening():
    zorder 102
    add "eyeopen"

screen eyeclosing():
    zorder 102
    add "eyeclose"

screen monitor():
    zorder 102
    add "gui/securityscreen.png"

screen recorder():
    zorder 102
    add "gui/recordingscreen.png"


define fade = Fade(0.5, 0.0, 0.5)
define fadewhite = Fade(0.5, 0.0, 0.5, color="#ffffff")
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")
define blackflash = Fade(0.1,0.0,0.5, color="#000000")
define smallshake = ComposeTransition(vpunch,before=hpunch)


style task_incomplete is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#FF0000"

style task_completed is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#FF0000"

style task_description is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 28
    color "#ffffff"

style task_label is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#F4F4EF"

style task_dominant is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#ff3333"

style task_charming is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#33ff33"

style task_balanced is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 36
    color "#33ffff"

style good_ending is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 24
    color "#ff6699"

style neutral_ending is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 24
    color "#ffff99"

style bad_ending is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 24
    color "#FF0000"

style taskline_label is text:
    font "font/IBMPlexSerif_Medium.ttf"
    size 48
    color "#ffffff"

style kanit_desc is text:
    font "font/Kanit_Medium.ttf"
    size 36
    color "#ffffff"
    xalign 0.5

style mada_desc is text:
    font "font/Mada_Medium.ttf"
    size 36
    color "#ffffff"
    xalign 0.5

style nanum_desc is text:
    font "font/NanumGothic_Bold.ttf"
    size 36
    color "#ffffff"
    xalign 0.5

style noto_desc is text:
    font "font/NotoSansSC_Medium.otf"
    size 36
    color "#ffffff"
    xalign 0.5

style roboto_desc is text:
    font "font/Roboto_Medium.ttf"
    size 36
    color "#ffffff"
    xalign 0.5


style rubik_desc is text:
    font "font/Rubik_Regular.ttf"
    size 36
    color "#ffffff"
    xalign 0.5



screen profile_screen():
    zorder 200
    modal True
    add gui.game_menu_background


    vbox:
        text _("Information") xpos 50 ypos 5 style "taskline_label"


        hbox:
            spacing 30
            xpos 50
            ypos 20
            text _("Charm: [charm.amount]") style "task_label"
            text _("Authority: [authority.amount]") style "task_label"

        hbox:
            spacing 50
            xpos 50
            ypos 75
            vbox:
                xalign 0.5
                xmaximum 250
                spacing 10
                imagebutton idle "images/Mai_BustShot.png" hover "images/Mai_BustShot.png" action NullAction()
                text ("[cMai.name]") style "task_label"
                text ("[cMai.job]") style "task_description"
                text("Morale Level: [cMai.morale]") style "task_description"
                if cMai.morale >=7:
                    text ("Mood: Mesmerized") style "good_ending"
                elif cMai.morale >=2:
                    text ("Mood: Friendly") style "neutral_ending"
                else:
                    text ("Mood: Apathetic") style "bad_ending"

            vbox:
                xalign 0.5
                xmaximum 250
                spacing 10
                imagebutton idle "images/Lisa_BustShot.png" hover "images/Lisa_BustShot.png" action NullAction()
                text ("[cLisa.name]") style "task_label"
                text ("[cLisa.job]") style "task_description"
                text("Morale Level: [cLisa.morale]") style "task_description"
                if cLisa.morale >=6:
                    text ("Mood: Happy") style "good_ending"
                elif cLisa.morale >=2:
                    text ("Mood: Outgoing") style "neutral_ending"
                else:
                    text ("Mood: Unbothered") style "bad_ending"

            vbox:
                xalign 0.5
                xmaximum 250
                spacing 10
                imagebutton idle "images/Bella_BustShot.png" hover "images/Bella_BustShot.png" action NullAction()
                text ("[cBella.name]") style "task_label"
                text ("[cBella.job]") style "task_description"
                text("Morale Level: [cBella.morale]") style "task_description"
                if cBella.morale >= 8:
                    text ("Mood: Cheerful") style "good_ending"
                elif cBella.morale >=2:
                    text ("Mood: Pleasant") style "neutral_ending"
                else:
                    text ("Mood: Apathetic") style "bad_ending"

            vbox:
                xalign 0.5
                xmaximum 250
                spacing 10
                imagebutton idle "images/Kim_BustShot.png" hover "images/Kim_BustShot.png" action NullAction()
                text ("[cKim.name]") style "task_label"
                text ("[cKim.job]" )style "task_description"
                text("Morale Level: [cKim.morale]") style "task_description"
                if cKim.morale >=8:
                    text ("Mood: Submissive") style "good_ending"
                elif cKim.morale >=2:
                    text ("Mood: Pleasant") style "neutral_ending"
                else:
                    text ("Mood: Intolerant") style "bad_ending"

            vbox:
                xalign 0.5
                xmaximum 250
                spacing 10
                imagebutton idle "images/Crissy_BustShot.png" hover "images/Crissy_BustShot.png" action NullAction()
                text ("[cCrissy.name]") style "task_label"
                text ("[cCrissy.job]") style "task_description"
                text("Morale Level: [cCrissy.morale]") style "task_description"
                if cCrissy.morale >=7:
                    text ("Mood: Cooperative") style "good_ending"
                elif cCrissy.morale >=2:
                    text ("Mood: Neutral") style "neutral_ending"
                else:
                    text ("Mood: Uncooperative") style "bad_ending"



    textbutton _("Return") action [Return(), Hide("profilescreen")] xalign 0.97 yalign 0.95


screen changelanguage():
    add gui.game_menu_background
    label _("Change Language") xpos 10 ypos 10 style "taskline_label"

    vbox:
        xalign 0.5
        yalign 0.3

        text _("We offer support for many languages!")
        text _("If you would like to translate Pantyhoes, email vcproductions@protonmail.com")
        text _("Or download from the Steam Workshop")
        #textbutton "English" action Language(None)
        #textbutton _("Español") style "roboto_desc" action Language("Spanish")
        #textbutton _("Français") style "roboto_desc" action Language ("French")
        #textbutton _("Português") style "roboto_desc" #action Language ("Portuguese")
        #textbutton _("Português(Brasil)") style "roboto_desc" action Language ("PortugueseBR")
        #textbutton _("Italiano") style "roboto_desc" action Language ("Italian")
        #textbutton _("Română") style "roboto_desc" action Language ("Romanian")

        #textbutton _("Deutsch") style "roboto_desc" action Language ("German")
        #textbutton _("Nederlands") style "roboto_desc" action Language ("Dutch")
        #textbutton _("Svenska") style "roboto_desc" action [Language ("Swedish")
        #textbutton _("Dansk") style "roboto_desc" action [Language ("Danish")
        #textbutton _("Norsk") style "roboto_desc" action [Language ("Norwegian")

        #textbutton _("Türkçe") style "roboto_desc" action [Language ("Turkish")

        #textbutton _("Руссиан") style "nanum_desc" action Language("Russian")
        #textbutton _("Ελληνικά") style "roboto_desc" action Language("Greek")
        #textbutton _("日本語") style "nanum_desc" action Language("Japanese")
        #textbutton _("한국어") style "nanum_desc" action Language("Korean")
        #textbutton _("中文简单") style "noto_desc" action Language("ChineseSimple")

        #textbutton _("ไทย") style "kanit_desc" action Language("Thai")
        #textbutton _("اللغه العربية") style "mada_desc" action Language("Arabic")
        #textbutton _("עברית") style "rubik_desc" action Language("Hebrew")

        #Latin languages
        #translate_font("Spanish", "font/Roboto_Regular.ttf")
        #translate_font("French", "font/Roboto_Regular.ttf")
        #translate_font("Portuguese", "font/Roboto_Regular.ttf")
        #translate_font("PortugueseBR", "font/Roboto_Regular.ttf")
        #translate_font("Italian", "font/Roboto_Regular.ttf")
        #translate_font("Romanian", "font/Roboto_Regular.ttf")
        #German languages
        #translate_font("German", "font/Roboto_Regular.ttf")
        #translate_font("Dutch", "font/Roboto_Regular.ttf")
        #translate_font("Swedish", "font/Roboto_Regular.ttf")
        #translate_font("Danish", "font/Roboto_Regular.ttf")
        #translate_font("Norwegian", "font/Roboto_Regular.ttf")
        #Turkish
        #translate_font("Turkish", "font/Roboto_Regular.ttf")
        #Cyrillic languages
        #translate_font("Russian", "font/NanumGothic_Regular.ttf")
        #Japanese
        #translate_font("Japanese", "font/NanumGothic_Regular.ttf")
        #Korean
        #translate_font("Korean", "font/NanumGothic_Regular.ttf")
        #Greek
        #translate_font("Greek", "font/NanumGothic_Regular.ttf")
        #Chinese Simple
        #translate_font("ChineseSimple", "font/NanumGothic_Regular.ttf")
        #Arabic
        #translate_font("Arabic", "font/Mada_Regular.ttf")
        #Hebrew
        #translate_font("Hebrew", "font/Rubik_Regular.ttf")
        #Thai
        #translate_font("Thai", "font/Kanit_Regular.ttf")

    textbutton _("Return") action [Return(), Hide("changelanguage")] xalign 0.97 yalign 0.95





label splashscreen:
    scene black
    with Pause(1)

    show vclogo with dissolve
    with Pause(1)

    scene black with dissolve
    with Pause(1)

return
