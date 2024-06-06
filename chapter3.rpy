label chapter3:
    if footlover == True:
        jump maifoottease
    else:
        scene black
        "(What's that noise?)"
        "(Something feels warm and heavy on my chest.)"
        "(Ugh!!)"
        hide screen eyeopening
        jump mcwakesup


    label maifoottease:
        show screen eyeopening
        scene maitoewigglesimp
        "(Mai?)"
        scene maitoewiggle
        "Hello, sleepy head."
        "(Mai..you're kind of heavy..)"
        "(Mai...what are you doing?)"
        hide screen eyeopening
        jump mcwakesup

    label mcwakesup:
        play music "music/track3.ogg"
        show screen eyeopening
        scene 1chapter3
        mai "Good Morning, [player_name]."
        "AHHHHH!!!!!!!!"
        hide screen eyeopening
        scene 2chapter3
        show chapter3title with easeinright:
            yalign 0.3
            alpha 0.8
            linear 2.0 alpha 1.0
            pause 4.0
            linear 3.0 alpha 0.0
        main "What time is it?"
        mai "It is 08: 15 in the morning, [player_name]."
        scene 3chapter3
        mai "Did you spend the night here?"
        main "Apparently I did."
        scene 4chapter3
        mai "My apologies but,"
        main "If it's about earlier-"
        scene 5chapter3
        mai "You stink, [player_name]."
        with smallshake
        "(There is a wet feeling down there.)"
        main "Is it that bad?"
        scene 4chapter3
        mai "Mmmmhmmm."
        main "I can't let anyone see or smell me like this."
        main "Thanks for waking me up, Mai."
        main "I'll go home and change."
        mai "You're welcome, [player_name]."
        jump mcgoeshome

    label mcgoeshome:
        stop music
        scene mcsapartment
        "(Home sweet home.)"
        "(I only have a few days before the auditor arrives.)"
        "(So I should interview every girl today, to get to the bottom of this.)"
        jump mcreturns

    label mcreturns:
        play music "music/track3.ogg"
        scene frontdesk
        show lisa smile2 at center
        lisa "Oh, hey [player_name], you're finally back."
        main "Good morning, Lisa."
        unwoman "So, the man of the hour has finally arrived."
        hide lisa smile2
        scene 7chapter3
        main "Lisa, who is this?"
        lisa "Uh, did your dad mention an auditor coming to the firm?"
        main "He did."
        scene 6chapter3
        lisa "{size=-10}That's her.{/size}"
        scene 8chapter3
        "Christina McNeill. A pleasure to meet you. "
        crissy "What you are looking at?"
        scene 9chapter3
        crissy "Let's go I have a lot to cover."
        crissy "I can't believe the owner of the company comes in this late."
        crissy "I don't have all day."
        scene 10chapter3
        "(Everyone's here, except for Kim.)"
        if cKim.morale >= 1:
            "(Even if things went well last night, I doubt she would show up to this meeting.)"
        else:
            "(Considering what happened last night, I don't expect her to be here.)"

        scene 11chapter3
        bella "Hey [player_name]."
        main "Hello, Bella."
        bella "Can I talk to you privately after this meeting?"
        bella "It's important."
        main "Sure, Bella."
        jump crissypresentation

    label crissypresentation:
        scene 24chapter3
        crissy "So, now that everyone is here, I would like to introduce myself."
        crissy "My name is Christina McNeill, and I'll be auditing your company for the next week."
        crissy "Our job is to-"
        scene 27chapter3
        lisa "We know what an auditor's job is."
        lisa "I'm not even sure why we are having this meeting."

        menu:
            lisa "Is this your first time doing this?"
            "She's not the only new person here." :
                scene meetingoffice
                $ charm.trait_up(1)
                show charmup at attributeup
                show crissy serious6 at center
                crissy "Oh, that's right, you're not John Shilling."
                crissy "I can't believe a kid straight out of school is now the CEO."
                hide crissy serious6
                show lisa angry1 at center
                lisa "Maybe you should come back later."
                lisa "Like, next week, when you're {i} supposed {/i} to."
                hide lisa angry1
                show crissy serious5 at center
                crissy "Hmm, do you need more time to hide things from me?"

                menu:
                    crissy "You're acting suspicious."
                    "Stop it!" :
                        $ authority.trait_up(2)
                        show authorityup at attributeup
                        main "Ms. McNeill, please continue."
                        hide crissy serious5
                        scene 25chapter3
                        crissy "Thank you."
                        crissy "So for the next week, I'll be asking everyone questions and reviewing all of the documents."
                        scene 28chapter3
                        menu:
                            crissy "I hope you don't mind if I work in this room, do you, [player_name]?"
                            "That's a little close for comfort" :
                                main "I didn't know that auditors work on site."
                                main "I thought they just take the papers and go back to their office."
                                scene meetingoffice
                                show crissy serious2 at center
                                crissy "Well-um- it's just more {i}convenient{/i} for me."
                                hide crissy serious2
                                scene 35chapter3
                                lisa "Can you come back later- when [player_name] is more adjusted?"
                                menu:
                                    lisa "He can help you better once he has familiarized himself with his surroundings."
                                    "That's a good idea, Lisa." :
                                        $ charm.trait_up(1)
                                        show charmup at attributeup
                                        $ cLisa.morale_up(2)
                                        scene meetingoffice
                                        main "This meeting is adjourned."
                                        show crissy surprised2 at center
                                        crissy "Wait-what-no-I'm not done!"
                                        main "I'll be upstairs."
                                        hide crissy surprised2
                                        jump privatetalkwithcrissy

                                    "It's fine, Lisa." :
                                        main "I'm prepared for anything."
                                        scene 30chapter3
                                        lisa "Ok..."
                                        lisa "Are we done here?"
                                        main "Yes."
                                        main "The meeting is over. I'll be upstairs."
                                        jump privatetalkwithcrissy
                            "Sure, I don't mind." :
                                scene meetingoffice
                                show crissy smile3 at center
                                crissy "Really?"
                                main "Yes, but not today."
                                show crissy surprised1 at center
                                crissy "Huh?"
                                main "You can start working here next week, when you're supposed to."
                                show crissy surprised2 at center
                                crissy "But-but-but-"
                                main "This meeting is adjourned."
                                main "I'll be upstairs."
                                hide crissy surprised2
                                jump privatetalkwithcrissy
                    "You are here earlier than expected":

                        show crissy sad1 at center
                        crissy "That's because I had a cancellation-"
                        main "I have only been here for 3 days, I don't even know the layout of the office."

                        menu:
                            crissy "Oh. I-"
                            "Please come back later":
                                $ authority.trait_up(1)
                                show authorityup at attributeup
                                main "This meeting is adjourned."
                                main "I'll be in my office."
                                show crissy surprised2 at center
                                crissy "No! Wait!"
                                hide crissy surprised2
                                jump privatetalkwithcrissy
                            "So please go slow." :
                                scene 25chapter3
                                crissy "Right."
                                crissy "For the next week, I'll be asking questions and reviewing all documents."
                                crissy "Just to make sure that everything is reported properly."
                                scene 35chapter3
                                lisa "All of the important documents are in the upstairs office."
                                lisa "I don't think you need to hover over our backs while you do your audit."

                                menu:
                                    crissy "Maybe I should."
                                    "That's enough." :
                                        main "I think this meeting is over."
                                        main "I'll be in my office."
                                        lisa "Thank goodness."
                                        scene meetingoffice
                                        show crissy angry14 at center
                                        crissy "Wait, I'm not done!"
                                        hide crissy angry14
                                        jump privatetalkwithcrissy
                                    "Back on topic,please." :
                                        scene 25chapter3
                                        crissy "Well, uhm."
                                        crissy "I had a graph and chart here but-"
                                        scene 29chapter3
                                        lisa "Oh my god, is this a high school presentation?"
                                        lisa "We get it, you're here to see if we paid our taxes."
                                        lisa "I'll get the tax forms myself."
                                        main "That sounds like a great idea, Lisa."
                                        scene 34chapter3
                                        lisa "Thanks, [player_name]."
                                        main "I'll be in my office. This meeting is adjourned."
                                        scene 33chapter3
                                        crissy "No!! Wait!!"
                                        jump privatetalkwithcrissy
            "Lisa." :
                scene 29chapter3
                $ authority.trait_up(2)
                show authorityup at attributeup
                lisa "Well, this isn't high school."
                lisa "Just tell us what you need and we'll get it for you."
                scene 28chapter3
                crissy "Well I need your financial documents, including income-"
                lisa "Ok, and anything else?"

                menu:
                    crissy "I'm not through, let me finish."
                    "Be polite, Lisa." :
                        $ authority.trait_up(1)
                        show authorityup at attributeup
                        scene meetingoffice
                        lisa "Go on."
                        show crissy smile2 at center
                        crissy "First I need those documents, then I will follow up with personal interviews."
                        lisa "Personal interviews, why?"
                        crissy "It's standard procedure."
                        bella "Will the interviews uh-will they happen this week? I'm pretty busy."
                        show crissy surprised2 at center
                        crissy "Oh-"
                        hide crissy surprised2
                        scene 35chapter3
                        lisa "This is why you should come when you're scheduled to."

                        menu:
                            lisa "To avoid problems like this."
                            "I agree" :
                                main "Please come back next week, Ms. McNeill."
                                scene meetingoffice
                                show crissy sad3 at center
                                crissy "But-but-but-"
                                main "This meeting is adjourned."
                                main "I'll be upstairs in my office if you need anything."
                                crissy "Wait!!"
                                hide crissy sad3
                                jump privatetalkwithcrissy
                            "She's here now" :
                                main "I'm sure I can figure everything out."
                                main "Welcome to SPH, Ms. McNeill."
                                main "Everyone is at your convenience."
                                main "This meeting is over."
                                scene meetingoffice
                                show crissy surprised2 at center
                                crissy "Wait!!"
                                hide crissy surprised2
                                main "I'll be in my office."
                                jump privatetalkwithcrissy
                    "What else do you need?" :
                        scene meetingoffice
                        show crissy sad5 at center
                        crissy "Interviews and-and-"
                        lisa "Interviews?"
                        crissy "Just to make sure everyone is doing their job."
                        scene 35chapter3
                        lisa "That's [player_name]'s job, not yours."
                        lisa "You just need to make sure everything we report is correct."
                        crissy "I-I-"
                        menu:
                            "That's enough for now." :
                                main "You can come up to my office."
                                main "I will provide you with everything you need."
                                scene meetingoffice
                                show crissy smile1 at center
                                crissy "Really?"
                                main "Yes. This meeting is adjourned."
                                lisa "Whew."
                                hide crissy smile1
                                main "I'll be upstairs."
                                jump privatetalkwithcrissy
                            "Relax." :
                                main "I will make sure you have everything you need to conduct your work efficiently."
                                scene meetingoffice
                                show crissy smile1 at center
                                crissy "Oh? Thank you, Mr. Shilling."
                                main "But I need a few days to prepare. So please come back later, Ms. McNeill."
                                show crissy surprised2 at center
                                crissy "Huh?"
                                main "This meeting is adjourned. I'll be upstairs."
                                crissy "No! Wait!!"
                                hide crissy surprised2
                                jump privatetalkwithcrissy


label privatetalkwithcrissy:
    stop music
    play sound "sfx/elevator_moving.ogg"
    scene elevator with fade
    "(That was exhausting.)"
    "(Why did the auditor come so early?)"
    stop sound
    scene upstairslounge
    play music "music/track1.ogg"
    show crissy serious1 at center
    crissy "Mr. Shilling, please hear me out."
    show crissy sad1 at center
    crissy "It's true, it's my first time doing an audit by myself-but I really need this job to prove myself."
    show crissy sad4 at center
    crissy "I promise I won't get in the way, but please let me start today, please?"
    hide crissy sad4
    main "Listen Ms. McNeill-"
    show crissy flirt2 at center
    "(What the?!!)"
    crissy "I know you were staring at them."

    menu:
        crissy "They're pretty nice, aren't they?"
        "Put those away!" :
            show crissy sad3 at center
            show authorityup at attributeup
            $ authority.trait_up(2)
            main "This is an office setting!"
            main "You don't even look professional."
            main "You look like a girl who decided to wear her private school uniform."
            main "Do you expect me to take you seriously?"
            crissy "I-I-"
            jump crissysoffer
        "Are those even real?" :

            show crissy angry1 at center
            crissy "Of course they're real!"
            crissy "Fake tits will never look as good as real ones!"
            jump crissysoffer
        "Yes they are" :

            show charmup at attributeup
            $ charm.trait_up(2)
            show crissy flirt1 at center
            crissy "They're all natural."
            jump crissysoffer



label crissysoffer:
    show crissy flirt3 at center
    crissy "Are you going to play with them or not?"
    crissy "You can't deny how nice they look."
    crissy "I mean I can do a quick titjob if you're hard enough."
    crissy "Here, I will take them out for you."
    show crissy flirt4 at center

    menu:
        crissy "Come on, I won't tell anyone, I promise."
        "Hmm ok" :
            $ authority.trait_up(2)
            show authorityup at attributeup
            crissy "What are you waiting for?"
            main "To get that stupid look off of your face."
            scene 12chapter3
            menu:
                crissy "Are you going to take your cock out or not?"
                "I will" :
                    if persistent.sexscenes == False:
                        scene black
                        crissy "There, all better, right?"
                        scene upstairslounge with fade
                        show crissy smile3 at center
                        $ crissytitfuck = True
                        main "Please leave."
                        main "Don't come back until next week."
                        show crissy sad3 at center
                        crissy "Wha-what?"
                        main "Leave. Now."
                        hide crissy sad3
                        jump atdesk
                    else:
                        jump crissytitjob
                "Just kidding!" :
                    $ charm.trait_up(2)
                    show charmup at attributeup
                    scene 13chapter3
                    crissy "You're a dick."
                    scene upstairslounge
                    show crissy angry5 at center
                    crissy "I can't believe I'm dealing with an immature kid."
                    main "You're the one acting immature."
                    main "Please leave."
                    main "Don't come back until next week."
                    crissy "Fine, dickhead."
                    hide crissy angry5
                    jump atdesk
        "Refuse" :
            $ authority.trait_up(3)
            show authorityup at attributeup
            main "No, get dressed."
            show crissy flirt1 at center
            crissy "You not into girls? That's a shame."
            main "I'm straight, but I have my limits."
            main "And my morals, compared to you."
            show crissy sad5 at center
            main "Now, please leave."
            main "And don't come back until next week."
            hide crissy sad5
            jump atdesk

label crissytitjob:
    scene crissytitfuck
    menu:
        "View 2" :
            jump crissytitjob2
        "Finish" :

            scene crissytitjobending
            crissy "Happy?"
            scene upstairslounge
            show crissy smile3 at center
            main "Please leave."
            main "Don't come back until next week."
            show crissy sad3 at center
            crissy "Wha-what?"
            main "Leave. Now."
            hide crissy sad3
            jump atdesk

label crissytitjob2:
    scene crissytitfuckv2
    menu:
        "View 1" :
            jump crissytitjob
        "Finish" :

            scene crissytitjobending
            crissy "Happy?"
            scene upstairslounge
            show crissy smile3 at center
            main "Please leave."
            main "Don't come back until next week."
            show crissy sad3 at center
            crissy "Wha-what?"
            main "Leave. Now."
            hide crissy sad3
            jump atdesk


label atdesk:
    scene upstairshall with fade
    if crissytitfuck == True:
        "(Now that I'm all cleaned up, I should try talking to the girls.)"
        jump talktogirls
    else:
        "(Now that I have settled that problem, I should try talking to the other girls.)"
        jump talktogirls

    label talktogirls:
        scene upstairshall
        play music "music/track3.ogg"

        menu:
            "(Who should I talk to?)"
            "Mai" if maitalk == False:
                "(Mai is the accountant and responsible for the financial reports.)"
                "(She would know about my dad's schemes due to preparing the balance sheets.)"
                main "Mai?"
                mai "Hello, [player_name], is there something you need?"
                main "Could you come upstairs for a minute? I would like to talk to you."
                mai "Sure, [player_name]."
                jump interrogatemai
            "Kim" if kimtalk == False:
                "(Kim did brag about helping John create the company.)"
                if cKim.morale == 0:
                    menu:
                        "(But after our argument last night, I'm not sure if I want to talk to her.)"
                        "Call her anyway" :
                            jump interrogatekim
                        "Forget about it" :
                            jump talktogirls
                else:
                    "(I'm sure she wouldn't mind answering my questions.)"
                    jump interrogatekim

            "Lisa" if lisatalk == False:
                "(I doubt Lisa knows anything, but it doesn't hurt to ask her.)"
                "(She was really vocal earlier.)"
                jump interrogatelisa

            "Bella" if bellatalk == False:
                "(Bella wanted to talk to me after the meeting.)"
                "(I hope I didn't keep her waiting long.)"
                "(This is the first time she would have spoken to me privately.)"
                jump interrogatebella

            "That's all for now" if bellatalk == True:
                "(I think I've gotten what I needed from those personal talks.)"
                if maitalk == False:
                    menu:
                        "(But maybe I should talk to Mai. She might know something.)"
                        "Call her" :
                            main "Mai?"
                            mai "Hello, [player_name], is there something you need?"
                            main "Could you come upstairs for a minute? I would like to talk to you."
                            mai "Sure, [player_name]."
                            jump interrogatemai
                        "No, I rather not" :
                            jump kimcheck
                else:
                    "(Mai didn't give me much information, but it was enough.)"
                    jump kimcheck


        label kimcheck:
            if kimtalk == False:
                menu:
                    "(I know I should talk to Kim, but who knows what she will tell me.)"
                    "Call her" :
                        jump interrogatekim
                    "Leave her alone" :
                        jump ch3ending
            else:
                "(Kim admitted to knowing what my dad was doing.)"
                "(She even believed she was helping him.)"
                "(That explains why she was upset when he left without her.)"
                jump ch3ending


label interrogatemai:
    scene upstairshall
    show mai smile2 at center
    mai "Hi."
    main "Come sit down."
    show mai sad1 at center
    label askmai2:
        mai "Is something wrong?"
        menu:
            "Ask about the revenue" if mairevenue == False:
                main "Have you been manipulating the financial reports?"
                show mai sad3 at center
                mai "Uhmm...."
                $ mairevenue = True
                main "Mai?"
                show mai sad5 at center
                mai "Am I in trouble?"
                main "Mai, this is pretty serious."
                main "We could go to jail for this."
                main "I need to know the truth."
                show mai sad9 at center
                mai "Please don't turn me in, [player_name]."
                mai "I only did what John told me to do."
                main "And what did John tell you?"
                show mai sad11 at center
                mai "To create two reports every three months- one for him and one for the investors."
                mai "I added extra income from the information Bella gave me."
                "(Bella is connected to this?)"
                show mai sad8 at center
                mai "I was just doing my job, please don't fire me, [player_name]."
                menu:
                    mai "Is there anything else you want to ask me?"
                    "No, that's all" :
                        hide mai sad8
                        jump finishaskmai2
                    "I have more to ask" :
                        hide mai sad8
                        jump askmai2

            "Ask about her income" if maiincome == False:
                show mai flirt1 at center
                mai "My income?"
                mai "Uhm..."
                $ maiincome = True
                main "What is it?"
                show mai serious4 at center
                mai "I..I don't know."
                with smallshake
                main "What?!?!"
                main "But on the-"
                show mai sad1 at center
                mai "John gives my income to my landlady and she gives me an allowance."
                main "Woah is that even legal?"
                show mai sad4 at center
                mai "He says he can't pay me directly because of laws, but he-he-he promised to help me get full citizenship."
                mai "I just have a visa now but-"
                main "No, no, that's fine."
                main "I'm sorry for asking."
                menu:
                    mai "Is there anything else?"
                    "No, that's all" :
                        hide mai sad4
                        jump finishaskmai2
                    "I have more to ask" :
                        hide mai sad4
                        jump askmai2


            "Ask about the taxes" if maitaxes == False:
                main "Mai, is there a reason why the taxes are low?"
                show mai serious2 at center
                mai "Hmmm?"
                main "I think we should be paying more taxes based on our revenue."
                show mai sad4 at center
                $ maitaxes = True
                mai "I-I don't know anything about paying taxes, [player_name]."
                mai "I just pay the amount John tells me to."
                main "Oh I thought an accountant like you would be uhm, an expert on the tax code."
                show mai smile6 at center
                mai "Haha! Maybe if I went to school and got a license."
                main "You're not certified ?!?!?"
                show mai sad8 at center
                mai "No. I just learned how to do this from my old job."
                mai "John decided to hire me based on that."
                main "What was your old job."
                show mai serious2 at center
                mai "I worked at a hotel."
                main "Oh."
                main "That's still impressive."
                menu:
                    mai "Is there anything else?"
                    "No, that's all" :
                        hide mai serious2
                        jump finishaskmai2
                    "I have more to ask" :
                        hide mai serious2
                        jump askmai2


label finishaskmai2:
    scene 14chapter3
    play music "music/track8.ogg"
    menu:
        "(She's crying.)"
        "Console her" :
            jump consolemai
        " Be firm" :
            jump befirmwithmai

    label befirmwithmai:
        $ authority.trait_up(1)
        show authorityup at attributeup
        main "You're not in trouble, Mai."
        scene 15chapter3
        mai "I'm not?"
        $ maitalk = True
        main "No, you simply followed orders."
        main "I'm in charge now. So things are different."
        main "And there is an auditor that came before she was supposed to."
        scene upstairshall
        show mai serious2 at center
        mai "Oh."
        mai "May I go back to my office?"
        main "Yes, you may."
        show mai smile3 at center
        mai "Oh..thank you, [player_name]."
        mai "I'll be leaving now."
        hide mai smile3
        stop music
        jump talktogirls

    label consolemai:
        scene 15chapter3
        $ charm.trait_up(1)
        show charmup at attributeup
        main "I understand, Mai."
        mai "Do you?"
        main "You just did what you needed to do to keep the job."
        scene 16chapter3
        main "Come here, Mai."
        main "Everything will be fine, Mai."
        scene 17chapter3
        "(......)"
        scene upstairshall
        show mai surprise at center
        mai "!!!!"
        mai "I'm sorry, I can't-"
        main "Can't what?"
        show mai flirt2 at center
        mai "You're my boss, I'm sorry, [player_name]."
        main "How do you explain what happened this morning?"
        if footlover == True:
            hide mai flirt2
            scene maitoewigglesimp
            main "You were sitting on top of me with your feet in my face."
            main "I don't think you're the type of girl who does that with anyone, are you?"
            scene upstairshall
            show mai flirt2 at center
            mai "Uhmm..."
            mai "You were sleeping so peacefully, I just did it."
            show mai flirt3 at center
            menu:
                mai "I won't do it again, I promise."
                " I kind of liked it" :
                    $ charm.trait_up(2)
                    show charmup at attributeup
                    main "I really liked it, Mai."
                    main "But not when I'm half-asleep."
                    show mai flirt6 at center
                    $ maitalk = True
                    mai "You really liked it?"
                    main "Yes, I do. But please keep it secret."
                    show mai smile5 at center
                    mai "I will."
                    hide mai smile5
                    scene 18chapter3
                    show moraleup at attributeup
                    $ cMai.morale_up(3)
                    mai "Thank you, [player_name]."
                    scene upstairshall
                    main "You're welcome, Mai"
                    "(Well, I'm glad I talked to her.)"
                    stop music
                    jump talktogirls
                "Please don't." :

                    main "I'm not what you call a feet person."
                    show mai flirt4 at center
                    mai "Oh?"
                    mai "Then why did you ask for my shoe size when we first met?"
                    show mai smile4 at center
                    "(Damn it, she got me.)"
                    main "It was..I was distracted by your beauty, I'm sorry."
                    show mai flirt5 at center
                    mai "Mmhmmm..."
                    mai "I think you liked it."
                    $ maitalk = True
                    main "Ok, ok, you are right. I did like it."
                    main "But not when I'm half-asleep."
                    show mai smile2 at center
                    show moraleup at attributeup
                    $ cMai.morale_up(1)
                    mai "You're so cute."
                    main "Thanks for talking to me, Mai."
                    scene 18chapter3
                    "(!!!!!!!)"
                    scene upstairshall
                    show mai smile7 at center
                    mai "Thank you, [player_name]."
                    hide mai smile7
                    "(You're welcome, Mai.)"
                    stop music
                    jump talktogirls
        else:

            main "I don't know what you did to me this morning."
            main "But I get the feeling it isn't something you do with anyone."
            show mai flirt2 at center
            mai "Uhm...."
            mai "I won't do it again, I promise."
            main "But what did you do, Mai?"
            show mai flirt6 at center
            mai "I was just teasing you with my feet, [player_name]."

            menu:
                mai "I thought you liked it."
                "I would if I was coherent." :
                    $ charm.trait_up(1)
                    show charmup at attributeup
                    $ footlover = True
                    mai "You like that kind of thing?"
                    main "Promise you won't tell anyone, but I do like feet."
                    show mai flirt5 at center
                    $ maitalk = True
                    $ cMai.morale_up(1)
                    show moraleup at attributeup
                    mai "Ok, I will do it when you are wide awake!"
                    main "Not here, though."
                    mai "Oh."
                    main "Thank you for coming by, Mai."
                    scene 18chapter3
                    mai "You're welcome, [player_name]."
                    stop music
                    jump talktogirls
                "Not really." :

                    show mai flirt1 at center
                    mai "Ok, how about a massage?"
                    main "A massage?"
                    mai "Yes, I'm very good at those."
                    main "I...I will consider it."
                    main "But not when I'm half-asleep, ok?"
                    main "That really creeped me out."
                    show mai flirt3 at center
                    mai "Before you sleep?"
                    $ maitalk = True
                    $ cMai.morale_up(1)
                    show moraleup at attributeup
                    main "Not at the office either."
                    main "Thanks, Mai."
                    show mai smile5 at center
                    mai "You're welcome, [player_name]."
                    hide mai smile5
                    stop music
                    jump talktogirls

label interrogatelisa:
    scene upstairshall
    show lisa smile1 at center
    lisa "Hey, [player_name], what's up?"
    main "Sit down, I have a few questions to ask."
    show lisa sad1 at center
    menu:
        lisa "If it's about earlier, I'm sorry."
        "No need to apologize." :
            show lisa smile1 at center
            $ charm.trait_up(1)
            show charmup at attributeup
            lisa "See I knew we would see eye-to-eye."
            $ cLisa.morale_up(1)
            show moraleup at attributeup
            jump interrogatelisacontinued
        " That was my job." :
            show lisa surprise3 at center
            show authorityup at attributeup
            $ authority.trait_up(1)
            lisa "Oh. I ...I won't do it again."
            jump interrogatelisacontinued


    label interrogatelisacontinued:
        show lisa surprise6 at center
        menu:
            lisa "So what did you want to ask me?"
            "Ask about revenue" if lisarevenue == False:
                main "Do you know about our extra sources of income?"
                show lisa surprise1 at center
                lisa "Extra sources?"
                main "Yes. There are two different income statements."
                main "Here."
                show lisa serious14 at center
                $ lisarevenue = True
                lisa "Woah...that's how much money we {i} really{/i} make?"
                lisa "I only get this one."
                show lisa serious7 at center
                lisa "Hahha. I knew this job was too good to be true."
                main "So you were in the dark."
                show lisa serious11 at center
                lisa "Of course. And I'm the one that talks to everyone outside of the company."
                lisa "No wonder John hired me."
                main "Why did he hire you?"
                show lisa serious14 at center
                lisa "I have a good track record of lying to people."
                main "How would John know that?!!? Isn't that a bad trait?"
                show lisa smile1 at center
                lisa "A little white lie is sometimes necessary in getting people to part with their money."
                lisa "And...John knew I was capable of doing that."
                show lisa smile4 at center
                lisa "But that's for another time."
                lisa "Is there anything else you wanted to ask me?"
                menu:
                    "That's everything" :
                        jump finishinterrogatelisa
                    "I have more to ask" :
                        jump interrogatelisacontinued

            "Ask about taxes" if lisataxes == False:
                show lisa serious10 at center
                lisa "Taxes?"
                lisa "That's the main reason why the auditor is here, right?"
                show lisa serious11 at center
                lisa "Have we been paying taxes? Are we late?"
                lisa " I thought Mai took care of that."
                $ lisataxes = True
                main "We've been paying the same amount in taxes every year."
                main "But our profits keep going up."
                show lisa serious6 at center
                lisa "Hmm...maybe John pulled a few strings."
                lisa "That's my theory."
                lisa "Is there anything else you want to ask me?"
                menu:
                    "That's everything" :
                        jump finishinterrogatelisa
                    "I have more to ask" :

                        jump interrogatelisacontinued

            "Ask about her income" if lisaincome == False:
                main "How much do you make?"
                show lisa surprise2 at center
                lisa "Woah-what?"
                lisa "Isn't that something {i}you{/i} are supposed to know?"
                main "I don't want to go through mountains of payroll when I can hear it directly."
                main "Besides, I need to know if you are all being paid the same."
                show lisa serious11 at center
                lisa "My salary is 75 thousand, before taxes."
                $ lisaincome = True
                lisa "At least that's what John told me. He said everyone gets paid equally."
                "(Hmm, on the investor income statement, what she says is true.)"
                "(But on the real one- that's false.)"
                show lisa serious6 at center
                lisa "It's not as much as I used to make, but for an entry-level job it's pretty good."
                main "This is your first job?"
                show lisa serious11 at center
                lisa "Yeah. My first {i}real{/i} job."

                menu:
                    lisa "Before that I was waiting tables and uh..haha."
                    "I don't need to know the details" :
                        main "Thanks, Lisa."
                        jump finishinterrogatelisa
                    "I'm curious" :
                        play music "music/track8.ogg"
                        show lisa sad4 at center
                        lisa "I wanted to be a fashion model. "
                        lisa "I graduated from high school early and moved to New York City for a while."
                        lisa "I lived in a cramped apartment while trying to book modeling gigs."
                        show lisa sad7 at center
                        lisa "Nothing happened for months and I needed to pay rent so I.."
                        lisa "I started doing web camming. In between go-sees."
                        main "Go-sees?"
                        show lisa serious9 at center
                        lisa "It's like an interview for a modelling job. They scrutinize you from head to toe."
                        lisa "They make you do poses like uh-"
                        main "I understand."
                        show lisa sad3 at center
                        lisa "Anyway, I was getting a lot of money from my webcam shows."
                        lisa "So much that I stopped looking for modelling jobs. I moved away from New York."
                        lisa "Then I got into a relationship with one of the website administrators."
                        lisa "He put me on the front page of the website."
                        show lisa sad7 at center
                        lisa "But he was so jealous and insecure, he wanted me to stop."
                        lisa "So I did."
                        lisa "I doubt you want to know hear the rest."
                        main "No, go on."
                        show lisa serious7 at center
                        lisa "The bastard got fired when his partners realized he was picking favorites."
                        lisa "And he wouldn't get another job. So he was just sitting around all day, playing video games."
                        lisa "I had to work odd-end jobs and that's how I ended up here."
                        main "Are you still with him now?"
                        show lisa angry1 at center
                        lisa "Heck no."
                        lisa "I kicked him out of my apartment."
                        show lisa angry3 at center

                        menu:
                            lisa "Though I wish I could go back."
                            "To fashion modelling?" :
                                show lisa angry2 at center
                                lisa "I'm way too old for that."
                                $ charm.trait_down(1)
                                show charmdown at attributedown
                                lisa "22 is considered ancient. Unless you're a plus sized model."
                                lisa "And I'm not a cow."
                                jump lisawantstoloseweight
                            "To webcamming?" :
                                $ charm.trait_up(2)
                                show charmup at attributeup
                                lisa "Yeah, but it's so competitive these days."
                                show lisa smile3 at center
                                lisa "I'm older now, not exactly a MILF, so I doubt there's room for me."
                                lisa "Besides I've gained weight from when I quit."
                                jump lisawantstoloseweight

    label lisawantstoloseweight:
        show lisa sad8 at center
        lisa "I'm so fat."
        menu:
            lisa "I need to lose weight badly."
            "You're not that fat" :
                show lisa angry1 at center
                lisa "Says you."
                lisa "I used to be so thin."
                $ charm.trait_down(1)
                show charmdown at attributedown
                main "Well-"
                $ lisatalk = True
                show lisa sad5 at center
                lisa "Those days are long gone."
                lisa "Anyway, I'll see you around, [player_name]."
                lisa "Good luck with the auditor."
                hide lisa sad5
                main "Thanks, Lisa."
                stop music
                jump talktogirls
            "I've gained a bit of weight myself." :
                show lisa sad9 at center
                lisa "Really?"
                $ charm.trait_up(3)
                show charmup at attributeup
                main "Yeah. I've gotten a bit of a beer belly."
                show lisa flirt2 at center
                lisa "Those clothes hide it well."
                main "I have an idea."
                main "Why don't we go to the gym together?"
                hide lisa flirt2
                scene 19chapter3
                lisa "....."
                $ lisaworkoutinvite = True
                $ lisatalk = True
                lisa "That's a great idea!"
                main "It can be after work. There's a gym in my apartment building."
                main "I have a lot on my plate, but working out always helps me focus and concentrate."
                scene upstairshall
                show lisa smile6 at center
                $ cLisa.morale_up(3)
                show moraleup at attributeup
                lisa "It's a deal!"
                lisa "Bye, [player_name], just call me when you want to go to the gym."
                main "Bye, Lisa."
                hide lisa smile6
                stop music
                jump talktogirls

    label finishinterrogatelisa:
        main "Thanks for coming in, Lisa."
        show lisa smile2 at center
        lisa "You're welcome, [player_name]."
        lisa "If there anything else you need-"
        main "I will call you."
        lisa "See you later, [player_name]."
        hide lisa smile2
        jump talktogirls


label interrogatekim:
    scene upstairshall
    show kim smile1 at center
    kim "So, why did you call me?"
    kim "Do you need some stress relief?"
    main "No, Kim."
    main "I have a few questions to ask you."
    show kim serious6 at center
    kim "No need to be so formal."

    label askkim2:
        kim "I can answer them right here."
        menu:
            "Ask her about the revenue" if kimrevenue == False:
                main "Do you know all of our sources of income?"
                show kim serious2 at center
                kim "Hmm?"
                kim "No. All I remember when John started the company is that he had a {i}billion dollar{/i} idea."
                $ kimrevenue = True
                kim "But I don't think we even made 10 million dollars."
                kim "I've never seen it, and John is quite a lavish spender."
                show kim serious6 at center
                kim "Is something wrong?"
                main "No, no."
                menu:
                    kim "Anything else?"
                    "That's it" :
                        jump finishaskkim2
                    "No, there's more" :
                        jump askkim2

            "Ask about her income" if kimincome == False:
                kim "That's an odd question."
                kim "Oh, that's right, you are new."
                show kim serious3 at center
                kim "I don't get a paycheck from the company."
                main "You don't?"
                show kim serious4 at center
                kim "No, John would give me a bonus pay once a year."
                kim "He would write it off as an expense."
                $ kimincome = True
                "(Wow. This...is worse than I expected)."
                main "Thanks, Kim."

                menu:
                    kim "Anything else?"
                    "That's it" :
                        jump finishaskkim2
                    "No, there's more" :
                        jump askkim2

            "Ask about taxes" if kimtaxes == False:
                kim "Taxes?"
                show kim smile7 at center
                kim "I remember years ago John, his lawyer, and his private accountant made a deal with a tax agent."
                $ kimtaxes = True
                kim "He probably bribed the tax agent."
                kim "So that's why the taxes remain the same no matter how much money we make each year."
                menu:
                    kim "Anything else?"
                    "That's it" :
                        jump finishaskkim2
                    "No, there's more" :
                        jump askkim2


    label finishaskkim2:
        show kim smile2 at center
        "Kim..?"
        kim "{size=+10}HAHAHAHA - HAHAHAHAHAHA!!!!!!{/size}"
        kim "{size=+10}HAHAHAHAHHAHAHAHAHAHAHHA!!!!!!!!!!!!!!!!!{/size}"
        hide kim smile2
        scene 20chapter3
        kim "{size=-10}He left me.{/size}"
        kim "{size=+10}{i}He fucking LEFT ME!!{/i}{/size}"
        scene 21chapter3
        play music "music/track8.ogg"
        kim "I'm just a used up whore."
        menu:
            kim "What am I going to do now?"
            "Advise her" :
                scene upstairslounge
                main "You could start over. Quit. Find a new passion or hobby."
                show kim sad5 at center
                kim "That's so funny."
                main "How is that funny? It's true."
                show kim serious2 at center
                kim "I don't have any fucking skills...except for using my body."
                kim "Even that has diminishing returns."
                main "With that you can go back to school, learn a new trade-"
                show kim serious6 at center
                kim "Do you {i}think{/i} I want to learn a new trade?"
                kim "I earn money doing nothing. Why would I go through more effort?"
                main "It's a-"
                stop music
                play music "music/track9.ogg"
                show kim smile6 at center
                kim "Why don't you join me?"
                kim "Couples get more money."
                kim "We can even do the webcam show here, after hours."

                menu:
                    kim "What do you say?"
                    "Accept" :
                        hide kim smile6
                        scene 22chapter3
                        kim "Well, you know where to find me."
                        $ kimcaminvite = True
                        $ kimtalk = True
                        kim "I'll be waiting."
                        stop music
                        jump talktogirls
                    "Decline" :

                        show kim sad9 at center
                        kim "Aww, that's so sad."
                        $ kimtalk = True
                        kim "We would have made a great couple."
                        kim "Well,if that's that, I'm leaving."
                        kim "Good bye, [player_name]."
                        hide kim sad9
                        stop music
                        jump talktogirls
            "Console her" :
                scene upstairslounge
                main "Kim I-"
                show kim sad3 at center
                kim "Don't touch me."
                kim "I'll -I'll be fine."
                main "If there's anything I could do-"
                show kim sad7 at center
                stop music
                play music "music/track9.ogg"
                kim "I could use some male attention."
                kim "The real kind."
                kim "In front of the camera, to make everyone jealous."
                main "You want me to participate in your little show?"
                show kim smile7 at center

                menu:
                    kim "Why not? It'll be fun."
                    "Sure" :
                        main "If it will help."
                        show kim smile4 at center
                        $ cKim.morale_up(2)
                        show moraleup at attributeup
                        $ kimcaminvite = True
                        $ kimtalk = True
                        kim "Oh, it certainly will."
                        kim "I wish we could do it now, but let's wait until we're alone."
                        hide kim smile4
                        scene 22chapter3
                        kim "You know where to find me."
                        kim "I'll be waiting."
                        stop music
                        jump talktogirls
                    "Sorry, I can't" :
                        show kim sad9 at center
                        kim "I thought you said you would do anything."
                        main "{i}Could{/i}, not would. There's a difference."
                        show kim sad10 at center
                        kim "I guess there is."
                        $ kimtalk = True
                        kim "You're not obligated to do anything."
                        kim "I'll figure all this bullshit out on my own."
                        kim "I'll be going, bye, [player_name]."
                        hide kim sad10
                        stop music
                        jump talktogirls
            "Scold her" :
                scene upstairslounge
                main "That is what you get for breaking our family apart."
                show kim smile2 at center
                kim "Hah. Maybe you shouldn't have told your mother a young woman was fucking your dad."
                show kim serious8 at center
                kim "Do you know she cleaned him out of his money? Most of his wealth went to her in the divorce."
                show kim angry7 at center
                kim "He was forced to start over. All because of {i}you{/i}."
                main "And now it's your turn."
                $ kimtalk = True
                main "Take some accountability for yourself."
                main "Start over."
                show kim serious5 at center
                kim "You're not John."
                kim "Are we done here?"
                main "Yeah, we're done."
                kim "Goodbye."
                hide kim serious5
                stop music
                jump talktogirls


label interrogatebella:
    scene upstairshall
    show bella curious4 at center
    bella "Hello, [player_name]."
    main "Hello, Bella. You wanted to talk to me?"
    bella "Yes. It's about tomorrow."
    bella "Am I still off tomorrow?"
    show bella serious6 at center
    bella "Before you came here, I submitted my vacation request to John and he approved it."
    bella "But now you're here and the auditor arrived-"
    show bella serious7 at center
    bella "{cps=*5}Ireallyreallyneedthistimeoffit'simportant.{/cps}"
    main "Woah..slow down, Bella."
    show bella sad7 at center
    bella "There's a robotics competition tomorrow."
    bella "I'm a judge."
    main "Robotics?"
    show bella smile2 at center
    bella "Yeah, it's nothing big. I participated in them when I was in school."
    main "Did you win anything?"
    show bella sad7 at center
    bella "I got third place at national competition. I also got a scholarship."
    main "Woah, third place. So wait, how did you end up here?"
    show bella sad6 at center
    bella "I don't want to talk about it."
    show bella serious2 at center
    bella "So am I still off for tomorrow."
    main "Uh, sure. You're still off."
    show bella smile3 at center
    bella "Thanks, [player_name]."
    main "Bel-"
    hide bella smile3
    "(And she's gone.)"
    "(She's a difficult one to crack.)"
    "(I didn't even get a chance to ask her any questions.)"
    $ bellatalk = True
    jump talktogirls

label ch3ending:
    "(That's everyone.)"
    "(I think I accomplished a lot today.)"
    "(Let me see what's on the computer.)"
    scene 23chapter3
    "(Hmm..what's this?)"
    "(Interview tapes?)"
    label watchinterviews:
        scene 23chapter3
        "(Should I watch them?)"
        menu:
            "I won't watch any of them" if notapes==True:
                jump watchnone
            "Watch Kim's tape" if kimtape == False:
                $ kimtape = True
                $ notapes = False
                jump kimstape
            "Watch Mai's tape" if maitape == False:
                $ maitape = True
                $ notapes = False
                jump maistape
            "Watch Lisa's tape" if lisatape == False:
                $ lisatape = True
                $ notapes = False
                jump lisastape
            "Watch Bella's tape" if bellatape == False:
                $ bellatape = True
                $ notapes = False
                jump bellastape
            "I won't watch any more tapes" if notapes == False:
                jump finishedwithtapes

    label watchnone:
        "(No, I refuse to watch the tapes.)"
        "(I won't even ask any of the girls about it.)"
        jump chapter3end

    label kimstape:
        scene kimtape4
        "This is a big office, John."
        "Too big for your tastes?"
        "Are you going to hire a lot of people, John?"
        "No, just enough to keep the business running."
        "Now here, sign this contract."
        scene kimtape5
        "A contract, but..why?"
        "I thought you trusted me."
        "To keep things official. Taxes, Investors."
        scene kimtape6
        "So I'm an employee?"
        "My most valuable one."
        scene kimtape1
        "Why is there a camera-"
        "Shhhh..."
        scene kimtape2
        "But ..{font=font/BPletterSquares.ttf} uncle {/font}.."
        scene kimtape3
        "We will have{font=font/BPletterSquares.ttf}everything we could ever want and more, princess.{/font}"
        "Just {font=font/BPletterSquares.ttf}beagoodgirl fordaddy..{/font}"
        scene black
        hide screen recorder
        "(I wonder what he said to her.)"
        jump watchinterviews

    label maistape:
        show screen recorder
        scene maitape1
        "Hello Mr. Shilling."
        "Please, call me John."
        "How was your flight?"
        scene maitape2
        "Very long."
        "Did you have to stay long in Customs?"
        "Hmm?"
        "You were able to get to your apartment easily?"
        "Yes, very easy."
        scene maitape3
        "I'm sorry about what happened to your village, with the typhoon."
        "....I worry about my family."
        "Well, as long as you work for me, I will help you and your family."
        "You, your family, your village, were so hospitable every time I visited there."
        "Just right now, I can only pay for your visa."
        scene maitape4
        "Oh."
        scene maitape5
        "I need you to sign this contract, it's extremely important."
        "...."
        scene maitape6
        "Mai."
        "Yes?"
        scene maitape7
        "It's very important that you follow my instructions, is that understood?"
        "Yes, Mr. Shil- John."
        "Good. Help me and I'll help you. That's how things work."
        hide screen recorder
        scene black with fade
        jump watchinterviews

    label lisastape:
        show screen recorder
        scene lisatape1
        "...."
        "Oh, good morning, Mr. Shilling."
        "A pleasure to meet you in person."
        "Alyssa. "
        "Hehe. Yes. Alyssa Rogers. Or is it Alina Rouge?"
        scene lisatape2
        "!!"
        "I thought-I thought no one would recognize me after a year."
        scene lisatape3
        "I cut my hair, made it darker."
        "That means I'm not going to get the job, am I?"
        "On the contrary. I called you for an interview, didn't I?"
        "Despite- or rather, in spite of- your past, I think you have the qualifications for the job."
        scene lisatape4
        "I do?"
        "Of course!"
        "So am I hired?"
        "Once you sign this contract, you will."
        "Contract?"
        "Just a Non-Disclosure Agreement."
        scene lisatape5
        "Oh, oh sure, I'll sign."
        "Welcome to SPH, Alyssa."
        "Thanks, Mr. Shilling."
        "Please, call me John."
        hide screen recorder
        scene black with fade
        jump watchinterviews


    label bellastape:
        show screen recorder
        scene bellatape1
        dad "I hope she isn't ugly."
        dad "I can't believe I agreed to do this."
        scene bellatape2
        bella "Good afternoon, Mr. Shilling. I'm sorry I'm late."
        dad "Please, have a seat."
        dad "Your father tells me you're a prodigy when it comes to computers."
        bella "Yes."
        scene bellatape3
        dad "You even helped him with his uh- what's it called- block chain money- crypto-?"
        bella "Cryptocurrency."
        dad "Mmm. Yes, yes that's it."
        scene bellatape4
        bella "What exactly will I be doing? My father said you had a job for me-"
        dad "Quality Assurance, just making sure that the software runs as intended."
        dad "You should thank your father. I normally don't hire friends or family."
        scene bellatape5
        bella "I-"
        dad "Just sign the contract. You start tomorrow."
        bella "Thank you, Mr. Shilling."
        hide screen recorder
        scene black with fade
        jump watchinterviews

    label finishedwithtapes:
        "(Sure,my dad coerced them into joining the company but,they all applied willingly.)"
        if bellatape == True:
            "(But Bella's tape was the most interesting.)"
            "(Something about a cryptocurrency.)"
        else:
            "(But nothing in those tapes gives me any clues in regards to the business.)"
            "(I will have to keep digging elsewhere.)"
        scene black
        jump chapter3end

label chapter3end:
    "(Home at last.)"
    "(Now to watch the news.)"
    scene newsreport
    play music "music/track6.ogg"
    newsreporter "Tonight, our top headline. An undersecretary working for the tax department is being investigated for bribery and corruption."
    newsreporter "Officials say that the secretary was receiving bribes in exchange for cutting taxes."
    newsreporter "We will be continue to update you on the situation."
    stop music
    scene black with fade
    "(Corruption and bribery..)"
    if kimtalk == True:
        "(Could it be related to what Kim said?)"
    else:
        "(Are we involved in some way?)"
    "(This makes me uneasy.)"
    "(Because of the auditor- even though she didn't look like one.)"
    "(I need to talk to the girls more and get more information out of them.)"
    play sound "sfx/misc_sound.ogg"
    show chapter3titleend with easeinright:
        yalign 0.4
        alpha 0.5
        linear 2.0 alpha 1.0
        pause 1.0
        linear 2.0 alpha 0.0

    jump chapter4
