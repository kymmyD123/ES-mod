init:
    image ext_warehouse_day = "mods/SMVIJPNNN/image/bg/ext_warehouse_day.jpg"
    image int_warehouse_day = "mods/SMVIJPNNN/image/bg/int_warehouse_day.png"
    $ d2_MT_palevo = False

label SMVIJPNNN_day2_label1:
    $ backdrop = "days"
    $ new_chapter(2, u"День второй.")
    $ day_time()
    $ persistent.sprite_time = "day"
    play ambience ambience_int_cabin_day fadein 2
    play sound sfx_close_cabinet
    scene int_house_of_mt_day with flash
    "Я услышал звук закрывающейся двери. {w}Именно он меня и вывел из сна."
    "Только проснувшись, я не сразу понял, где я нахожусь."
    th "Точно, я же в лагере теперь... {w}Надо бы привыкнуть."
    "Лера всё еще лежала на боку и сопела в стенку."
    th "Будить я её пока не хочу. {w}Лучше пойду ей одежду посмотрю."
    "За наше время, проведенное вместе, я уже давно выучил всё о ней, в том числе и размер её одежды, поэтому я не думаю, что поиск займет большое количество времени."
    th "Черт, сегодня же еще и линейка. {w}Надо бы успеть."
    "Я мигом встал с кровати и начал одеваться."
    "Галстук опять отказывался меня слушаться, поэтому я просто на него наплевал."
    "Завязав галстук на кое-как я пулей вылетел из домика."
    play sound sfx_close_cabinet
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    scene ext_house_of_mt_day with flash 
    "Лучи солнца ударили мне по глазам. {w}Лагерь постепенно начал наполняться жизнью."
    "Пионеры уже во всю умываются, но мне сейчас не до этого."
    "Я решил быстрым шагом добраться до склада, но не привлекать к себе внимания."
    scene ext_houses_day with dissolve
    $ renpy.pause (1)
    scene ext_square_day with dissolve
    $ renpy.pause (1)
    scene ext_dining_hall_away_day with dissolve
    $ renpy.pause (1)
    scene ext_warehouse_day with dissolve
    "Вот я и нахожусь у склада. {w}Хвост не привел, на горизонте чисто."
    th "Искренне надеюсь, что он не заперт."
    "Так оно и вышло. Дверь была отперта."
    th "Да мне сегодня везет."
    "Я решил медленно открыть дверь, чтобы не попасться."
    play sound sfx_open_door_mines_metal
    scene int_warehouse_day with dissolve
    extend " Бл*ть, как же громко."
    "Склад пердставлял из себя тоже, что я и видел в игре, только пыли слегка больше."
    "Благо я уже знаю, что да где находится, мне не составило труда найти одежду для Леры в кротчайшие сроки."
    "Я взял для неё полный комплект одежды."
    th "Тут нельзя долго оставаться, надо бы убегать отсюда."
    scene ext_warehouse_day with dissolve
    th "Я мог бы подумать, что мне повезло сегодня, но это совершенно не так. Всегда бывают белые и черные полосы."
    "На горизонте показалась Ольга Дмитриевна."
    th "Чёрт, что же делать? {w}Что будет, если она меня поймает с комплектом женской одежды."
    scene ext_warehouse_day with flash
    show prologue_dream
    show mt angry pioneer close at center with dissolve
    mt "ИЗВРАЩЕНЕЦ!"
    scene ext_warehouse_day with dspr
    th "Что же делать? Что же делать? Что же делать?"
    menu:
        "Бежать":
            $ d2_MT_palevo = True
            "Мне остается только бежать."
            "Я мигом рванул с места."
            mt "Семён!"
            "Её слова растворились в звуках моего бега."
            "Я бежал так быстро, как только мог."
            "Вожатая просто стояла на месте, пытаясь поднять челюсть с пола."
            scene ext_dining_hall_away_day with dissolve
            $ renpy.pause (1)
            scene ext_square_day with dissolve
            $ renpy.pause (1)
            scene ext_house_of_mt_day with dissolve
            "Я наконец-то оторвался от вожатой и прибежал к дому. {w}Надеюсь, что Лера уже проснулась."
            play ambience ambience_int_cabin_day fadeout 2 fadein 1
            scene int_house_of_mt_day with dissolve
            
            
        
        "Спрятать под одежду":
            "Надо быстро спрятать одежду под рубашку."
            "Я повернулся спиной к вожатой и быстро произвел все нужные мне действия."
            "Когда я развернулся, вожатая была уже в 15 метрах от меня."
            "Сердце бешено колотится, а руки трясутся."
            "Вот расстояние всё сокращается и сокращается."
            show mt normal pioneer at center with dissolve
            mt "Доброе утро, Семён, а что ты тут делаешь?"
            th "Думай... Думай... {w}О, придумал."
            me "Да я вот решил с утра прогуляться и заблудился. Я же ещё лагеря толком не знаю."
            mt "Так тебе куда нужно было? К умывальникам, наверное?"
            me "Ну... Да."
            show mt laugh pioneer at center
            mt "Так тебе совершенно в другую сторону. Тебе надо пройти..."
            "Я уже совершенно не слушал вожатую. Я же знаю, где находятся умывальники."
            "Я был просто поражен тем, что я как-то выкрутился."
            show mt smile pioneer at center
            mt "Ты понял?"
            me "А? {w}То есть да, понял. Спасибо."
            mt "Ну и отлично. Жду на линейке, не опаздывай."
            me "Да, хорошо."
            "Я улыбнулся и пошел дальше."
            scene ext_dining_hall_away_day with dissolve
            $ renpy.pause (1)
            scene ext_square_day with dissolve
            $ renpy.pause (1)
            scene ext_house_of_mt_day with dissolve
            "Надеюсь Лера уже проснулась. Не хочется её будить самому."
            play ambience ambience_int_cabin_day fadeout 2 fadein 1
            scene int_house_of_mt_day with dissolve
            
        
        "Ничего не делать":
            "Я решил, что смогу как-то выкрутиться словесно."
            "Я просто ждал, пока Ольга Дмитриевна сама подойдет ко мне."
            th "Что она делает?"
            "Она просто не идет в мою сторону. {w}Она проходит мимо."
            th "Она что, меня не заметила?!"
            "Так это только мне наруку."
            "Я продолжал стоять на месте, дожидаясь пока вожатая пройдет мимо."
            th "Чувствую себя Сэмом Фишером."
            "Вот и вожатая скрылась из виду."
            th "Пора идти."
            scene ext_dining_hall_away_day with dissolve
            $ renpy.pause (1)
            scene ext_square_day with dissolve
            $ renpy.pause (1)
            scene ext_house_of_mt_day with dissolve
            "Интересно, Лера еще спит? Даже я уже проснулся."
            th "Буду надеяться, что она уже проснулась. {w}Не хочется нарушать её сон."
            play ambience ambience_int_cabin_day fadeout 2 fadein 1
            scene int_house_of_mt_day with dissolve
            
    
    "И да, я угадал. Лера уже натягивала джинсы на себя."
    return