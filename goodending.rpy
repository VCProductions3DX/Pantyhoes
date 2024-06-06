label goodending:
    play music "music/track12.ogg"

    mom "Whew that's over."
    mom "Good job, [player_name]. You just survived your first trial."
    main "I hope it's my last."
    if pickkim == True:
        scene kimnotguiltyverdict
        kim "I can't believe it."
        kim "They didn't find you guilty on anything!"
        main "I didn't do anything."
        main "Nothing to prove."
        kim "I'm so happy, we can finally start our new life together."
        jump kimgoodending
    elif picklisa== True:
        scene lisanotguiltyverdict
        lisa "We can finally go to New York."
        lisa "I'm so happy."
        lisa "Things are finally going my way."
        mom "The best of luck to the two of you."
        jump lisagoodending
    elif pickmai ==True:
        scene mainotguiltyverdict
        mai "[player_name]!"
        mai "You're free."
        main "Yeah, I am."
        mom "Well, I guess it's down the hallway so you two can get married."
        mom "And a formal wedding, of course."
        jump maigoodending
    elif pickbella == True:
        scene notguiltyverdict2
        mom "So, what's next?"
        main "I was going to help Bella with her invention."
        mom "Wow, you're an ambitious one."
        mom "Well, if you need any help filing paperwork, you know how to contact me."
        jump bellagoodending
    elif pickcrissy == True:
        scene notguiltyverdict2
        mom "So, what's next?"
        main "I'm not sure."
        main "Maybe a career in politics."
        mom "Good thing you have a clean record for now."
        mom "Try to stay out of trouble."
        main "I will."
        jump crissygoodending
    else:
        scene notguiltyverdict2
        mom "So what's next?"
        main "I don't know."
        mom "Come to New York."
        mom "You'll fit right in."
        main "But I don't want to get into any trouble."
        mom "You won't."
        mom "I'll be watching over you."
        jump maingoodending

label kimgoodending:
    scene black with fade
    $persistent.endings += 1
    show text "3 Years Later" with Pause (5.0)
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 3.0
        linear 2.0 alpha 0.0
    scene newsreporterending1
    newsreporter "As the world becomes more and more connected, cybersecurity plays a vital role in all of our lives."
    newsreporter "There are a lot of cybersecurity firms competing to give you the best bang for your buck."
    newsreporter "But one firm stands about the rest- Shilling Securities. Today, we have the founder and CEO of Shilling Securities, Mr. [player_name] Shilling."
    newsreporter "How are you this evening?"
    scene newsreporterending2
    main "I'm doing fine, thanks."
    newsreporter "So, what made you decide to get into cybersecurity?"
    main "A personal experience years ago."
    scene newsreporterending3
    main "I was in charge of a firm and I thought our private data was secure."
    main "Turns out it wasn't very secure at all and everything we kept secret was revealed to be public."
    main "That caused a huge legal headache for me, so I decided to do something about it."
    scene newsreporterending4
    newsreporter "And so you did. Out of all of the cybersecurity firms, your firm has been rated #1 by businesses this year."
    newsreporter "And hope of going into cybersecurity for individuals?"
    main "No, that's way too much work."
    newsreporter "Very well, Mr. [player_name] Shilling, everyone!"
    $persistent.kimgoodending = True
    scene kimgoodending1 with fade
    kim "Welcome home, honey."
    main "Where are the kids?"
    scene kimgoodending3
    kim "They're all asleep, including the one in here."
    kim "I saw your news interview."
    kim "You're becoming quite popular these days."
    kim "I'm so proud of you."
    scene kimgoodending2
    main "Thank you, Kim."
    kim "Hmm?"
    scene kimgoodending6
    $renpy.notify("New Pictures Unlocked in Kim's Gallery!")
    main "Even though we didn't get off to a good start. Thanks for being there for me."
    kim "You're welcome. I'll always be here for you. No matter what, [player_name]."
    stop music
    show kimgoodendingcard with Pause (10.0)
    $achievement.grant("Achievement03_KimGood")
init:
    $achievement.register("Achievement03_KimGood")
    $achievement.sync()
return

label lisagoodending:
    scene black with fade
    show text "5 Years Later" with Pause (5.0)
    $persistent.endings += 1
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 3.0
        linear 2.0 alpha 0.0
    $persistent.lisagoodending = True
    scene lisagoodending1
    lisa "There are so many people here."
    lisa "I can't believe it. I made it to the big leagues."
    main "I knew you could do it."
    scene lisagoodending2
    lisa "Aww...[player_name]. I couldn't do anything without you."
    lisa "You take care of the kids while I'm at school and you take care of the back end of the business."
    main "It's worth it, isn't it?"
    scene lisagoodending3
    $renpy.notify("New Pictures Unlocked in Lisa's Gallery!")
    lisa "Yes, it is. My own fashion brand on New York Fashion Week. A loving husband. Two kids."
    lisa "I couldn't ask for anything more."
    stop music
    show lisagoodendingcard with Pause (10.0)
    $achievement.grant("Achievement04_LisaGood")
init:
    $achievement.register("Achievement04_LisaGood")
    $achievement.sync()

return

label maigoodending:
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 3.0
        linear 2.0 alpha 0.0
    scene maigoodending3
    $persistent.endings += 1
    priest "Do you, Mai take [player_name] to be your lawfully wedded husband?"
    mai "Yes."
    priest "And do you, [player_name] take Mai to be your lawfully wedded wife?"
    main "Yes."
    scene maigoodending4
    "Then I hereby pronounce you as husband and wife. You may now kiss the bride."
    scene maigoodending5
    priest "Mr. and Mrs. [player_name] Shilling."
    scene black with fade
    show text "3 Years Later" with Pause (5.0)
    $persistent.maigoodending = True
    scene maigoodending1
    mai "This place is huge."
    main "Big enough for your family?"
    scene maigoodending2
    $renpy.notify("New Pictures Unlocked in Mai's Gallery!")
    mai "More than enough. But...you really want to be a farmer, [player_name]?"
    main "I don't have to deal with as many people and we have a lot of land."
    main "I've been researching aquaponics. We're farming for the future."
    mai "As long as you don't neglect your duties."
    main "I won't."
    show maigoodendingcard with Pause (10.0)
    stop music
    $achievement.grant("Achievement05_MaiGood")
init:
    $achievement.register("Achievement05_MaiGood")
    $achievement.sync()
return

label bellagoodending:
    scene black with fade
    show text "5 Years Later" with Pause (5.0)
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    scene newsreporterending1
    $persistent.endings += 1
    newsreporter "Today, the popular Roboling has reached over 100 million sales worldwide. We are here with the CEO of Robolings, Mr. [player_name] Shilling."
    newsreporter "How are you this evening?"
    main "I'm doing well. "
    scene newsreporterending2
    newsreporter "How does it feel that your invention is now being used in households across the globe?"
    main "Well, it isn't my invention. It's my wife's."
    scene newsreporterending3
    main "She's the quiet, studious type. Never believed anyone would appreciate it. She's overwhelmed by its success."
    newsreporter "Oh. So what's next?"
    scene newsreporterending4
    $persistent.bellagoodending = True
    main "Not sure. Probably something for commercial purposes."
    newsreporter "Interesting. Well, that wraps up our segment, you can purchase a Roboling today at RobolingEnterprises.com"
    scene bellagoodending1
    $renpy.notify("New Pictures Unlocked in Bella's Gallery!")
    bella "Good job on the interview, [player_name]."
    main "Thanks, Bella."
    scene bellagoodending2
    main "Aren't you tired?"
    bella "Never! I just got another robot idea!"
    show bellagoodending3 with Pause (10.0)
    stop music
    $achievement.grant("Achievement06_BellaGood")
init:
    $achievement.register("Achievement06_BellaGood")
    $achievement.sync()
return

label crissygoodending:

    scene black with fade
    show text "5 Years Later" with Pause (5.0)

    scene crissygoodending1
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    judge "I, state your name."
    crissy "I, Christina McNeill."
    $persistent.endings += 1
    $persistent.crissygoodending = True
    judge "Pledge to fulfill my duties to the state and to the people."
    crissy "Pledge to fulfill my duties to the state and to the people."
    judge "And to uphold the judicial system."
    crissy "And to uphold the judicial system."
    $renpy.notify("New Pictures Unlocked in Christina's Gallery!")
    judge "So help me."
    crissy "So help me."
    scene crissygoodending2
    crissy "As your Attorney General, I pledge to crack down on organized crime.."
    show crissygoodending with Pause(10.0)
    stop music
    $achievement.grant("Achievement07_CrissyGood")
init:
    $achievement.register("Achievement03_CrissyGood")
    $achievement.sync()
return

label maingoodending:
    $persistent.endings += 1

    scene black with fade
    show text "5 Years Later" with Pause (5.0)
    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    scene nyapartment
    "(Another long day at work.)"
    scene sologoodending
    "(I haven't been in contact with any of the girls at SPH.)"
    "(Instead, I've mostly focused on my career.)"
    "(And enjoying New York.)"
    show sologoodendingcard with Pause(10.0)
    stop music
    $achievement.grant("Achievement08_MainGood")
init:
    $achievement.register("Achievement08_MainGood")
    $achievement.sync()
return
