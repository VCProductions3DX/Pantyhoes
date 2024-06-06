label neutralending:
    if pickkim == True:
        jump kimneutralending
    elif picklisa == True:
        jump lisaneutralending
    elif pickmai == True:
        jump maineutralending
    else:
        jump mainneutralending

label kimneutrallending:
    scene kimneutralending1

    play music "music/track3.ogg"
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0

    kim "Welcome home, [player_name]."
    $persistent.endings += 1
    $persistent.neutral_ending = True
    main "You look different."
    kim "Oh do I?"
    scene kimneutralending3
    kim "I'm pregnant, [player_name]."
    kim "You're going to be a daddy."
    kim "Come, let's watch the news."
    scene kimneutralending5
    newsreporter "Today, authorities have arrested John Shilling, former CEO of the now defunct Shilling Holdings and Publishings."
    newsreporter "Mr. Shilling is connected to a widescale tax fraud scheme along with other businesses in the area."
    newsreporter "Details at 11 p.m."
    scene kimneutralending8
    kim "So they finally got him."
    kim "I wonder how he will wiggle his way out of this situation."
    main "He won't."
    scene kimneutralending11
    kim "I hope not. You and I have to work to do."
    scene kimneutralending7
    kim "Starting with a foot massage."
    scene black with fade
    show text "3 Years Later" with Pause (5.0)
    scene dadreturnsneutralending
    "(Time for me to go to work. I better not disturb Kim and the baby.)"
    unvoice "Hello there, [player_name]."
    main "Dad??!!?"
    stop music
    play sound "sfx/misc_sound.ogg"
    show neutralendingcard with Pause (10.0)
    stop sound
    $achievement.grant("Achievement09_NeutralEnding")
init:
    $achievement.register("Achievement09_NeutralEnding")
    $achievement.sync()
return

label lisaneutralending:
    #$setup_textbox = "scene"
    scene lisaneutralending1

    play music "music/track3.ogg"
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0

    $persistent.endings += 1
    $persistent.neutral_ending = True
    lisa "Welcome home, [player_name]."
    lisa "I'm happy you're home."
    scene lisaneutralending2
    main "Thanks. You...you look different."
    lisa "Do I?"
    scene lisaneutralending3
    main "What's the matter?"
    lisa "...I'm pregnant."
    scene lisaneutralending4
    main "Hey, I said I would be a stay-at-home dad didn't I?"
    lisa "Yeah, but..how are we going to make this work?"
    main "We'll find a way. What's important is that we are together now."
    scene lisaneutralending5
    lisa "Yeah."
    scene black with fade
    show text "3 Years Later" with Pause (5.0)
    "(Time for me go to work. I better not disturb Lisa.)"
    scene dadreturnsneutralending

    unvoice "Hello there, [player_name]."
    main "Dad??!!?"
    stop music
    play sound "sfx/misc_sound.ogg"
    show neutralendingcard with Pause (10.0)
    stop sound
    $achievement.grant("Achievement09_NeutralEnding")
init:
    $achievement.register("Achievement09_NeutralEnding")
    $achievement.sync()
return

label maineutralending:
    #$setup_textbox = "scene"
    play music "music/track3.ogg"

    scene maineutralending1
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    $persistent.endings += 1
    $persistent.neutral_ending = True
    mai "Welcome home, [player_name]."
    main "Thanks. Wow..you really cleaned the place."
    scene maineutralending1
    mai "You're still a child in some ways, [player_name]."
    main "What? No I-"
    mai "But not anymore."
    scene maineutralending2
    mai "I'm pregnant."
    scene maineutralending3
    main "R-r-reallly?"
    mai "Mmhmm..feel."
    scene maineutralending5
    main "Maybe you need a massage."
    mai "I think you're just horny, [player_name]."
    scene maineutralending6
    mai "But I'm ready when you are."
    scene black with fade
    show text "3 Years Later" with Pause (5.0)
    "(Time for me go to work. I better not disturb Mai and the kids.)"
    scene dadreturnsneutralending

    unvoice "Hello there, [player_name]."
    main "Dad??!!?"
    stop music
    play sound "sfx/misc_sound.ogg"
    show neutralendingcard with Pause (10.0)
    stop sound
    $achievement.grant("Achievement09_NeutralEnding")
init:
    $achievement.register("Achievement09_NeutralEnding")
    $achievement.sync()
return


label mainneutralending:
    #$setup_textbox = "scene"
    scene black with fade

    play music "music/track3.ogg"
    show text "3 Years Later" with Pause (5.0)

    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    $persistent.endings += 1
    $persistent.neutral_ending = True
    "(Back in New York City.)"
    "(Thanks to Mom, I was able to get a new job and a nice apartment.)"
    "(It does feel a bit lonely, but I'm glad I can start over.)"
    scene nyapartment
    "(My door is open.)"
    "(Hmm...did someone break into my apartment?)"
    scene soloneutralending
    unvoice "Welcome home, [player_name]."
    main "Dad?!?!?!"
    stop music
    play sound "sfx/misc_sound.ogg"
    show soloneutralendingcard with Pause (10.0)
    stop sound
    $achievement.grant("Achievement09_NeutralEnding")
init:
    $achievement.register("Achievement09_NeutralEnding")
    $achievement.sync()
return
