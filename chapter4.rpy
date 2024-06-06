label chapter4:
    scene upstairsdesk
    "(I have a few days before the auditor comes back.)"
    play music "music/track12.ogg"
    menu:
        "(What should I do.)"
        "Call Lisa to go workout" if lisaworkoutinvite == True and lisaworkout == False:
            main "Lisa?"
            show lisaphone at topright
            lisa "[player_name]?"
            lisa "Is there something you need?"
            main "Did you want to workout after work?"
            lisa "Sure!"
            lisa "You don't have to stay late, do you?"
            lisa "The closest gym is far away."
            main "There's a gym at my place."
            main "We can workout there."
            lisa "I don't have my workout clothes on me."
            main "Take an extended lunch break to get them."
            lisa "Sure, [player_name], see you there."
            hide lisaphone
            jump workoutwithlisa

        "Participate in Kim's camshow" if kimcaminvite == True and kimshow == False:
            "(I do have some free time.)"
            show kimphone at topright
            main "Kim?"
            kim "Everyone will be gone after 6 p.m."
            kim "You can come to my office then."
            main "I have something to ask you Kim."
            kim "Yes? What is it?"
            main "Did you watch the news last night?"
            kim "No, I didn't. Why?"
            main "Someone got arrested for bribery."
            kim "And?"
            main "They worked for the tax office."
            kim "Oh. Oh dear."
            main "kim maybe we should-"
            kim "Are you still coming down here?"
            menu:
                kim "Or are you going to wallow in misery?"
                "I'll be down there.":
                    kim "Good."
                    kim "Let's forget about our troubles for one night."
                    hide kimphone
                    jump joinkimsshow
                "No, this is important.":
                    main "What if he's the reason why the auditor came early?"
                    kim "That's your problem, not mine, [player_name]."
                    kim "You killed the mood."
                    kim "I just don't feel like it tonight."
                    "(She hung up.)"
                    "(Great.)"
                    hide kimphone
                    jump chapter4


        "Request something from Mai":
            "(I need all of the tax forms.)"
            "(I'll ask Mai to get them.)"
            show maiphone at topright
            main "Mai?"
            mai "Yes, [player_name], did you need something?"
            main "I need all of the tax forms. From when the company started to now."
            mai "Tax forms?"
            main "Yes."
            mai "Hmm ok. It will take a while. Do you need anything else?"
            main "And sales reports. I need that as well."
            mai "You ask for so much, [player_name]."
            main "I need it before the auditor comes."
            mai "Very well, I will get them for you."
            hide maiphone
            "(Now to wait.)"
            if lisatalk == True and lisaworkout == False:
                menu:
                    "(Maybe I should invite Lisa to workout.)"
                    "Yes":
                        main "Lisa?"
                        show lisaphone at topright
                        lisa "[player_name]?"
                        main "I wanted to follow up on that workout offer."
                        lisa "Really?"
                        lisa "I don't have my gym clothes on me and the closest gym is far from here."
                        main "There's a gym at my place, we can go there."
                        main "You can take an extended lunch break to get your clothes."
                        lisa "Really? Thanks."
                        main "See you after work."
                        hide lisaphone
                        jump workoutwithlisa
                    "No":
                        jump kim2ndcheck
            else:
                jump kim2ndcheck

    label kim2ndcheck:
        if kimtalk==True and kimshow == False:

            menu:
                "(I should check up on Kim and ask how she is doing.)"
                "Yes":
                    main "Kim?"
                    kim "Did you need something from me, [player_name]?"
                    main "How are you?"
                    kim "You called me to ask how I'm doing?"
                    kim "I'm terribly lonely, [player_name]."
                    kim "Come join me tonight."
                    menu:
                        "Agree":
                            kim "I'll be waiting after all of the girls leave."
                            jump joinkimsshow

                        "Refuse":
                            kim "Then stop calling me."
                            jump sleepuntilmaicomes
                "No":
                    jump sleepuntilmaicomes
        else:
            jump sleepuntilmaicomes



    label sleepuntilmaicomes:
        show screen eyeclosing
        "I'll just take a nap."
        hide screen eyeclosing
        jump maicomeswiththepapers

#Lisa -------------------
    label workoutwithlisa:
        scene gym with fade
        "(Well I'm here. Lisa is taking her time getting dressed.)"
        scene lisagym1
        lisa "Hey, [player_name]."
        main "Ready to start?"
        lisa "Not really. I think I'll take it easy today."
        $lisaworkout = True
        lisa "You liar."
        main "Hmm?"
        scene lisagym2
        menu:
            lisa "You look like you live here."
            "Well, I do live here.":
                $charm.trait_up(3)
                show charmup at attributeup
                main "In this apartment building."
                scene lisagym3
                lisa "....."
                lisa "Ok, you got me there. Still, I don't see a beer belly anywhere."
                main "It's there, I'm just not showing it to you."
                lisa "Fair enough."
                jump startworkingout

            "What do you mean?":
                lisa "You work out here every day, don't you?"
                main "Not since I started working."
                main "I've also been eating a lot of takeout- pizza, Chinese."
                lisa "Oh. You still look great, though."
                main "As do you."
                lisa "Please."
                jump startworkingout

    label startworkingout:
        scene lisagym10
        lisa "Is the gym usually this quiet?"
        main "Yeah, except for New Year's. Then it gets really crowded for two weeks."
        lisa "New Year's Resolution people. I think it's the same everywhere."
        main "Why do you ask?"
        lisa "It's a lot better than the gym I used to go to."
        lisa "I hope membership isn't that expensive."
        scene lisagym5
        main "I can see if I can add a company plan."
        lisa "Haha, thanks."
        lisa "But.."
        main "What?"
        lisa "There won't be a company much longer, will there, [player_name]?"
        main "What do you mean? "
        scene lisagym6
        lisa "I saw the news last night."
        lisa "And this morning, you looked really stressed out."
        label asklisaquestions3:
            lisa "Between the two of us, is there anything on your mind?"
            menu:
                "This entire business":
                    main "It feels like one big scam."
                    main "Do you even talk to customers?"
                    scene lisagym7
                    lisa "I-I-"
                    lisa "I talk to the investors as well."
                    lisa "I convince them not to pull their money out of the company."
                    lisa "I promise a good return on their investment."
                    lisa "We're not publicly listed, so it's a matter of blind faith."
                    lisa "And the financial records, of course."
                    lisa "But usually, in scams, the business is {i} bleeding {/i} money. Not making more."
                    main "You're right."
                    main "I'm missing something. Something important."
                    jump asklisaquestions3

                "Bella":
                    scene lisagym8
                    lisa "Bella?"
                    lisa "She's an..oddball."
                    lisa "A genius, but an oddball."
                    main "Yeah. Why did my dad hire her."
                    if bellatape == True:
                        main "He mentioned something about a cryptocurrency."
                        lisa "Aren't those things scams?"
                        main "Fifteen years ago, maybe. Now? They're mainstream. Even big investment banks are cashing in."
                        lisa "Are we making it? Or buying and reselling it?"
                        main "I don't know, I will have to ask her."
                        jump asklisaquestions3
                    else:
                        lisa "Bella rarely talks to anyone."
                        lisa "She's usually on her computer all of the time."
                        lisa "Watching the stock market."
                        main "The stock market?"
                        lisa "Currencies, to be exact."
                        lisa "It's all a bunch of graphs to me."
                        lisa "But Bella is glued to the screen."
                        main "Hmm, you might be onto something."
                        lisa "You'll have to ask her yourself."
                        lisa "Maybe she's re-investing the money into penny stocks."
                        main "That makes things even more suspicious."
                        jump asklisaquestions3

                "Why you take this job.":
                    main "You could have gone back to webcamming."
                    scene lisagym9
                    lisa "Hah, well. I was blacklisted. I still am."
                    main "From every website?"
                    lisa "Just the major ones. The ones that bring in a lot of money."
                    lisa "Sure I had a few diehard fans, but most of my customers just went to another girl."
                    lisa "So it was normal, boring jobs for me."
                    main "My dad was one of those diehard fans, wasn't he?"
                    lisa "Yeah, he was."
                    lisa "I was so worried that he was going to ask for a private show, but he didn't."
                    main "He didn't?"
                    lisa "No. He just gave me the job. He said he felt sorry for me."
                    lisa "He offered a good salary and on the job training so I couldn't refuse."
                    lisa "And it was all for one big scam."
                    jump asklisaquestions3

                "I have nothing else left to ask":
                    scene lisagym6
                    lisa "Whew, that was an exhausting workout."
                    lisa "Time to go take a shower."
                    jump incelapproacheslisa


    label incelapproacheslisa:
        scene lisagym12
        incel "Hey babe, you need a hand up?"
        lisa "No, I'm fine, thanks."
        incel "Wow, are you a model?"
        scene lisagym13
        lisa "No. I wouldn't be here if I was."
        menu:
            incel "Are you by yourself? Do you need someone to walk you home?"
            "Let Lisa handle it":
                $authority.trait_down(1)
                show authoritydown at attributeup
                scene lisagym14
                lisa "I'm with a friend of mine."
                incel "Yeah, where is that friend of yours?"
                lisa "He's right there."
                scene lisagym15
                incel "Oh."
                incel "You're better off with me."
                scene lisagym16
                incel "Unless you don't like short guys."
                incel "Your loss."
                jump lisaworriedabouttheincel

            "  Intervene":
                $authority.trait_up(1)
                show authorityup at attributeup
                main "She's with me."
                scene lisagym15
                incel "Oh really?"
                incel "You're that rich kid, aren't you?"
                scene lisagym16
                incel "Gold digger."
                scene lisagym17
                show moraleup at attributeup
                $cLisa.morale_up(2)
                lisa "Thanks [player_name]."
                jump lisaworriedabouttheincel


    label lisaworriedabouttheincel:
        scene lisagym25
        main "Something wrong?"
        lisa "That guy..he makes me feel a little uneasy."
        menu:
            lisa "He looks like the type of guy that..you know.."
            "Want me to put him in his place?":
                scene lisagym26
                $authority.trait_up(2)
                show authorityup at attributeup
                main "Go ahead and get changed."
                main "I'll make sure that he doesn't see you leave."
                show moraleup at attributeup
                $cLisa.morale_up(1)
                lisa "Oh-yeah, thanks, [player_name]. See you tomorrow."
                scene lisagym21
                main "Hey, you."
                incel "What do you want?"
                main "I saw the way you were looking at her."
                scene lisagym22
                incel "Oh yeah? Maybe she's better off with a nice guy like me than you."
                incel "You probably got the whole world handed to you on a silver plate."
                incel "You never had to work a day in your whole life!"
                main "I don't think you're know what I'm capable of."
                scene lisagym19
                main "{size=-5}Want to find out?{/size}"
                scene lisagym24
                incel "Get-get-get away you from me!"
                main "You bother her again and you won't get another chance at anything."
                incel "Mo- fine."
                scene gym
                "(Looks like Lisa is gone.)"
                "(I should call her.)"
                scene mcsapartment
                main "Lisa?"
                lisa "[player_name]?"
                main "Where are you? Are you home?"
                lisa "Ah, I'm just waiting at the bus stop."
                lisa "It should be here in 10 minutes."
                menu:
                    " Offer to spend the night at your place.":
                        $charm.trait_up(2)
                        show charmup at attributeup
                        main "If you don't feel safe you can spend the night at my place."
                        lisa "Really?"
                        main "Yeah. Don't worry though, that guy won't bother you on the way back."
                        main "I'm in Apartment 2005."
                        lisa "Sure, I'll be there."
                        jump lisacomestomcsapartment

                    "Wish her good night.":
                        main "Good night, Lisa."
                        main "Don't worry about that guy."
                        lisa "If something happens, I'll call."
                        main "Nothing will, but I'll pick up if you do."
                        scene black with fade
                        "(That was a nice workout.)"
                        "(Plus I have extra information to ask Bella.)"
                        jump chapter4


            "Want to spend the night at my place?":
                scene lisagym26
                $charm.trait_up(4)
                show charmup at attributeup
                lisa "What?"
                main "I don't know how far it is from your place, so you can spend the night at mine."
                lisa "What-oh-oh sure."
                main "Here's my spare key. Apartment 2005. I just need a quick word with the guy."
                show moraleup at attributeup
                $cLisa.morale_up(1)
                lisa "Yeah, thanks [player_name]."
                main "Hey, you."
                scene lisagym21
                menu:
                    incel "Yeah, what do you want?"
                    "  Don't go near her.":
                        scene lisagym22
                        $authority.trait_up(2)
                        show authorityup at attributeup
                        incel "Who said I was?"
                        main "I know that look."
                        scene lisagym23
                        incel "Hey, just because you've had everything given to you by your rich dad doesn't mean you can bully others."
                        incel "Besides, you're just going to dump her for a hotter girl anyway."
                        scene lisagym19
                        main "{cps=*0.5}Leave. Her. Alone.{/cps}"
                        main "That goes for any of my employees."
                        main "If you do, I won't go to the police. I'll come directly for you."
                        main "Is that understood?"
                        scene lisagym24
                        incel "Yeah, I got it, sheesh."
                        main "Good."
                        "(Now to go upstairs.)"
                        jump lisacomestomcsapartment

                    "Just giving you a friendly warning.":
                        scene lisagym20
                        $charm.trait_up(1)
                        $authority.trait_up(1)
                        show authorityup at attributeup
                        main "Don't mess with her."
                        incel "I wasn't planning on it. Unless you want to-"
                        show charmup at attributeup
                        scene lisagym19
                        main "No."
                        incel "Woah, woah I don't swing that way!"
                        incel "I won't go near her, sheesh."
                        scene lisagym24
                        incel "Typical jerk."
                        "(Time to go meet Lisa upstairs.)"
                        jump lisacomestomcsapartment



    label lisacomestomcsapartment:
        play music "music/track9.ogg"
        scene 9lisaprivate1
        lisa "Wow, nice place."
        main "You found your way up here easily."
        lisa "Yeah, there was no one in the lobby or elevator."
        scene 12lisaprivate1
        main "Is something wrong?"
        lisa "I think I hit something with my foot."
        main "Want me to check it out?"
        lisa "Yeah, sure."
        scene lisatoewigglev2
        main "Doesn't look broken, but I'll give it a massage."
        lisa "Thanks."
        main "What are your plans?"
        scene 17lisaprivate1
        lisa "Hmm, what do you mean?"
        main "Well..there's a possibility I might have to dissolve the company so-"
        scene 5lisaprivate1
        lisa "Gee, I never really thought about that."
        lisa "Hmm...maybe I'll go back to school."
        lisa "Getting an actual degree would be nice."
        main "In what?"
        scene 2lisaprivate1
        lisa "Marketing, probably. Although I would love to get into fashion school."
        lisa "I can't be a model, so why not work for a fashion agency?"
        main "I'm sure you can get in."
        lisa "I just wonder if I'm too old."
        main "No- never-"
        scene 18lisaprivate1
        main "Lisa?"
        lisa "Hahahha,  you're tickling me."
        main "Like this?"
        scene 7lisaprivate1
        lisa "Stop! That's not fair!"

        menu:
            lisa "Do you have some sort of tickling fetish?"
            "Yes.":
                $charm.trait_up(1)
                show charmup at attributeup
                lisa "Bully."
                main "But I can stop tickling your feet if you want to."
                lisa "Please."
                main "I'll just tickle you elsewhere."
                jump tacklinglisa

            "No, but it's fun to see you laugh.":
                $charm.trait_up(2)
                show charmup at attributeup
                lisa "Hehe.."
                lisa "Well not my feet."
                lisa "It just feels weird."
                main "Then how about here?"
                jump tacklinglisa

            "Actually, I have a foot fetish." if footlover == True:
                $charm.trait_up(1)
                show charmup at attributeup
                lisa "Mai told me about that."
                lisa "I thought she was a bit crazy, but I guess she isn't."
                lisa "Still unfair to take advantage of me, though."
                main "You didn't have fans with a foot fetish?"
                lisa "I did, but you're my boss."
                main "...I'm sorry, I won't tickle you again."
                lisa "Is it just tickling or?"
                main "No, it's a lot more."
                lisa "What do you mean?"
                jump smellinglisasfeet


    label smellinglisasfeet:
        scene 16lisaprivate1
        lisa "Wow, I.."
        main " What?"
        scene lisatoewiggle
        lisa "So you have a sniffing fetish?"
        main "And?"
        main "Are you going to tell Mai?"
        $lisafoot = True
        lisa "No, no. This is between you and me."
        lisa "So that's why so many of my fans wanted to buy my socks."
        main "They do smell nice."
        scene 34lisaprivate1
        lisa "They also wanted my panties."
        main "Did you sell them?"
        lisa "Hell no, I didn't want to get in trouble selling panties."
        lisa "It's illegal here."
        main "Or maybe you're too embarrassed."
        lisa "Hey-"
        scene 27lisaprivate1
        main "It smells good here too."
        lisa "Hehehehe"
        scene 35lisaprivate1
        main "What's wrong?"
        lisa "We uh...shouldn't be doing this."
        scene 14lisaprivate1
        menu:
            "I'll stop, then.":
                menu:
                    lisa "........"
                    "I can keep going if you like.":
                        scene 33lisaprivate1
                        lisa " We won't get in trouble for this?"
                        main "As long as you don't tell."
                        lisa "I won't."
                        main "It'll be our secret."
                        lisa "But I feel really ...dirty."
                        main "Well, let's take a shower then."
                        jump lisaandmcshowertogether

                    "You're right. We shouldn't do this.":
                        main "There are extra towels,soap, and washcloths underneath the sink."
                        scene 12lisaprivate1
                        $cLisa.morale_up(1)
                        show moraleup at attributeup
                        lisa "Thanks, [player_name]."
                        main "Let's just forget that this happened, ok?"
                        lisa "Sure. It's our secret."
                        jump lisatakesshoweralone

            "Well, we are.":
                scene 8lisaprivate1
                $charm.trait_up(1)
                show charmup at attributeup
                lisa "What will the other girls say?"
                menu:
                    lisa "They'll probably think I'm a slut."
                    "They won't say anything if you don't tell.":
                        scene 9lisaprivate1
                        lisa "You have a point there."
                        lisa "I-I just don't want to give you the impression that I'm...you know.."
                        main "Trying to get a raise doing this?"
                        lisa "Yeah."
                        main "Well, you're not."
                        main "Getting a raise, that is."
                        lisa "Oh..that's reassuring."
                        lisa "Still..I feel so dirty.."
                        scene 12lisaprivate1
                        main "Want to take a shower?"
                        lisa "Together?"
                        main "More efficient."
                        lisa "....Yeah, sure."
                        jump lisaandmcshowertogether

                    "Compared to?":
                        scene 9lisaprivate1
                        lisa "......."
                        lisa "You have a point there."
                        lisa "I mean Bella is odd, Kim fucked John regularly, the auditor has her tits hanging around everywhere.."
                        lisa "And Mai...she just can't stop talking about you."
                        scene 8lisaprivate1
                        menu:
                            lisa "Still, this feels wrong."
                            "What would be right?":
                                lisa "I don't know, we go out on a normal date, you pay.."
                                main "And we would end up right here."
                                scene 11lisaprivate1
                                lisa "Well, not the sniffing part."
                                main "Then what's next?"
                                lisa "....I think you know."
                                main "The shower it is, then."
                                lisa "I-okay, you win."
                                jump lisaandmcshowertogether

                            "We can stop for now.":
                                scene 12lisaprivate1
                                main "If it makes you uncomfortable, I'll stop."
                                main "There's towels, washcloths, and soap underneath the sink."
                                $cLisa.morale_up(1)
                                show moraleup at attributeup
                                main "Just let me know if you need anything."
                                lisa "Thanks, [player_name]."
                                jump lisatakesshoweralone


    label tacklinglisa:
        scene 29lisaprivate1
        lisa "Eeeeee!!!!!!"
        lisa "Oh my god, stop stop!"
        main "Ok, I'll stop."
        scene 31lisaprivate1
        lisa "......"
        main "What's wrong?"
        lisa "This..all of this is wrong."

        menu:
            lisa "You're my boss, I-"
            "Not for much longer.":
                main "After all, I will probably either dissolve or restructure the company."
                lisa "Can we...wait until then?"
                main "Wait to do what?"
                scene 10lisaprivate1
                lisa "This. I mean-"

                menu:
                    lisa "I just don't want the other girls to think I'm trying to get favors from you."
                    "I can wait":
                        scene 33lisaprivate1
                        main "We can have a real relationship when this all blows over."
                        $cLisa.morale_up(1)
                        show moraleup at attributeup
                        lisa "Thanks, [player_name], I appreciate it."
                        main "There are towels, soap, and washcloths underneath the sink."
                        main "Let me know if you need anything."
                        lisa "Thanks again."
                        jump lisatakesshoweralone

                    "They won't if they don't know":
                        scene 33lisaprivate1
                        lisa "You have a point there."
                        lisa "I just wish things were a bit...natural."
                        main "You mean dinner and a movie?"
                        lisa "Yeah."
                        main "A bit boring, but we can do it next time we workout."
                        scene 8lisaprivate1
                        main "It will still end this way."
                        lisa "...you have a point there."
                        lisa "So what happens next?"
                        main "...A shower."
                        main "I have my limits to being smelly."
                        lisa "Same."
                        jump lisaandmcshowertogether

            "And?":
                scene 8lisaprivate1
                $charm.trait_up(1)
                show charmup at attributeup
                lisa "And we can't do this."

                menu:
                    lisa "I just don't want to be seen as the office slut."
                    "I think someone else fits that description.":
                        scene 12lisaprivate1
                        $cLisa.morale_up(1)
                        show moraleup at attributeup
                        lisa "It'll be me if we keep doing this."
                        main "Fine. There's towels, soap, and washcloths underneath the sink."
                        lisa "Thanks, [player_name]."
                        jump lisatakesshoweralone

                    "No, you won't.":
                        scene 33lisaprivate1
                        main "We can keep this a secret."
                        main "Pretend like this didn't happen."
                        main "Come on, we're both stressed."
                        lisa "You're right, [player_name]."
                        lisa "I do wish I was a little cleaner, though."
                        main "Shower?"
                        lisa "I knew you would suggest that."
                        lisa "Sure."
                        jump lisaandmcshowertogether


    label lisaandmcshowertogether:
        scene lisashower1
        $lisashowerfuck = True
        $charm.trait_up(2)
        show charmup at attributeup
        lisa "[player_name]."
        main " ? "
        lisa "You liar."
        main "Huh?"
        scene lisashower3
        lisa "You're ripped."
        lisa "No beer belly at all."
        main "Trying to kill the mood are you?"
        lisa "No-no I just had to say it-"
        if persistent.sexscenes == False:
            jump aftershowersex

        else:
            jump lisashowersex

    label lisashowersex:
        scene lisashowersex
        menu:
            "View 2":
                jump lisashowersex2

            "View 3":
                jump lisashowersex3

            "Finish":
                jump aftershowersex

    label lisashowersex2:
        scene lisashowersexv4
        menu:
            "View 1":
                jump lisashowersex

            "View 3":
                jump lisashowersex3

            "Finish":
                jump aftershowersex

    label lisashowersex3:
        scene lisashowersexv3
        menu:
            "View 1":
                jump lisashowersex

            "View 2":
                jump lisashowersex2

            "Finish":
                jump aftershowersex


    label aftershowersex:
        scene lisainbed
        $cLisa.morale_up(3)
        show moraleup at attributeup
        lisa "Wow...Never had that before."
        main "First time for every thing."
        main "I'll go get the towels."
        scene mcsapartment
        main "Lisa..?"
        "(What time is it?)"
        "(It's 7:00 am!)"
        "(There's a note here.)"
        show lisanote at fromtheleft
        "{color=#ffccee}Hey, [player_name], thanks for letting me stay over last night. I really enjoyed it.
        {p}I promise I won't lead you on again. It's been a long time since I've had any fun.
        {p}Sincerely, Lisa.{/color}"
        hide lisanote
        scene black with fade
        "(Well, time for me to take a shower.)"
        "(I just hope she won't tell anyone. It will make things worse at the office.)"
        stop music
        jump chapter4

    label lisatakesshoweralone:
        scene mcsapartment
        "(I'll go lay on the couch.)"
        "(I don't want to make her any more uncomfortable.)"
        lisa "[player_name]?"
        main "Yes?"
        lisa "The water isn't getting warm!"

        menu:
            lisa "I'm freezing in here!"
            "Wait a few minutes":
                main "It's a bit slow, but it does get warmer."
                lisa "Ok."
                scene mcsbed
                main "Lisa?"
                "(Crap, what time is it?)"
                "(It's 7:30...did Lisa leave while I was asleep?)"
                "(Hm...there's a note.)"
                show lisanote at fromtheleft
                "{color=#ffccee}Hey, [player_name]. Thanks for letting me stay over for the night. You slept like a baby and I didn't want to wake you up.
                {p}I ...want to do this again, but not when you're still my boss.
                {p}Lisa{/color}"
                hide lisanote
                scene black with fade
                "(Well, at least she's not angry at me.)"
                "(Guess I'll take a shower and get back to work.)"
                stop music
                jump chapter4

            "Let me check it out.":
                scene lisashower2
                main "You don't look cold."
                lisa "I am. Come join me, [player_name]."
                menu:
                    "Join her":
                        jump lisaandmcshowertogether

                    "Refuse":
                        main "I'm ok."
                        lisa "Aww."
                        "(I'll wait here on the couch.)"
                        scene mcsbed
                        main "Lisa?"
                        "(Crap, what time is it?)"
                        "(It's 7:30...did Lisa leave while I was asleep?)"
                        "(Hm...there's a note.)"
                        show lisanote at fromtheleft
                        "{color=#ffccee}Hey, [player_name]. Thanks for letting me stay over for the night. You slept like a baby and I didn't want to wake you up.
                        {p}I ...want to do this again, but not when you're still my boss.
                        {p}Lisa{/color}"
                        hide lisanote
                        scene black with fade
                        "(Well, at least she's not angry at me.)"
                        "(Guess I'll take a shower and get back to work.)"
                        stop music
                        jump chapter4

#Kim ------------------------
    label joinkimsshow:
        scene 5kimtalk
        "You know how to keep a girl waiting."
        scene 1kimtalk
        "My show is almost starting."
        play music "music/track9.ogg"
        scene 4kimtalk
        "Get naked."
        $kimshow = True
        "You heard me, [player_name]."
        scene 6kimtalk
        "Get naked. And stand over there."
        scene 2kimprivate1
        "Welcome to the show. Today I have a special guest with me."
        scene 5kimprivate1
        "So I hope you all will enjoy the show. I know I will."
        scene 12kimprivate1
        "Get on your knees and get behind me."
        scene 11kimprivate1
        "How do I know him? He's a very good friend of mine."
        kim "And he's going to do something you have all dreamed of- pleasing me."
        scene 3kimprivate1
        kim "Be a good boy and lick me."
        kim "{size=-10}Just do it.{/size}"
        scene 4kimprivate1
        kim "I need to unbutton my shirt, I'm getting so hot."
        scene 8kimprivate1
        kim "Ahhh...right there...."
        kim "Do you all want to lick me too?"
        kim "Donate and maybe I'll fly you in for a private show."
        kim "Ah...keep licking..."
        scene 4kimprivate1
        "(What is she doing?)"
        kim "Yes, I'm very close...ahhh..."
        if persistent.timed_choices == True:
            $timeout_label = "kimsquirtsonmc"
            jump kimcumming
        else:
            $timeout_label = None
            jump kimcumming


    label kimcumming:
        menu:
            "Let her cum":
                jump kimsquirtsonmc

            "Pull away":
                jump mcstopstheshow

            "Fuck Her" if authority.amount >= 5:
                jump mcfuckskim


    label kimsquirtsonmc:
        $timeout_label = None
        scene black with fade
        kim "{size=+10}Ahhh yes!!{/size}"
        jump afterkimsquirt


    label afterkimsquirt:
        scene 16kimprivate1
        kim "That..felt so good."
        $kimsquirt = True
        kim "A short break and then it's private time."
        $cKim.morale_up(2)
        show moraleup at attributeup
        kim "Look at you, all soaking wet."

        menu:
            kim "Did you like it?"
            "I didn't expect it.":
                scene 21kimprivate1
                $authority.trait_down(1)
                show authoritydown at attributedown
                kim "But you liked it, right?"
                kim "Well, if you want a more private show after I leave.."
                kim "You know where to find me."
                kim "Don't take it personally, but your tongue could use more work."
                scene black with fade
                "(I can't believe I agreed to do that.)"
                stop music
                jump chapter4

            "I don't see how anyone would pay for this":
                scene 3kimtalk
                kim "You would be surprised."
                kim "I got a good number of tips just from that."
                kim "They all thought about being you."
                "(If only they knew the real Kim.)"
                kim "Though next time you could give a more convincing performance."
                main "I don't plan to perform with you ever again."
                scene 21kimprivate1
                kim "Awww."
                kim "Good night then, [player_name]."
                scene black with fade
                "(I'm never doing that again.)"
                stop music
                jump chapter4

    label mcstopstheshow:
        $timeout_label = None
        scene 17kimprivate1
        kim "Hey- wait, where are you going?"
        main "Don't touch me!"
        kim "Come on, it wasn't going to be that bad."
        main "I think I know what you were going to do."
        main "You can save it for your audience."

        menu:
            kim "Are you really going to leave me hanging, [player_name]?"
            "Yes":
                $cKim.morale_down(2)
                show moraledown at attributeup
                kim "You're no fun."
                main "Fun doesn't consist of pissing on me for cash."
                kim "I wasn't going to piss on you."
                kim "I just get really wet when I cum."
                main "I have my limit and that's it."
                scene 22kimprivate1
                main "Get off of me."
                kim "[player_name]"
                main "I should kick you out of this office right now, but I won't."
                main "I want you gone by next week."
                kim "Yes sir."
                scene black with fade
                stop music
                "(I can't believe she tried to do that.)"
                jump chapter4

            "No":
                kim "....."
                kim "But I'm so close."
                kim "Just a little more for me, please..."
                jump chapter4


    label mcfuckskim:
        $timeout_label = None

        if persistent.sexscenes == False:
            scene black
            kim "What the fuck are you doing?"
            $authority.trait_up(3)
            main "Giving your fans a real show."
            $cKim.morale_up(3)
            $kimfuck = True
            scene 7kimtalk with fade
            main "I think your fans liked it."
            main "Those donations are coming in like crazy."
            scene 7kimprivate1
            kim "FUCK YOU!"
            main "We can go again."
            kim "I should make you eat it."
            main "I rather not."
            scene 8kimtalk
            kim "Son of a bitch."
            scene black with fade
            stop music
            "(That settles that.)"
            "(I will lock up for the night.)"
            jump chapter4

        else:
            scene 9kimprivate1
            kim "What the fuck are you doing?"
            $authority.trait_up(3)
            show authorityup at attributeup
            main "Giving your fans a real show."
            $cKim.morale_up(3)
            kim "No-no, this isn't how it works!"
            scene black
            kim "I'm in charge!"
            main "No, I'm your boss."
            jump kimdoggyoffice

label kimdoggyoffice:
    scene kimdoggy
    menu:
        "View 2":
            jump kimdoggyoffice2

        "Finish":
            jump mccreampieskim

label kimdoggyoffice2:
    scene kimdoggyv2
    menu:
        "View 1":
            jump kimdoggyoffice

        "Finish":
            jump mccreampieskim




label mccreampieskim:
    scene 14kimprivate1
    kim "Mmm...Fuck..."
    scene 18kimprivate1
    kim "Oh..my...god.."
    kim "What did you do?"
    main "Give them a show, of course."
    kim "You..."
    main "I think your fans liked it."
    main "Those donations are coming in like crazy."
    main "That was more fun than licking your pussy."
    scene 7kimprivate1
    kim "FUCK YOU!"
    main "We can go again."
    kim "I should make you eat it."
    main "I rather not."
    scene 8kimtalk
    kim "Son of a bitch."
    scene black with fade
    stop music
    "(That settles that.)"
    "(I'll lock up for the night.)"
    jump chapter4




#Mai--------------------------------
    label maicomeswiththepapers:
        show screen eyeopening
        scene 8maiprivate1
        "[player_name]?"
        "Oh..[player_name]?"
        "How should I wake him up?"
        "Maybe I should do this."
        hide screen eyeopening
        scene 19maiprivate1
        "!!!"
        main "Get off me!!"
        scene black
        with smallshake
        mai "Ahhhhh!!!!"
        with hpunch
        scene 12maiprivate1 with fade
        mai "You look so peaceful when you sleep."
        main "You always catch me when I'm sleeping."
        scene 13maiprivate1
        mai "I don't mind, [player_name]."
        main "So you have the tax forms?"
        mai "Yes, they're right here."
        scene 15maiprivate1
        "(Hmmm...let's see.)"
        mai "Is something wrong,  [player_name]?"
        main "We haven't been paying our share of taxes, that's for certain."
        main "The amount is really low."
        scene 14maiprivate1
        mai "Here are the revenue reports."
        main "Thanks."
        "(Yup, there's extra money coming into the company.)"
        if bellatape == True:
            "(I bet it has something to do with Bella and the cryptocurrency.)"
            "(I will have to question her when she gets back.)"
        else:
            "(I will just have to question Bella when she gets back.)"
            "(She is holding important information.)"
        scene 10maiprivate1
        mai "[player_name]?"
        main "Yes Mai?"
        mai "You look very stressed."

        menu:
            mai "Would you like a massage?"
            "Accept Mai's Offer":
                scene 17maiprivate1
                main "Sure, but not here."
                mai "Oh, where?"
                show moraleup at attributeup
                $cMai.morale_up(2)
                main "My apartment."
                mai "Are you sure?"
                main "I don't want to fall asleep here again."
                mai "Ok, I will get my things."
                main "There is no need to rush."
                main "I need to look at a few more pages."
                main "Mai?"
                scene upstairsdesk
                "(And she's gone.)"
                "(I'll just place a bookmark here.)"
                jump maicomestomcsapartment

            "Refuse Mai's Offer":
                mai "Are you sure, [player_name]?"
                if footlover == True:
                    mai "Unless you want me to do the thing with my feet-"
                    main "No, no."
                    main "This is more important."
                    menu:
                        mai "You will feel better, I promise."
                        "I give in.":
                            scene 16maiprivate1
                            $cMai.morale_up(1)
                            show moraleup at attributeup
                            mai "I knew you would."
                            main "I'll be downstairs shortl-"
                            scene upstairsdesk
                            "(And she's gone.)"
                            "(Well, I'll put something here and read the rest tomorrow.)"
                            jump maicomestomcsapartment

                        "No is no":
                            scene 18maiprivate1
                            mai "Aww, ok."
                            if lisafoot == True:
                                $cMai.morale_down(1)
                                show moraledown at attributedown
                                mai "You like Lisa better don't you?"
                                main "Mai. I just need some space."
                                mai "Fine, good night, [player_name]."
                                scene upstairsdesk
                                "(Why did she have to rub it in like that..)"
                                "(Back to these reports.)"
                                "(Ugh, I'm getting so sleepy.)"
                                "(I'll read the rest tomorrow.)"
                                jump chapter4end
                            else:
                                $cMai.morale_down(1)
                                show moraledown at attributeup
                                mai "Ok, [player_name]."
                                mai "Another time?"
                                main "Sure, sure."
                                mai "Good night, [player_name]."
                                scene upstairsdesk
                                "(She's so persistent.)"
                                "(But she is right. I can't focus.)"
                                "(I'll just go home and watch some tv.)"
                                jump chapter4end

                else:
                    scene 12maiprivate1
                    mai "it's just a massage, [player_name]."
                    menu:
                        mai "Nothing else."
                        "Fine, you win":
                            scene 17maiprivate1
                            $cMai.morale_up(1)
                            show moraleup at attributeup
                            mai "I'll go get my things."
                            main "We're not leaving right no-"
                            scene upstairsdesk
                            "(And she's gone.)"
                            "(Well I'll just place something where I left off.)"
                            "(I'll continue the rest tomorrow.)"
                            jump maicomestomcsapartment
                        "No.":
                            $cMai.morale_down(1)
                            show moraledown at attributeup
                            mai "Ok then."
                            mai "Good night, [player_name]."
                            scene upstairsdesk
                            "(She's becoming clingy.)"
                            "(And I can't focus on this any more tonight.)"
                            "(I'll leave something here and return to it tomorrow.)"
                            jump chapter4end


    label maicomestomcsapartment:
        play music "music/track9.ogg"
        scene mcsapartment
        main "Home sweet home."
        show mai smile2 at center
        mai "Oh, what a nice apartment you have, [player_name]."
        main "Thanks, Mai."
        $maimassage = True
        mai "You have no roommates?"
        main "No, it's just me. Dad-I mean John- got this apartment for me."
        show mai smile3 at center
        mai "He must care about you to give you such a nice apartment."
        main "Did you want something to drink, Mai?"
        mai "No, no I'm fine, [player_name]."
        main "Is there something wrong, Mai?"
        show mai sad11 at center
        mai "I'm sorry about earlier."
        main "About?"
        mai "Sitting on your table."
        mai "Sitting on your lap."
        mai "I really like you, [player_name]."
        mai "I-"
        show mai sad3 at center
        mai "I don't know how long I can still do this, [player_name]."
        mai "I want to go home. I want to see my family."
        mai "I don't want to work here any more."
        mai "John sponsored me and-and-"
        show mai sad10 at center
        mai "I haven't seen my family in years!"
        main "Shhh. It's ok, Mai."
        main "If you don't want to work here anymore, I'll send you home."
        show mai sad2 at center
        mai "Really?"
        mai "But who will take my spot?"
        mai "I don't think-"
        main "That's for me to figure out, Mai."
        mai "...."
        scene 20maiprivate1
        mai "Thank you, [player_name]."
        mai "You're the first person to really care about me."
        main "So..the massage?"
        scene 5maiprivate1
        mai "Right!"
        main "What is it?"
        mai "Nothing."
        scene 1maiprivate1
        mai "Close your eyes and take deep breaths."
        mai "You have a few pressure points here."
        mai "Let me know if it hurts."
        scene 3maiprivate1
        main "That's the spot, Mai."
        mai "Do you want to lay down?"
        main "Yeah, that would be great."
        scene 2maiprivate1
        mai "Better?"
        main "Much better."
        "(She has really strong hands..)"
        show screen eyeclosing
        scene mcskitchen
        "(But at the same time, they're soft.)"
        hide screen eyeclosing
        show mai smile2 at center
        mai "Did you fall asleep again?"
        main "You're done?"
        show mai smile5 at center
        mai "I finished 15 minutes ago."
        show mai smile8 at center
        mai "Uhm. It's really late, [player_name]."
        mai "I should be going."
        main "What time is it?"
        show mai sad6 at center
        mai "It's after 10 p.m."
        main "No, no, stay here."
        main "You can sleep on the bed, I'll sleep on the couch."
        show mai smile6 at center
        mai "Really?"
        main "Yes."
        main "What's so funny?"
        show mai flirt5 at center
        mai "Nothing.."
        with smallshake
        show mai smile4 at center
        mai "Do you want me to fix that for you?"
        main "How were you going to fix it?"
        show mai serious1 at center
        mai "With my feet, of course."

        menu:
            mai "You like them, don't you?"
            "Yes I do":
                show mai smile4 at center
                $cMai.morale_up(2)
                show moraleup at attributeup
                main "Sure, but just this once."
                hide mai smile4
                jump maisfootjob

            "Your hands are better":
                show mai smile6 at center
                $cMai.morale_up(2)
                show moraleup at attributeup
                mai "My hands?"
                main "That was an amazing massage."
                mai "So you want a handjob?"
                main "Yes, please."
                hide mai smile6
                jump maishandjob

            "How about a blowjob?" if authority.amount >=7:
                show mai smile4 at center
                $cMai.morale_up(1)
                show moraleup at attributeup
                mai "A blowjob?"
                main "If you don't mind."
                mai "I don't."
                hide mai smile4
                jump maisblowjob

            "No, thanks.":
                main "I'll take care of it on my own."
                show mai sad4 at center
                mai "Aww."
                main "There are extra towels,soap and washcloths underneath the sink."
                main "If you need anything else, let me know."
                mai "No, I am fine. Thanks, [player_name]."
                hide mai sad4
                scene maishower1
                "(Wow..she looks so innocent.)"
                "(This feels wrong, I'll go lay on the couch.)"
                main "Sorry, Mai."
                jump chapter4end

    label maishandjob:
        if persistent.sexscenes == False:
            scene black with fade
            mai "How does that feel, [player_name]?"
            main "Great I-"
            mai "You made a mess, [player_name]."
            main "I...needed that."
            main "There are extra towels,soap and washcloths underneath the sink."
            main "If you need anything else, let me know."
            mai "No, I am fine. Thanks, [player_name]."
            jump chapter4end
        else:
            scene maihandjob
            mai "How does that feel, [player_name]?"
            main "Great I-"
            scene maihandjobend
            $maihandjob = True
            mai "You made a mess, [player_name]."
            main "I...needed that."
            main "There are extra towels,soap and washcloths underneath the sink."
            main "If you need anything else, let me know."
            mai "No, I am fine. Thanks, [player_name]."
            stop music
            jump chapter4end

    label maisfootjob:
        if persistent.sexscenes == False:
            scene black with fade
            mai "How does that feel, [player_name]?"
            main "Great I-"
            mai "You made a mess, [player_name]."
            main "I...needed that."
            main "There are extra towels,soap and washcloths underneath the sink."
            main "If you need anything else, let me know."
            mai "No, I am fine. Thanks, [player_name]."
            jump chapter4end
        else:
            scene maifootjob
            mai "How does that feel, [player_name]?"
            scene maifootjobend
            $maifootjob = True
            mai "You made a mess, [player_name]."
            main "I...needed that."
            main "There are extra towels,soap and washcloths underneath the sink."
            main "If you need anything else, let me know."
            mai "No, I am fine. Thanks, [player_name]."
            stop music
            jump chapter4end

    label maisblowjob:
        if persistent.sexscenes == False:
            scene black with fade
            mai "How does that feel, [player_name]?"
            main "Great I-"
            mai "You made a mess, [player_name]."
            main "I...needed that."
            main "There are extra towels,soap and washcloths underneath the sink."
            main "If you need anything else, let me know."
            mai "No, I am fine. Thanks, [player_name]."
            jump chapter4end
        else:
            scene maiblowjob
            menu:
                "Finish":
                    scene maihandjobend
                    mai "You made a mess, [player_name]."
                    main "I...needed that."
                    main "There are extra towels,soap and washcloths underneath the sink."
                    main "If you need anything else, let me know."
                    mai "No, I am fine. Thanks, [player_name]."
                    stop music
                    jump chapter4end




    label chapter4end:
        scene black
        "Whew, that was close."
        play music "music/track10.ogg"
        scene crissyinspect4
        crissy "She's the last one gone. It's a good thing she didn't notice me in the bathroom."
        scene crissyinspect6
        crissy "Now to get to work."
        crissy "I can't believe everyone is so careless."
        scene crissyinspect2
        crissy "I hope I can find something useful."
        stop music
        scene black with fade
        play sound "sfx/misc_sound.ogg"
        show chapter4titleend with easeinright:
            yalign 0.4
            alpha 0.5
            linear 2.0 alpha 1.0
            pause 4.0
            linear 3.0 alpha 0.0
        stop sound
        jump chapter5
