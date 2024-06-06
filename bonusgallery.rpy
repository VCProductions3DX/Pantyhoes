
screen bonusgallery():


    add gui.game_menu_background
    label _("Character Gallery") xpos 10 ypos 10 style "taskline_label"

    vbox:
        style_prefix "gallery_nav"


        textbutton _("Bella") action Show("gallery_a")
        textbutton _("Christina") action Show("gallery_b")
        textbutton _("Kim") action Show("gallery_c")
        textbutton _("Lisa") action Show("gallery_d")
        textbutton _("Mai") action Show ("gallery_e")

    textbutton _("Return") action [Return(), Hide("bonusgallery")] xalign 0.97 yalign 0.95


style gallery_nav_vbox:
    xalign 0.03
    yalign 0.5
    spacing 40

screen gallery_a():

    default cg_page_a = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_a", 1)
        textbutton _("2") action SetLocalVariable("cg_page_a", 2)


    showif cg_page_a == 1:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_bellagallery01","bonus/thumbnails/bellabonus1.webp")
            add g.make_button("cg_bellagallery02","bonus/thumbnails/bellabonus2.webp")
            add g.make_button("cg_bellagallery03","bonus/thumbnails/bellabonus3.webp")
            add g.make_button("cg_bellagallery04","bonus/thumbnails/bellabonus4.webp")
            add g.make_button("cg_bellagallery05","bonus/thumbnails/bellabonus5.webp")
            add g.make_button("cg_bellagallery06","bonus/thumbnails/bellabonus6.webp")
            add g.make_button("cg_bellagallery07","bonus/thumbnails/bellabonus7.webp")
            add g.make_button("cg_bellagallery08","bonus/thumbnails/bellabonus8.webp")
            add g.make_button("cg_bellagallery09","bonus/thumbnails/bellabonus19.webp")
            add g.make_button("cg_bellagallery10","bonus/thumbnails/bellabonus20.webp")
            add g.make_button("cg_bellagallery11","bonus/thumbnails/bellabonus11.webp")
            add g.make_button("cg_bellagallery12","bonus/thumbnails/bellabonus12.webp")
            add g.make_button("cg_bellagallery13","bonus/thumbnails/bellabonus21.webp")
            add g.make_button("cg_bellagallery14","bonus/thumbnails/bellabonus22.webp")
            add g.make_button("cg_bellagallery15","bonus/thumbnails/bellabonus23.webp")
            add g.make_button("cg_bellagallery16","bonus/thumbnails/bellabonus24.webp")

            add g.make_button("cg_bellagallery17","bonus/thumbnails/bellabonus9.webp")
            add g.make_button("cg_bellagallery18","bonus/thumbnails/bellabonus10.webp")
            add g.make_button("cg_bellagallery19","bonus/thumbnails/bellabonus13.webp")
            add g.make_button("cg_bellagallery20","bonus/thumbnails/bellabonus14.webp")
            add g.make_button("cg_bellagallery21","bonus/thumbnails/bellabonus15.webp")
            add g.make_button("cg_bellagallery22","bonus/thumbnails/bellabonus16.webp")
            add g.make_button("cg_bellagallery23","bonus/thumbnails/bellabonus17.webp")
            add g.make_button("cg_bellagallery24","bonus/thumbnails/bellabonus18.webp")
            add g.make_button("cg_bellagallery25","bonus/thumbnails/bellabonus25.webp")




    elif cg_page_a == 2:
        grid 3 2:
            style_prefix "gallery_stuff"
            add g.make_button("cg_bellagallery26","bonus/thumbnails/bellabonus26.webp")
            add g.make_button("cg_bellagallery27","bonus/thumbnails/bellabonus27.webp")
            add g.make_button("cg_bellagallery28","bonus/thumbnails/bellabonus28.webp")
            add g.make_button("cg_bellagallery29","bonus/thumbnails/bellabonus29.webp")
            add g.make_button("cg_bellagallery30","bonus/thumbnails/bellabonus30.webp")
            null





screen gallery_b():

    default cg_page_b = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_b", 1)
        textbutton _("2") action SetLocalVariable("cg_page_b", 2)
        textbutton _("3") action SetLocalVariable("cg_page_b", 3)

    showif cg_page_b == 1:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_crissygallery01","bonus/thumbnails/crissybonus1.webp")
            add g.make_button("cg_crissygallery02","bonus/thumbnails/crissybonus2.webp")
            add g.make_button("cg_crissygallery03","bonus/thumbnails/crissybonus3.webp")
            add g.make_button("cg_crissygallery04","bonus/thumbnails/crissybonus4.webp")
            add g.make_button("cg_crissygallery05","bonus/thumbnails/crissybonus5.webp")
            add g.make_button("cg_crissygallery06","bonus/thumbnails/crissybonus7.webp")
            add g.make_button("cg_crissygallery07","bonus/thumbnails/crissybonus8.webp")
            add g.make_button("cg_crissygallery08","bonus/thumbnails/crissybonus9.webp")
            add g.make_button("cg_crissygallery09","bonus/thumbnails/crissybonus10.webp")
            add g.make_button("cg_crissygallery10","bonus/thumbnails/crissybonus17.webp")
            add g.make_button("cg_crissygallery11","bonus/thumbnails/crissybonus18.webp")
            add g.make_button("cg_crissygallery12","bonus/thumbnails/crissybonus19.webp")
            add g.make_button("cg_crissygallery13","bonus/thumbnails/crissybonus20.webp")
            add g.make_button("cg_crissygallery14","bonus/thumbnails/crissybonus21.webp")
            add g.make_button("cg_crissygallery15","bonus/thumbnails/crissybonus22.webp")
            add g.make_button("cg_crissygallery16","bonus/thumbnails/crissybonus23.webp")

            add g.make_button("cg_crissygallery17","bonus/thumbnails/crissybonus6.webp")
            add g.make_button("cg_crissygallery18","bonus/thumbnails/crissybonus11.webp")
            add g.make_button("cg_crissygallery19","bonus/thumbnails/crissybonus12.webp")
            add g.make_button("cg_crissygallery20","bonus/thumbnails/crissybonus13.webp")
            add g.make_button("cg_crissygallery21","bonus/thumbnails/crissybonus14.webp")
            add g.make_button("cg_crissygallery22","bonus/thumbnails/crissybonus15.webp")
            add g.make_button("cg_crissygallery23","bonus/thumbnails/crissybonus16.webp")
            add g.make_button("cg_crissygallery24","bonus/thumbnails/crissybonus24.webp")
            add g.make_button("cg_crissygallery25","bonus/thumbnails/crissybonus25.webp")


    elif cg_page_b == 2:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_crissygallery26","bonus/thumbnails/crissybonus26.webp")
            add g.make_button("cg_crissygallery27","bonus/thumbnails/crissybonus27.webp")
            add g.make_button("cg_crissygallery28","bonus/thumbnails/crissybonus28.webp")
            add g.make_button("cg_crissygallery29","bonus/thumbnails/crissybonus29.webp")
            add g.make_button("cg_crissygallery30","bonus/thumbnails/crissybonus30.webp")
            add g.make_button("cg_crissygallery31","bonus/thumbnails/crissybonus31.webp")
            add g.make_button("cg_crissygallery32","bonus/thumbnails/crissybonus32.webp")
            add g.make_button("cg_crissygallery33","bonus/thumbnails/crissybonus33.webp")
            add g.make_button("cg_crissygallery34","bonus/thumbnails/crissybonus34.webp")
            add g.make_button("cg_crissygallery35","bonus/thumbnails/crissybonus35.webp")
            add g.make_button("cg_crissygallery36","bonus/thumbnails/crissybonus36.webp")
            add g.make_button("cg_crissygallery37","bonus/thumbnails/crissybonus37.webp")
            add g.make_button("cg_crissygallery38","bonus/thumbnails/crissybonus38.webp")
            add g.make_button("cg_crissygallery39","bonus/thumbnails/crissybonus39.webp")
            add g.make_button("cg_crissygallery40","bonus/thumbnails/crissybonus40.webp")
            add g.make_button("cg_crissygallery41","bonus/thumbnails/crissybonus41.webp")
            add g.make_button("cg_crissygallery42","bonus/thumbnails/crissybonus42.webp")
            add g.make_button("cg_crissygallery43","bonus/thumbnails/crissybonus43.webp")
            add g.make_button("cg_crissygallery44","bonus/thumbnails/crissybonus44.webp")
            add g.make_button("cg_crissygallery45","bonus/thumbnails/crissybonus45.webp")
            add g.make_button("cg_crissygallery46","bonus/thumbnails/crissybonus46.webp")
            add g.make_button("cg_crissygallery47","bonus/thumbnails/crissybonus47.webp")
            add g.make_button("cg_crissygallery48","bonus/thumbnails/crissybonus48.webp")
            add g.make_button("cg_crissygallery49","bonus/thumbnails/crissybonus49.webp")
            add g.make_button("cg_crissygallery51","bonus/thumbnails/crissybonus51.webp")

    elif cg_page_b == 3:
        grid 3 3:
            style_prefix "gallery_stuff"
            add g.make_button("cg_crissygallery52","bonus/thumbnails/crissybonus52.webp")
            add g.make_button("cg_crissygallery53","bonus/thumbnails/crissybonus53.webp")
            add g.make_button("cg_crissygallery54","bonus/thumbnails/crissybonus54.webp")
            add g.make_button("cg_crissygallery55","bonus/thumbnails/crissybonus55.webp")
            add g.make_button("cg_crissygallery56","bonus/thumbnails/crissybonus56.webp")
            add g.make_button("cg_crissygallery57","bonus/thumbnails/crissybonus57.webp")
            add g.make_button("cg_crissygallery58","bonus/thumbnails/crissybonus58.webp")
            add g.make_button("cg_crissygallery59","bonus/thumbnails/crissybonus59.webp")
            null

screen gallery_c():

    default cg_page_c = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"
        textbutton _("1") action SetLocalVariable("cg_page_c", 1)
        if persistent.kimgoodending == True:
            textbutton _("2") action SetLocalVariable("cg_page_c", 2)
            textbutton _("3") action SetLocalVariable("cg_page_c", 3)
            textbutton _("4") action SetLocalVariable("cg_page_c", 4)

    showif cg_page_c == 1:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_kimgallery01","bonus/thumbnails/kimbonus1.webp")
            add g.make_button("cg_kimgallery02","bonus/thumbnails/kimbonus2.webp")
            add g.make_button("cg_kimgallery03","bonus/thumbnails/kimbonus3.webp")
            add g.make_button("cg_kimgallery04","bonus/thumbnails/kimintro.webp")
            add g.make_button("cg_kimgallery05","bonus/thumbnails/kimbonus5.webp")
            add g.make_button("cg_kimgallery06","bonus/thumbnails/kimbonus6.webp")
            add g.make_button("cg_kimgallery07","bonus/thumbnails/kimbonus7.webp")
            add g.make_button("cg_kimgallery08","bonus/thumbnails/kimbonus8.webp")
            add g.make_button("cg_kimgallery09","bonus/thumbnails/kimbonus9.webp")
            add g.make_button("cg_kimgallery10","bonus/thumbnails/kimbonus12.webp")
            add g.make_button("cg_kimgallery11","bonus/thumbnails/kimbonus13.webp")
            add g.make_button("cg_kimgallery12","bonus/thumbnails/kimbonus14.webp")
            add g.make_button("cg_kimgallery13","bonus/thumbnails/kimbonus22.webp")
            add g.make_button("cg_kimgallery14","bonus/thumbnails/kimbonus23.webp")
            add g.make_button("cg_kimgallery15","bonus/thumbnails/kimbonus24.webp")
            add g.make_button("cg_kimgallery16","bonus/thumbnails/kimbonus25.webp")
            add g.make_button("cg_kimgallery17","bonus/thumbnails/kimbonus26.webp")

            add g.make_button("cg_kimgallery18","bonus/thumbnails/kimbonus4.webp")
            add g.make_button("cg_kimgallery19","bonus/thumbnails/kimbonus10.webp")
            add g.make_button("cg_kimgallery20","bonus/thumbnails/kimbonus11.webp")
            add g.make_button("cg_kimgallery21","bonus/thumbnails/kimbonus15.webp")
            add g.make_button("cg_kimgallery22","bonus/thumbnails/kimbonus16.webp")
            add g.make_button("cg_kimgallery23","bonus/thumbnails/kimbonus17.webp")
            add g.make_button("cg_kimgallery24","bonus/thumbnails/kimbonus18.webp")
            add g.make_button("cg_kimgallery25","bonus/thumbnails/kimbonus19.webp")


    elif cg_page_c == 2:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_kimgallery26","bonus/thumbnails/kimbonus20.webp")
            add g.make_button("cg_kimgallery27","bonus/thumbnails/kimbonus21.webp")
            add g.make_button("cg_kimgallery28","bonus/thumbnails/kimbonus28.webp")
            add g.make_button("cg_kimgallery29","bonus/thumbnails/kimbonus29.webp")
            add g.make_button("cg_kimgallery30","bonus/thumbnails/kimbonus30.webp")
            add g.make_button("cg_kimgallery31","bonus/thumbnails/kimbonus31.webp")
            add g.make_button("cg_kimgallery32","bonus/thumbnails/kimbonus32.webp")
            add g.make_button("cg_kimgallery33","bonus/thumbnails/kimbonus33.webp")
            add g.make_button("cg_kimgallery34","bonus/thumbnails/kimbonus34.webp")
            add g.make_button("cg_kimgallery35","bonus/thumbnails/kimbonus35.webp")
            add g.make_button("cg_kimgallery36","bonus/thumbnails/kimbonus36.webp")
            add g.make_button("cg_kimgallery37","bonus/thumbnails/kimbonus37.webp")
            add g.make_button("cg_kimgallery38","bonus/thumbnails/kimbonus38.webp")
            add g.make_button("cg_kimgallery39","bonus/thumbnails/kimbonus39.webp")
            add g.make_button("cg_kimgallery40","bonus/thumbnails/kimbonus40.webp")
            add g.make_button("cg_kimgallery41","bonus/thumbnails/kimbonus41.webp")
            add g.make_button("cg_kimgallery42","bonus/thumbnails/kimbonus42.webp")
            add g.make_button("cg_kimgallery43","bonus/thumbnails/kimbonus43.webp")
            add g.make_button("cg_kimgallery44","bonus/thumbnails/kimbonus44.webp")
            add g.make_button("cg_kimgallery45","bonus/thumbnails/kimbonus45.webp")
            add g.make_button("cg_kimgallery46","bonus/thumbnails/kimbonus46.webp")
            add g.make_button("cg_kimgallery47","bonus/thumbnails/kimbonus47.webp")
            add g.make_button("cg_kimgallery48","bonus/thumbnails/kimbonus48.webp")
            add g.make_button("cg_kimgallery49","bonus/thumbnails/kimbonus49.webp")
            add g.make_button("cg_kimgallery50","bonus/thumbnails/kimbonus50.webp")

    elif cg_page_c == 3:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_kimgallery51","bonus/thumbnails/kimbonus51.webp")
            add g.make_button("cg_kimgallery52","bonus/thumbnails/kimbonus52.webp")
            add g.make_button("cg_kimgallery53","bonus/thumbnails/kimbonus53.webp")
            add g.make_button("cg_kimgallery54","bonus/thumbnails/kimbonus54.webp")
            add g.make_button("cg_kimgallery55","bonus/thumbnails/kimbonus55.webp")
            add g.make_button("cg_kimgallery56","bonus/thumbnails/kimbonus56.webp")
            add g.make_button("cg_kimgallery57","bonus/thumbnails/kimbonus57.webp")
            add g.make_button("cg_kimgallery58","bonus/thumbnails/kimbonus58.webp")
            add g.make_button("cg_kimgallery59","bonus/thumbnails/kimbonus59.webp")
            add g.make_button("cg_kimgallery60","bonus/thumbnails/kimbonus60.webp")
            add g.make_button("cg_kimgallery61","bonus/thumbnails/kimbonus61.webp")
            add g.make_button("cg_kimgallery62","bonus/thumbnails/kimbonus62.webp")
            add g.make_button("cg_kimgallery63","bonus/thumbnails/kimbonus63.webp")
            add g.make_button("cg_kimgallery64","bonus/thumbnails/kimbonus64.webp")
            add g.make_button("cg_kimgallery65","bonus/thumbnails/kimbonus65.webp")
            add g.make_button("cg_kimgallery66","bonus/thumbnails/kimbonus66.webp")
            add g.make_button("cg_kimgallery67","bonus/thumbnails/kimbonus67.webp")
            add g.make_button("cg_kimgallery68","bonus/thumbnails/kimbonus68.webp")
            add g.make_button("cg_kimgallery69","bonus/thumbnails/kimbonus69.webp")
            add g.make_button("cg_kimgallery70","bonus/thumbnails/kimbonus70.webp")
            add g.make_button("cg_kimgallery71","bonus/thumbnails/kimbonus71.webp")
            add g.make_button("cg_kimgallery72","bonus/thumbnails/kimbonus72.webp")
            add g.make_button("cg_kimgallery73","bonus/thumbnails/kimbonus73.webp")
            add g.make_button("cg_kimgallery74","bonus/thumbnails/kimbonus74.webp")
            add g.make_button("cg_kimgallery75","bonus/thumbnails/kimbonus75.webp")

    elif cg_page_c == 4:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_kimgallery76","bonus/thumbnails/kimbonus76.webp")
            add g.make_button("cg_kimgallery77","bonus/thumbnails/kimbonus77.webp")
            add g.make_button("cg_kimgallery78","bonus/thumbnails/kimbonus78.webp")
            add g.make_button("cg_kimgallery79","bonus/thumbnails/kimbonus79.webp")
            add g.make_button("cg_kimgallery80","bonus/thumbnails/kimbonus80.webp")
            add g.make_button("cg_kimgallery81","bonus/thumbnails/kimbonus81.webp")
            add g.make_button("cg_kimgallery82","bonus/thumbnails/kimbonus82.webp")
            add g.make_button("cg_kimgallery83","bonus/thumbnails/kimbonus83.webp")
            add g.make_button("cg_kimgallery84","bonus/thumbnails/kimbonus84.webp")
            add g.make_button("cg_kimgallery85","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery86","bonus/thumbnails/kimbonus86.webp")
            add g.make_button("cg_kimgallery87","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery88","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery89","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery90","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery91","bonus/thumbnails/kimbonus85.webp")
            add g.make_button("cg_kimgallery92","bonus/thumbnails/kimbonus75.webp")
            add g.make_button("cg_kimgallery93","bonus/thumbnails/kimbonus75.webp")
            add g.make_button("cg_kimgallery94","bonus/thumbnails/kimbonus87.webp")
            add g.make_button("cg_kimgallery95","bonus/thumbnails/kimbonus88.webp")
            add g.make_button("cg_kimgallery96","bonus/thumbnails/kimbonus89.webp")
            add g.make_button("cg_kimgallery97","bonus/thumbnails/kimbonus90.webp")
            add g.make_button("cg_kimgallery98","bonus/thumbnails/kimbonus91.webp")
            add g.make_button("cg_kimgallery99","bonus/thumbnails/kimbonus92.webp")
            null


screen gallery_d():

    default cg_page_d = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_d", 1)
        if persistent.lisagoodending == True:
            textbutton _("2") action SetLocalVariable("cg_page_d", 2)
            textbutton _("3") action SetLocalVariable("cg_page_d", 3)

    showif cg_page_d == 1:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_lisagallery01","bonus/thumbnails/lisabonus1.webp")
            add g.make_button("cg_lisagallery02","bonus/thumbnails/lisabonus2.webp")
            add g.make_button("cg_lisagallery03","bonus/thumbnails/lisabonus3.webp")
            add g.make_button("cg_lisagallery04","bonus/thumbnails/lisabonus4.webp")
            add g.make_button("cg_lisagallery05","bonus/thumbnails/lisabonus5.webp")
            add g.make_button("cg_lisagallery06","bonus/thumbnails/lisabonus6.webp")
            add g.make_button("cg_lisagallery07","bonus/thumbnails/lisabonus9.webp")
            add g.make_button("cg_lisagallery08","bonus/thumbnails/lisabonus10.webp")
            add g.make_button("cg_lisagallery09","bonus/thumbnails/lisabonus11.webp")
            add g.make_button("cg_lisagallery10","bonus/thumbnails/lisabonus19.webp")
            add g.make_button("cg_lisagallery11","bonus/thumbnails/lisabonus20.webp")
            add g.make_button("cg_lisagallery12","bonus/thumbnails/lisabonus21.webp")
            add g.make_button("cg_lisagallery13","bonus/thumbnails/lisabonus22.webp")
            add g.make_button("cg_lisagallery14","bonus/thumbnails/lisabonus23.webp")
            add g.make_button("cg_lisagallery15","bonus/thumbnails/lisabonus24.webp")
            add g.make_button("cg_lisagallery16","bonus/thumbnails/lisafootsiethumb.webp")
            add g.make_button("cg_lisagallery17","bonus/thumbnails/lisafootballthumb.webp")

            add g.make_button("cg_lisagallery18","bonus/thumbnails/lisabonus7.webp")
            add g.make_button("cg_lisagallery19","bonus/thumbnails/lisabonus8.webp")
            add g.make_button("cg_lisagallery20","bonus/thumbnails/lisabonus12.webp")
            add g.make_button("cg_lisagallery21","bonus/thumbnails/lisabonus13.webp")
            add g.make_button("cg_lisagallery22","bonus/thumbnails/lisabonus14.webp")
            add g.make_button("cg_lisagallery23","bonus/thumbnails/lisabonus15.webp")
            add g.make_button("cg_lisagallery24","bonus/thumbnails/lisabonus16.webp")
            add g.make_button("cg_lisagallery25","bonus/thumbnails/lisabonus17.webp")


    elif cg_page_d == 2:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_lisagallery26","bonus/thumbnails/lisabonus18.webp")
            add g.make_button("cg_lisagallery27","bonus/thumbnails/lisabonus27.webp")
            add g.make_button("cg_lisagallery28","bonus/thumbnails/lisabonus28.webp")
            add g.make_button("cg_lisagallery29","bonus/thumbnails/lisabonus29.webp")
            add g.make_button("cg_lisagallery30","bonus/thumbnails/lisabonus30.webp")
            add g.make_button("cg_lisagallery31","bonus/thumbnails/lisabonus31.webp")
            add g.make_button("cg_lisagallery32","bonus/thumbnails/lisabonus32.webp")
            add g.make_button("cg_lisagallery33","bonus/thumbnails/lisabonus33.webp")
            add g.make_button("cg_lisagallery34","bonus/thumbnails/lisabonus34.webp")
            add g.make_button("cg_lisagallery35","bonus/thumbnails/lisabonus35.webp")
            add g.make_button("cg_lisagallery37","bonus/thumbnails/lisabonus37.webp")
            add g.make_button("cg_lisagallery38","bonus/thumbnails/lisabonus38.webp")
            add g.make_button("cg_lisagallery39","bonus/thumbnails/lisabonus39.webp")
            add g.make_button("cg_lisagallery40","bonus/thumbnails/lisabonus40.webp")
            add g.make_button("cg_lisagallery41","bonus/thumbnails/lisabonus41.webp")
            add g.make_button("cg_lisagallery42","bonus/thumbnails/lisabonus42.webp")
            add g.make_button("cg_lisagallery43","bonus/thumbnails/lisabonus43.webp")
            add g.make_button("cg_lisagallery44","bonus/thumbnails/lisabonus44.webp")
            add g.make_button("cg_lisagallery45","bonus/thumbnails/lisabonus45.webp")
            add g.make_button("cg_lisagallery46","bonus/thumbnails/lisabonus46.webp")
            add g.make_button("cg_lisagallery47","bonus/thumbnails/lisabonus47.webp")
            add g.make_button("cg_lisagallery48","bonus/thumbnails/lisabonus48.webp")
            add g.make_button("cg_lisagallery49","bonus/thumbnails/lisabonus49.webp")
            add g.make_button("cg_lisagallery50","bonus/thumbnails/lisabonus50.webp")
            add g.make_button("cg_lisagallery51","bonus/thumbnails/lisabonus51.webp")

    elif cg_page_d == 3:
        grid 5 4:
            style_prefix "gallery_stuff"
            add g.make_button("cg_lisagallery52","bonus/thumbnails/lisabonus52.webp")
            add g.make_button("cg_lisagallery53","bonus/thumbnails/lisabonus53.webp")
            add g.make_button("cg_lisagallery54","bonus/thumbnails/lisabonus54.webp")
            add g.make_button("cg_lisagallery55","bonus/thumbnails/lisabonus55.webp")
            add g.make_button("cg_lisagallery57","bonus/thumbnails/lisabonus57.webp")
            add g.make_button("cg_lisagallery58","bonus/thumbnails/lisabonus58.webp")
            add g.make_button("cg_lisagallery59","bonus/thumbnails/lisabonus59.webp")
            add g.make_button("cg_lisagallery60","bonus/thumbnails/lisabonus60.webp")
            add g.make_button("cg_lisagallery62","bonus/thumbnails/lisabonus62.webp")
            add g.make_button("cg_lisagallery63","bonus/thumbnails/lisabonus63.webp")
            add g.make_button("cg_lisagallery64","bonus/thumbnails/lisabonus64.webp")
            add g.make_button("cg_lisagallery65","bonus/thumbnails/lisabonus65.webp")
            add g.make_button("cg_lisagallery66","bonus/thumbnails/lisabonus66.webp")
            add g.make_button("cg_lisagallery67","bonus/thumbnails/lisabonus67.webp")
            add g.make_button("cg_lisagallery68","bonus/thumbnails/lisabonus68.webp")
            add g.make_button("cg_lisagallery69","bonus/thumbnails/lisabonus69.webp")
            add g.make_button("cg_lisagallery70","bonus/thumbnails/lisabonus70.webp")
            add g.make_button("cg_lisagallery71","bonus/thumbnails/lisabonus71.webp")
            add g.make_button("cg_lisagallery72","bonus/thumbnails/lisabonus72.webp")
            add g.make_button("cg_lisagallery73","bonus/thumbnails/lisabonus73.webp")

screen gallery_e():

    default cg_page_e = 1

    zorder 100
    tag menu

    hbox:
        style_prefix "gallery_stuff"

        textbutton _("1") action SetLocalVariable("cg_page_e", 1)

        textbutton _("2") action SetLocalVariable("cg_page_e", 2)
        textbutton _("3") action SetLocalVariable("cg_page_e", 3)

    showif cg_page_e == 1:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_maigallery01","bonus/thumbnails/maibonus1.webp")
            add g.make_button("cg_maigallery02","bonus/thumbnails/maibonus2.webp")
            add g.make_button("cg_maigallery03","bonus/thumbnails/maibonus3.webp")
            add g.make_button("cg_maigallery04","bonus/thumbnails/maibonus4.webp")
            add g.make_button("cg_maigallery05","bonus/thumbnails/maibonus5.webp")
            add g.make_button("cg_maigallery06","bonus/thumbnails/maibonus6.webp")
            add g.make_button("cg_maigallery07","bonus/thumbnails/maibonus7.webp")
            add g.make_button("cg_maigallery08","bonus/thumbnails/maibonus8.webp")
            add g.make_button("cg_maigallery09","bonus/thumbnails/maibonus9.webp")
            add g.make_button("cg_maigallery10","bonus/thumbnails/maifootsiethumb.webp")
            add g.make_button("cg_maigallery11","bonus/thumbnails/maibonus11.webp")
            add g.make_button("cg_maigallery12","bonus/thumbnails/maibonus12.webp")
            add g.make_button("cg_maigallery13","bonus/thumbnails/maibonus13.webp")
            add g.make_button("cg_maigallery14","bonus/thumbnails/maibonus22.webp")
            add g.make_button("cg_maigallery15","bonus/thumbnails/maibonus23.webp")
            add g.make_button("cg_maigallery16","bonus/thumbnails/maibonus24.webp")
            add g.make_button("cg_maigallery17","bonus/thumbnails/maibonus25.webp")
            add g.make_button("cg_maigallery18","bonus/thumbnails/maibonus26.webp")
            add g.make_button("cg_maigallery19","bonus/thumbnails/maibonus27.webp")

            add g.make_button("cg_maigallery20","bonus/thumbnails/maibonus10.webp")
            add g.make_button("cg_maigallery21","bonus/thumbnails/maibonus14.webp")
            add g.make_button("cg_maigallery22","bonus/thumbnails/maibonus15.webp")
            add g.make_button("cg_maigallery23","bonus/thumbnails/maibonus16.webp")
            add g.make_button("cg_maigallery24","bonus/thumbnails/maibonus17.webp")
            add g.make_button("cg_maigallery25","bonus/thumbnails/maibonus18.webp")


    elif cg_page_e == 2:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_maigallery26","bonus/thumbnails/maibonus19.webp")
            add g.make_button("cg_maigallery27","bonus/thumbnails/maibonus20.webp")
            add g.make_button("cg_maigallery28","bonus/thumbnails/maibonus21.webp")
            add g.make_button("cg_maigallery29","bonus/thumbnails/maibonus29.webp")
            add g.make_button("cg_maigallery30","bonus/thumbnails/maibonus30.webp")
            add g.make_button("cg_maigallery31","bonus/thumbnails/maibonus31.webp")
            add g.make_button("cg_maigallery32","bonus/thumbnails/maibonus32.webp")
            add g.make_button("cg_maigallery33","bonus/thumbnails/maibonus33.webp")
            add g.make_button("cg_maigallery34","bonus/thumbnails/maibonus34.webp")
            add g.make_button("cg_maigallery35","bonus/thumbnails/maibonus35.webp")
            add g.make_button("cg_maigallery36","bonus/thumbnails/maibonus36.webp")
            add g.make_button("cg_maigallery37","bonus/thumbnails/maibonus37.webp")
            add g.make_button("cg_maigallery38","bonus/thumbnails/maibonus38.webp")
            add g.make_button("cg_maigallery39","bonus/thumbnails/maibonus39.webp")
            add g.make_button("cg_maigallery40","bonus/thumbnails/maibonus40.webp")
            add g.make_button("cg_maigallery41","bonus/thumbnails/maibonus41.webp")
            add g.make_button("cg_maigallery42","bonus/thumbnails/maibonus42.webp")
            add g.make_button("cg_maigallery43","bonus/thumbnails/maibonus43.webp")
            add g.make_button("cg_maigallery44","bonus/thumbnails/maibonus44.webp")
            add g.make_button("cg_maigallery45","bonus/thumbnails/maibonus45.webp")
            add g.make_button("cg_maigallery46","bonus/thumbnails/maibonus46.webp")
            add g.make_button("cg_maigallery47","bonus/thumbnails/maibonus47.webp")
            add g.make_button("cg_maigallery48","bonus/thumbnails/maibonus48.webp")
            add g.make_button("cg_maigallery49","bonus/thumbnails/maibonus49.webp")
            add g.make_button("cg_maigallery50","bonus/thumbnails/maibonus50.webp")


    elif cg_page_e == 3:
        grid 5 5:
            style_prefix "gallery_stuff"
            add g.make_button("cg_maigallery51","bonus/thumbnails/maibonus51.webp")
            add g.make_button("cg_maigallery52","bonus/thumbnails/maibonus52.webp")
            add g.make_button("cg_maigallery53","bonus/thumbnails/maibonus53.webp")
            add g.make_button("cg_maigallery54","bonus/thumbnails/maibonus54.webp")
            add g.make_button("cg_maigallery55","bonus/thumbnails/maibonus55.webp")
            add g.make_button("cg_maigallery56","bonus/thumbnails/maibonus56.webp")
            add g.make_button("cg_maigallery57","bonus/thumbnails/maibonus57.webp")
            add g.make_button("cg_maigallery58","bonus/thumbnails/maibonus58.webp")
            add g.make_button("cg_maigallery59","bonus/thumbnails/maibonus59.webp")
            add g.make_button("cg_maigallery60","bonus/thumbnails/maibonus60.webp")
            add g.make_button("cg_maigallery61","bonus/thumbnails/maibonus61.webp")
            add g.make_button("cg_maigallery62","bonus/thumbnails/maibonus62.webp")
            add g.make_button("cg_maigallery63","bonus/thumbnails/maibonus63.webp")
            add g.make_button("cg_maigallery64","bonus/thumbnails/maibonus64.webp")
            add g.make_button("cg_maigallery65","bonus/thumbnails/maibonus65.webp")
            add g.make_button("cg_maigallery66","bonus/thumbnails/maibonus66.webp")
            add g.make_button("cg_maigallery67","bonus/thumbnails/maibonus67.webp")
            add g.make_button("cg_maigallery68","bonus/thumbnails/maibonus68.webp")
            add g.make_button("cg_maigallery69","bonus/thumbnails/maibonus69.webp")
            add g.make_button("cg_maigallery70","bonus/thumbnails/maibonus70.webp")
            add g.make_button("cg_maigallery71","bonus/thumbnails/maibonus71.webp")
            add g.make_button("cg_maigallery72","bonus/thumbnails/maibonus72.webp")
            add g.make_button("cg_maigallery73","bonus/thumbnails/maibonus73.webp")
            add g.make_button("cg_maigallery74","bonus/thumbnails/maibonus74.webp")
            null


style gallery_stuff_grid:
    xalign 0.55
    yalign 0.5
    xspacing 20
    yspacing 20

style gallery_stuff_hbox:
    xalign 0.5
    yanchor 0.95
    ypos 0.97
    xspacing 10
