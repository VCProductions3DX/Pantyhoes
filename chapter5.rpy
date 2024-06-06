label chapter5:
    scene messyoffice
    "(Another day at work.)"
    "(Hmm?)"
    "(My office is a mess!)"
    with smallshake
    "(I don't remember it being this dirty!)"
    "(Did someone break in?)"
    show chapter5title with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    scene messyoffice2
    "(I should go through everything and see if anything is missing.)"
    "(What's the commotion downstairs?)"
    show screen monitor
    play music "music/track3.ogg"
    scene 1chapter5
    lisa "Welcome back, Bella!"
    scene 2chapter5
    lisa "You're here early."
    bella "Yeah, I forgot a few things."
    scene 3chapter5
    bella "Did you guys rearrange the office again?"
    lisa "No, why?"
    bella "It just looks different, that's all."
    scene 4chapter5
    bella "Oh, I brought a little friend for you guys."
    lisa "Oh, how cute!"
    scene 5chapter5
    bella "I don't need it, and it's programmed to recognize your faces."
    lisa "Wow, you are....a genius, Bella."
    bella "I know."
    lisa "By the way, [player_name] wanted to talk to you."
    lisa "He's in his office right now."
    bella "Sure, I'll go meet him."
    scene 6chapter5
    bella "Hmm, someone's been on my computer lately."
    hide screen monitor
    stop music
    jump bellashortexplanation

label bellashortexplanation:
    play music "music/track1.ogg"
    scene upstairshall
    show bella serious2 at center
    bella "Hello [player_name]."
    main "Welcome back, Bella, how was your competition?"
    bella "Oh it went fantastic. There were so many new inventions."
    show bella smile3 at center
    bella "I have to get back to my office, I'm working on a project myself."
    bella "What did you want to talk to me about?"
    main "It's about your job."
    show bella surprised1 at center
    bella "My job?"
    main "Yes. What exactly do you do?"
    show bella sad4 at center
    bella "I just make sure all of the programs work."
    bella "Fixing bugs and fixing more bugs."
    main "So you wouldn't know anything about buying, selling, trading, or making cryptocurrency would you?"
    show bella surprised4 at center
    bella "!!!"
    bella "Where did you hear it from?"
    if bellatape == True:
        main "I saw it on your interview tape."
        show bella sad6 at center
        bella "Oh...that."
        main "Your dad is on good terms with my dad."
        show bella serious3 at center
        bella "Yeah, I needed a job at the time, there weren't any teaching positions open at the university."
        bella "So my dad asked John to uh 'do an internship' while waiting for one to open."
    else:
        main "I heard about it from the other employees."
        show bella curious2 at center
        bella "Who? Mai? Lisa? "
        main "It doesn't matter."
        bella "Oh well, yeah. Your dad hired me to work on it."

    show bella curious3 at center
    bella "You know how cryptocurrency works, right?"
    bella "It's like banking but without the bankers."
    show bella serious7 at center
    bella "I could spend a whole day discussing how blockchain works but I-"
    main "I want to know how this company is involved."
    show bella surprised4 at center
    bella "Oooh. Well, in the beginning we were just buying it. The cryptocurrency that is."
    main "And then?"
    show bella serious6 at center
    bella "And then your dad wanted to be part of it. I would say 'create it' but that's inaccurate."
    show bella serious3 at center
    bella "You know, I really have to get back to my office-"
    main "I'll come with you. We can talk more there."
    bella "Really?"
    main "Yes, let's go."
    stop music
    jump inbellaslab

label inbellaslab:
    play music "music/track9.ogg"
    scene bellaslab
    show bella smile4 at center
    bella "And here we are."
    show bella serious5 at center
    bella "Could you stay right there please? I get disoriented quickly."
    main "Sure."
    main "So about the cryptocurrency."
    show bella serious4 at center
    bella "The original plan was to run a mining farm, but John thought it was too expensive."
    bella "So he came up with another idea."
    main "Which is?"
    show bella curious2 at center
    bella "We sold people's personal data for it."
    main "How?"
    show bella smile2 at center
    bella "Right when they press the 'agree to terms of service' contract before installing the software."
    bella "The 'anti-piracy' software I install actually collects and sends their browsing data to us."
    show bella serious2 at center
    bella "And then we sell that to another company for cash, which we use to buy cryptocurrency."
    bella "Buy low, sell high. Add it to our revenue."
    bella "And investors throw money at us."
    show bella sad7 at center
    bella "According to John, that's off the books. All the investors see is that we have a good cash flow."
    bella "They don't care how we get it."
    main "Isn't this all dependent on the value of cryptocurrency?"
    show bella serious4 at center
    bella "When cooking the books for investors, yes."
    bella "Of course, the government has been skeptical about cryptocurrency."
    bella "So we keep that hidden."
    main "And that's why there are two different income statements."
    show bella smile1 at center
    bella "That's the entire deal."
    menu:
        bella "Now if you will excuse me, I have work to do."
        "Thanks Bella":
            main "I should get back to the office."
            bella "You're welcome, [player_name]."
            bella "I'm glad I could help you."
            stop music
            jump catchingcrissy
        "What are you working on?":
            main "You seem really preoccupied."
            bella "A service robot."
            jump bellasrobotics

label bellasrobotics:
    $bellarobot = True
    scene bellarobot1
    bella "This one is meant to service hospitals."
    bella "Providing meals, snacks, and drinks for patients. I thought about adding medicine but it would take a lot longer."
    bella "I don't want to be responsible for overdosing."
    scene bellarobot2
    main "Are there any others you have made?"
    bella "I did make a mining one. Not computer mining, but actual mining."
    scene bellarobot3
    bella "Less humans mining with better efficiency."
    main "What happened?"
    bella "Someone patented it."
    bella "I was too naive at the time.."
    scene bellarobot4
    bella "And I don't have the money to buy it back. My father won't give me any."
    bella "So I'm stuck working for your dad- well you- until I get the money."
    main "Then, what will you do?"
    scene bellarobot5
    bella "Buy it and quit."
    main "Actually, I was thinking of dissolving the company and starting something new."
    bella "Oh?"
    main "Yeah, pay off debts and start over. I just don't know what though."
    main "But building robots-"
    scene bellarobot6
    bella "Is extremely expensive and you need a lot of capital. Tangible capital."
    scene bellarobot7
    bella "I appreciate your interest, but it will be a couple of years before robots become mainstream."
    main "Enough time to get the money."
    bella "I'm not counting on it."
    show moraleup at attributeup
    $cBella.morale_up(4)
    main "I should get going. Thanks for everything, Bella."
    bella "You're welcome, [player_name]."
    stop music
    jump watchsurveywithcrissy

label catchingcrissy:
    scene downstairsoffice
    show lisa serious6 at center
    lisa "There you are!"
    main "Sorry, I had to talk to Bella."
    show lisa serious8 at center
    lisa "That woman came in here and went straight to your office."
    main "Woman?"
    show lisa angry1 at center
    lisa "You know? The auditor."
    lisa "She had a cocky smile on her face, like she won the lottery."
    show lisa serious10 at center
    lisa "We tried to call you but you wouldn't pick up."
    lisa "And Kim's not in her office."
    main "It's fine, I'll take care of it."
    hide lisa serious10
    play sound "sfx/elevator_moving.ogg"
    scene elevator with fade
    "(It's still too early for her to start working here.)"
    stop sound
    play sound "sfx/fgrunt.ogg"
    main "Who's there?"
    stop sound
    play music "music/track6.ogg"
    scene crissycaught1
    main "You!"
    main "What are you doing in my office???"
    scene crissycaught2
    crissy "I can explain-"
    main "Why are you going through my things?"
    scene crissycaught3
    crissy "It's not what it looks like-"
    main "Then what does it look like?"
    scene crissycaught4
    crissy "I-"
    scene crissycaught5
    crissy "Please, I really need this job!"
    main "Get up!! Now!!"
    scene upstairshall
    main "Get out of this office! Get out before I call the police for trespassing!"
    show crissy sad2 at center
    crissy "....."
    main "And don't come back."
    show crissy flirt1 at center
    crissy "You know, you're way too stressed out."

    menu:
        "(This again?)"
        "That's none of your business.":
            show crissy smile2 at center
            crissy "Then maybe this is."
            crissy "Your employees know all about your affairs."
            main "My affairs?"
            show crissy smile3 at center
            crissy "I heard all about it on that laptop."
            main "Get out."
            main "Just get out!"
            show crissy smile5 at center
            crissy "At least I'm upfront and honest about it."
            menu:
                crissy "You don't need to play with my feelings to get what you want."
                "Get the fuck out!":
                    main "You're fired."
                    main "I'll hire another auditor."
                    $authority.trait_up(4)
                    show authorityup at attributeup
                    show crissy angry6 at center
                    crissy "I will remember this."
                    stop music
                    hide crissy angry6
                    jump spyondownstairs

                "And what are you offering?":
                    show crissy flirt3 at center
                    crissy "Just some stress relief."

                    menu:
                        crissy "Come on."
                        "Accept":
                            jump acceptcrissysoffer

                        "Refuse":
                            show crissy angry7 at center
                            $authority.trait_up(2)
                            show authorityup at attributeup
                            main "Leave."
                            main "You're fired."
                            main "I'll hire another auditor."
                            show crissy angry6 at center
                            crissy "Ok, [player_name], I'll remember this."
                            main "And don't come back."
                            hide crissy angry6
                            stop music
                            jump spyondownstairs

        "Cover that up.":
            show crissy sad6 at center
            $authority.trait_up(2)
            show authorityup at attributeup
            crissy "You're not a tit man, are you?"
            main "What do you think this is, a porn video?"
            show crissy serious7 at center
            crissy "No, but from what I heard, it sounds like one of those video games where the guy sleeps with all of the girls."
            crissy "And they fight over him."
            show crissy smile5 at center
            crissy "Except it's actually real, isn't it?"
            main "No, you're delusional."
            show crissy sad1 at center
            crissy "I heard a lot of interesting things on that laptop."
            if footlover== True:
                crissy "A foot fetish.."
            else:
                crissy "You just had to fuck your hot employees, didn't you?"
            show crissy smile1 at center
            crissy "At least I'm upfront about offering it."

            menu:
                crissy "No feelings or strings attached."
                "Get out of my office.":
                    show crissy sad3 at center
                    $authority.trait_up(1)
                    show authorityup at attributeup
                    main "I never want to see you again."
                    main "You're fired."
                    main "I'll hire another auditor."
                    main "NOW or I'll get the police."
                    show crissy angry6 at center
                    crissy "Fine, have it your way."
                    stop music
                    hide crissy angry6
                    jump spyondownstairs

                "That's your offer?":
                    show crissy flirt3 at center
                    crissy "Just a little stress relief."
                    crissy "Whatever you want to do."

                    menu:
                        crissy "I'll be quiet, I promise."
                        "Accept":
                            main "It doesn't change anything."
                            main "You're fired."
                            main "I'll hire another auditor."
                            jump acceptcrissysoffer

                        "Refuse":
                            show crissy sad6 at center
                            $authority.trait_up(1)
                            show authorityup at attributeup
                            main "You're pathetic."
                            main "I don't see how anyone can take you seriously."
                            main "Just leave."
                            hide crissy sad6
                            crissy "Good bye, [player_name]."
                            stop music
                            jump spyondownstairs

label acceptcrissysoffer:
    $crissyfuck = True
    crissy "Just close your eyes and relax."
    main "I have a better offer."
    if persistent.sexscenes == False:
        scene black with fade
        crissy "Do..you...have..to..be..so..rough.."
        crissy "Ugh!"
        jump aftercrissyfuck
    else:
        scene crissysofa1
        crissy "What's that?"
        main "Lay down and spread your legs."
        crissy "What?"
        main "Now."
        scene crissysofa2
        crissy "Fuck, ok."
        crissy "Are you really going to fuck me?"
        main "You asked for it."
        jump crissyofficefuck


label crissyofficefuck:
    scene crissyoffice
    menu:
        "View 2":
            jump crissyofficefuck2
        "View 3":
            jump crissyofficefuck3
        "Finish":
            jump aftercrissyfuck
label crissyofficefuck2:
    scene crissyofficev2
    menu:
        "View 1":
            jump crissyofficefuck
        "View 3":
            jump crissyofficefuck3
        "Finish":
            jump aftercrissyfuck

label crissyofficefuck3:
    scene crissyofficev4
    menu:
        "View 1":
            jump crissyofficefuck
        "View 2":
            jump crissyofficefuck2
        "Finish":
            jump aftercrissyfuck




label aftercrissyfuck:
    scene upstairslounge
    show crissy smile4 at center
    crissy "Don't take my word for it, [player_name]- go look at the laptop yourself."
    crissy "They were talking all about you."
    show crissy sad6 at center
    crissy "Good bye, [player_name]."
    crissy "I'll keep this between the two of us."
    stop music
    hide crissy sad6
    "(I have to see if what she said was true.)"
    jump spyondownstairs


label watchsurveywithcrissy:
    play music "music/track10.ogg"
    scene downstairslounge
    "(I'm finally back.)"
    "(Where is everyone?)"
    scene messyoffice
    "(Why does my office look different?)"
    "(It's like someone has gone through my stuff.)"
    "(Let me check the laptop.)"
    show screen monitor
    scene crissycaught1
    crissy "And these records here..."
    crissy "That should do!"
    crissy "There's no safe or anything."
    crissy "This is going to be difficult unless..I can access Bella's computer."
    scene crissycaught5
    crissy "There! A system override. I can look at her files from here."
    crissy "Well, well...what do we have here.."
    crissy "I'm just going to send an email."
    scene crissycaught6
    "(I'm beginning to think she's not an auditor at all.)"
    "(But a private districtattorney.)"
    "(Or worse, the police.)"
    jump spyondownstairs

label spyondownstairs:
    stop music
    show screen monitor
    play music "music/track3.ogg"
    scene lisamaitalk1
    lisa "What should we name the little guy?"
    mai "Hmmm..why not call it Little [player_name]?"
    scene lisamaitalk2
    lisa "Mini [player_name]?"
    mai "Yeah!"
    mai "It's like he's here even though he's not here."
    scene lisamaitalk3
    lisa "I have an idea."
    scene lisamaitalk4
    lisa "3...2...1..."
    play sound "sfx/fscream.ogg"
    with smallshake
    scene kimprank1
    kim "{size=+10}A MOUSE! SOMEONE HELP!!!!{/size}"
    stop sound
    scene kimprank2
    kim "No..that's not a mouse..it's..a robot.."
    scene kimprank3
    kim "Oh, I'm surrounded by idiots."
    kim "I can't wait to leave them behind."
    scene kimprank4
    kim "I'm leaving for the day."
    kim "I'll ask [player_name] to carry my things tomorrow."
    scene lisamaitalk5
    lisa "I haven't...had...a good laugh...in ...so long.."
    mai "She's such a scaredy-cat."
    lisa "Good job, Mini [player_name]."
    scene lisamaitalk6
    mai "It seems to really like you, Lisa."
    lisa "No I just think- does it have a thing for feet?"
    scene lisamaitalk7
    if footlover == True:
        mai "Then it really is like [player_name]."
    else:
        mai "Or maybe it wants to look at something else."
    scene lisamaitalk8
    lisa "Designing a perverted robot, that Bella."
    mai "Lisa may I ask you a question?"
    lisa "Yeah, what is it, Mai?"
    scene lisamaitalk9
    mai "Are you close to [player_name]?"
    "(Oh no..Christina was right.)"
    if lisatalk == True:
        lisa "Well, he did call me up to his office the other day."
        lisa "I ended up ranting to him about my dreams and my past..."
        if lisaworkout == True:
            lisa "Then we went to workout at the gym near his place."
            lisa "He's a closet gym freak."
            if lisafoot == True:
                lisa "Then I spent the night at his place and he..smelled my feet."
                mai "!!"
                lisa "It was weird, but that's all we did."
                jump maisside
            elif lisashowerfuck == True:
                lisa "Then I spent the night at his place and we..made out.."
                lisa "Actually..it was uh...more than that."
                mai " !!"
                jump maisside
            else:
                lisa "Some asshole loser hit on me, but [player_name] threatened him and went home."
                lisa "That's all we did."
                jump maisside

        else:
            lisa "Other than that, nothing really happened."
            jump maisside
    else:
        lisa "No, not really."
        jump maisside

label maisside:
    scene lisamaitalk10
    lisa "What about you? Are you close to [player_name]?"
    if maitalk == True:
        mai "[player_name] asked me about the financial records and..."
        lisa "You told him everything, didn't you?"
        mai "Yeah."
        if maimassage == True:
            mai "Then I gave him a massage."
            mai "You are right, he is ripped."
            lisa "My goodness."
            mai "Lots of sore muscles and tight joints, though."
            if maifootjob == True:
                mai "Uhm..."
                lisa "What is it?"
                mai "He asked for a footjob."
                lisa "What?"
                if lisafoot== True:
                    lisa "After smelling my feet!"
                    mai "I know."
                    lisa "I'm going to chew him out!"
                    mai "Count me in!"
                    hide screen monitor
                    jump aftermonitor
                elif lisashowerfuck ==True:
                    lisa "After we..."
                    lisa "....I knew he was a ladies man.."
                    lisa "And I still.."
                    mai "We should talk to him."
                    lisa "Yeah, we should."
                    hide screen monitor
                    jump aftermonitor
                else:
                    scene lisamaitalk11
                    lisa "He seems to like you a lot if he's doing that."
                    lisa "But I wonder if he's done anything with Kim or that cow.."
                    mai "Oh..."
                    lisa "Let's confront him."
                    lisa "And make [player_name] set the record straight."
                    mai "Ok, thanks Lisa."
                    hide screen monitor
                    jump aftermonitor

            elif maihandjob == True:
                mai "Uhm..."
                lisa "What is it?"
                mai "He asked for a handjob."
                lisa "What?"
                if lisafoot== True:
                    lisa "After smelling my feet!"
                    mai "I know."
                    lisa "I'm going to chew him out!"
                    mai "Count me in!"
                    hide screen monitor
                    jump aftermonitor
                elif lisashowerfuck ==True:

                    lisa "After we..."
                    lisa "....I knew he was a ladies man.."
                    lisa "And I still.."
                    mai "We should talk to him."
                    lisa "Yeah, we should."
                    hide screen monitor
                    jump aftermonitor
                else:
                    scene lisamaitalk11
                    lisa "He seems to like you a lot if he's doing that."
                    lisa "But I wonder if he's done anything with Kim or that cow.."
                    mai "Oh..."
                    lisa "Let's confront him."
                    lisa "And make [player_name] set the record straight."
                    mai "Ok, thanks Lisa."
                    hide screen monitor
                    jump aftermonitor

            else:
                scene lisamaitalk11
                lisa "Well I think he's leading us on."
                lisa "We should talk to him."
                hide screen monitor
                jump aftermonitor
        else:
            scene lisamaitalk11
            mai "That was it."
            mai "We didn't do anything."
            lisa "He does seem like a ladies man, doesn't he?"
            mai "Yeah."
            lisa "Want to talk to him?"
            mai "Yeah, we should."
            hide screen monitor
            jump aftermonitor

    else:
        scene lisamaitalk11
        mai "No, not really."
        lisa "Oh."
        mai "I was just asking. He is a really sweet guy but he seems like a ladies man."
        lisa "Yeah he does."
        lisa "I wonder if Kim has tried to sink her fangs into him."
        lisa "She seems like the type to manipulate any guy."
        lisa "I think we should talk to him."
        mai "Yeah."
        hide screen monitor
        jump aftermonitor

label aftermonitor:
    play music "music/track1.ogg"
    scene messyoffice
    "(This isn't good.)"
    "(I'll deal with them tomorrow.)"
    "(First I should check and see what's missing.)"
    scene messyoffice2
    "(The papers Mai brought me.)"
    "(And the notebook.)"
    "(They're gone.)"
    "(What else did Christina steal?)"
    play sound "sfx/ElevatorDing.ogg"
    jump lisamaiconfrontation

label lisamaiconfrontation:
    stop sound
    scene upstairshall
    show lisa serious11 at left
    show mai sad3 at right
    lisa "Hello [player_name]."
    main "Hi Lisa, Mai."
    main "I thought you ladies left the office."
    show lisa angry2 at left
    lisa "You have some explaining to do."
    main "Explaining?"
    show lisa serious12 at left
    lisa "Are you screwing everyone in this office?"
    lisa "We need to know."
    lisa "Because I don't want to work here anymore if you are."
    menu:
        lisa "And don't lie."
        "No":
            if maimassage == True:
                show mai sad2 at right
                mai "But I gave you a massage."
                main "And that's all we did."
                if maifootjob == True:
                    show mai serious3 at right
                    mai "No, we did more than that."
                    show lisa angry5 at left
                    lisa "Oh my god, I said don't lie,  [player_name]."
                    lisa "Screw this. I'm quitting."
                    lisa "Fuck you two and fuck this company."
                    lisa "Goodbye."
                    hide lisa angry5
                    jump maiprivatetime
                elif maihandjob == True:
                    show mai serious3 at right
                    mai "No, we did more than that."
                    show lisa angry5 at left
                    lisa "Oh my god, I said don't lie,  [player_name]."
                    lisa "Screw this. I'm quitting."
                    lisa "Fuck you two and fuck this company."
                    lisa "Goodbye."
                    hide lisa angry5
                    jump maiprivatetime
                else:
                    show mai sad8 at right
                    mai "You're right."
                    lisa "That's it?"
                    main "Yes, that's it."
                    lisa "And did you like it?"
                    menu:
                        "Of course I did":
                            main "It's a massage."
                            lisa "And you're a boss."
                            jump mcplayerend
                        "It was just one time":
                            show lisa angry5 at left
                            lisa "Yeah, sure."
                            lisa "Tell yourself that."
                            lisa "I'll leave you two lovebirds alone."
                            lisa "I quit."
                            lisa "Goodbye."
                            hide lisa angry5
                            jump maiprivatetime
            else:
                show mai sad4 at right
                mai "He's telling the truth, Lisa."
                mai "We didn't do anything."
                if lisahomeinvite == True:
                    show lisa angry4 at left
                    lisa "We still did something. Together."
                    lisa "So he didn't tell the entire truth."
                    mai "Oh."
                    lisa "Mai, do you mind giving us some private time?"
                    mai "Yes, I will Lisa."
                    mai "I am going home now."
                    hide mai sad4
                    jump lisaprivatetime
                else:
                    lisa "Ok, time for a direct approach."
                    lisa "Do you like any of us, [player_name]?"

                    menu:
                        lisa "Or are we just a bunch of fuckdolls for you?"
                        "I like you, Lisa":
                            show lisa surprise3 at left
                            lisa "You do?"
                            main "Yes, I do."
                            show lisa smile4 at left
                            lisa "Hahaha."
                            lisa "Beat you there, Mai."
                            show mai sad7 at right
                            mai "......"
                            lisa "She ran off."
                            hide mai sad7
                            jump lisaprivatetime

                        "I like Mai.":
                            show lisa sad3 at left
                            lisa "I guess you lucked out, Mai."
                            lisa "You should make sure he's telling the truth."
                            lisa "As for me, I'm quitting."
                            lisa "This is too much for me."
                            hide lisa sad3
                            main "Lisa wait-"
                            jump maiprivatetime

                        "I don't like anyone.":
                            lisa "Sure, sure."
                            jump mcplayerend



        "Just you, Lisa":
            if maifootjob == True:
                show mai sad6 at right
                mai "That's not true and you know it, [player_name]."
                lisa "I said not to lie."
                jump mcplayerend
            elif maihandjob == True:
                show mai sad6 at right
                mai "That's not true and you know it, [player_name]."
                lisa "I said not to lie."
                jump mcplayerend
            else:
                show lisa smile3 at left
                lisa "So you are telling the truth."
                lisa "I guess you're a good guy after all, [player_name]."
                mai "I'm leaving."
                lisa "Thanks for coming with me, Mai."
                hide mai sad3
                jump lisaprivatetime

        "Yeah I am.":
            jump mcplayerend

label mcplayerend:

    $charm.trait_down(5)
    show charmdown at attributedown
    show lisa angry1 at left
    lisa "Did you fuck that cow and Kim as well?"
    lisa "Are we all just your playthings?"
    show mai sad5 at right
    mai "Say something, please [player_name]."
    main "I..."
    show lisa sad5 at left
    lisa "Forget it, Mai."
    show lisa angry5 at left
    lisa "He still thinks he's in college and can fuck any girl he wants without any consequences."
    show mai sad10 at right
    lisa "When you grow up, please let one of us know."
    lisa "Good bye, [player_name]."
    hide lisa angry5
    mai "Good bye, [player_name]."
    hide mai sad10
    "(Shit that didn't go well.)"
    jump kimasksformcshelp

label lisaprivatetime:
    $picklisa = True
    main "I'm sorry for the confusion, Lisa."
    main "I would really like to get to know you better."
    show lisa sad9 at center
    lisa "So when you say, 'get to know you better', do you mean..?"
    main "Dinner, movies, going to festivals."
    show lisa serious4 at center
    if lisafoot == True:
        lisa "Not just smelling my feet?"
        main "Well, that too."
        lisa "Pervert."
    else:
        lisa "So not just sex?"
        main "Of course not."

    show lisa sad9 at center
    lisa "Do you mind if I tell you something?"
    main "Yeah, sure."
    show lisa sad7 at center
    lisa "I was thinking of going back to school."
    lisa "Getting a degree in fashion design."
    show lisa sad3 at center
    lisa "I'm too old to be a model, but I think I have what it takes to be a fashion designer."
    lisa "Of course, I would have to move to New York City so I would be quitting the firm.."
    lisa "I-I have never been in a long distance relationship."
    main "We can make it work. I might move the business to New York City. Or completely shut it down."
    show lisa serious9 at center
    lisa "But what about the others?"
    main "I'm sure they can find jobs elsewhere. I can offer recommendations."
    show lisa sad9 at center
    lisa "You would do all of that...for me?"
    main "Of course."
    hide lisa sad9
    scene lisamcmakeup1
    show moraleup at attributeup
    $cLisa.morale_up(4)
    lisa "You're a sweetheart, [player_name]."
    lisa "Well, I need to finish up a few things before going home."
    scene lisamcmakeup2
    lisa "I'll call you later."
    jump kimasksformcshelp

label maiprivatetime:
    $pickmai = True
    show mai sad8 at center
    mai "So does this mean we're uhm..."
    main "I said I would help you."
    show mai smile5 at center
    mai "Thank you, [player_name]."
    mai "May I stay over at your place tomorrow?"
    mai "I will even cook dinner for you."
    show mai curious2 at center
    mai "You can not eat only pizza, [player_name]."
    "(She noticed that?!?)"
    hide mai curious2
    main "Well..."
    scene maimcmakeup1
    mai "You're so cute, [player_name]."
    show moraleup at attributeup
    $cMai.morale_up(4)
    scene maimcmakeup2
    mai "I am going back to work. I will call you tonight."
    jump kimasksformcshelp


label kimasksformcshelp:
    play sound "sfx/cellvibe.ogg"
    "(Who's calling me now?)"
    stop sound
    main "Hello?"
    show kimphone at topleft
    kim "[player_name], do you mind helping me carrying my things to my apartment?"

    menu:
        kim "It's so heavy."
        "Sure.":
            main "I'll be down there shortly."
            hide kimphone
            scene kimsoffice
            show kim smile3 at center
            kim "Aww, thanks [player_name]."
            show moraleup at attributeup
            $cKim.morale_up(3)
            kim "You are a sweetheart."
            show kim smile7 at center
            kim "My apartment isn't far but I have so much to carry."
            hide kim smile7
            stop music
            jump atkimsapartment
        "I'm busy.":
            show moraledown at attributedown
            $cKim.morale_down(2)
            kim "Oh.."
            main "Just make multiple trips or something."
            main "You don't live far from here, do you?"
            kim "No, I don't."
            main "Goodbye, Kim."
            hide kimphone
            stop music
            jump mcgoeshomeafterrejection

label atkimsapartment:
    play music "music/track12.ogg"
    scene kimsapartment
    show kim smile8 at center
    kim "Home Sweet Home."
    kim "You can put that box over there."
    show kim sad3 at center
    kim "It's really over, isn't it?"
    if cKim.morale >= 4:
        main "What's over?"
        show kim serious2 at center
        kim "Everything Jo-your dad and I had."
        jump kimslifestory
    else:
        show kim sad8 at center
        kim "But who wants to listen to a used-up whore like me?"

        menu:
            kim "You have something better to do right?"
            "Yes":
                show kim sad10 at center
                kim "Thanks for everything, [player_name]."
                kim "Good luck with the business."
                main "You too, Kim."
                jump mcgoeshomeafterrejection
            "I don't mind.":
                show kim smile10 at center
                kim "You want to listen to me?"
                show moraleup at attributeup
                $cKim.morale_up(3)
                show kim smile9 at center
                kim "Where to begin.."
                jump kimslifestory

label kimslifestory:
    show kim serious5 at center
    kim "Your father and I met at my dad's wedding."
    kim "We hit it off right away."
    show kim sad5 at center
    kim "I became his personal assistant, travelling with him all of the time."
    kim "But lately he started going on trips without me."
    kim "He stopped asking me for favors."
    show kim serious4 at center
    kim "Then you came."
    main "I'm sure he'll be ba-"
    show kim sad1 at center
    kim "He won't. Do you remember the last company he ran? He did the exact same thing."
    main "That was a sell off. It was in the news."
    main "He said he hated the industry, he wanted to go back to his first love-"
    kim "All smoke and mirrors."
    show kim serious3 at center
    kim "Did that spoiled brat tell you everything?"
    main "She did. But I don't see how-"
    kim "He used the company to launder funds from his {i} other{/i} ventures."
    kim "His overseas off-the-books ventures."
    show kim sad7 at center
    kim "There's no way a company makes over a million dollars on buying and hosting abandoned software."
    kim "Or from selling people's data either."
    kim "It's just a way to clean money from his real business."
    main "Which is?"
    show kim sad9 at center
    kim "I'm not telling. I rather not."
    show kim sad10 at center
    kim "He's gone. Forever."
    kim "What am I to do?"
    show kim sad3 at center
    kim "I have no real skills."
    kim "I don't know anything in regards to technology."
    kim "Just be a play toy."
    main "What about the webcam thing?"
    show kim sad1 at center
    kim "That won't be forever."
    kim "New girls come every day. Younger, thinner, prettier, sweeter."
    kim "And I don't really need the money from it. I just needed a purpose."
    main "Maybe you should go travel and find a new one."
    kim "......."
    show kim sad5 at center
    kim "I wanted to have a family with John, to be honest."
    kim "I thought I would be the perfect housewife with little kids and a dog or two.."
    show kim sad8 at center
    menu:
        kim "But it's all gone now."
        "I'm sorry to hear that, Kim.":
            main "That's what you get for breaking up our family."
            show kim sad6 at center
            kim "Hmph, you would say that."
            jump rejectkim
        "There's still time, Kim.":
            main "You can still have a family."
            show kim sad4 at center
            kim "You think so, [player_name]?"
            main "You're not that old."
            jump kimsproposition


    label kimsproposition:
        show kim serious2 at center
        kim "What about you, [player_name]?"
        kim "Do you want a family? With me?"
        main "I-"
        kim "Or the other girls?"
        if picklisa == True:
            show kim serious3 at center
            kim "Lisa, Lisa, Lisa."
            kim "She reminds me so much of myself."
            kim "Seeing her ambitions die because of a man."
            kim "Working a low end job just to support him."
            show kim serious5 at center
            kim "And now she's found someone to support her."
            kim "I wonder how long it will be before her eye wanders for attention again."
            main "She's not like that."
            show kim serious6 at center
            kim "Oh? You're young, [player_name]."
            kim "Trust me, she's the type to chase any guy for attention."
            kim "But she hasn't realized that won't work forever."

            menu:
                kim "Do you still want to be with her?"
                "Yes":
                    show kim serious10 at center
                    kim "Don't come to me if you find out she's cheating on you."
                    show moraledown at attributedown
                    $cKim.morale_down(2)
                    kim "Or takes half of your money in a divorce."
                    hide kim serious10 at center
                    jump mcgoeshomeafterrejection
                "Well..now that you mention it.":
                    show kim smile5 at center
                    kim "See? She's no good for you."
                    kim "But I am."
                    scene kimseduce1
                    kim "We can start a family, the two of us."

                    menu:
                        kim "You can have a mommy to take care of you."
                        "Get off of me.":
                            show moraledown at attributedown
                            $cKim.morale_down(2)
                            kim "Just leave."
                            kim "Don't ever talk to me again."
                            jump mcgoeshomeafterrejection
                        "That sounds nice.":
                            kim "I know, doesn't it?"
                            kim "We can start right now."
                            jump acceptkim

        elif pickmai == True:
            show kim serious6 at center
            kim "Mai, that little minx."
            kim "They're all the same."
            kim "So cute and charming until they get married."
            show kim serious4 at center
            kim "Then the monster comes out."
            kim "Controlling your money, your actions until one day they get homesick and go back home."
            kim "Taking whatever kids you had and never seeing them again."

            menu:
                kim "Do you really want that fate?"
                "Mai isn't like that.":
                    main "You're just judging her based off of your assumptions."
                    show moraledown at attributedown
                    $cKim.morale_down(2)
                    kim "I'm predicting her behavior based off of my experience."
                    kim "But you're a difficult learner, so enjoy the lesson."
                    kim "Good bye, [player_name]."
                    jump mcgoeshomeafterrejection
                "You have a point.":
                    scene kimseduce1
                    kim "I'm always right."
                    kim "And we should be together, just the two of us."
                    jump acceptkim

        else:
            show kim serious6 at center
            kim "Are you chasing after those girls in the office?"
            kim "They all got to where they are based on their looks."
            main "How are you any different?"
            show kim smile3 at center
            kim "At least I knew my place."
            kim "And I had a simple end goal."

            menu:
                kim "To be a housewife."
                "Good luck with that.":
                    show kim sad1 at center
                    main "Maybe one day you'll make it on television. Real Housewives of Whatever-"
                    show moraledown at attributedown
                    $cKim.morale_down(2)
                    kim "I have to be married first and look at me-"
                    main "I'm sure you can find someone with your looks."
                    main "Just don't tell them about your past."
                    jump rejectkim

                "And you think you can achieve that with me?":
                    show kim smile3 at center
                    kim "Why not?"
                    kim "You're young, tall, handsome..."
                    kim "And rich."
                    main "Not for long, I doubt."
                    kim "It's better to settle now than later when you'll have nothing but gold diggers."
                    jump acceptkim

label acceptkim:
    scene kimseduce2
    kim "Why hesitate?"
    kim "I know you can't resist me."
    if kimsquirt == True:
        kim "I bet you loved the way my pussy tasted, didn't you?"
    elif kimfuck == True:
        kim "You just couldn't resist fucking me on camera, didn't you?"
    else:
        kim "I bet you're hard right now, aren't you?"
        kim "Your cock is just dying to fuck me."
    scene kimseduce3
    kim "So here I am. I resisted you before, but not any more."
    kim "You can have me all to yourself."

    menu:
        kim "And show me off in front of your parents."
        "I'm leaving.":
            scene kimsapartment
            show kim smile3 at center
            kim "Did I hit a soft spot?"
            kim "I'm so sorry."
            show kim smile4 at center
            kim "I can make it all better."
            kim "I can even give you a personal show."

            menu:
                kim "The same one I gave your father when you discovered us."
                "No is no.":
                    show kim sad3 at center
                    $cKim.morale_down(2)
                    show moraledown at attributedown
                    kim "Fine, just-just go then."
                    jump mcgoeshomeafterrejection

                "Show me.":
                    kim "It goes like this."
                    jump kimsdance

        "Don't bring them up.":
            scene kimsapartment
            show kim serious10 at center
            kim "Aww did I hit a touchy memory for you?"
            kim "Want to relive the night you discovered me?"
            menu:
                kim "But this time up close?"
                "No.":
                    show kim sad7 at center
                    $cKim.morale_down(2)
                    show moraledown at attributedown
                    kim "..."
                    kim "Get out of my apartment."
                    jump mcgoeshomeafterrejection

                "Sure.":
                    kim "Well, it started like this."
                    jump kimsdance

label kimsdance:
    scene kimseduce4
    $cKim.morale_up(4)
    show moraleup at attributeup
    $pickkim = True
    kim "We returned after buying a lot of property overseas."
    kim "Over 10 million dollars."
    kim "I didn't want to go home, so John let me stay the night at your house."
    kim "Your mother was away, he said and you were asleep."
    scene kimseduce7
    kim "But you weren't. Because you saw me do this, didn't you?"
    kim "Was my pussy the first pussy you ever saw? Does it look better now than when you were a little boy?"
    kim "But you saw more than my pussy. You saw me climb onto your dad-"
    scene kimseduce8
    kim "And ride him just like this."
    scene kimseduce9
    kim "Now it's your turn."
    kim "I can feel your cock, it's so hard for me, isn't it?"
    if picklisa == True:
        play sound "sfx/cellvibe.ogg"
        kim "Ignore that."
        stop sound
    elif pickmai == True:
        play sound "sfx/cellvibe.ogg"
        kim "Ignore that."
        stop sound
    else:
        kim "I hope no one was expecting you tonight."
    kim "Take off your clothes."
    scene kimseduce6
    kim "We're going to do this all night long."
    kim "So sit back, relax, and let me do all of the work."
    if persistent.sexscenes == False:
        scene black with fade
        jump afterkim2ndfuck

    else:
        scene 1kimprivate2
        kim "Fuck me, [player_name]. I want you to fuck my pussy."
        kim "I know you want me, don't hold back."
        scene 8kimprivate2
        kim "I want to feel you inside of me."
        jump kimcowgirlfuck

    label kimcowgirlfuck:
        scene kimcowgirl
        menu:
            "View 2":
                jump kimcowgirlfuck2

            "View 3":
                jump kimcowgirlfuck3

            "Finish":
                scene 5kimprivate2
                kim "Your cum feels so good inside of me."
                scene black with fade
                jump afterkim2ndfuck

    label kimcowgirlfuck2:
        scene kimcowgirlv2
        menu:
            "View 1":
                jump kimcowgirlfuck

            "View 3":
                jump kimcowgirlfuck3

            "Finish":
                scene 5kimprivate2
                kim "Your cum feels so good inside of me."
                scene black with fade
                jump afterkim2ndfuck

    label kimcowgirlfuck3:
        scene kimcowgirlv3
        menu:
            "View 1":
                jump kimcowgirlfuck

            "View 2":
                jump kimcowgirlfuck2

            "Finish":
                scene 5kimprivate2
                kim "Your cum feels so good inside of me."
                scene black with fade
                jump afterkim2ndfuck


    label afterkim2ndfuck:
        scene kiminbed
        kim "Where are you going?"
        main "To work."
        kim "Awww..I'll be waiting, then."
        kim "I'll even cook you dinner."
        stop music
        jump districtattorneyshowsup

label rejectkim:
    show kim angry2 at center
    kim "Like father, like son."
    kim "I hope you don't go down the same path he did."
    main "What do you mean?"
    show kim sad1 at center
    kim "Always chasing a new girl. Trading out the old for someone younger, prettier-"
    main "Are you upset?"
    kim "At first, but not any more."
    kim "I thought I could make it up to the son whose life I ruined."
    hide kim sad1
    main "How?"
    scene kimseduce2
    kim "By giving myself to him."
    kim "Completely."
    kim "One loyal woman."
    if picklisa == True:
        kim "But you want the model don't you?"
        menu:
            kim "Are you sure?"
            "I'm pretty sure.":
                scene kimsapartment
                show kim sad3 at center
                main "I'm going home."
                $cKim.morale_down(2)
                show moraledown at attributedown
                main "Take care, Kim."
                kim "...."
                jump mcgoeshomeafterrejection

            "I don't know.":
                scene kimseduce3
                kim "Then pick me instead."
                kim "Forget about her."
                kim "Just sit back and relax."
                kim "And let me tell you a little story."
                jump kimsdance

    elif pickmai == True:
        kim "But you want to help that poor little secretary, don't you?"
        kim "Her tears got to you, didn't it?"
        menu:
            kim "But you don't have to help her with her burdens, you know."
            "I made a promise.":
                scene kimsapartment
                show kim sad3 at center
                kim "I guess you did."
                $cKim.morale_down(2)
                show moraledown at attributedown
                main "I'm going home."
                main "Good bye, Kim."
                jump mcgoeshomeafterrejection

            "You've got a point.":
                scene kimseduce3
                kim "Relax and have fun with me instead."
                kim "You don't have to worry about immigration papers or anything."
                kim "We can have all the fun right here, right now."
                jump kimsdance

    else:
        scene kimseduce3
        kim "Or did you fancy the fat cow?"
        kim "Or the rich girl?"
        kim "Such odd tastes..when there's me."

        menu:
            kim "Forget them and stay with me, [player_name]."
            "No thanks.":
                scene kimsapartment
                show kim sad3 at center
                $cKim.morale_down(2)
                show moraledown at attributedown
                kim "..."
                main "I'm leaving, good night Kim."
                jump mcgoeshomeafterrejection

            "Just for tonight.":
                kim "Very well then."
                kim "How about I tell you a little story."
                jump kimsdance

label mcgoeshomeafterrejection:
    stop music
    scene mcsapartment with fade
    "(Glad I got away from her.)"
    if pickmai == True:
        scene mchomealone4
        "(My phone's buzzing.)"
        "(It's Mai.)"
        main "Hello?"
        scene mchomealone3
        mai "Hi, [player_name], are you home?"
        main "Yeah, I am, why? Are you home?"
        mai "No, I'm outside your door."
        main "You-you are?"
        main "I'll answer the door then."
        jump maicomesover
    elif picklisa == True:
        scene mchomealone4
        "(My phone's buzzing.)"
        "(It's Lisa.)"
        main "Hello?"
        scene mchomealone3
        lisa "Hey [player_name], how are you?"
        main "I'm fine. I'm at home, and you?"
        lisa "Hehe."
        main "What's wrong?"
        lisa "Oh, I just- I'm actually outside your door."
        main "You- you are?"
        lisa "Yeah, I couldn't stop thinking about what you said earlier."
        lisa "Do you mind if I stay the night?"
        main "Sure, sure."
        jump lisacomesover
    else:
        menu:
            "(Should I make up with Lisa or Mai?)"
            "Make up with Lisa":
                scene mchomealone3
                lisa "Hello?"
                main "Hey Lisa, it's me, [player_name]."
                lisa "Oh, hey."
                main "I'm sorry about earlier."
                main "I was too stunned with what happened."
                lisa "Yeah, I guess we did put that decision on you."
                main "I want to make it up with you."
                lisa "Really?"
                main "Yeah. Come over, you remember how to get here, right?"
                lisa "Yeah, I do."
                $picklisa = True
                jump lisacomesover

            "Make up with Mai":
                scene mchomealone3
                mai "Hello?"
                main "Mai, it's me, [player_name]."
                mai "Oh, hi [player_name]."
                main "I'm sorry about earlier- I was confused."
                mai "It's ok, [player_name]."
                mai "Is that why you called me? To apologize?"
                main "And to invite you over."
                mai "Oh...I will be over shortly."
                $pickmai = True
                jump maicomesover

            "Don't make up with either of them.":
                scene mchomealone3
                "(None of them are worth my time.)"
                "(I have other things on my mind.)"
                "(Like the cryptocurrency.)"
                "(I'll call it a night, then.)"
                jump districtattorneyshowsup

label lisacomesover:
    play music "music/track12.ogg"
    scene mcskitchen
    show lisa smile2 at center
    lisa "Hey [player_name]."
    show lisa sad3 at center
    lisa "I'm sorry for yelling at you earlier today."
    lisa "I can have a short temper at times."
    lisa "I just can't stop thinking about you."
    main "I'll make sure not to make you angry, Lisa."
    show lisa flirt4 at center
    lisa "So is there any way I can make up for that?"
    lisa "I know you said dinner and a movie.."
    main "A private show?"
    show lisa flirt2 at center
    lisa "Is that what you want?"
    $cLisa.morale_up(4)
    show moraleup at attributeup
    main "Why would I want anything else?"
    lisa "You have a point."
    if persistent.sexscenes == False:
        scene black with fade
        jump afterlisa2ndfuck
    else:
        scene 1lisasex1
        lisa "I used to be really dramatic."
        lisa "But the Girlfriend Experience was the most popular."
        scene 2lisasex1
        lisa "So something like this."
        lisa "You must have had a long day, [player_name]."
        menu:
            lisa "How can I help you relax?"
            "A footjob":
                main "Your feet."
                scene 3lisasex1
                lisa "My feet?"
                scene 4lisasex1
                lisa "So you're a feet guy, [player_name]."
                scene lisafootjob
                lisa "Don't worry, it's our little secret."
                jump afterlisa2ndfuck

            "Just stay right here.":
                lisa "Huh?"
                jump lisadoggysex

label lisadoggysex:
    scene lisadoggy
    menu:
        "View 2":
            jump lisadoggysex2
        "View 3":
            jump lisadoggysex3
        "Finish":
            jump afterlisa2ndfuck

label lisadoggysex2:
    scene lisadoggyv2
    menu:
        "View 1":
            jump lisadoggysex
        "View 3":
            jump lisadoggysex3
        "Finish":
            jump afterlisa2ndfuck

label lisadoggysex3:
    scene lisadoggyv4
    menu:
        "View 1":
            jump lisadoggysex
        "View 2":
            jump lisadoggysex2
        "Finish":
            jump afterlisa2ndfuck


label afterlisa2ndfuck:
    scene lisainbed
    lisa "Sleep tight."
    scene black with fade
    "(She's sleeping. I won't disturb her.)"
    "(I need to get to the office.)"
    stop music
    jump districtattorneyshowsup

label maicomesover:
    play music "music/track12.ogg"
    scene mcskitchen
    show mai smile1 at center
    main "Hello Mai."
    mai "Hi, [player_name]."
    main "What are you doing here this late at night?"
    mai "I came to see you of course."
    $cMai.morale_up(4)
    show moraleup at attributeup
    main "Thanks I-"
    show mai sad5 at center
    mai "Is something wrong?"
    show mai cynic1 at center
    mai "Do you need another massage?"
    main "No, actually this time I'll give you a massage."
    if persistent.sexscenes == False:
        scene black with fade
        jump aftermai2ndfuck
    else:
        show mai smile5 at center
        mai "Oh?"
        main "Yeah, sure. Make yourself comfortable on the bed."
        show mai curious2 at center
        mai "Comfortable?"
        scene 1maisex1
        mai "Like this?"
        mai "I don't think you're in the mood for a massage, [player_name]."
        mai "I think you want to see my feet again, right?"
        scene 2maisex1
        mai "Right???"
        main "Yes, I do."
        mai "You're so adorable, [player_name]."
        mai "I'll just sit here like this so you can enjoy them."
        scene 3maisex1
        mai "Here's a better view."
        scene 4maisex1
        mai "[player_name]?"
        scene maisidefuck
        mai "{cps=*0.5}[player_name].....{/cps}"#slow this down
        scene maisidefuckv2
        mai "{cps=*0.2}[player_name]....{/cps}"
        scene 6maisex1
        mai "So that's what you want."
        mai "You're so simple, [player_name]."
        scene 7maisex1
        mai "Sometimes I think you're a virgin."
        mai "Or you don't want know what you want."
        scene 8maisex1
        mai "Do you want me, [player_name]?"
        mai "Like this?"
        scene 9maisex1
        mai "Or like this?"
        scene 10maisex1
        mai "You're showing again. Don't take too long."
        scene 11maisex1
        mai "So you do like to smell feet!"
        jump aftermai2ndfuck

label aftermai2ndfuck:
    scene maiinbed
    mai "[player_name]."
    mai "I love you, [player_name]."
    scene mcsapartment with fade
    "(I need to head to the office.)"
    stop music
    jump districtattorneyshowsup

label districtattorneyshowsup:
    play music "music/track2.ogg"
    scene outsideoffice
    "(There's someone inside the building.)"
    "(They don't look familiar.)"
    scene investigatoratoffice1
    "(Who is she?)"
    districtattorney "Mr.Shilling?"
    main "Yes, that's me. Welcome to Shillin-"
    scene investigatoratoffice2
    districtattorney "We have a search warrant, for both digital and paper files."
    main "What do you mean? What's going on?"
    scene investigatoratoffice3
    districtattorney "We're doing an investigation regarding tax evasion and money laundering."
    with smallshake
    "(WHAT?!)"
    scene  investigatoratoffice4
    districtattorney "I do hope you will cooperate with us, Mr. Shilling. My men will be here shortly."
    main "Sure, sure. I'll tell my employees."
    scene black with fade
    "(I need to get in touch with dad...but how?)"
    "(This is not what I agreed to!)"
    stop music
    jump chapter5end

label chapter5end:
    play sound "sfx/misc_sound.ogg"
    show chapter5titleend with easeinright:
        yalign 0.4
        alpha 0.5
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0

    stop sound

label fifthending:
    play music "music/track11.ogg"
    scene mchomealone1
    "(What do I do now?)"
    play sound "sfx/cellvibe.ogg"
    "(Who is calling me this late at night?)"
    scene mchomealone2
    stop sound
    "Hello?"
    unwoman "You finally picked up the phone, [player_name]."
    scene mchomealone3
    "{size=+10} MOM?!?!!?!?{/size}"
    with smallshake
    mom "So, your dad put you into a bind."
    mom "I'm flying in next week."
    mom "You're going to need my help."
    stop music
    jump chapter6
