


## Characters ##
define mai = Character ("Mai", image= "mai", ctc="ctc", ctc_position="nestled")
define lisa = Character ("Lisa", image = "lisa" ,ctc="ctc", ctc_position="nestled")
define bella = Character ("Bella", image = "bella", ctc="ctc", ctc_position="nestled")
define kim = Character ("Kim", image = "kim", ctc="ctc", ctc_position="nestled")
define crissy = Character("Christina", image = "crissy" , ctc="ctc", ctc_position="nestled")
define dad = Character ("Dad",image= "dad", ctc="ctc", ctc_position="nestled")
define mom = Character("Mom", image = "mom", ctc="ctc", ctc_position="nestled")

define unvoice = Character ("Unknown Voice",ctc="ctc", ctc_position="nestled")
define unwoman = Character ("Unknown Woman", ctc="ctc", ctc_position="nestled")
define main= Character("[player_name]", ctc="ctc", ctc_position="nestled")
define narrator = Character(ctc="ctc", ctc_position="nestled")
define newsreporter = Character("News Reporter", ctc="ctc", ctc_position="nestled")
define incel = Character("Gym Regular", ctc="ctc", ctc_position="nestled")
define officer = Character("Officer", ctc="ctc", ctc_position="nestled")
define judge = Character("Judge", ctc="ctc", ctc_position="nestled")
define districtattorney = Character("District Attorney", ctc="ctc", ctc_position="nestled")
define priest = Character ("Priest", ctc="ctc", ctc_position="nestled")
define bailiff = Character ("Bailiff", ctc= "ctc", ctc_position="nestled")

#Background Images #
image bellaslab = "images/bg/bellalab.webp"
image cityhall = "images/bg/cityhall.webp"
image courthouse = "images/bg/courthouse.webp"
image gym = "images/bg/gym.webp"
image kimsapartment = "images/bg/kimapt.webp"
image kimsbed = "images/bg/kimapt2.webp"
image frontdesk = "images/bg/lower1.webp"
image downstairsoffice = "images/bg/lower2.webp"
image downstairsdesk = "images/bg/lower3.webp"
image downstairswindow = "images/bg/lower4.webp"
image downstairslounge = "images/bg/lower5.webp"
image kimsoffice = "images/bg/lower6.webp"
image downstairssofa = "images/bg/lower7.webp"
image meetingoffice = "images/bg/lower9.webp"
image elevator = "images/bg/lower10.webp"
image frontdesk2 = "images/bg/lower11.webp"
image mcsapartment = "images/bg/mcapt1.webp"
image mcsbed = "images/bg/mcapt2.webp"
image mcsbathroom = "images/bg/mcapt3.webp"
image mcsdoor = "images/bg/mcapt4.webp"
image mcskitchen = "images/bg/mcapt5.webp"
image newhouse = "images/bg/newhouse.webp"
image newsreport = "images/bg/newsreporter.webp"
image nyapartment = "images/bg/nycapartment.webp"
image outsideoffice = "images/bg/outsideoffice.webp"
image outsidepolice = "images/bg/outsidepolice.webp"
image policestation = "images/bg/policestation.webp"
image restaurant = "images/bg/restaurant.webp"
image upstairslounge = "images/bg/upper1.webp"
image upstairslounge2 = "images/bg/upper2.webp"
image shelves = "images/bg/upper3.webp"
image upstairsdesk = "images/bg/upper4.webp"
image upstairschair = "images/bg/upper5.webp"
image computer = "images/bg/upper6.webp"
image upstairshall = "images/bg/upper7.webp"
image downstairsdeskpng = "images/bg/lower3.png"

image frontdeskclear = "images/bg/frontdesk2.webp"




## Stats ##
default cMai = Contact ("Mai Amaya", "Accountant",  morale=0, moralemax=10)
default cLisa = Contact ("Alyssa Rogers", "Customer Relations and Support", morale=0, moralemax=10)
default cBella = Contact ("Isabella Cole", "Informational and Technical Support",  morale=0, moralemax=10)
default cKim = Contact ("Kimberly Taylor", "Executive Assistant", morale=0, moralemax=10)
default cCrissy = Contact ("Christina McNeill", "Auditor", morale=0, moralemax=10)

default charm = Trait("Charm", amount= 0, max = 20)
default authority = Trait ("Authority", amount =0, max = 20)

default playtime = 0
default persistent.sexscenes = False



label start:
    stop music

    scene disclaimer
    show text "This is a work of fiction." with Pause (1)
    show text "All names, characters, businesses,places, events, locales, and incidents are either products of the author's imagination or used in a fictitous manner." with Pause (2)
    show text "Any resemblance to actual persons, living or dead, or actual events is purely coincidental."

    menu:
        "Are you 18 years old?"
        "Yes":
            jump sexscenesdecision

        "No":
            $ renpy.quit()

label sexscenesdecision:
    show text "All sexual activity in this work consensual and all characters are over the age of 21."

    menu:
        "Show Sex Scenes?"
        "Show Sex Scenes":
            $persistent.sexscenes = True
            "All explicit sex scenes will be shown."
            "You can change this filter in the {b}Options{/b} menu."
            jump timedchoicesdecision
        "Hide Sex Scenes":
            "All explicit sex scenes will be skipped automatically. Some nudity will be still be shown."
            "You can change this filter in the {b}Options{/b} menu."
            jump timedchoicesdecision

label timedchoicesdecision:
    show text "Some decisions in this game are timed. For more relaxing gameplay, you can turn timed choices off."
    menu:
        "Turn Timed Choices on?"
        "Timed Choices On":
            jump chapter1
        "Timed Choices Off":
            $persistent.timed_choices = False
            jump chapter1
