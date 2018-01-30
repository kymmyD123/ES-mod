init:
    image ext_warehouse_day = "mods/SMVIJPNNN/image/bg/ext_warehouse_day.jpg"
    image int_warehouse_day = "mods/SMVIJPNNN/image/bg/int_warehouse_day.png"
    image lineup = "mods/SMVIJPNNN/image/cg/day2/d2_lineup.jpg"
    
    $ Ler_SM = Character(u'Лера', color="99FF99", what_color="E2C778")
    
    $ Vlr_SM = Character(u'Кристина', color="660066", what_color="E2C778")
    
    $ bus_engine = "mods/SMVIJPNNN/music/bus_engine.mp3"
    $ nobody_secret = "mods/SMVIJPNNN/music/nobody_secret.mp3"
    $ Sakura = "mods/SMVIJPNNN/music/Sakura.mp3"
    $ homyak_theme = "mods/SMVIJPNNN/music/homyak_theme.mp3"
    $ soft_horn = "mods/SMVIJPNNN/music/soft_horn.mp3"
    $ spring = "mods/SMVIJPNNN/music/spring.mp3"
    $ silent_garden = "mods/SMVIJPNNN/music/silent_garden.mp3"
    $ Saya = "mods/SMVIJPNNN/music/Saya.mp3"
    
    $ d1_Lera_diner_ploho = False
    $ d2_MT_palevo = False
    
    image Kristy normal pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_sp_1.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy angry pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy smile pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/4.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy shy pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    
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
    "Склад представлял из себя тоже, что я и видел в игре, только пыли слегка больше."
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
    play music spring fadein 2
    me "Доброе утро, а я тебе за одеждой сходил."
    "Сказал я с улыбкой."
    Ler_SM "Доброе утро, спасибо."
    th "Как же она прекрасна. {w}Ее растрепанные волосы, заспанный вид, она очень красиво выглядит в солнечных лучах, пробивающихся через окно."
    me "Ты очень прекрасно выглядишь!"
    if d1_Lera_diner_ploho:
        Ler_SM "Ага, спасибо."
        "Она сказала это как-то с обидой. Почему же? Чем я её обидел? Чёрт!"
        me "Лер, все хорошо?"
        Ler_SM "Абсолютно, просто я еще не проснулась."
        "Что же случилось, блин."
        "Я решил разобраться с этом потом, ведь скоро линейка."
    else:
        Ler_SM "Спасибо, Сенечка."
        "Она покраснела."
        me "Как ты спала? Что тебе снилось?"
        "Лера задумчиво посмотрела на меня и её настроение переменилось. {w}Она стала грустной и все время смотрела в сторону."
        Ler_SM "Я не помню, извини."
        th "Она что-то скрывает, ладно."
        "Я не стал её допрашивать, ведь она только проснулась, да и делать этого особо не хотелось, поэтому я сказал."
        
    me "Ладно, пойдем на линейку, опоздание неприемлимо."
    Ler_SM "Линейку? Ну пойдем."    
    scene ext_house_of_mt_day with dissolve
    $ renpy.pause(1)
    scene ext_houses_day with dissolve
    stop music fadeout 4
    $ renpy.pause (1)
    scene ext_square_day with dissolve
    me "Вот мы и пришли."
    "Сказал я шепотом, чтобы другие пионеры не услышали."
    Ler_SM "Ага, пришли."
    "Я решил молчать далее, так как было бы глупо если бы меня заметили разговаривающим с самим собой."
    "А вот и Ольга Дмитриевна."
    show mt normal pioneer at center with dissolve
    mt "Итак пионеры, начнем линейку."
    mt "Сегодня у нас в планах..."
    "Я не стал её слушать, ведь я итак знаю что мне делать в этом лагере."
    scene lineup with dissolve
    $ set_mode_nvl()
    "Меня мучало много вопросов. {w}Один из них - это почему Кристина видит Леру, а остальные нет."
    "Ответ на этот вопрос так и не найден, а будет ли вообще?"
    "Так же я не понимал, что происходит с Лерой, ей вроде все нравилось в лагере."
    "С ней надо поговорить, иначе вообще потеряю её."
    "Мои размышления прервал звук призывающий к завтраку."
    $ set_mode_adv()
    play sound sfx_dinner_horn_processed
    scene ext_square_day with dissolve
    show mt normal pioneer at center with dissolve
    mt "Вот, я как раз таки закончила говорить."
    mt "А теперь все на завтрак!"
    scene ext_dining_hall_away_sunset with dissolve
    $ renpy.pause (1)
    scene ext_dining_hall_near_sunset with dissolve
    show dv angry pioneer far at cleft with dissolve
    show us normal pioneer far at cright with dissolve
    dv "Ну что, вот ты и нашелся, Дурачелло."
    dv "Сейчас ты у меня получишь за вчерашнее!"
    show us surp2 pioneer far at cright with dissolve
    us "Алиса, давай не будем сейчас, ведь мы завтрак можем пропустить, а я очень голодная."
    dv "Нет уж, Уль, он сейчас мигом будет просить о пощаде."
    "Я не потерплю подобного в мой адрес!"
    Ler_SM "Семён, спокойнее!"
    menu:
        "Устроить им взбучку":
            show dv angry pioneer far at cleft with dissolve
            show us normal pioneer far at cright with dissolve
            me "Ну держись, я тебе сейчас..."
            show sl serious pioneer far center with dissolve
            sl "Что это тут происходит?"
            sl "Двачевская, опять ты?!"
            sl "Семен, иди кушай, я с ними разберусь!"
            
        "Пройти мимо сделав вид, что незаметил":
            show dv angry pioneer far at cleft with dissolve
            show us normal pioneer far at cright with dissolve
            "А смысл реагировать, проблем не хочется."
            "Мы с Лерой прошли мимо и она толкнула плечом Алису."
            dv "Ну держись, сейчас ты получишь!"
            "Она хотела было накинуться на меня, но тут знакомый голос меня спас."
            sl "Двачевская! Что ты делаешь?"
            show dv shocked  pioneer far at cleft with dissolve
            show us surprise pioneer far at cright with dissolve
            show sl serious pioneer far center  with dissolve
            sl "Семён иди кушай, я с ней поговорю."
            
    
    me "Хорошо, спасибо Славя."
    dv "Я тебе ещё припомню..."
    play ambience ambience_dining_hall_full fadeout 2 fadein 1
    scene int_dining_hall_people_sunset with dissolve
    "Её слова растворились, позади меня."
    Ler_SM "Потом мне еду принесёшь, я постою рядом, пока ты кушаешь."
    me "Обязательно Лера, обязательно."
    "Я взял поднос и начал выискивать столик."
    "Свободный оказался лишь рядом с Кристиной."
    show Kristy smile pioneer far at cleft with dissolve
    Vlr_SM "Привет, ребята."
    me "Привет, Кристя."
    "Мы произнесли это вдвоем."
    Vlr_SM "Лера, что стоишь, возьми стул и присаживайся с нами."
    Ler_SM "Нет, я постою."
    me "Потом с тобой поговорим, Кристина."
    show Kristy normal pioneer far at cleft with dissolve
    Vlr_SM "А о чем?"
    Ler_SM "У меня есть, одна проблема, я думаю ты это имел в виду, Семён."
    Vlr_SM "Хорошо, я выслушаю вас позже."
    "Завтрак кончился и я первый вышел из столовой. {w}Девочки шли позади и болтали о своём."
    play ambience ambience_camp_center_evening fadeout 2 fadein 1
    scene ext_dining_hall_near_sunset
    show mt normal pioneer far at center with dissolve
    show Kristy normal pioneer far at cleft with dissolve
    th "Она держит обходной, значит мне предстоит знакомство с остальными жителями."
    mt "Привет, Семён. У меня для тебя задание."
    me "Здравствуйте Ольга Дмитриевна. Да я готов ко всему."
    "Я сказал улыбаясь и вожатая тоже начала улыбаться."
    show mt smile pioneer far at center with dissolve
    mt "Ничего такого, просто обходной лист, ты должен его пройти как можно быстрее!"
    me "Вас понял, будет сделано."
    mt "Постарайся пройти до обеда, а то голодный будешь потом ходить."
    show mt angry pioneer far at center with dissolve
    mt "А ты Кристина, помнишь что я говорила на линейке?"
    show Kristy shy pioneer far at cleft with dissolve
    Vlr_SM "Да."
    mt "Иди выполняй!"
    show Kristy smile pioneer far at cleft with dissolve
    Vlr_SM "Хорошо."
    "Нотка грусти прозвучала в ее ответе."
    mt "Все идите ребята, не смею задерживать вас."
    scene ext_houses_day with dissolve
    show Kristy normal pioneer far at cleft with dissolve
    Ler_SM "Ладно Семён, иди лист проходи, а я с Кристей пойду."
    show Kristy shy pioneer far at cleft with dissolve
    me "Хорошо, удачи вам девочки."
    Vlr_SM "И тебе удачи, Семён."
    
    return