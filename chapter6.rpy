label chapter6:
    scene newsreport
    show chapter6title with easeinright:
        yalign 0.3
        alpha 0.8
        linear 2.0 alpha 1.0
        pause 4.0
        linear 3.0 alpha 0.0
    play music "music/track1.ogg"
    newsreporter "In today's headlines, investigations into Shilling Publishing and Holdings have been completed. Authorities say.."
    "(So they've finished ransacking the entire place.)"
    "(I wonder if they noticed a bunch of files were missing.)"
    play sound "sfx/knocknock.ogg"
    scene mcsdoor
    show crissy serious12 at center
    crissy "Hello, [player_name]."
    stop sound
    crissy "Surprised?"
    main "No."
    show crissy smile11 at center
    crissy "I put on a great performance, didn't I?"
    crissy "These really came in handy."
    main "Why are you here?"
    crissy "Oh, that's right."
    hide crissy smile11
    scene crissypolice1
    crissy "You're under arrest, [player_name] Shilling."
    main "What?"
    crissy "You have the right to remain silent. anything you say can and will be used against you in a court of law."
    main "You can't be seri-"
    scene crissypolice2
    crissy "You have the right to speak to an attorney. If you cannot afford an attorney, one will be appointed for you."
    crissy " Do you understand these rights as they have been read to you?"
    main "Yes but-"
    scene mcsdoor
    show crissy serious11 at center
    crissy "Ok, let's go down to the courthouse then."
    main "Do I have to go?"
    crissy "Yes, [player_name]. Iris was going to get a whole squad to take you down there, but I said I could do it by myself."
    main "Iris?"
    crissy "The District Attorney, my superior. The one who turned your place upside down."
    main "No, that was you."
    show crissy angry9 at center
    crissy "I just gave her the starting evidence. She did the rest."
    main "And you don't feel guilty or anything? Knowing that I was new?"
    show crissy sad11 at center
    crissy "Well.."
    show crissy sad12 at center
    crissy "A little, but we've been investigating your company for years."
    crissy "We just needed a breakthrough."
    crissy "And you were it."
    show crissy serious11 at center
    crissy "Look, Iris wants to throw the book at you-"
    main "The book?"
    show crissy serious10 at center
    crissy "She has a lot of charges and she wants you guilty on all of them."
    crissy "But the judges can be lenient."
    show crissy sad12 at center
    crissy "Just...think about your options, ok, [player_name]."
    main "Yeah, I've definitely had a lot of options since I got here!"
    crissy "Let's go then. Oh, make sure you have your wallet with you. To post bail."
    main "I have a question, Christina."
    show crissy angry10 at center
    crissy "It's Officer McNeill."
    main "Does your boss know what you did? In my office?"
    show crissy angry11 at center
    crissy "..You shouldn't be talking."
    main "Maybe I should. I really don't think whoring is part of your job description."
    show crissy serious10 at center
    crissy "Shut up. Let's go before I call backup."
    main "I really hope you don't lose your job after I tell the judge what you did."
    show crissy angry11 at center

    menu:
        crissy "You know you are threatening an officer of the law, right?"
        "Am I?":
            show crissy angry12 at center
            $authority.trait_up(4)
            show authorityup at attributeup
            crissy "Yes, you are."
            main "Why are you frightened? I'm in handcuffs."
            show crissy sad11 at center
            crissy "I-I-"
            main "So your boss {i}doesn't{/i} know."
            show crissy serious12 at center
            crissy "It should stay that way."
            crissy "Like I said when we first met, I'm willing to do anything to get what I want."
            main "It would be a shame if I confessed everything to the judge-"
            show crissy sad11 at center
            crissy "Please don't. Just cooperate. I really need this for my promotion."
            crissy "Please, [player_name], I'm begging you."
            crissy "Let's go."
            stop music
            jump mcfirstappearance

        "A bad one at that.":
            show crissy serious10 at center
            $authority.trait_up(2)
            show authorityup at attributeup
            crissy "A bad one? I don't harm or injure anyone while wearing the badge-"
            main "But you spread your legs and flash your tits when you don't."
            main "I don't know how anyone takes you seriously."
            show crissy smile10 at center
            crissy "Well they do. And thanks to me, I ended a decade-long investigation."
            crissy "Maybe a bit of unorthodoxy can go a long way."
            stop music
            jump mcfirstappearance


label mcfirstappearance:
    scene mcfirstappearance
    play music "music/track6.ogg"
    judge "My name is Judge Marshall and I am the judge of this Court. I am here to give you the warnings required by law."
    judge "I am to inform you of the allegations made against you,"
    judge "To inform you of the range of punishment for the crime with which you have been charged, AND"
    judge "To set bail for you."
    judge "This is not an arraignment, and I cannot hear your plea or hear any testimony regarding the alleged offense."
    judge "That will take place when you are arraigned."
    judge "Are you [player_name] Shilling?"
    main "Yes."
    judge "You are alleged to have committed the offense of embezzlement, tax fraud and money laundering."
    judge "The range of punishment for the offenses stated is a fine of 500 000, confinement in jail for 5 years or both. "
    judge "Do you understand the allegation against you and the full range of punishment for this offense?"
    main "Yes."
    judge "You have the following rights:"
    "(This again. Just get it over with.)"
    judge "Do you understand these rights?"
    main "Yes."
    judge "Then please sign this document."
    judge "Do you want a court-appointed attorney?"
    main "No."
    judge "Just a few more questions so I can set bail."
    main "I-"
    crissy "Your Honor, the questions about [player_name]'s financials is on the second page."
    "(She's been watching the entire time?)"
    judge "Oh, oh yes, my apologies."
    judge "[player_name] Shilling, your bail is set at $10,000. If you have a method of paying the bond now, you can do as after court is adjourned."
    judge "I will see you in court next week, [player_name] Shilling. Court is adjourned."
    stop music
    jump mccomeshomeafterpostingbail

label mccomeshomeafterpostingbail:
    scene mcsapartment
    play music "music/track1.ogg"
    "(That was nerve-wrecking.)"
    "(Some deal. Five years and nearly all of the business' assets.)"
    if pickkim == True:
        jump kimoptions
    else:
        jump otheroptions

label kimoptions:
    if pickkim and pickmai == True:
        jump pickbetweenkimandmai
    elif pickkim and picklisa == True:
        jump pickbetweenkimandlisa
    else:
        jump kimstaysthenight

label pickbetweenkimandmai:
    show maiphone at right
    main "Hello?"
    mai "[player_name]?"
    mai "I tried calling you the past two days..were you busy?"
    main "Uh, yeah. I mean. I got arrested and-"
    mai "I even showed up at your apartment but you weren't there."
    mai "Were you with Kim?"
    main "No, no."
    mai "Are you sure, [player_name]? You always stutter when you lie."

    menu:
        mai "Please be honest with me, [player_name]. I want the truth."
        "I'm sorry Mai":
            $pickmai = False
            mai "You're a bad liar, [player_name]."
            mai "Well, my visa got revoked, so I will be leaving in a month."
            mai "Thanks for everything, [player_name]."
            hide maiphone
            $cMai.morale_down(5)
            show moraledown at attributedown
            "(You're welcome, Mai.)"
            jump kimstaysthenight
        "I want only you, Mai":
            mai "Really?"
            main "Yes, come over to my apartment."
            main "I need you now."
            mai "Ok, [player_name]."
            hide maiphone
            $pickkim = False
            show kimphone at right
            kim "Hello?"
            main "Kim..I.."
            kim "So, that's how it ends."
            $cKim.morale_down(5)
            show moraledown at attributedown
            kim "Don't say I didn't warn you, [player_name]."
            hide kimphone
            jump maistaysthenight

label pickbetweenkimandlisa:
    show lisaphone at right
    main "Hello?"
    lisa "[player_name]?"
    main "Oh, hey Lisa."
    lisa "I've been calling you the past two days."
    lisa "Where have you been?"
    main "Well, I got arrested and how to go to court-"
    lisa "Yeah, but I called you before then."
    main "It was a really long night and-"
    lisa "Don't lie to me, [player_name]."
    lisa "You were with Kim, weren't you?"
    main "Just to help her move."

    menu:
        lisa "No..I know Kim. She always does this...always stealing from people."
        "I'm sorry Lisa":
            lisa "Burn me once, shame on you."
            lisa "Burn me twice, shame on me."
            lisa "I think it's best if we cut ties, [player_name]."
            $cLisa.morale_down(5)
            show moraledown at attributedown
            lisa "Good luck with the trial."
            main "Thanks.."
            lisa "Goodbye, [player_name]"
            hide lisaphone
            "(Goodbye, Lisa.)"
            $picklisa = False
            jump kimstaysthenight
        "I want only you, Lisa":
            main "No one can steal me."
            main "I'm my own person."
            main "Let's go out to eat, Lisa."
            main "You pick the place."
            lisa "Fine, I know the perfect spot."
            hide lisaphone
            $pickkim = False
            show kimphone at right
            kim "Hello?"
            main "Kim, it's-"
            $cKim.morale_down(5)
            show moraledown at attributedown
            kim "No, no. I understand."
            kim "I hope you have no regrets."
            hide kimphone
            kim "Goodbye, [player_name]."
            jump lisastaysthenight

label otheroptions:
    if picklisa == True:
        jump lisastaysthenight
    elif pickmai == True:
        jump maistaysthenight
    else:
        jump mcmakesvisits

label mcmakesvisits:
    play music "music/track1.ogg"
    "(Those were a lot of charges.)"
    menu:
        "(I know I shouldn't be out in public, but I need to talk to someone.)"
        "Visit Kim" if kimvisit == False:
            jump mcvisitskim
        "Visit Bella" if bellavisit == False:
            jump mcvisitsbella
        "Ask Mai to stay over" if bellavisit == True and pickbella == False:
            show maiphone at right
            mai "Hello?"
            main "Mai?"
            mai "[player_name]?"
            mai "How are you?"
            main "Not good, Mai."
            mai "Do you need another massage from me?"
            mai "To ease your mind?"
            main "Yes, please."
            mai "I'm on my way."
            hide maiphone
            $pickmai = True
            $cMai.morale_up(5)
            jump maistaysthenight
        "Ask Lisa to stay over" if bellavisit == True and pickbella == False:
            show lisaphone at right
            lisa "Hello?"
            main "Lisa?"
            lisa "[player_name]?"
            lisa "How are you?"
            main "I could be better."
            lisa "Same."
            main "Want to go out?"
            lisa "Yeah. I know a good place to hang out."
            main "Thanks Lisa."
            hide lisaphone
            $cLisa.morale_up(5)
            $picklisa = True
            jump lisastaysthenight
        "Wait for mom":
            "(I'll wait for mom to come.)"
            "(She should be here in the morning.)"
            jump mchomealone


label mcvisitskim:
    play music "music/track8.ogg"
    scene kimsapartment
    show kim frumpy1 at center
    kim "What do you want?"
    main "I came by to see how you were doing."
    kim "I'm fine. Looks like I quit the company at just the right time."
    show kim frumpy2 at center
    kim "All those charges.."
    show kim frumpy3 at center
    kim "They want me to make a statement."
    main "They?"
    show kim frumpy4 at center
    kim "The fat cow and her sidekick. Or boss."
    kim "Even though I no longer work there."
    main "Will you?"
    show kim frumpy5 at center
    kim "I'm not sure yet."
    kim "Maybe I should. Maybe I shouldn't."
    show kim frumpy6 at center
    kim "It doesn't matter. From what I could tell, they will keep visiting me."
    kim "Asking me questions I don't want to answer."
    main "About my dad, right?"
    show kim frumpy7 at center
    kim "Your dad , his colleagues, my whole life.."
    kim "They have a much bigger case on your dad than on you."
    kim "If I talk to them, I'll have to change my whole identity forever."
    show kim frumpy8 at center
    kim "I'm just not sure if I want to do that."
    main "Change your identity, why?"
    kim "I'm just as guilty as he is, [player_name]."
    kim "I benefitted the most from the theft and crime."
    show kim frumpy9 at center
    kim "I...I just didn't expect him to leave me alone."
    kim "But he did."
    menu:
        kim "And if I tell on him...I..."
        "Would have done the right thing.":
            main "I know we didn't see eye-to-eye on everything."
            main "You were a victim of my dad-"
            show kim frumpy10 at center
            kim "I was a willing participant, [player_name]."
            kim "I did it because I wanted to."
            kim "Because I {i}liked{/i} having expensive clothes and fancy purses."
            kim "I travelled the world and experienced things my classmates only dreamed of."
            kim "But it came at price."
            main "....."
            show kim frumpy11 at center
            kim "Aww, don't be sad for me, [player_name]."
            kim "I've lived a good life."
            kim "Some of us are just made to be whores. Nothing more."
            kim "But you're young, [player_name]."
            show kim frumpy12 at center
            $kimvisit = True
            $kimdead = True
            kim "Start fresh, from a clean slate."
            kim "Don't carry your father's burdens."
            kim "Be free, [player_name]."
            kim "Good bye."

            stop music
            scene mcsapartment
            jump mcmakesvisits

        "Would be able to do what you want to do.":
            show kim frumpy13 at center
            kim "What I want to do?"
            main "You spoke about your dreams and desires."
            kim "I did."
            main "So pursue them."
            main "But not as John Shilling's former mistress."
            main "But as Kimberly Taylor."
            show kim frumpy14 at center
            kim "As..."
            $kimvisit = True
            kim "You're right, [player_name]."
            kim "To think someone so young could be so wise."
            kim "I'm sorry for everything I did, [player_name]."
            kim "I wish I could make it up to you."
            show kim frumpy15 at center
            main "Forgive yourself, Kimberly."
            kim "...I will."
            stop music
            scene mcsapartment
            jump mcmakesvisits

label mcvisitsbella:
    scene bellavisit1
    main "Bella?"
    bella "Oh, hello [player_name]."
    scene bellaslab
    show bella serious2 at center
    bella "What are you doing here? Did you need something from me again?"
    main "I just wanted to see how you were doing."
    bella "I'm fine. Mostly annoyed."
    show bella serious1 at center
    bella "I was in the middle of my research when Christina and some districtattorney showed up."
    bella "They wanted me to write an affa- a statement against you."
    show bella sad5 at center
    bella "Christina was an undercover cop. Who knew."
    main "I didn't."
    show bella sad3 at center
    bella "Did any of the other girls know?"
    main "No."
    $bellavisit = True
    show bella sad4 at center
    bella "Well it's just fraud right? Nothing to do with the cryptocurrency so-"
    bella "Even then, I'm sure my father will get a good lawyer for me."
    show bella sad6 at center
    bella "He can't afford to have a scandal during his re-election campaign."
    show bella sad5 at center
    bella "I should be more aware of things."
    bella "I'm always immersed myself in my work, neglecting the outside world."
    show bella yawn

    menu:
        bella "Guess that's why I'm stuck here."
        "Be more social, Bella.":
            show bella serious2 at center
            bella "Easy for you to say, [player_name]."
            bella "I'm a one-on-one type of person."
            bella "Good luck with your trial, [player_name]."
            hide bella serious2
            scene mcsapartment
            jump mcmakesvisits
        "Not forever.":
            show bella surprised2 at center
            bella "What do you mean?"
            main "You will present your ideas to the world and-"
            show bella smile2 at center
            bella "I already told you, too expensive."
            main "I'll fund it."
            show bella smile3 at center
            bella "You're a crazy one."
            main "Takes one to know one."
            bella "You're right."
            show bella smile2 at center
            $pickbella = True
            bella "Well, if you {b} get acquitted on all charges {/b}, then come my way."
            bella "We can start a robot empire together."
            main "Robot....Empire?"
            hide bella smile2
            scene bellavisit3
            $cBella.morale_up(7)
            show moraleup at attributeup
            bella "You come up with a better name then."
            bella "Good luck, [player_name]."
            scene mcsapartment
            jump mcmakesvisits

label mchomealone:
    jump mcsmomarrives

label kimstaysthenight:
    scene kimvisit11
    kim "Oh I missed you so much, [player_name]."
    scene kimvisit1
    kim "I thought about you all day."
    scene kimvisit6
    kim "We should move in together."
    kim "This place could use a woman's touch."
    scene kimvisit15
    kim "Can you believe that fat cow is a police officer?"
    kim "She and her boss came to my apartment asking questions."
    main "Did you tell them anything?"
    kim "No. I told them I needed to call an attorney."
    main "My mom's coming tomorrow."
    scene kimvisit4
    kim "She is?"
    scene kimvisit5
    kim "This should be a fun family reunion."
    scene kimvisit14
    kim "For now, let's have some fun."
    if persistent.lewdfilter== True:
        scene black with fade
        jump mcmomandkim
    else:
        scene 2kimprivate3
        play music "music/track9.ogg"
        kim "You like my feet, don't you?"
        scene 1kimprivate3
        kim "Does mommy's feet feel good on your cock?"
        scene 3kimprivate3
        kim "You're so hard."
        scene 4kimprivate3
        kim "Now lick mommy's pussy."
        scene 7kimprivate3
        kim "Ahhh..that feels so good. Don't stop."
        scene 8kimprivate3
        kim "Time for another round."
        scene kimsidefuck
        kim "Ahhh fuck me, [player_name]."
        kim "Make me a mommy."
        scene 10kimprivate3
        kim "I want to feel you cum inside of me, [player_name]."
        scene 9kimprivate3
        kim "You're such a good boy."
        kim "Time to sleep."
        stop music
        jump mcmomandkim

label mcmomandkim:
    scene kiminbed
    kim "Good morning, baby."
    kim "You sleep so peacefully."
    play sound "sfx/knocknock.ogg"
    "(Shit!)"
    scene momintro
    stop sound
    play music "music/track2.ogg"
    mom "Hello, dear."
    main "Hi, Mom."
    scene kimmcmom1
    mom "Hmmm..who is that over there."
    scene kimmcmom2
    mom "You."
    kim "Hello, Lara. Long time no see."
    scene kimmcmom3
    mom "What are you doing here?"
    scene kimmcmom4
    kim "Comforting your baby boy."
    kim "Are you surprised I got to him as well?"
    scene kimmcmom5
    mom "He will NEVER be your baby boy."
    main " STOP IT!"
    scene kimmcmom6
    mom "I'm sorry dear I am just.."
    mom "Surprised. Because you should be in jail."
    kim "I'm not. I didn't even get served."
    scene kimmcmom8
    mom "You should. "
    scene kimmcmom9
    kim "Are you going to represent him, Lara?"
    mom "Of course I would. He's my son."
    kim "The hot shot lawyer strikes again."
    kim "You know, we're allies now, Lara. No need to be so hostile."
    scene kimmcmom10
    mom "....I want to talk with my son. Alone."
    mom "Unlike {i} you {/i}, I can actually help him."
    kim "He's all yours, Lara."
    scene kimmcmom11
    kim "{size=-10}Early congratulations on being a grandmother.{/size}"
    jump mcandmomalone

label maistaysthenight:
    scene maivisit1
    mai "Hello [player_name]."
    with smallshake
    main "That's a lot of food."
    mai "Hmmm? No, I think it's enough."
    scene maivisit2
    main "Wow, that food smells really nice."
    mai "Better than pizza, right?"
    scene maivisit3
    mai "Dinner is served."
    scene maivisit12
    "(This is overwhelming.)"
    scene maivisit4
    mai "...[player_name]..."
    main "Yes, Mai?"
    mai "Are you going to jail?"
    main "I hope not."
    main "What's wrong?"
    scene maivisit5
    mai "My visa got revoked."
    main "Revoked?"
    mai "Because of what happened."
    scene maivisit6
    mai "I have to go back home."
    main "Is there any way to get it back?"
    mai "No."
    main "Not even if I marry you?"
    scene maivisit7
    mai "!!!!!"
    mai "I hear that process takes a long time and a lot of money."
    scene maivisit13
    mai "Are you sure you want to do this, [player_name]?"
    main "Yes. If that's what you want."
    scene maivisit14
    main "Mai, will you marry me?"
    mai "Yes!"
    scene maivisit8
    mai "When do we get married?"
    scene maivisit15
    main "After the trial. Assuming I get off on all charges."
    main "My mom is coming tomorrow. To represent me."
    mai "Oh...I should clean up the place."
    main "Good idea."
    stop music
    jump mcmomandmai

label mcmomandmai:
    scene momintro
    mom "Hello, [player_name]."
    scene maimcmom1
    play music "music/track2.ogg"
    mom "What's that smell."
    mom "Wow, have you taken up cooking?"
    main "No I-"
    scene maimcmom2
    mom "Who is this?"
    mai "Hello, Miss- Mrs-"
    mom "You can call me Lara. What's your name?"
    mai "Mai."
    scene maimcmom3
    mom "Mai, have you been taking care of my son?"
    mom "I can smell a home cooked meal."
    mai "Yes, I-I-I am."
    scene maimcmom4
    mom "Don't be so nervous, come here."
    mom "I always hoped my son would find a nice sweet girl."
    mom "I can tell you're perfect for him."
    scene maimcmom5
    mom "What's wrong?"
    mai "I...."
    mom "Shhh...it's ok. What happened, [player_name]?"
    main "Her visa got revoked."
    main "She's supposed to go home in 90 days."
    scene maimcmom6
    mom "Shhh...shhh..it's ok, Mai."
    main "But I'm going to stop it."
    mom "How?"
    main "Marrying her, of course."
    scene maimcmom7
    mom "Oh dear. Hmm...."
    mom "I know a good immigration lawyer that can expedite the process."
    mai "Oh, thank you, Lara."
    scene maimcmom8
    mom "We will sort it out after the trial."
    scene maimcmom9
    mom "I'll even help you buy a wedding dress and plan a small ceremony."
    mai "Oh thank you, thank you Lara."
    scene maimcmom10
    mom "Now, my son and I need some alone time. Is that ok?"
    mai "Mmhmmm."
    jump mcandmomalone

label lisastaysthenight:
    scene lisavisit1
    main "Wow, this place is really nice."
    lisa "Yeah, I always wanted to come here with someone special."
    scene lisavisit2
    lisa "So..this is how things turn out."
    scene lisavisit3
    lisa "I knew she was up to no good."
    lisa "But a police officer? ...I should have seen it coming."
    scene lisavisit4
    lisa "So what are you going to do?"
    main "My mom's coming."
    lisa "Your mom?"
    main "She's a lawyer. One of the best in the country."
    main "You know those Wall Street scandals?"
    lisa "Yeah."
    main "She got everyone a light sentence."
    scene lisavisit5
    lisa "Impressive."
    main "There's no telling what she did for my dad before he divorced her."
    lisa "Or how much money she got from him after they divorced."
    main "She did get him to pay for my education. Private school, undergrad, business school."
    scene lisavisit6
    lisa "So where does that leave us?"
    main "New York City, right? You wanted to go to school for fashion?"
    lisa "Yeah, I did. Like a fashion publicist or an editor."
    scene lisavisit7
    lisa "Are you having second thoughts?"
    main "No. Just admiring you."
    lisa "Let's get a to-go box and finish this at your place."
    if persistent.sexscenes == False:
        scene black with fade
        jump mclisaandmom
    else:
        scene 4lisasex2 with fade
        play music "music/track9.ogg"
        lisa "Miss these?"
        lisa "Go on, smell them."
        scene 1lisasex2
        lisa "Hey! That tickles!"
        scene 2lisasex2
        lisa "I've never done a footjob like this before."
        lisa "Is this better?"
        scene 8lisasex2
        lisa "Ahhh....fuck me, [player_name]."
        jump lisadoggyfuck

label lisadoggyfuck:
    scene lisadoggy
    menu:
        "View 2":
            jump lisadoggyfuck2
        "View 3":
            jump lisadoggyfuck3
        "Finish":
            stop music
            jump mclisaandmom

label lisadoggyfuck2:
    scene lisadoggyv2
    menu:
        "View 1":
            jump lisadoggyfuck
        "View 3":
            jump lisadoggyfuck3
        "Finish":
            stop music
            jump mclisaandmom

label lisadoggyfuck3:
    scene lisadoggyv4
    menu:
        "View 1":
            jump lisadoggyfuck
        "View 2":
            jump lisadoggyfuck2
        "Finish":
            stop music
            jump mclisaandmom


label mclisaandmom:
    play sound "sfx/knocknock.ogg"
    scene momintro with fade
    mom "Hello, [player_name]."
    main "Hi, mom."
    stop sound
    scene lisamcmom1
    play music "music/track2.ogg"
    mom "Did I come at a bad time?"
    main "No, no, not at all."
    scene lisamcmom2
    mom "Who is this?"
    lisa "Alyssa. I'm uh, [player_name]'s girlfriend."
    scene lisamcmom3
    mom "Oh, girlfriend? Impressive. You two must get a lot of looks."
    lisa "Yes, I-I mean we do."
    mom "And how did you two meet?"
    scene lisamcmom4
    lisa "Oh at wo-"
    mom "At work. What did you do, exactly?"
    lisa "I worked in sales so-"
    scene lisamcmom5
    mom "You got pretty good at lying to people."
    lisa "You could say that."
    mom "Lighten up. I'm just trying to get to know you, Lisa."
    mom "Though I will make it very clear."
    scene lisamcmom6
    mom "{size=-10}Lie to my son and you will have to deal with me.{/size}"
    mom "Is that clear?"
    lisa "Yes, Ms-"
    mom "Lara."
    mom "Now I need to talk to my son. Do you mind leaving us alone for a while?"
    lisa "Yeah, sure thing."
    jump mcandmomalone

label mcsmomarrives:
    scene momintro
    mom "Hello, [player_name]."
    main "Hi, mom."
    stop sound
    scene momintro2
    play music "music/track2.ogg"
    mom "Nice place."
    mom "Well, let's get to work."
    jump mcandmomalone

label mcandmomalone:
    scene mcsapartment
    if pickkim == True:
        show lara angry6 at center
        mom "Her?"
        main "Is there a problem?"
        mom "Listen, [player_name]."
        show lara angry5 at center
        mom "I can get you off of most-almost all of these charges."
        mom "But her- she has a lot of skeletons in her closet."
        show lara angry1 at center
        mom "If you stay with her, you might have go to under Witness Protection."
        mom "We won't be able to see each other again."
        main "...I know, and I'm prepared."
        show lara serious6 at center
        mom "I'm just concerned for you, [player_name]."
        mom "But if she makes you happy, then I'm happy."
        mom "Now that we have that out of the way."
        show lara serious10 at center
        mom "Let me explain your options."
        mom "You can plea guilty, not guilty, or no contest."
        mom "Do you need me go over these options?"
        main "Yes, please."
        jump momexplainsoptions
    elif pickmai == True:
        show lara smile3 at center
        mom "Such a lovely girl."
        mom "I hope you're not treating her like a charity case."
        main "I'm not."
        show lara serious8 at center
        mom "Good, because my colleagues will."
        show lara smile5 at center
        mom "But if it makes you happy, then I'm happy."
        mom "Now that we have that out of the way."
        show lara serious10 at center
        mom "Let me explain your options."
        mom "You can plea guilty, not guilty, or no contest."
        mom "Do you need me go over these options?"
        main "Yes, please."
        jump momexplainsoptions
    elif picklisa == True:
        show lara smile8 at center
        mom "She reminds me of myself."
        mom "Young, beautiful, full of energy."
        show lara serious6 at center
        mom "The kind of girl who is never fully happy."
        main "She's at peace with me."
        mom "I'll take your word for it."
        show lara smile3 at center
        mom "As long as you're happy, I'm happy."
        mom "Now that we have that out of the way."
        show lara serious10 at center
        mom "Let me explain your options."
        mom "You can plea guilty, not guilty, or no contest."
        mom "Do you need me go over these options?"
        main "Yes, please."
        jump momexplainsoptions
    else:
        show lara serious10 at center
        mom "Let me explain your options."
        mom "You can plea guilty, not guilty, or no contest."
        mom "Do you need me go over these options?"
        main "Yes, please."
        jump momexplainsoptions

label momexplainsoptions:
    scene momtalk3
    menu:
        "Guilty option":
            mom "If you plead guilty, there's no doubt that you will be offered a nice deal."
            mom "You will have to cooperate with them."
            mom "They want Jo-your father. You are their best way to get them."
            main "What will happen then?"
            mom "Depending on the severity of the case, you might have to go under Witness Protection."
            mom "So we won't be able to see each other unless you leave the program."
            mom "But you will get a fresh start in life."
            mom "It's the easy route."
            jump momexplainsoptions
        "Not Guilty option":
            mom "If you plead not guilty, we go to court."
            mom "I'll prepare the case, get as many witnesses to testify on your behalf."
            mom "I hope some of your employees will help out."
            mom "I can get you off of most charges. But a few are difficult if the DA has everything she needs."
            mom "It's the lengthy route, but can be the most rewarding."
            jump momexplainsoptions
        "No Contest option":
            mom "No Contest means you accept all of the charges."
            mom "You will be sentenced right away."
            mom "I don't recommend it. Even if you take the fall for your father's business, it will never go away."
            mom "You're looking at jail time."
            mom "Think carefully before choosing this option."
            mom "Especially if you have someone to take care of."
            jump momexplainsoptions
        "I understand everything now.":
            mom "If that's all, then I'll be leaving."
            mom "Please think over your options."
            mom "As your attorney, I will go with whatever decision you make."
            mom "But as your mom, I want you to have a clean slate."
            mom "You're not responsible for your father's mistakes."
            main "Thanks, Mom."
            mom "Good night, [player_name]."
            stop music
            jump dadcalls

label dadcalls:
    scene mcsitsoncouch
    play music "music/track1.ogg"
    "(She's gone.)"
    "(What should I do?)"
    play sound "sfx/cellvibe.ogg"
    scene mconphone
    main "Hello?"
    stop sound
    show dadphone at topright
    dad "......[player_name]!!!"
    dad "Don't say a word, listen."
    dad "You can't sell me out, ok?"
    dad "I know I got you knee deep in this shit, but I promise I'll get you out."
    dad "Do your old man a favor and take one for the team, ok?"
    main "Ok."
    main "I want answers, dad. I'm by myself. No one can hear me."
    dad "What answers do you want, kiddo?"
    main "Was there ever a trust fund for me?"
    dad "No. I mean, there was a 'trust fund', but it was never for you."
    dad "Not directly, anyway."
    main "So you give me a ...Ponzi scheme business and tell me to fix it?"
    main "And now, you're telling me NOT to sell out?"
    dad "Alright, alright. I can tell your mother has sunken her fangs into you."
    dad "I'm in a much bigger, much more profitable business."
    dad "I just needed a little extra capital, if you understand  what I'm saying."
    dad "SPH was just a way to get that extra capital."
    dad "Just do this favor for me, and I'll let you in on my real business."
    main "I'll think on it."
    dad "Don't think! Just do!"
    dad "I've got to go. Don't want the feds on my ass again."
    dad "Bye, [player_name]."
    main "Bye, dad."
    jump afterdadcalls

label afterdadcalls:
    if pickkim == True:
        scene kimvisit7
        play music "music/track9.ogg"
        kim "I'm back."
        kim "That was eventful."
        scene kimvisit8
        kim "Same old Lara."
        scene kimvisit9
        kim "So what are you going to do?"
        main "I'm not sure yet."
        scene kimvisit10
        kim "Well, remember to keep me and our child in mind."
        main "You're pregnant?"
        kim "Not yet, but soon enough."
        kim "What's the matter, sweetie?"
        main "It's nothing."
        scene kimvisit12
        kim "Then let me put your mind at ease."
        if persistent.sexscenes == False:
            scene black with fade
            jump arraignment
        else:
            scene 1kimprivate3
            kim "Just relax and let me do all of the work."
            scene 2kimprivate3
            kim "Oh, you feel so good, [player_name]."
            scene 3kimprivate3
            kim "Cum inside of my pussy."
            kim "I want to feel your cum."
            scene 4kimprivate3
            kim "Good night, [player_name]."
            stop music
            jump arraignment
    elif pickmai == True:
        play music "music/track9.ogg"
        scene maivisit9
        mai "I'm back."
        main "More groceries?"
        mai "Just some cleaning products."
        scene maivisit10
        mai "Your mom really likes me, [player_name]."
        main "Yeah, that's a lot coming from her."
        scene maivisit11
        mai "Is something wrong?"
        main "No...no..."
        mai "You need another massage, [player_name]."
        if persistent.sexscenes == False:
            scene black with fade
            jump arraignment
        else:
            scene 1maisex2
            mai "Does that feel good?"
            scene 2maisex2
            mai "Or like this?"
            scene 3maisex2
            mai "You're so hard now, [player_name]."
            scene 4maisex2
            mai "Just a little more."
            scene 5maisex2
            mai "Lick my pussy, [player_name]."
            scene 6maisex2
            mai "That feels good..mmmm...."
            scene 7maisex2
            mai "Fuck me, [player_name]."
            scene maimissionary
            mai "We...should...give...your...mom...grandkids..."
            mai "Cum inside of me, [player_name]."
            scene 8maisex2
            mai "Let's go again."
            stop music
            jump arraignment
    elif picklisa == True:
        scene lisavisit8
        play music "music/track9.ogg"
        lisa "I'm back."
        main "Welcome back."
        lisa "You're a lot like your mother, [player_name]."
        scene lisavisit9
        lisa "Straight-forward and to the point."
        main "Yeah, but she also has a nice side."
        lisa "So, what are you going to do?"
        main "I'm not sure yet."
        scene lisavisit10
        lisa "I hope everything works out."
        lisa "....I'm so used to things not going my way."
        scene lisavisit11
        lisa "Promise me you'll make the right decision, [player_name], please."
        main "I will."
        scene lisavisit14
        lisa "Good, because I'm going to New York regardless."
        scene lisavisit15
        lisa "So make the right choice."
        stop music
        jump arraignment
    else:
        jump crissystopsby


    label crissystopsby:
        scene mcsdoor
        show crissy sad10 at center
        main "What are you doing here?"
        crissy "I'm...on paid leave."
        crissy "I told my supervisor what I did and...she put on probation."
        crissy "She didn't want me to mess up her big case."
        main "So why did you come here?"
        show crissy sad9 at center
        crissy "I...I need you to keep quiet about this, [player_name]."
        crissy "Please."
        crissy "I really want to pursue a career in politics. This is expected."
        main "You're really selfish, you know that?"
        main "You also have low standards."
        show crissy serious9 at center
        crissy "Please, [player_name]. Keep everything that happened a secret."

        menu:
            crissy "Please."
            "Yes, now go away.":
                show crissy sad7 at center
                main "Have some respect for yourself."
                main "Someone might take advantage of you."
                show crissy smile6 at center
                crissy "Thanks, [player_name]."
                stop music
                jump arraignment
            "No.":
                scene crissybeg1
                $authority.trait_up(3)
                show authorityup at attributeup
                crissy "Please! Please! I'll do anything!"
                main "Anything?"
                crissy "Yes, anything. Testify for you, get you connections...even take care of your needs."

                menu:
                    crissy "I'll do anything."
                    "Well in that case.":
                        if persistent.sexscenes == False:
                            scene black
                            crissy "Are you-are you filming this?"
                            main "As insurance."
                            $pickcrissy = True
                            crissy "I hate you!"
                            $pickbella = False
                            main "Three times a week."
                            crissy "Fine."
                            jump arraignment
                        else:
                            jump crissysextoy

                    "No, now go away.":
                        crissy "I'm sorry, [player_name]."
                        stop music
                        jump arraignment


label crissysextoy:
    scene crissysex1 with fade
    $pickcrissy = True
    play music "music/track9.ogg"
    crissy "You're such a simple guy, [player_name]."
    scene crissysex1
    crissy "mmhmhmmhhhhhhhhhhh"
    scene crissysex2
    "(At least I have one person on my side.)"
    scene crissysex3
    $pickbella = False
    "(But just in case.)"
    scene crissysex4
    main "Smile for the camera."
    scene crissysex5
    crissy "You had a camera on this whole time?"
    scene crissysex6
    crissy "Answer me!"
    jump crissyroughfuck

label crissyroughfuck:
    scene crissydoggy
    menu:
        "View 2":
            jump crissyroughfuck2
        "Finish":
            jump aftercrissyrf

label crissyroughfuck2:
    scene crissydoggyv3
    menu:
        "View 1":
            jump crissyroughfuck
        "Finish":
            jump aftercrissyrf



label aftercrissyrf:
    scene crissysex7
    crissy "You..came inside of me...?"
    scene crissysex8
    main "Three times a week. Unless I say otherwise."
    crissy "Ugh...."
    main "It's our secret."
    scene crissysex9
    main "Now leave."
    stop music
    jump arraignment
