label chapter1:
    scene outsideoffice
    show chapter1title with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    play music "music/track3.ogg"
    "(8020 Whaling Street.)"
    "(This is the address that my father e-mailed me a few days ago.)"
    "(I haven't seen him since my parents divorced 10 years ago. Since then, he's opened up a new business while I attended college.)"
    "(To be truthful, I'm a bit nervous. I just hope this is the right building.)"
    scene frontdeskclear
    "Hello? Is anyone there?"
    "Hello?"
    scene 1chapter1
    "Welcome to Shilling Private Holdings, my name is Mai Amaya."
    "How may I help you?"
    scene downstairsdesk
    show mai smile2 at center
    "(Well the company name is correct.)"
    "Does a John Shilling work here?"
    mai "He does. Did you have an appointment with him this morning?"
    "No, not really. I-uh-"
    show mai serious4 at center
    mai "Well, he happens to be in his office, which is unusual for a Saturday morning."
    "(It's Saturday?)"
    show mai smile2 at center
    mai "Would you like for me to call him and tell him you're here?"
    "Yes, sure."
    mai "Your name?"
    scene 2chapter1
    $player_name = renpy.input("")
    $player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Robert"
    main "[player_name]"
    "(That's me by the way. Fresh out of Business School.)"
    scene downstairsdesk
    show mai serious1 at center
    mai "{cps=*0.2}[player_name]....[player_name].....[player_name].....{/cps}"
    main "Are you ok, Miss Amaya?"
    show mai smile6 at center
    mai "Oh, I was just memorizing your name, sorry. I will go call him now."
    scene 3chapter1
    "So are you the only one working here or?"
    mai "No, there are others, but I am here first."
    scene 4chapter1
    "Hello John? This is Mai. Mister.."
    "[player_name]"
    "Mister [player_name] is requesting to meet you. Shall I send him up?"
    "Mmm hmm.."
    "Yes."
    "I will send him up shortly."
    scene frontdesk2
    show mai smile2 at center
    main "Thank you, Miss Amaya."
    mai "Oh, you can just call me Mai."
    main "Uhm. I have a question, Mai."
    show mai smile3 at center

    label talktomai1:
        menu:
            mai "Yes?"
            "Do you have any advice?":
                jump mai_advice1
            "What is John Shilling like?":
                jump mai_advice2
            "What is your shoe size?":
                jump mai_advice3

    label mai_advice1:
        show mai curious1 at center
        mai "Any advice?"
        main "Yeah, like a pep talk."
        main "I haven't really seen my d- I haven't seen John in years."
        show mai smile5 at center
        mai "Just be yourself."
        mai "John doesn't like pomp-pomp-"
        main "Pompous?"
        mai "Yeah, he doesn't like people who are fancy with their words."
        main "I will take that advice, thanks, Mai."
        mai "You're welcome, [player_name]"
        hide mai smile5
        jump intheelevator

    label mai_advice2:
        show mai serious1 at center
        mai "Well. He's tall. And big. Very big."
        mai "Almost scary."
        "(Perfect description of my dad.)"
        main "Likes and dislikes?"
        mai "He likes girls and hates boys."
        "(Definitely my father.)"
        show mai serious3 at center
        mai "Oh! And he likes good business ideas! So make sure you have one!"
        main "I will, thanks."
        show mai smile2 at center
        mai "You're welcome, [player_name]."
        hide mai smile2
        jump intheelevator

    label mai_advice3:
        show mai curious2 at center
        show charmup at attributeup
        $charm.trait_up(1)
        mai "My shoe size?"
        with smallshake
        $footlover = True
        "(Crap! Did I blurt that out loud?)"
        show mai serious1 at center
        mai "Well, if you're going to buy me shoes, I am a size 6. I think that's the right shoe size."
        main "Uh--sorry for the question, Mai."
        show mai serious2 at center
        mai "You should go now. John doesn't like to wait."
        hide mai serious2
        jump intheelevator

    label intheelevator:
        stop music
        play sound "sfx/elevator_moving.ogg"
        scene elevator
        "(It's been 12 years since I've seen my dad. Will he even recognize me?)"
        "(He didn't even come to my graduation, despite paying all of my tuition and fees.)"
        stop sound
        scene upstairslounge with fade
        play music "music/track3.ogg"
        "(This office is really small.)"
        "{size=+10}[player_name]!!!!{/size}"
        scene 6chapter1
        "(John Shilling, CEO of Shilling Private Holdings.)"
        "(Once owner of a Fortune 500 company and a multi-millionaire.)"
        scene upstairslounge2
        show john happy1 at center
        dad "Come give your old man a hug for old time's sake!"
        main "I'm not 12 any more, dad."
        show john stern1 at center
        dad "No, you're not."
        dad "Although according to your grades, you still are."
        with smallshake
        "(So he has been checking on me!)"
        show john laugh1 at center
        dad "If you could see the look on your face right now!"
        show john laugh2 at center
        dad "Guilty as charged!"
        "(He got me.)"
        "(I did party a lot in college, but I straightened up when I got into Business School.)"
        show john stern2 at center
        dad "Playtime's over, [player_name]."
        dad "Starting today, you're going to put that degree I paid for to use."
        main "How?"
        dad "By running my business while I go on vacation, of course."
        with smallshake
        main "{size=+20}{b}WHAT?!?!{/b}{/size}"
        main "Don't-don't-don't you think I should spend a few months interning before you hand over the business to me?"
        show john stern5 at center
        dad "Did I have an 'internship' when I started my own business?"
        dad "No."
        main "But-but-but Dad-"
        show john stern9 at center
        dad "Don't be a pussy! Do you still want your inheritance or not?"
        main "I-I-"
        jump kimarrives

    label kimarrives:
        unwoman "John? What's going on?"
        "(Wait a second, I recognize that voice.)"
        hide john stern9
        scene kimintro
        "(Kimberly, the woman I caught my dad having an affair with.)"
        "(She was reason why my parents divorced.)"
        scene 20chapter1
        kim "Who is this?"
        dad "So good of you to join us."
        dad "[player_name], this is my -well now your-executive assistant, Kim."
        dad "Kim, this is [player_name], he will be in charge now. Take good care of him."
        scene 21chapter1
        kim " {size=+20}{b}{cps=*0.75}'IN CHARGE???'{/cps}{/b}{/size} "
        scene 22chapter1
        dad "If you could go downstairs for a moment, [player_name]."
        dad "Personal business."
        kim " {size=+20}{b}{cps=*1.5}DON'T IGNORE ME LIKE THAT!{/cps}{/b}{/size}"
        jump backdownstairs

    label backdownstairs:
        scene elevator with fade
        stop music
        play sound "sfx/elevator_moving.ogg"
        "(She doesn't remember me. I'm not sure if that's a good or bad thing.)"
        stop sound
        play music "music/track3.ogg"
        scene 8chapter1
        "So the boss has a kid. I never knew him to be the family type."
        "Yes, he's very cute."
        if footlover == True:
            "He is a bit weird, though."
            "Weird?"
            "Yeah. I tell you later."
            jump meetlisa
        else:
            jump meetlisa


    label meetlisa:
        scene 9chapter1
        "Why hello there handsome."
        mai "Hello."
        "You must be the dashing gentleman Mai has been gushing over."
        mai "I just said he was very cute."
        scene 10chapter1
        "Name's Alyssa Rogers, but you can call me Lisa."
        "[player_name], I guess you figured out who I am."
        "Nice to meet you."
        scene downstairsoffice
        show lisa smile1 at center
        lisa "You're pretty young.  Are you still in college?"
        main "Actually I just got my MBA in Management."
        show lisa surprise1 at center
        lisa "Oh-hoh an MBA! We have a professional now!."
        lisa "I really want to go back to school someday, but your dad- John- keeps us working all day, even on Saturdays."
        main "My dad can be a bit of a workaholic."
        main "He didn't come home a lot when I was young."
        hide lisa surprise1
        play sound "sfx/multiple_thumps.ogg"
        with smallshake
        stop sound
        main "What's that noise?!"
        show lisa serious8 at center
        lisa "Oh that? Probably our resident couple having a fight."
        lisa "Though, it's been weeks since they've had {i}that kind{/i} of fight."
        lisa "She should be down in 3....2.....1.."
        play sound "sfx/ElevatorDing.ogg"
        hide lisa serious8
        scene 11chapter1
        stop sound
        "(Well she doesn't look injured, but she isn't as composed as before)"
        scene 12chapter1
        lisa "Good morning Kim."
        kim "Piss off."
        scene downstairssofa
        show john stern7 at center
        dad "Well, everyone's here. I have an announcement to make."
        show john right1 at center
        dad "Wait, where's Bella?"
        scene 13chapter1
        bella "Hmm?"
        lisa "Earth to Bella"
        scene 14chapter1
        bella "Good morning."
        scene 15chapter1
        dad "Now. As of today, I will no longer be the CEO of this company."
        dad "I am officially retiring and leaving the company to my son, [player_name]."
        scene 16chapter1
        dad "Even though he is a bit green behind the ears, I assure you he will do a good job running this business in my stead."
        dad "Be sure to give him any and all information that he needs to ensure the success of this company."
        scene chapter1reactions
        "(They look just as surprised as I am.)"
        scene 17chapter1
        "Well, that's over. Let's go back upstairs."
        stop music
        jump backupstairs

    label backupstairs:
        play music "music/track1.ogg"
        scene upstairslounge2 with fade
        show john happy2 at center
        dad "So, what do you think of my employees?"
        "(Wait a second.)"
        main "They're all women!"
        show john happy4 at center
        dad "Isn't it great?"
        dad "Having a bunch of young, beautiful women around gets your testosterone flowing!"

        jump mcsfirstresponse

    label mcsfirstresponse:
        menu:
            dad "And makes a man more productive!"
            "If you say so, dad.":
                jump begrudinglysaysso

            "Dad, that's a bit sexist.":
                jump argueswithdad

            "Say nothing.":
                jump mcsilentlyagrees



        label begrudinglysaysso:
            show john happy5 at center
            dad "Heh, I guess you're not such a wuss after all."
            dad "Well, come on, let me give you a quick tour of the office."
            jump tourtheoffice

        label argueswithdad:
            show john stern6 at center
            show authorityup at attributeup
            $authority.trait_up(1)
            dad "I can tell that your mother raised you."
            dad "I don't intend on coddling you to make up for the years I wasn't there to raise you."
            dad "Come on, let me give you a quick tour of the office."
            jump tourtheoffice

        label mcsilentlyagrees:
            show john stern2 at center
            dad "Cat got your tongue?"
            dad "Well, you were always a mute."
            dad "Come on, let me give you a quick tour of the office."
            jump tourtheoffice

        label tourtheoffice:
            $timeout_label = None
            scene 23chapter1
            dad "Welcome to your new home!"
            dad "Expect to spend a lot of nights here."
            show 24chapter1
            dad "Over there are all the files and documents."
            dad "Investor Reports, Income Statements, Payroll, Bank Statements."
            dad "Physical copies in case the computer isn't working."
            scene 25chapter1
            dad "Your own personal bathroom. I imagine you will spend a lot of time in there."
            dad "My best ideas came from the toilet!"
            main "Too much information."
            scene 18chapter1
            dad "And here is where you'll be making all of the big decisions."
            dad "Big decisions?"
            dad "Never make a big decision down there. Always up here."
            scene 26chapter1
            dad "Well, that's everything."
            dad "If you have any questions, just call one of the girls to come upstairs."
            dad "They're a smart, hardworking lot."
            main "Uhm..so..."
            scene upstairslounge2
            show john stern5 at center
            dad "Spit it out?"
            main "What am I supposed to do, exactly?"
            show john stern4 at center
            dad "Put that business degree of yours to use and run my business."
            dad "Well, now it's {i} your{/i} business."
            with smallshake
            "({b} MY BUSINESS??{/b})"
            show john stern8 at center
            dad "There's an auditor coming some time next week."
            dad "You just need to convince him that everything is correct."
            dad "That you are re-organizing the business."
            main "So..about my trust fund."
            dad "That?"
            with smallshake
            show john laugh2 at center
            dad "Ha! There was never a trust fund!"
            dad "Paying your tuition was your trust fund!"
            show john happy5 at center
            dad "This business is your trust fund!"
            dad "Trust funds are for lazy snot-nosed brats who will never contribute anything to society!"
            show john stern4 at center
            dad "You're not one of them!"
            dad "You're a Shilling!"
            show john happy7 at center
            dad "Hey, don't look so glum."
            dad "I left you with a good amount of cash."
            dad "Just don't spend it all at once."
            dad "Invest. Inflate. Divest."
            show john right2 at center
            dad "Now I have to catch my flight."
            main "Where are you going?"
            dad "A place where you can't call me and ask a thousand questions."
            dad "You have to fly with your own wings, son."
            show john stern4 at center
            dad "I'm counting on you!"
            main "Thanks..dad."
            hide john stern4
            "(And he's gone.)"
            "(An auditor...that couldn't be good.)"
            "(I should check the files on his computer)"
            "(It's coming from that laptop.)"

            play sound "sfx/click3.ogg"
            scene 19chapter1
            "Shilling Private Holdings Security System."
            "(Dad is a bit paranoid when it comes to his employees.)"
            stop sound
            "(Probably just a standard security system.)"
            stop music
            show screen monitor
            play music "music/track3.ogg"
            scene lisafootsie
            lisa "So, what do you think of our new boss?"
            scene maifootsie
            mai "He's tall, dark, handsome...and young.."
            scene lisafootsie
            lisa "He also looks single, too."
            if footlover == True:
                scene maifootsie
                mai "But he asked me a strange question."
                lisa "What did he ask you? Your phone number?"
                mai "No, he asked for my shoe size!"
                scene lisafootsie
                lisa "Weird..you don't think he's one of those {i} foot-loving freaks{/i}?"
                scene maifootsie
                mai "Foot-loving freaks?"
                scene lisafootsie
                lisa "He doesn't look like one though. They are usually old and disgusting."
                lisa "But if he is..I don't mind."
                scene maifootsie
                mai "Are you jealous he didn't ask for {i} your {/i} shoe size, Lisa?"
                lisa "A little.."
            else:
                scene maifootsie
                mai "But he seemed really shy and scared of his own father."
                mai "He didn't know how to talk to him."
                scene lisafootsie
                lisa "He isn't alone. Even I don't know how to talk to John sometimes."
                lisa "He's so intimidating."
                lisa "I can handle this guy, though."
                scene maifootsie
                mai "You like younger guys, Lisa?"
                scene lisafootsie
                lisa "Well, they're more manageable."
            scene bellafootsie
            bella "I'm worried about the auditor next week."
            bella "I don't think [player_name]...is it? I don't think he's ever interacted with an auditor before."
            bella "And I'll be busy with my competition."
            scene lisafootsie
            lisa "You have a competition? Can you bring back a robot, pretty please, Bella?"
            scene bellafootsie
            bella "Sure."
            hide screen monitor
            scene upstairschair
            "(I don't think I left a good impression on them.)"
            "(I should check what's on the computer.)"
            scene computer
            "(Everything is labelled perfectly. What's this folder?)"
            "( A password? Hmmm..)"
            label try_password:
                $password_input = renpy.input(" Enter Password Below: ")
                if password_input == player_name:
                    "(Well, that was easy.)"
                    "(Why did dad copy all of the folders in here?)"
                    "(What's this?)"
                    "{i}Under NO circumstance can the auditor or anyone outside of the office see this. {/i}"
                    "{i}Here is the real business data. {/i}"
                    "(Real business data?!?)"
                    "(I need to compare it.)"
                    scene computerwithrecords
                    with smallshake
                    "(The public folder shows we've been running at a loss.)"
                    "(But the private one shows...)"
                    "(We've been growing and had record profits!)"
                    "(Did my dad just set me up?!?!)"
                    stop music
                    scene black with fade
                    jump chapter1end
                else:
                    #beep
                    "(Wrong one.)"
                    "(It can't be this difficult.)"
                    "(I should try something simple, like {b}my name{/b}.)"
                    jump try_password

            label chapter1end:
                play sound "sfx/misc_sound.ogg"
                show chapter1titleend with easeinright:
                    yalign 0.4
                    alpha 0.5
                    linear 2.0 alpha 1.0
                    pause 4.0
                    linear 3.0 alpha 0.0
                jump chapter2
