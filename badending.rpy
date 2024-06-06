label badending2:
    if pickkim == True:
        scene kimguiltyverdict
        "(I'm sorry, Kim.)"
        jump badending
    elif picklisa== True:
        scene lisaguiltyverdict
        "(I'm sorry, Lisa.)"
        jump badending
    elif pickmai ==True:
        scene maiguiltyverdict
        "(I'm sorry, Mai.)"
        jump badending
    else:
        jump badending



label badending:
    scene black
    "(I have a visitor.)"
    $persistent.endings += 1
    $persistent.bad_ending == True
    play music "music/track11.ogg"
    scene mominjail1

    show epiloguetitle with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    main "Mom?"
    mom "Hello, honey. How are you?"
    main "I'm uh..I'm doing well."
    main "How are you? How are things outside?"
    mom "Well.."
    if pickkim == True:
        mom "...I'm sorry you have to hear this from me."
        scene mominjail2
        mom "But..Kimberly...committed suicide."
        scene badending8
        "(WHAT?!?!!)"
        mom "She left this note for you."
        scene mominjail4
        "To my dearest [player_name] {b}I{/b} couldn't bear t{b}h{/b}e thought of being {b}a{/b}lone for three years."
        "After e{b}ve{/b}rything I have done, I did {b}no{/b}t want to burden you on{b}c{/b}e you are released from prison."
        "I want you to {b}h{/b}ave a fresh start in life with{b}o{/b}ut me. {b}I{/b} sin{b}c{/b}erely lov{b}e{/b} you, Kim"
        ".........."
        scene mominjail3
        mom "I'm sorry, [player_name]."
        mom "Even though I didn't like her, I know how much she meant to you."
        mom "...I hope you're not regretting your decision right now."
        mom "Here is another letter from your landlord regarding your things."
        mom "....Goodbye, [player_name]."
        scene mominjail5
        "Listen, she wasn't necessary. You don't need her anymore."
        "Your things are packed away in storage."
        "I'll be waiting for you - Dad."
        jump mcreleasedfromjail
    elif pickmai == True:
        scene mominjail2
        mom "...Well. I did my best to keep Miss Amaya in the country."
        mom "But the judge set some harsh conditions."
        main "What do you mean?"
        mom "She's not allowed to do any form of accounting any more."
        mom "And with no other viable skills...her visa couldn't be renewed."
        scene badending10
        mom "So she went home."
        main "But I promised her..I would marry her.."
        scene mominjail3
        if nocontest == True:
            mom "And that went out of the window the moment you pleaded no contest."
        else:
            mom "And you got convicted."
        mom "You have to wait a decade before you could go through the whole process."
        mom "Do you really think she would wait that long?"
        main "I..."
        mom "I hope you don't regret your decision."
        mom "You are my son, but you need to be on your own now."
        mom "Here's a letter for you."
        scene mominjail4
        "Don't worry about her, you will see her again in due time. And get as many massages from her as you like!"
        scene mominjail5
        "Your things are in storage, I'll be waiting for you- Dad."
        jump mcreleasedfromjail
    elif picklisa == True:
        scene mominjail2
        mom "You know how I said Lisa was exactly like me?"
        main "Yeah."
        mom "I meant it."
        main "What do you mean?"
        mom "When the going gets tough, she leaves."
        mom "She's not the type to stay around if her 'Mr.Perfect' isn't perfect."
        main "But her dreams...New York."
        mom "Oh she's in New York alright. Living her dream."
        scene badending9
        mom "If you call being an escort to rich men a dream."
        "(.........)"
        scene badending3
        mom "No regrets. She was that kind of girl. You dodged a bullet."
        mom "Likewise, I think it's time for me to let you fly on your own."
        mom "Here's a letter for you."
        scene badending4
        "You will have prettier, more submissive girls to chooose from. Leave her alone."
        scene badending5
        "Your things are in storage, I'll be waiting for you- Dad."
        jump mcreleasedfromjail
    else:
        scene mominjail2
        mom "Well..."
        mom "Do you remember Kimberly Taylor?"
        main "Of course I do."
        mom "...She committed suicide."
        "(WHAT?)"
        scene badending3
        mom "They found her body in her apartment, on her bed."
        mom "Along with a note."
        scene badending8
        "I have no other purpose in life now. I have done everything I needed to do."
        "I wish I could have had a normal life, but it's not possible."
        "Tell [player_name] thanks for making me realize how worthless I really am."
        "I won't ruin anyone's life anymore."
        "(.....)"
        scene badending10
        mom "Let's see. Mai Amaya was deported back to her home country. I hear they're still recovering from that natural disaster years ago."
        scene badending11
        mom "Alyssa Rogers was charged with investor fraud as well, but she got a light sentence. Who knows what's she's doing."
        mom "Isabella Cole didn't even have a trial. Her father pulled a lot of strings to get her case dismissed."
        mom "And that officer got paid leave, but returned to work."
        scene mominjail3
        mom "Do you feel satisfied with your decision?"
        main "....."
        mom "You should have taken the deal. Your father wasn't worth all of this."
        mom "No matter what, you will always be my son."
        mom "But I don't think you need my help any more."
        mom "Also, this letter came for you. It's from your landlord I suppose."
        scene badending4
        "Don't let anyone read this."
        "Your stuff is stored away in storage. Below is the address."
        scene badending5
        "I'll be waiting for you when you get out. I'll throw a big party for you! - Dad."
        stop music
        jump mcreleasedfromjail

label mcreleasedfromjail:
    scene black with fade
    show text "5 Years Later" with Pause (5.0)
    play music "music/track10.ogg"
    "(It's been five years.)"
    scene badending5
    "(And no one's here to greet me.)"
    "(According to the letter, my things are in a storage container.)"
    scene badending6
    "(Guess I will walk there.)"
    scene badending7
    unvoice "[player_name] Shilling?"
    main "Yeah, that's me."
    unvoice "Get in the car. Your dad's waiting for you."
    scene emptylobby with fade
    "(Man that was a long flight.)"
    "(This place is fancy.)"
    dad "[player_name]!!!!!!!"
    scene badending1
    main "Hey, dad."
    dad "So you're not a sellout. For a moment there, I was worried."
    scene badending2
    dad "You're a real stand-up guy, son."
    dad "I'm proud of you."
    main "So what happens now?"
    scene badending3
    dad "We get to work on our new business."
    dad "Luxury travel."
    dad "This is your new office. Our new office."
    scene badending4
    dad "Trust me, it's going to be a lot of fun."
    show badendingcard with Pause (10.0)
    $achievement.grant("Achievement10_BadEnding")
init:
    $achievement.register("Achievement10_BadEnding")
    $achievement.sync()
return
