label chapter2:
    play music "music/track1.ogg"
    scene 1chapter2
    show chapter2title with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    "(Ok, simple enough. All I have to do is find the income statements and compare them.)"
    "(Hopefully one of these notebooks has them.)"
    scene upstairshall
    play sound "sfx/ElevatorDing.ogg"
    show lisa serious13 at center
    lisa "Hey [player_name], I-"
    stop sound
    show lisa surprise7 at center

    label answerlisa1:
        if persistent.timed_choices == True:
            $timeout_label = "lisastunned"
            jump answerlisa
        else:
            $timeout_label = None
            jump answerlisa

    label answerlisa:
        menu:
            lisa "What's going on here?"
            "I'm in the middle of something, ok?":
                $timeout_label = None
                show lisa sad1 at center
                $authority.trait_up(1)
                show authorityup at attributeup
                lisa "Ok...I can come back later."
                main "No, you're here now, what is it?"
                show lisa serious13 at center
                lisa "I have a new business for you to look at."
                main "Well, you can show me over there."
                lisa "Yeah, I will."
                jump lisasfirstpitch

            "I know it's messy, but it's not that bad, is it?":
                $timeout_label = None
                show lisa serious14 at center
                show charmup at attributeup
                $charm.trait_up(1)
                lisa "No, no I've seen worse."
                main "Really?"
                lisa "Typical college roommates. Beer cans and pizza everywhere."
                menu:
                    lisa "This is nothing."
                    "Something wrong?":
                        lisa "No, not really."
                        lisa "Just reminiscing about my younger days."
                        show lisa sad1 at center
                        lisa "I'll just go back downstairs."
                        main "No, no you came up here to talk to me about something, what is it?"
                        show lisa serious11 at center
                        lisa "I have a business-uh-elevator pitch."
                        menu:
                            lisa "But without the elevator, of course."
                            "Of course":
                                show lisa serious13 at center
                                $charm.trait_up(1)
                                show charmup at attributeup
                                main "Just sit over there."
                                main "I'll make my way over shortly."
                                jump lisasfirstpitch
                            "Sure, I'll listen to it.":
                                show lisa smile2 at center
                                $charm.trait_up(2)
                                show charmup at attributeup
                                lisa "Great!"
                                main "Just sit over there."
                                main "I'll make my way over shortly."
                                jump lisasfirstpitch

                    "You miss that kind of life?":
                        show lisa angry1 at center
                        $charm.trait_down(1)
                        show charmdown at attributedown
                        lisa "No. Ew."
                        lisa "How you can boys live like that I have no clue."
                        menu:
                            lisa "I'll just go back downstairs."
                            "No, don't leave me":
                                show lisa flirt1 at center
                                $charm.trait_up(1)
                                show charmup at attributeup
                                lisa "Didn't know you were the needy type."
                                lisa "I'll be waiting for over there."
                                jump lisasfirstpitch
                            " You came all this way to go back downstairs?":
                                show lisa sad1 at center
                                $authority.trait_up(1)
                                show authorityup at attributeup
                                lisa "Uhm...welll.."
                                main "Take a seat over there."
                                main "I'll be over there shortly."
                                jump lisasfirstpitch

    label lisastunned:
        $timeout_label = None
        show lisa serious13 at center
        lisa "Never mind, I won't ask."
        main "Oh, I-I'm just trying to make sense of all of this paperwork."
        lisa "Do you need any help?"
        main "I need to do this on my own."
        show lisa flirt2 at center
        lisa "Aww. You're so cute, being the big guy in the office."
        main "Did you need something?"
        show lisa smile3 at center
        lisa "I have a new business venture for you to look at."
        lisa "But I can come back later."
        main "No, no I'll view it now."
        jump lisasfirstpitch

    label lisasfirstpitch:
        scene upstairslounge2
        show lisa serious2 at center
        lisa "So you have you ever played any sports?"
        main "Sports?"
        lisa "Football, Track and Field, Tennis, Basketball?"
        main "I did track and field in high school. Lunges, actually."
        show lisa serious1 at center
        lisa "And what about roleplaying games? The turn-based type?"
        main "In high school, but nothing recent."
        lisa "Really?"
        lisa "Well, this game is like a combination of the two genres!"
        main "A combination?"
        lisa "Yeah, it's a game with athletes using their skills to save the world!"
        scene lisafootball
        lisa "But in a sexy outfit, of course."
        lisa "After every victory, they do a special dance."
        lisa "There's a story mode and a player versus player mode where they can compete for prizes."
        scene 2chapter2
        lisa "What do you think? The developer wants an answer today if you want to help publish his game."
        lisa "Hey are you listening to me?"
        lisa "I know that look."
        scene 3chapter2
        main "What are you doing?"
        scene 4chapter2
        lisa "Making sure you pay attention, of course."
        main "I am paying attention. "
        scene upstairslounge
        show lisa serious6 at center
        lisa "So are we going to buy it or not?"
        if persistent.timed_choices == True:
            $timeout_label = "lisahuffy"
            jump answerlisa2
        else:
            $timeout_label = None
            jump answerlisa2

        label answerlisa2:
            menu:
                lisa "The developer wants an answer, today."
                "I just got here.":
                    show lisa serious10 at center
                    $timeout_label = None
                    lisa "And you're the boss."
                    lisa "I need an answer now."
                    main "Ok..I guess."
                    show lisa surprise3 at center
                    lisa "I guess?"
                    main "Yes. Yes."
                    lisa "You really are new to this, aren't you?"
                    main "I am."
                    show lisa serious12 at center
                    lisa "You need to be more convincing. Like {b}YES!!{/b}."
                    main "{b} YES!{/b}"
                    show lisa smile2 at center
                    lisa "There we go."
                    lisa "I will let the developer know."
                    jump interrogatelisa1


                "Yes.":
                    show lisa surprise1 at center
                    lisa "Oh. That was quick."
                    $timeout_label = None
                    $authority.trait_up(2)
                    show authorityup at attributeup
                    lisa "I will let the developer know."
                    jump interrogatelisa1


    label lisahuffy:
        $timeout_label = None
        show lisa angry3 at center
        lisa "Well, if you don't have an answer for me, I'll just tell the developer no."
        main "I have a lot of questions."
        lisa "What kind of questions?"
        main "Platform, target age group, and why he wants {i}us{/i} to host it."
        main "Couldn't he host it himself?"
        show lisa sad1 at center
        lisa "Well-uh-I said mobile, and it's primarily for men, and I don't think he can afford to host it."
        lisa "So that's why he is selling it to us."
        lisa "Does that clear things up for you?"
        main "Yes it does. We'll buy it."
        show lisa smile2 at center
        lisa "Good!"
        jump interrogatelisa1



    label interrogatelisa1:
        main "I have a question for you, Lisa."
        show lisa serious3 at center
        menu:
            lisa "Oh? What is it, [player_name]?"
            "What are your responsibilities?":
                show lisa serious9 at center
                lisa "My responsibilities?"
                lisa "I am the first point of contact for anyone inquiring about doing business with us."
                main "What kind of businesses do we attract?"
                show lisa serious11 at center
                lisa "Oh, well we're a tech company, so mostly we buy software applications and games no one wants to host anymore."
                lisa "I get all of their information, the boss- that's you- approves of the sale,Mai buys the software, and then Bella hosts it."
                lisa "The developer is free of their creation and we get another source of income."
                menu:
                    lisa "Does that answer your question?"
                    "What does Kim do?":
                        show lisa serious14 at center
                        lisa "Kim?"
                        lisa "Well she uh.."
                        lisa "She takes care of bank deposits."
                        main "That isn't Mai's job?"
                        lisa "No, she just records the numbers."
                        lisa "Maybe you should talk to her."
                        jump lisaisconcerned

                    "Yes it does.":
                        show lisa serious14 at center
                        lisa "Is something wrong?"
                        main "No..."
                        lisa "If it's about the auditor, you should ask Mai to come in here."
                        lisa "She is the one who handles all of the important paperwork."
                        main "Oh. Thanks."
                        jump lisaischarmed

            "What do you know about this company?":
                show lisa serious13 at center
                lisa "We buy abandoned software and host it."
                lisa "That's it. We get all of the revenue from people buying and using the abandoned software."
                main "And your job is..?"
                show lisa serious2 at center
                lisa "I convince the developer to sell their software to us."
                menu:
                    lisa "Is there anything else?"
                    "And Kim? What does she do?":
                        show lisa surprise1 at center
                        lisa "Kim? Oh..you should ask her yourself."
                        lisa "All I know is that she was John's executive assistant and uh-"
                        lisa "Hahah. Oh, do you know about the auditor that's coming next week?"
                        main "I do."
                        lisa "I think you should talk to Mai."
                        lisa "She can help you with a lot of things."
                        jump lisaisconcerned

                    "No, that's all for now.":
                        show lisa surprise2 at center
                        lisa "Are you ok?"
                        lisa "You look a bit anxious."
                        lisa "Wait, do you..know about the auditor that's coming?"
                        main "I do now."
                        lisa "I think Mai can help you if you need help with finances."
                        lisa "She is the accountant, after all."
                        main "Thanks."
                        jump lisaischarmed



    label lisaischarmed:
        show lisa flirt3 at center
        $cLisa.morale_up(1)
        show moraleup at attributeup
        lisa "[player_name], you're not at all like your dad."
        main "Is that a bad thing?"
        lisa "Not for me. It's great."
        lisa "But. How do I put this?"
        show lisa angry4 at center
        lisa "I don't think being{i} charming {/i}is going to work on Kim."
        main "Hmm."
        show lisa serious4 at center
        lisa "Sometimes you can't be our friends. You've got to have a little authority."
        lisa "So just keep an eye on how you approach the situation, ok?"
        main "Sure."
        if footlover == True:
            show lisa flirt1 at center
            lisa "You know, {i} my{/i} shoe size is a size 7."
            lisa "And I like to wear high heels."
            with smallshake
            show lisa smile5 at center
            lisa "I also like foot massages!"
            lisa "Anyway, talk to you later, [player_name]."
            hide lisa smile5
            jump afterlisaleaves
        else:
            show lisa smile2 at center
            lisa "I'll be leaving now, see you later, [player_name]."
            main "Yeah, sure. See you later, Lisa."
            hide lisa smile2
            jump afterlisaleaves

    label lisaisconcerned:
        show lisa serious14 at center
        lisa "[player_name], you're a bit like your father."
        main "I am?"
        lisa "Yeah, he's a bit pushy sometimes."
        menu:
            lisa "I thought you would be different."
            "That's just who I am.":
                show lisa sad1 at center
                lisa "I see."
                lisa "Well, I think that kind of attitude works well with Kim."
                lisa "I doubt Bella cares."
                lisa "I'll be going then. I need to call the developer and tell him the game is a go!"
                main "See you Lisa."
                jump afterlisaleaves

            "Uh, I'll try to lighten up then.":
                $authority.trait_down(1)
                show authoritydown at attributedown
                if footlover == True:
                    show lisa flirt2 at center
                    lisa "You could always buy me a pair of shoes."
                    lisa "I'm a size 6."
                    with smallshake
                    show lisa smile4 at center
                    lisa "Hahah, I'm kidding!"
                    lisa "I need to call the developer."
                    lisa "Talk to you later, [player_name]."
                    hide lisa smile4
                    jump afterlisaleaves

                else:
                    show lisa sad3 at center
                    lisa "I didn't mean to shame you."
                    lisa "It's just, sometimes working at this office can be suffocating."
                    lisa "And I didn't expect someone so young to be so dominating."
                    main "Oh, it just came to me."
                    lisa "Well that kind of thinking works well with Kim."
                    show lisa serious13 at center
                    lisa "I should be going then."
                    lisa "I need to call the developer."
                    main "Yeah, go ahead."
                    lisa "See you later."
                    hide lisa serious13
                    jump afterlisaleaves

    label afterlisaleaves:
        scene messyfloor
        "(I'm glad Lisa came up here.)"

        menu:
            "(Maybe I should take Lisa's advice and ask Mai for help.)"
            "Call Mai":
                jump askformaishelp
            "Forget it":
                "(Nah, I'm better off it doing this myself.)"
                jump doitonhisown


    label doitonhisown:

        "(As for this mess.)"
        "(I should start somewhere.)"
        "(Hmm..I'll pick this book and this one.)"
        "(...They're both income statements.)"
        "(I think I might be onto something.)"
        jump compareincomestatements

    label askformaishelp:
        scene 5chapter2
        main "Hello, Mai?"
        mai "Huh? Who is this?"
        main "It's [player_name]."
        mai "Oh..why are you calling me from your cell phone?"
        main "Uh. I can't get to my office phone."
        main "Do you mind coming up here for a second?"
        mai "Sure."
        scene shelves
        show mai curious1 at center
        mai "What did you need me for?"
        show mai serious4 at center
        mai "Ohh. This office is a mess. I thought Lisa cleaned everything for you."
        main "Mai..."
        scene 6chapter2
        mai "{cps=*0.5}Here are all of the accounting records..Invoices...{/cps}"
        mai "I think these are the bank statements."
        scene 7chapter2
        "MAI!!!"
        mai "Hmm? Oh, I'm sorry."
        main "Where are the income statements?"
        mai "Oh, the income statements?"
        scene 8chapter2
        mai "Hmm...here."
        mai "And you'll need this notebook as well."
        main "Why do I need this notebook?"
        scene shelves
        show mai sad1 at center
        mai "Uhm."
        mai "John has two copies of everything."
        mai "So you need both of them."
        show mai serious2 at center
        if footlover == True:
            menu:
                mai "Is there anything else you need?"
                "No.":
                    show mai smile2 at center
                    mai "Ok, I will be going now."
                    mai "If you need anything else, please call me using the{i}office phone{/i}"
                    with smallshake
                    main "Yeah, thanks for reminding me."
                    mai "Bye now!"
                    hide mai smile2
                    "(So these two books.)"
                    "(Time to get cracking.)"
                    jump compareincomestatements


                "I'm sorry for earlier.":
                    show mai serious3 at center
                    mai "Hmm?"
                    main "I'm sorry that I- I asked for your shoe size."
                    mai "Oh!"
                    main "I don't want you to think that I'm a creep."
                    menu:
                        mai "Hahha...did Lisa tell you that?"
                        "No, she didn't.":
                            main "She just told me {i}her{/i} shoe size."
                            show mai sad4 at center
                            mai "Oh."
                            mai "She must really like you, then."
                            main "Anyway, thank you, Mai for your help."
                            show mai smile2 at center
                            mai "You're welcome, [player_name]."
                            hide mai smile2
                            "(So these two books.)"
                            "(Time to get cracking.)"
                            jump compareincomestatements


                        "She didn't say it, but..":
                            show mai flirt4 at center
                            mai "Oh, that is Lisa for you."
                            mai "I know you're not a creep, [player_name]."
                            main "You do?"

                            menu:
                                mai "Yeah, you haven't tried to touch me, even though we're alone."
                                "I'm a gentleman.":
                                    $charm.trait_up(2)
                                    show charmup at attributeup
                                    main "And your boss."
                                    mai "I know, I know-"
                                    main "Wait, did my dad do it?"
                                    show mai flirt6 at center
                                    mai "Uh...hahahha."
                                    mai "No, no. Just at my old job."
                                    mai "Lots of touching!"
                                    main "Anyway, thank you, Mai for your help."
                                    $cMai.morale_up(2)
                                    show moraleup at attributeup
                                    show mai smile4 at center
                                    mai "You're welcome, [player_name]."
                                    hide mai smile4
                                    "(So these two books.)"
                                    "(Time to get cracking.)"
                                    jump compareincomestatements

                                "Is that an invitation?":
                                    $charm.trait_down(1)
                                    show charmdown at attributedown
                                    show mai cynic2 at center
                                    mai "...No."
                                    mai "I'll just kick you if you do."
                                    mai "!!!"
                                    with smallshake
                                    show mai surprise at center
                                    mai "No, no, I didn't mean that!"
                                    mai "I'm sorry, please don't fire me."
                                    main "You're pretty scary when you threaten people, Mai."
                                    main "Anyway, thank you, Mai for your help."
                                    show mai smile4 at center
                                    mai "You're welcome, [player_name]."
                                    hide mai smile4
                                    "(So these two books.)"
                                    "(Time to get cracking.)"
                                    jump compareincomestatements





        else:
            mai "Is there anything else you need?"
            main "No, nothing else."
            main "I have everything I need. Thank you, Mai."
            show mai sad1 at center
            mai "Mmm...."
            main "Is something wrong?"
            mai "No. You're welcome, [player_name]."
            hide mai sad1
            "(I'll find out later. For now, these two books.)"
            "(Time to get cracking.)"
            jump compareincomestatements

    label compareincomestatements:
        scene messyfloor
        show fakeincomestatement at topleft
        "Here's the public one."
        show realincomestatement at topright
        "Here's the real one."
        "Hmmm..."
        "Higher revenue."
        "The incomes aren't consistent."
        "And the taxes are the same."
        hide fakeincomestatement
        hide realincomestatement
        "Time for a short nap."
        scene black with fade
        jump passoutfromreading



    label passoutfromreading:
        show screen eyeopening
        scene nightfloor1
        stop music
        play sound "sfx/mast3.ogg"
        "(What time is it?)"
        "(And what's the noise?)"
        hide screen eyeopening
        play music "music/track6.ogg"
        scene nightfloor2
        "(It must be coming from the laptop.)"
        "(Looks like everyone's gone, except for her.)"
        if persistent.sexscenes == False:
            scene nightfloor3
            "Ahhhh....."
        else:
            show screen monitor
            scene kimmast3
            "Ohh..my pussy feels so good."
            "I wish you all could feel how nice and wet I am."
            scene kimmasturbate
            "Mmmm...."

        menu:
            "(What should I do.)"
            "Keep watching":
                if persistent.sexscenes == False:
                    stop sound
                    scene 9chapter2 with fade
                    kim "Did you enjoy the show, [player_name]?"
                    scene 10chapter2
                    kim "I know you're watching me."
                    kim "Do you need some help? I'll be up there shortly."
                    stop music
                    hide screen monitor
                else:
                    scene kimorgasm1
                    "Ahhhh!!!!"
                    scene kimmast1
                    "That felt nice."
                    stop sound
                    scene 9chapter2 with fade
                    kim "Did you enjoy the show, [player_name]?"
                    scene 10chapter2
                    kim "I know you're watching me."
                    kim "Do you need some help? I'll be up there shortly."
                    stop music
                    hide screen monitor
                play music "music/track1.ogg"
                scene upstairshall
                show kim smile3 at center
                kim "Hello [player_name]."
                kim "So, were you turned on by my performance?"
                kim "Do you need a bit of relief?"
                show kim smile4 at center
                menu:
                    kim "I can help you, that's {i}my{/i} job after all."
                    "Stay away from me":
                        main "You're disgusting."
                        show kim serious3 at center
                        kim "Me? You watched me dear."
                        kim "And I know you liked it."
                        main "So your job was to jack off my dad whenever he felt like it?"
                        show kim smile7 at center
                        kim "I did other things as well, but that's not important, is it?"
                        main "It is. There's an audit-"
                        show kim smile10 at center
                        kim "Shhh. Just show the auditor all of the {i} correct{/i} forms."
                        menu:
                            kim "Now, be a good boy and let me take care of you."
                            "I said stay away from  me!":
                                $authority.trait_up(2)
                                show authorityup at attributeup
                                show kim sad4 at center
                                kim "Aww, poor baby."
                                kim "Is this your first blowjob?"
                                kim "I can make it memorable."
                                main "That's none of your business."
                                main "Leave."
                                jump kimneutralending

                            "Fine, just this once.":
                                main "But don't tell the others."
                                kim "I won't."
                                kim "It will be our secret."
                                jump kimfirstbj

                    "Say nothing.":
                        kim "You're so cute."
                        kim "Come here, let me take care of you."
                        jump kimfirstbj

            "Turn off the internet":
                "(Time to ruin her little show in {cps=*0.2}3..2..1.{/cps})"
                scene 11chapter2
                kim "Huh? Disconnected?"
                kim "There's no internet??"
                scene 12chapter2
                kim "You turned it off, didn't you, [player_name]?"
                scene 10chapter2
                kim "I know you're watching me."
                kim "Do you want a private show?"
                kim "I can come up and give you one."
                hide screen monitor
                stop music
                "(There's no avoiding her now.)"
                play music "music/track1.ogg"
                scene upstairshall
                show kim smile1 at center
                kim "Hello [player_name]."
                kim "Did you like the show?"
                main "Why are you doing webcam shows in the office, after hours?"
                show kim serious3 at center
                kim "Because I can."
                kim "And I always have."
                kim "Is that a problem, [player_name]?"
                show kim smile4 at center
                kim "I promise I'll only do it when no one else is here."
                kim "Please?"
                jump kimfirstfight

    label kimfirstfight:
        if persistent.timed_choices == True:
            $timeout_label = "kimwussending"
            jump arguewithkim1
        else:
            $timeout_label = None
            jump arguewithkim1

    label arguewithkim1:
        menu:
            "(It's weird to hear and see her like this.)"
            "Sweet talk is not going to work on me.":
                $authority.trait_up(1)
                jump kimrebuttal1
            "Business comes first.":
                $charm.trait_up(1)
                show charmup at attributeup
                main "You can do your webcam shows at home."
                main "When you're here, you're working for me."
                jump kimbelittle1

        label kimrebuttal1:
            show authorityup at attributeup
            show kim serious2 at center
            kim "Then what will?"
            kim "Because I think we need to come to a mutual understanding."
            menu:
                kim "I'm your {i}senior{/i} and things go {i}my way{/i}."
                "I'm in charge now. Things are different.":
                    $authority.trait_up(2)
                    jump kimrebuttal2
                "Is that so?":
                    $charm.trait_up(1)
                    jump kimbelittle2

        label kimrebuttal2:
            show authorityup at attributeup
            show kim angry2 at center
            kim "Oh? I'm sorry. Should I repeat myself? I started this company with John, not you."
            kim "You were still living with your mommy crying about why daddy left."
            show kim angry11 at center
            kim "Maybe you shouldn't have told your precious mommy about your daddy's affairs."
            menu:
                kim "So why don't you show some respect for your senior employee?"
                "I could just fire you.":
                    $authority.trait_up(1)
                    jump kimrebuttal3
                "How should I respect you? After all you've done?":
                    jump kimbelittle3

        label kimrebuttal3:
            show kim angry3 at center
            kim "You can't fire me!"
            show authorityup at attributeup
            menu:
                kim "You're not the REAL boss!"
                "As of now, I am the boss and I can fire you.":
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    jump kimbelittle4
                "Calm down.":
                    $authority.trait_up(2)
                    jump kimrebuttal4

        label kimrebuttal4:
            show kim sad1 at center
            show authorityup at attributeup
            main "You're taking this too far."
            main "Take a few deep breaths and we can talk like adults."
            menu:
                "(Why is she approaching me?)"
                "(Wait)":
                    jump kimdominantending
                "What are you doing?":
                    jump kimneutralending


        label kimbelittle1:
            show kim serious4 at center
            kim "{i}I turn it off when I say so.{/i}"
            kim "This isn't elementary school."
            menu:
                kim "It's a business, little boy."
                "I am not a little boy. I am your boss.":
                    $authority.trait_up(1)
                    jump kimrebuttal1
                "I know it's a business. I'm just establishing a boundary.":
                    jump kimbelittle5

        label kimbelittle2:
            show kim serious6 at center
            show charmup at attributeup
            kim " {i}Is that so?{/i}"
            kim "Of course it is."
            menu:
                kim "You wouldn't know since you just got here."
                "And I am in charge, like you said.":
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    main "Things will be different now."
                    jump kimrebuttal2
                "I know I just got here-":
                    $authority.trait_down(1)
                    jump kimbelittle6


        label kimbelittle3:
            show kim serious7 at center
            kim "I don't know, maybe you should get on your knees and kiss my feet."

            menu:
                kim "I bet you would like that, wouldn't you?"
                "You're going too far. Calm down":
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    main "That would get us in a lot of trouble."
                    main "And I would be better off firing you."
                    jump kimrebuttal3
                "Yeah, that sounds great.":
                    $charm.trait_up(1)
                    jump kimbelittle7


        label kimbelittle4:
            show kim angry9 at center
            kim "I'm his most valuable employee."
            main "If my dad valued you so much, why didn't he take you on his extended vacation?"
            kim "Shut. Up."
            kim "Our relationship is none of your business."
            kim "He didn't take you along either, now did he?"
            main "Who would run the business if both of us were gone?"
            show kim sad5 at center
            kim "{cps=*0.2}..........{/cps}"
            if authority.amount >= charm.amount:
                "(She's quiet.)"
                jump kimdominantending
            else:
                "(She's gazing off.)"
                jump kimneutralending

        label kimbelittle5:
            show kim angry7 at center
            kim "Maybe you need a little course on how this business works."
            kim "You order the other girls around, and I do whatever I please in my office."

            menu:
                kim "Is that understood?"
                " No. You're an employee. I'm the boss.":
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    main "And I can fire you for being incompetent and wasting company money."
                    jump kimrebuttal3

                "Understood as long as you do what I ask of you.":
                    main "I am still the boss here."
                    if authority.amount >= charm.amount:
                        kim "(.....)"
                        jump kimneutralending
                    else:
                        kim "You just don't get it, do you?"
                        jump kimwussending



        label kimbelittle6:
            show kim angry10 at center
            kim "So technically I am your superior."
            show authoritydown at attributedown

            menu:
                kim "And you should listen to me."
                "That's not how it works.":
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    main "I'm still the boss."
                    main "It doesn't matter if you were here before me."
                    show kim angry9 at center
                    kim "It doesn't matter?!?!"
                    jump kimrebuttal4

                "Please, grace me with your sage advice.":
                    $charm.trait_up(1)
                    show kim angry8 at center
                    show charmup at attributeup
                    kim "Here is my advice, [player_name]."
                    kim "{cps=*0.3}Leave. Me. Alone.{/cps}"
                    jump kimwussending

        label kimbelittle7:
            show charmup at attributeup
            kim "Don't play coy with me, little boy."
            kim "You're not even fit to be in the same room as me."
            jump kimwussending



    label kimwussending:
        $timeout_label = None
        show kim serious1 at center
        kim "I don't have to deal with this."
        show kim angry9 at center
        kim "{cps=*0.5}You. Will.{size=+10} NEVER.{/size} Be. Your. Father.{/cps}"
        kim "If you think your smart ass comments and smile will work on me, it won't."
        show kim serious3 at center
        kim "You will turn that internet back on IF you know what's good for you and this company."
        main "I'll consider it."
        show kim angry7 at center
        kim "You're a pushover."
        main "Good night, Kim."
        kim "And you can kiss your little office good-bye."
        hide kim angry7
        "(And just like that, she's gone.)"
        jump endofchapter2


    label kimneutralending:
        $timeout_label = None
        main "I'll turn the internet back on."
        main "And you can do your little webcam shows."
        show kim smile3 at center
        kim "I knew we could come to an understanding!"
        show moraleup at attributeup
        $cKim.morale_up(1)
        main "But with a condition."
        show kim smile1 at center
        kim "And that is?"
        main "When the auditor arrives-"
        show kim smile7 at center
        kim "Of course. I'll help you with anything you need."
        kim "It's time for me to go but-"

        menu:
            kim "Are you sure you don't need some relief?"
            "I'm sure.":
                show kim sad7 at center
                kim "Aww, ok."
                kim "Good night, [player_name]."
                hide kim sad7
                "(And like that, she's gone.)"
                jump endofchapter2

            "Well-":
                show kim smile4 at center
                kim "Of course you do."
                jump kimfirstbj

    label kimdominantending:
        $timeout_label = None
        show kim smile4 at center
        kim "Listen. You're stressed out."
        kim "Why don't you let mommy take care of you."
        kim "Let her blow off a load."
        main "You're not my mom."
        show kim smile7 at center
        kim "Well how about your sister?"
        kim "I bet you always wanted me as one."
        main "Kim, just-"

        menu:
            kim "I promise, it will clear your mind."
            "Fine just this one time":
                jump kimfirstbj
            "I have a clear mind":
                kim "Huh?"
                main "I said I have a clear mind."
                jump kimneutralending

    label kimfirstbj:
        scene kimbj2
        kim "That's a good boy. Just relax and let me take care of the rest."
        if persistent.sexscenes == False:
            scene black with fade
            jump afterkimsfirstbj
        else:
            jump kimbjview

    label kimbjview:
        scene kimbj
        menu:
            "View 2":
                jump kimbjview2
            "View 3":
                jump kimbjview3
            "Stop":
                jump afterkimsfirstbj

    label kimbjview2:
        scene kimbjv2
        menu:
            "View 1":
                jump kimbjview
            "View 3":
                jump kimbjview3
            "Stop":
                jump afterkimsfirstbj

    label kimbjview3:
        scene kimbjv3
        menu:
            "View 1":
                jump kimbjview
            "View 2":
                jump kimbjview2
            "Stop":
                jump afterkimsfirstbj

    label afterkimsfirstbj:
        scene upstairshall
        show kim smile7 at center
        kim "So, do you want this every night?"
        main "No."
        kim "Why not? We can keep this our little secret."
        main "I have more important things to require my attention."
        main "You can do your little webcam show - but after I leave the office."
        show kim smile10 at center
        kim "Aww, I knew you would come around."
        show moraleup at attributeup
        $cKim.morale_up(3)
        kim "Well, I'm done for the night."
        kim "If you need anything else-"
        main "No, I'm fine."
        kim "Good night, [player_name]."
        hide kim smile10
        "(Whew, she's gone.)"
        jump endofchapter2

    label endofchapter2:
        scene messyfloor
        "Now back to this."
        scene 14chapter2
        "(Hmm..what's in this notebook.)"
        scene 15chapter2
        "(A hidden ledger?)"
        "(Things aren't adding up.)"
        "(This is overwhelming.)"
        "(I'll deal with it tomorrow.)"
        stop music
        scene black with fade
        play sound "sfx/misc_sound.ogg"
        show chapter2titleend with easeinright:
            yalign 0.4
            alpha 0.5
            linear 2.0 alpha 1.0
            pause 4.0
            linear 3.0 alpha 0.0

        jump chapter3
            
