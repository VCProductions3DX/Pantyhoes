label arraignment:
    scene courthouse
    play music "music/track6.ogg"
    show judge1 at center
    judge "The court calls the case of The People versus [player_name] Shilling, case no. 63367290."
    judge "Are you [player_name] Shilling? Is that your true and correct name?"
    main "Yes, it is."
    judge "In case no.  63367290, you have been charged with the offenses of investor fraud, embezzlement, and money laundering."
    judge "This courtroom proceeding is your arraignment. The purpose of today's proceeding is to ensure that you are the person charged in the information (or indictment), to inform you of the range of punishment for the offense for which you are charged, and to take your plea."
    judge "Are you [player_name] Shilling, the person named in the information?"
    main "Yes."
    show judge2 at center
    judge "Do you understand the allegations against you and the full range of punishment for this offense?"
    main  "Yes."
    judge "How do you plead?"

    menu:
        "(I need to make the {b} right choice {/b} here.)"
        "Plea Guilty":
            hide judge2
            bailiff"I will read the rights that you have and the consequences of a plea of guilty."
            bailiff "Is there a plea bargain agreement between the people and the defendant?"
            show iris1 at left
            districtattorney "Yes, there is."
            bailiff "Will the prosecution please present the terms of the plea bargain to the court."
            show iris7 at left
            districtattorney "Here are the following terms of the plea bargain:"
            districtattorney "90 days in federal prison, following 3 years of probation."
            districtattorney "Cooperation with the authorities with their ongoing investigation."
            districtattorney "Liquidation of all assets gained by SPH and paid to investors."
            hide iris7
            show judge1 at left
            judge "Do you accept the terms of the plea bargain?"
            show lara serious7 at right
            mom "Yes, he does."
            hide judge1
            hide lara serious7
            jump pleaguilty

        "Plea Not Guilty":
            show judge6 at center
            judge "You are hereby ordered to appear and be ready for trial 30 days from now."
            judge "Court is adjourned."
            hide judge6
            stop music
            jump pleanotguilty

        "Plea No Contest":
            show lara sad2 at left
            mom "[player_name]!"
            judge "Are you entering this plea freely and of your own will?"
            main "Yes, I am."
            $nocontest = True
            show judge4 at right
            judge "Then we will move to the punishment phase of the trial."
            judge "As stated before in the indictment, the punishment for the offenses is a $100 000 fine and 5 years in prison."
            judge "If you agree to this plea, you will start your sentence immediately."
            judge "Do you agree?"
            main "Yes."
            show judge3 at right
            judge "I hearby sentence Mr. [player_name] Shilling to 5 years in prison and a  $100 000 fine."
            judge "Court is adjourned."
            hide judge3
            hide lara sad2
            scene mcinhandcuffs
            mom "..You didn't have to do this, [player_name]."
            mom "I'll contact you later."
            stop music
            jump badending

label pleanotguilty:
    scene mcsapartment
    play music "music/track2.ogg"
    show lara serious10 at center
    mom "To court then."
    mom "Those charges are quite hefty."
    show lara smile3 at center
    mom "But I think I can clear you on all of those charges."
    mom "First, I want you to tell me anything that might convince the judge you're a gullible person."

    label extrainfo:
        mom "Anyone you worked with, your employees, the arresting officer."
        menu:
            "Christina":
                if pickcrissy == True:
                    main "The arresting officer."
                    show lara serious6 at center
                    mom "Hm?"
                    main "She said she would testify on my behalf."
                    mom "Oh? An officer of the law testifying against the prosecution?"
                    main "Is that even possible?"
                    show lara angry2 at center
                    mom "I think if she wants to keep her job, she won't."
                    mom "But she may not reveal everything in her testimony."
                    $crissytestifies = True
                    jump extrainfo
                else:
                    main "The arresting officer."
                    show lara angry7 at center
                    mom "What about him?"
                    main "Her."
                    mom "What about her?"
                    main "She was an undercover agent at the firm."
                    show lara serious8 at center
                    mom "And?"
                    main "Are undercover agents allowed to have sex on the job?"
                    mom "Sex? Usually that's the vice department. Dealing with drug lords and sex trafficking pimps."
                    mom "Not for white-collar crimes."
                    show lara sad1 at center
                    mom "Though..I wouldn't put it past them."
                    main "...."
                    mom "Did she coerce you at any time?"
                    if crissyfuck == True:
                        main "Well, there was that one time she begged me to fuck her."
                        main "I wouldn't say coerce."
                        show lara serious6 at center
                        mom "....No, we can't bring that up in court."
                        mom "It might lead to a mistrial."
                        jump extrainfo
                    else:
                        main "Well. Several times she tried to get me to have sex with her."
                        main "But I refused."
                        mom "Hmmm....and did she threaten you?"
                        main "...I did that."
                        show lara smile3 at center
                        mom "I see. It's nice that you have morals."
                        mom "If she decides to testify, I'll bring it up."
                        $crissycrossexam == True
                        jump extrainfo

            "Mai" if maitalk==True:
                if pickmai == True:
                    main "There is Mai."
                    show lara smile2 at center
                    mom "Such a sweet girl. What was her role in all of this?"
                    main "She was the accountant."
                    show lara serious10 at center
                    mom "Certified?"
                    main "I ...don't think so."
                    main "I think dad offered to pay for her license if she worked for him."
                    main "Actually, dad promised her a lot of things."
                    show lara serious6 at center
                    mom "As long as she did what she was told."
                    mom "We can get her to testify on our behalf."
                    mom "That's at least one person in our corner."
                    $maitestifies = True
                    jump extrainfo
                else:
                    main "The accountant."
                    show lara angry2 at center
                    mom "Hmm?"
                    main "She was forced to falsify everything for the investors."
                    main "I made her give the real numbers."
                    show lara serious6 at center
                    mom "So the whole time she knew about the embezzlement."
                    main "Yes."
                    if cMai.morale >=2:
                        main "I think I can get her to testify on my behalf."
                        mom "Really?"
                        $maitestifies = True
                        main "Yes."
                        jump extrainfo
                    else:
                        main "I doubt she will want to testify in my favor."
                        $maicrossexam = True
                        mom "I will just bring it up in cross-examination."
                        jump extrainfo

            "Lisa" if lisatalk == True:
                if picklisa == True:
                    main "There is Lisa."
                    show lara angry4 at center
                    mom "The liar."
                    main "She's not a l-"
                    show lara serious8 at center
                    mom "What did she really do?"
                    main "She had to convince investors to not sell their shares."
                    mom "Was she compromised in any way?"
                    main "Dad knew about her past job as a cam girl."
                    show lara smile4 at center
                    mom "You certainly have high standards."
                    mom "Do you think she will testify in our favor?"
                    $lisatestifies = True
                    main "Yes."
                    mom "I leave the rest to you."
                    jump extrainfo
                else:
                    main "The customer service representative."
                    show lara smile6 at center
                    mom "Hmm?"
                    main "She had to convince investors to buy and not sell their shares."
                    mom "So she participated in the scheme."
                    if cLisa.morale >=2:
                        main "I think I can convince her to testify on my behalf."
                        mom "Really?"
                        main "Yes."
                        $lisatestifies = True
                        mom "I'll leave it to you."
                        jump extrainfo
                    else:
                        main "I doubt she'll testify in my favor."
                        $lisacrossexam = True
                        mom "We will get that out of her in cross-examination."
                        jump extrainfo


            "Kim" if kimtalk == True:
                if pickkim == True:
                    main "There is Kim."
                    main "She can testify for us."
                    main "That I didn't do anything."
                    show lara angry6 at center
                    mom "Yes and in doing so she incriminates herself."
                    mom "But more than likely after your case, she will be next."
                    mom "I hope you are prepared for more court battles."
                    $kimtestifies = True
                    main "I will."
                    jump extrainfo
                else:
                    main "Kim."
                    show lara angry2 at center
                    mom "That bitch."
                    mom "Oh..I'm sorry, I shouldn't have said that."
                    show lara serious6 at center
                    mom "Yes, she knows everything."
                    mom "I am surprised she didn't get arrested."
                    if kimvisit == True:
                        main "I spoke to her before you came."
                        main "She said they were asking her to testify against me."
                        show lara smile3 at center
                        mom "Oh, that's just precious."
                        mom "You don't have to say anything else, dear."
                        mom "I'll get her to confess in court."
                        $kimcrossexam= True
                        main "If she shows up."
                        mom "She won't have a choice."
                        jump extrainfo
                    else:
                        main "She didn't?"
                        show lara smile7 at center
                        mom "No, otherwise I would be jumping for joy."
                        mom "Well, if she decides to testify, I'll make her regret it."
                        $kimcrossexam= True
                        main "Thanks, Mom."
                        jump extrainfo

            "Bella" if bellatalk == True:
                main "There is the IT specialist."
                main "She collected the data and sold it.."
                main "It was a pretty confusing process."
                show lara serious6 at center
                mom "Hmmm..."
                mom "What's her name?"
                main "Isabella Cole."
                mom "...Senator Cole's daughter. Yeah I doubt she will testify."
                show lara serious8 at center
                mom "Reputation is everything for that family."
                mom "If the prosecution brings her, I'll do my best in cross-examination."
                mom "But I'm sure her father's lawyer will stop me at every turn."
                if pickbella == True:
                    main "Actually she said she would testify for me."
                    show lara smile3 at center
                    mom "Hmm, that's a surprise."
                    $bellatestifies = True
                    mom "Well, that's at least one person on our side."
                    jump extrainfo
                else:
                    mom "I doubt she will show up in court."
                    mom "So I will have to plan my defense accordingly."
                    jump extrainfo

            "That's everything.":
                mom "Are you sure?"
                menu:
                    mom "There isn't anything else?"
                    "I'm positive":
                        scene momtalk10
                        mom "Then I will prepare my case."
                        mom "You sit here and rest. Clear your mind."
                        mom "We have a big fight ahead of us."
                        stop music
                        jump trial
                    "Well..":
                        jump extrainfo


label pleaguilty:
    scene kimnotguiltyverdict
    mom "You did the right thing, [player_name]."
    mom "Now, just cooperate with the police."
    scene neutralending1
    districtattorney "Thank you for cooperating with us, Mr. Shilling."
    districtattorney "Now for a few questions."
    districtattorney "When was the last time you had contact with your father?"
    main "Before the trial."
    scene neutralending2
    districtattorney "Your phone."
    main "Here."
    districtattorney "Thank you, Mr. Shilling. This is all we need."
    main "Nothing else?"
    districtattorney "No."
    main "And what do I get in return-"
    scene neutralending3
    districtattorney "You can apply for Witness Protection, but that's out of my jurisdiction."
    districtattorney "I can refer you to an agent."
    main "No..thanks."
    districtattorney "I'll be keeping an eye out on you, Mr. Shilling."
    if pickcrissy == True:
        districtattorney "And my subordinate as well."
        stop music
        jump neutralending
    else:
        districtattorney "Don't get into any more trouble."
        stop music
        jump neutralending


label trial:
    scene courthouse
    play music "music/track6.ogg"
    "(I'm early.)"
    show lara smile3 at center
    mom "So you're an early bird, too [player_name]."
    mom "I raised you well."
    main "Is there a jury?"
    show lara smile5 at center
    mom "No, just a judge. It's a small case."
    main "That's a relief."
    show lara serious12 at center
    mom "Now, listen closely."
    mom "Let me do all of the talking."
    mom "Do not say anything unless I tell you."
    show lara angry7 at center
    mom "Is that clear?"
    main "Yes, mom."
    mom "Good."
    jump trialstart


label trialstart:
    scene judgeenters
    bailiff "All rise. {i} The People v. [player_name] Shilling {/i} is now in session."
    bailiff "Judge Marshall presiding. Please be seated."
    scene courthouse
    show judge1 at center
    judge "Good morning, ladies and gentlemen. Calling the case of The People versus [player_name] Shilling."
    judge "Are both sides ready?"
    hide judge1
    show iris3 at left
    districtattorney "Ready for the People, Your Honor."
    show lara serious10 at right
    mom "Ready for the defense, Your Honor."
    hide lara serious10
    hide iris3
    show iris11 at center
    districtattorney "Your Honor,the defendant has been charged with the crime of investor fraud and embezzlement of funds."
    districtattorney "The evidence I present will prove to you that the defendant is guilty as charged."
    hide iris11
    show lara serious8 at center
    mom "Your Honor, under the law my client is presumed innocent until proven guilty. During this trial, you will hear no real evidence against my client."
    mom "You will come to know the truth: that [player_name] Shilling had no involvement in the charges brought by the prosecution. Therefore my client is not guilty."
    judge "The prosecution may call its first witness."
    hide lara serious8
    jump prosecutioncase

label prosecutioncase:
    if maitestifies == False:
        districtattorney "The People call Mai Amaya to the stand."
        scene maiswearsoath
        bailiff "Please raise your hand."
        bailiff "Do you promise that the testimony you shall give in the case before this court shall be the truth, the whole truth, and nothing but the truth?"

        mai "I do."
        bailiff "For the record, please state your name."
        mai "Mai Amaya."
        scene courthouse
        show iris5 at left
        districtattorney "If you could please, state your position at SPH."
        show mai court3 at right
        mai "Accounting and Finance."
        districtattorney "Thank you, under the time that [player_name] was in office, what were your duties?"
        show mai court4 at right
        mai "To provide him with financial statements."
        districtattorney "And were these financial statements accurate to the best of your ability?"
        mai "..Yes."
        show iris8 at left
        districtattorney "Thank you."
        districtattorney "Miss Amaya, during the discovery phase, we uncovered two sets of conflicting financial reports. Did you author both of those reports?"
        mai "Yes."
        districtattorney "To whom were those reports for?"
        show mai court3 at right
        mai "The defendant, your honor."
        if maicrossexam == True:
            hide iris8
            show lara serious8 at left
            mom "Objection."
            judge "Proceed."
            mom "Miss Amaya, what was the reason for the two financial reports?"
            show mai court2 at right
            mai "To correct an error."
            mom "Was this error made before my client arrived at your office?"
            mai "Yes."
            mom "And did you make this error on behalf of my client?"
            districtattorney "Objection."
            judge "Denied."
            show mai court4 at right
            mai "...No."
            mom "Thank you."
            $authority.trait_up(2)
            show authorityup at attributeup
            bailiff "You may be seated."
            hide mai court4
            hide lara serious8
            jump lisavsmc
        else:
            show iris6 at left
            districtattorney "By requesting Miss Amaya to create two financial reports, the defendant was knowingly participating in fraud."
            districtattorney "That concludes my questioning."
            bailiff "You may be seated."
            hide iris6
            hide mai court3
            jump lisavsmc
    else:
        jump lisavsmc

label lisavsmc:
    if lisatestifies == False:
        scene courthouse
        districtattorney "The People call Alyssa Rogers to the stand."
        bailiff "Please raise your hand."
        bailiff "Do you promise that the testimony you shall give in the case before this court shall be the truth, the whole truth, and nothing but the truth?"
        scene lisaswearsoath
        lisa "I do."
        bailiff "For the record, please state your name."
        lisa "Alyssa Rogers."
        scene courthouse
        show iris5 at left
        districtattorney "If you could please, state your position at SPH."
        show lisa court1 at right
        lisa "Customer Service Representative."
        districtattorney "What were your duties as a Customer Service Representative?"
        lisa "To deal with customer's problems."
        districtattorney "Just customers or also investors?"
        show lisa court3 at right
        lisa "Investors as well."
        show iris6 at left
        districtattorney "And how exactly did you help with investors?"
        lisa "I convinced them to buy and keep stock in the company."
        districtattorney "Even though the company was bleeding money?"
        if lisacrossexam == True:
            lisa "Yes I-"
            hide iris6
            mom "Objection."
            judge "Proceed."
            show lara angry2 at left
            mom "Were you aware of the company's real financial position before my client arrived?"
            show lisa court4 at right
            lisa "Real financial position?"
            show lara angry7 at left
            mom "According to the records, the company was not-and never- in the red."
            show lisa court5 at right
            lisa "Uhm. no."
            mom "And did you continue doing this job after my client arrived?"
            lisa "I...No."
            mom "Thank you."
            hide lara angry7
            $authority.trait_down(1)
            show authoritydown at attributedown
            bailiff "You may be seated."
            hide lisa court5
            jump kimvsmc
        else:
            show lisa court1 at right
            lisa "Yes."
            districtattorney "And you did this while the defendant was in charge?"
            lisa "Yes."
            districtattorney "Did the defendant request to stop you at any time?"
            show lisa court6 at right
            lisa "No."
            districtattorney "That concludes my questioning."
            hide iris6
            hide lisa court6
            bailiff "You may be seated."
            jump kimvsmc
    else:
        jump kimvsmc

label kimvsmc:
    if kimtestifies == False:
        scene courthouse
        districtattorney "The People call Kimberly Taylor to the stand."
        scene kimswearsoath
        bailiff "Please raise your hand."
        bailiff "Do you promise that the testimony you shall give in the case before this court shall be the truth, the whole truth, and nothing but the truth?"
        kim "I do."
        bailiff "For the record, please state your name."
        kim "Kimberly Taylor."
        scene courthouse
        show iris3 at left
        districtattorney "If you could please, state your position at SPH."
        show kim court2 at right
        kim "Executive Assistant."
        districtattorney "And what did you assist the owner of SPH with?"
        kim "Setting up meetings, depositing checks, anything that was asked of me."
        if kimcrossexam == True:
            hide iris3
            mom "Objection."
            judge "Proceed."
            show lara angry2 at left
            mom "Were any of those responsibilites done when my client was in office?"
            show kim court4 at right
            kim "...No."
            mom "Was there anything my client asked of you while you were in office?"
            districtattorney "Objection."
            judge "Denied."
            kim "No."
            mom "Thank you."
            hide lara angry2
            $authority.trait_up(2)
            show authorityup at attributeup
            bailiff "You may be seated."
            hide kim court4
            jump crissyvsmc
        else:
            districtattorney "Even if it was embezzling money?"
            show kim court4 at right
            kim "Yes."
            districtattorney "Thank you, that concludes my questioning."
            bailiff "You may be seated."
            jump crissyvsmc
    else:
        jump crissyvsmc


label crissyvsmc:
    districtattorney "The People call Officer Christina McNeill to the stand."
    mom "Here's our chance."
    scene crissyswearsoath
    bailiff "Please raise your hand."
    bailiff "Do you promise that the testimony you shall give in the case before this court shall be the truth, the whole truth, and nothing but the truth?"
    crissy "I do."
    bailiff "For the record, please state your name."
    scene courthouse
    show crissy court2 at right
    crissy "{i}Detective {/i}Christina McNeill."

    districtattorney "Detective McNeill, would you care to explain your time at Shilling Publishing and Holding?"
    crissy "Yes, I was there to investigate any fraudulent activity at the firm under the guise of a new hire."
    show lara angry6 at left
    mom "Objection."
    judge "Proceed."
    mom "Miss McNeill, why did you-and the prosecution- decide to go under cover at the firm?"
    show crissy court3 at right
    crissy "I-uh-"
    districtattorney "Objection. Question irrelevant to the case."
    show lara serious2 at left
    mom "Oh I disagree. My client would have willingly consented to work with the authorities if you had been upfront about your intentions."
    if crissycrossexam == True:
        show lara smile3 at left
        mom "Otherwise the witness would have not compromised both my client and herself in getting the information you need."
        districtattorney "Objection."
        judge "Denied. Proceed."
        show lara serious9 at left
        mom "My client attests that the witness on the stand, Officer McNeill, routinely forced herself onto him when caught investigating his office."
        mom "Causing my client to make decisions while under {i}significant{/i} duress."
        mom "I do believe this goes outside of her duties."
        show lara angry3 at left
        mom "Requesting to strike Officer McNeill's testimony from the trial."
        judge "Is this true, Officer McNeill?"
        $charm.trait_up(5)
        $authority.trait_up(5)
        show authorityup at attributeup
        show crissy court4 at right
        crissy "...Yes."
        judge "Request granted. You may be seated."
        hide lara angry3
        hide crissy court4
        jump prosecutiondone
    else:
        districtattorney "Your Honor, The State has tried to cooperate with SPH in the past and failed. An undercover investigation was necessary."
        show lara serious8 at left
        mom "That was prior to when my client arrived to the firm."
        mom "My client had no warning that the authorities were investigating him."
        mom "Which means that Officer McNeill was conducting unlawful search and seizure."
        districtattorney "The search warrant, Your Honor."
        show lara angry6 at left
        mom "In which the evidence to obtain it was retrieved outside of Officer McNeill's jurisidiction."
        judge "Is that true, Officer McNeill?"
        if crissytestifies == True:
            show crissy court4 at right
            crissy "Yes."
            mom "Request to strike Officer McNeill's testimony from the trial."
            judge "Request granted. You may be seated."
            $charm.trait_up(5)
            $authority.trait_up(5)
            hide crissy court4
            hide lara angry6
            show authorityup at attributeup
            jump prosecutiondone
        else:
            show crissy court2 at right
            crissy "......"
            crissy "No. Your Honor."
            crissy "[player_name] Shilling permitted me access to his office, allowing me to investigate."
            crissy "Everything was obtained lawfully."
            "(Bullshit!)"
            judge "I see, thank you."
            judge "You may be seated."
            hide lara angry6
            hide crissy court2
            jump prosecutiondone

label prosecutiondone:
    districtattorney "Your Honor, the People rest their case."
    judge"Is the defense ready with its case?"
    mom "Yes, Your Honor."
    jump defensescase


label defensescase:
    if maitestifies == True:
        scene maiswearsoath with fade
        mom "The defense calls Mai Amaya to the stand."
        mom "For the record, will you state your name."
        mai "Mai Amaya."
        scene courthouse
        show lara serious10 at left
        mom "And your position at Shilling Publishing and Holding."
        show mai court5 at right
        mai "Accounting."
        mom "Can you describe your responsibilites there?"
        mai "I was in charge of creating financial reports."
        show lara smile7 at left
        mom "My client found a discrepncy between the financial data his father left him and the one you provided."
        mom "Were you instructed to falsify data in your financial reports?"
        show mai court4 at right
        mai "Yes."
        show lara serious9 at left
        mom "And who instructred you to falsify that data?"
        mai "John Shilling."
        mom "So not my client, correct?"
        show mai court3 at right
        mai "Correct."
        show lara serious10 at left
        mom "One last question Miss Amaya."
        mom "Did you falsify the data based on an immient reward from Mr. John Shilling?"
        $charm.trait_up(5)
        $authority.trait_up(5)
        show charmup at attributeup
        show mai court2 at right
        mai "Yes."
        mom "Thank you."
        hide lara serious10
        hide mai court2
        jump lisaformc
    else:
        jump lisaformc

    label lisaformc:
        if lisatestifies == True:
            scene lisaswearsoath
            mom "The defense calls Alyssa Rogers to the stand."
            mom "For the record, will you state your name."
            lisa "Alyssa Rogers."
            scene courthouse
            show lara serious10 at left
            mom "And your position at Shilling Publishing and Holdings."
            show lisa court2 at right
            lisa "Customer service representative."
            mom "Could you describe your job description?"
            lisa "It was to convince investors to buy stock in the company."
            lisa "And to rectify any problems with the software."
            show lara smile3 at left
            mom "Thank you. In regards to the first task, were you assisted by the accountant?"
            show lisa court5 at right
            lisa "I don't understand."
            show lara serious2 at left
            mom "Did you use financial records created by the accountant, Miss Mai Amaya, in order to complete your first task?"
            show lisa court3 at right
            lisa "Yes."
            mom "And did you do so by the request of my client?"
            lisa "No."
            show lara serious8 at left
            mom "So you convinced investors to buy stock at the request of someone other than my client, correct?"
            $charm.trait_up(5)
            $authority.trait_up(5)
            show charmup at attributeup
            show lisa court6 at right
            lisa "Correct."
            mom "Thank you."
            hide lisa court6
            hide lara serious8
            jump kimformc
        else:
            jump kimformc


    label kimformc:
        if kimtestifies == True:
            scene kimswearsoath
            mom "The defense calls Kimberly Taylor to the stand."
            mom "For the record, will you state your name."
            kim "Kimberly Taylor."
            scene courthouse
            show lara serious8 at left
            mom "And your position at Shilling Publishing and Holdings."
            show kim court1 at right
            kim "Executive Assistant until two weeks ago."
            show lara angry6 at left
            mom "And what exactly did you assist my client with?"
            show kim court3 at right
            kim "Uh. I had submitted my two weeks notice when the defendant started. "
            mom "So you didn't assist my client with anything?"
            kim "No."
            $charm.trait_up(5)
            $authority.trait_up(5)
            show charmup at attributeup
            mom "Anything to do with stealing funds or-"
            show kim court3 at right
            kim "No, [player_name] did not ask me to do any of that."
            show lara smile3
            mom "Thank you."
            hide lara smile3
            hide kim court3
            jump bellaformc
        else:
            jump bellaformc


    label bellaformc:
        if bellatestifies == True:
            scene bellaswearsoath
            mom "The defense calls Isabella Cole to the stand."
            mom "For the record, will you state your name."
            bella "Isabella Cole."
            scene courthouse
            show lara serious10 at left
            mom "And your position at Shilling Publishing and Holdings."
            bella "IT- Information Technology Specialist."
            mom "And what exactly were your responsibilities in that position?"
            show bella court2 at right
            bella "To make sure that the software was running as designed."
            show lara serious8 at left
            mom "Were there any other duties that you were assigned?"
            show bella court5 at right
            bella "No."
            mom "At the time that my client was in office, did he request any information from you?"
            $charm.trait_up(5)
            $authority.trait_up(5)
            show charmup at attributeup
            bella "No."
            mom "Thank you."
            hide bella court5
            hide lara serious8
            jump defenseend
        else:
            jump defenseend





label defenseend:
    scene courthouse
    show judge1 at center
    judge "Does the defense rest?"
    mom "Yes, Your Honor."
    judge "Are you ready with the final arguments?"
    districtattorney "Yes, Your Honor."
    mom"Yes, Your Honor."
    hide judge1
    scene daending
    districtattorney "Your Honor,according to the testimony provided today along with the evidence, we can conclude the following:"
    districtattorney "That the defendant, after taking over the company from his father, proceeded to embezzle funds into a personal bank account"
    scene maiincriminate
    districtattorney "That he instructed his accountant to falsify financial data,"
    scene lisaincriminate
    districtattorney "Permitted his customer service representative to gain investor confidence with the data,"
    scene kimincriminate
    districtattorney "And embezzled the funds with the aid of his executive assistant."
    scene daending
    districtattorney "These acts alone prove that  [player_name] Shilling participated in investor fraud, embezzlement and money laundering, Your Honor."
    scene momrebuttal
    mom "Your Honor,there is a reasonable doubt to the prosecution's case against the defendant."
    mom "That all of the incidents related to the charges occurred before my client arrived at SPH."
    mom" Therefore, you must find [player_name]Shilling not guilty of investor fraud, money laundering, and embezzlement as he had nothing to do with the activity."
    jump sentencing

label sentencing:
    if charm.amount >=4 and authority.amount >=4:
        scene courthouse
        judge "[player_name] Shilling, please rise."
        judge "You stand accused of investor fraud, embezzlement and money laundering."
        scene notguiltyverdict
        judge "You are found not guilty on all charges. You are free to leave."
        judge "Court is adjourned."
        "(It's over..)"
        stop music
        jump goodending
    else:
        scene courthouse
        judge "[player_name] Shilling, please rise."
        judge "You stand accused of  investor fraud, embezzlement and money laundering."
        judge "On the accounts of embezzlement and money laundering, the court finds you not guilty."
        scene guiltyverdict
        judge "However, the Court finds you guilty of investor fraud."
        judge "I, Judge Marshall sentence you to a $50 000 fine, liquidation of assets and 90 days of prison, followed by 3 years of probation."
        judge "Court is adjourned."
        scene mcinhandcuffs
        "(So this is how it ends.)"
        mom "I'm sorry, [player_name]."
        mom "I tried to get you off of all of the charges."
        main "Thanks, mom."
        stop music
        jump badending2
