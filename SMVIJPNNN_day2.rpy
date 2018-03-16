init:
    image ext_warehouse_day = "mods/SMVIJPNNN/image/bg/ext_warehouse_day.jpg"
    image int_warehouse_day = "mods/SMVIJPNNN/image/bg/int_warehouse_day.png"
    image lineup = "mods/SMVIJPNNN/image/cg/day2/d2_lineup.jpg"
    image d2_mi_pose_smvij_nn = "mods/SMVIJPNNN/image/cg/day2/d2_mi_pose_smvij_nn.png"
    image ext_houses_night = "mods/SMVIJPNNN/image/bg/ext_houses_night.jpg"
    image plane_dream_int = "mods/SMVIJPNNN/image/bg/plane_dream_int.jpg"
    
    $ Ler_SM = Character(u'Лера', color="99FF99", what_color="E2C778")
    $ Pioners_SMVIJ = Character(u'Пионеры', color ="#009966", what_color = "E2C778")
    $ SILer_SM_together = Character(u'Семён и Лера', color="00cc00", what_color="E2C778")
    
    $ Vlr_SM = Character(u'Кристина', color="660066", what_color="E2C778")
    $ Devishka_SM = Character(u'Девушка', color="99FF99", what_color="E2C778")
    $ ya_SMVIJ = Character(u'Я', color ="#009966", what_color = "E2C778")
    $ Personal_SM = Character(u'Стюардесса', color="660066", what_color="E2C778")
    
    $ sfx_aplauds_miku = "mods/SMVIJPNNN/music/sfx_aplauds_miku.mp3"
    $ Padenie = "mods/SMVIJPNNN/music/Padenie.mp3"
    $ airplane_int = "mods/SMVIJPNNN/music/airplane_int.mp3"
    $ sfx_padenie_miku = "mods/SMVIJPNNN/music/sfx_padenie_miku.mp3"
    $ miku_music_piano = "mods/SMVIJPNNN/music/miku_music_piano.mp3"
    $ bus_engine = "mods/SMVIJPNNN/music/bus_engine.mp3"
    $ nobody_secret = "mods/SMVIJPNNN/music/nobody_secret.mp3"
    $ Sakura = "mods/SMVIJPNNN/music/Sakura.mp3"
    $ morning = "mods/SMVIJPNNN/music/morning.mp3"
    $ soft_horn = "mods/SMVIJPNNN/music/soft_horn.mp3"
    $ spring = "mods/SMVIJPNNN/music/spring.mp3"
    $ silent_garden = "mods/SMVIJPNNN/music/silent_garden.mp3"
    $ Saya = "mods/SMVIJPNNN/music/Saya.mp3"
    $ alice_guitar = "mods/SMVIJPNNN/music/alice_guitar.mp3"
    
    
    $ ES_Alisa_comfort_points_SMVIJ = 0
    $ ES_Ulya_comfort_points_SMVIJ = 0
    $ ES_Lena_comfort_points_SMVIJ = 0
    $ ES_Miku_comfort_points_SMVIJ = 0
    
    $ d2_med_sv_vh = False
    $ d2_Lena_nnd = False
    $ d2_Miku_plastinka = False
    
    $ day2_poisk_necessary_done = 0
    
    $ d2_clubs_smv_vh = False
    $ d2_muzclub_smv_vh = False
    $ d2_library_smv_vh = False
    $ d2_aidpost_smv_vh = False
    
    $ d2_sport_area_smv_vh = False
    $ d2_boat_station_smv_vh = False
    $ d2_camp_entrance_smv_vh = False
    $ d2_forest_smv_vh = False
    
    
    $ d2_MT_palevo = False
    $ d2_SL_svidanka = False
    $ d2_LN_pomosh = False
    $ d2_Al_scene = False
    
    image Kristy normal pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_sp_1.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy angry pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy smile pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/4.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    image Kristy shy pioneer sunset = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) )
    
    
    image Kristy normal pioneer day = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_sp_1.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image Kristy angry pioneer day = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_angry.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image Kristy smile pioneer day = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/4.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    image Kristy shy pioneer day = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_shy.png"), im.matrix.tint(0.83, 0.88, 0.92) )
    
    image Kristy shy pioneer night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82 ) )
    image Kristy smile pioneer night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/4.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    image Kristy angry pioneer night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    image Kristy normal pioneer night = im.MatrixColor( im.Composite((900,1080), (0,0), "mods/SMVIJPNNN/image/sprites/uno/uno_sp_1.png"), im.matrix.tint(0.63, 0.78, 0.82) )
    
    
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
    "Склад представлял собой тоже, что я и видел в игре, только пыли слегка больше."
    "Благо я уже знаю, что да где находится, мне не составило труда найти одежду для Леры в кротчайшие сроки."
    "Я взял для неё полный комплект одежды."
    th "Тут нельзя долго оставаться, надо бы убегать отсюда."
    scene ext_warehouse_day with dissolve
    th "Я мог бы подумать, что мне повезло сегодня, но это совершенно не так. Всегда бывают белые и черные полосы."
    "На горизонте показалась Ольга Дмитриевна."
    th "Чёрт, что же делать? {w}Что будет, если она меня поймает с комплектом женской одежды."
    scene ext_warehouse_day with dspr
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
            "Так это только мне на руку."
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
    "Пусть я и вижу это очень часто, но в данном месте, где лучи солнца освещают её полузакрытые глаза, она выглядит потрясающе."
    me "Ты очень прекрасно выглядишь!"

    Ler_SM "Спасибо, Сенечка."
    "Она покраснела."
    me "Как ты спала? Что тебе снилось?"
    "Лера задумчиво посмотрела на меня и её настроение переменилось. {w}Она стала грустной и все время смотрела в сторону."
    Ler_SM "Я не помню, извини."
    th "Она что-то скрывает, ладно."
    "Я не стал её допрашивать, ведь она только проснулась, да и делать этого особо не хотелось, поэтому я решил её немного обрадовать."
    me "Я тебе комплект одежды принес."
    Ler_SM "Что? Летняя одежда? Ура!"
    "Лера приняла подарок и сразу начала переодеваться."
    "Спустя какое-то время:"
    Ler_SM "Ну как я тебе?"
    "На ней эта форма сидит замечательно."
    me "Потрясающе. Жалко, что этого другие не видят."
    "Лера покраснела."
    
   
    me "Ладно, пойдем на линейку, опоздание неприемлемо."
    Ler_SM "Линейку? {w}Ну пойдем."
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    scene ext_house_of_mt_day with dissolve
    $ renpy.pause(1)
    scene ext_houses_day with dissolve
    stop music fadeout 2
    $ renpy.pause (1)
    scene ext_square_day with dissolve
    me "Вот мы и пришли."
    "Сказал я шепотом, чтобы другие пионеры не услышали."
    Ler_SM "Ага, пришли."
    "Я решил молчать далее, так как было бы глупо если бы меня заметили, разговаривающим с самим собой."
    "А вот и Ольга Дмитриевна."
    show mt normal pioneer at center with dissolve
    mt "Итак пионеры, начнем линейку."
    mt "Сегодня у нас в планах..."
    "Я не стал её слушать, ведь я итак знаю что мне делать в этом лагере."
    scene lineup with dissolve
    $ set_mode_nvl()
    "Меня мучило много вопросов. {w}Один из них - это почему Кристина видит Леру, а остальные нет."
    "Ответ на этот вопрос так и не найден. {w}И будет ли вообще?"
    "Да и некоторые сцены тоже нарушены. Я прекрасно понимаю, что не все мои действия соответствуют Семёну в игре, но это всё равно слишком."
    "Вот возьмём пример : я сегодня вышел из домика рано утром, задолго до начала линейки. {w}А где же Славя?"
    "Ведь она всегда бегает по утрам и не изменяет своим традициям и привычкам."
    "Да взять ту же Лену. {w}Где она была весь день? Я должен был увидеть её вечером на скамейке возле Генды, но я её не видел."
    "Это, конечно, можно списать на то, что расстояние было большое и я просто мог её не увидеть, но я бы не сказал, что у меня плохое зрение. Я бы даже сделал себе комплемент, что у меня самое лучшее зрение в этом лагере."
    "Ну и переходим к главной загадке всего лагеря - Кристина."
    "Первое - почему она видит Леру? {w}Должна же быть какая-то причина этому. Она так же попала в лагерь, как и мы? Она что-то наподобие пионера? {w}Или может даже Юли?"
    "В любом случае будет интересно, и нам предстоит пройти это, ведь выбор у нас не большой."
    "А что если мы застрянем в бесконечных циклах? {w}Что же делать в этом случае?"
    "Да и сделать мы особо ничего не сможем, если честно. Надо будет просто проживать неделя за неделей, стирая пыль из сознания, и стараться прожить каждую неделю как новую."
    "Лагерь точно останется в памяти Леры. Это её полуфантомное состояние точно отразится на её восприятии мира. Искренне надеюсь, что этот период в нашей жизни останется позади или же запомнится моментами, проведенными в этой по-настоящему волшебной атмосфере."
    "Я всем сердцем желаю, чтобы девочки увидели Леру, хочу, чтобы они подружились. Я не хочу, чтобы Лера ходила с сердцем, разрезанным мечом страданий и одиночества."
    "Я просто хочу, чтобы все были счастливы..."
    play sound sfx_dinner_horn_processed
    
    "Мои размышления прервал звук призывающий к завтраку."
    $ set_mode_adv()

    scene ext_square_day 
    show mt normal pioneer at center 
    with dissolve
    mt "Вот, я как раз таки закончила говорить."
    mt "А теперь все на завтрак!"
    Pioners_SMVIJ "Есть!" with vpunch
    "Громко отозвались пионеры вокруг."
    th "Даже в ушах зазвенело."
    "Бросив взгляд на Леру, я заметил, что она тоже закрыла уши руками."
    th "Ну да, в слухе я ей точно проигрываю. Надо меньше музыки в наушниках слушать."
    "Лера зацепила меня за край рубашки и потянула за собой."
    Ler_SM "Пошли уже, что встал. {w}Места же не найдем."
    scene ext_dining_hall_away_day with dissolve
    $ renpy.pause (1)
    scene ext_dining_hall_near_day with dissolve
    $ renpy.pause (0.8)
    play music music_list["awakening_power"] fadein 1
    show dv angry pioneer far at cleft 
    show us normal pioneer far at cright 
    with dissolve
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
            me "Хорошо, спасибо Славя."
            dv "Я тебе ещё припомню..."
            stop music fadeout 2
            
        "Пройти мимо сделав вид, что не заметил":
            $ ES_Lera_comfort_points_SMVIJ += 1
            show dv angry pioneer far at cleft with dissolve
            show us normal pioneer far at cright with dissolve
            "А смысл реагировать, проблем не хочется."
            "Мы с Лерой прошли мимо и она толкнула плечом Алису."
            dv "Ну держись, сейчас ты получишь!"
            "Она хотела было накинуться на меня, но тут знакомый голос меня спас."
            sl "Двачевская! Что ты делаешь?"
            show dv shocked  pioneer far at cleft with dissolve
            show us surp1 pioneer far at cright with dissolve
            show sl serious pioneer far center  with dissolve
            sl "Семён иди кушай, я с ней поговорю."
            me "Хорошо, спасибо Славя."
            dv "Я тебе ещё припомню..."
            stop music fadeout 2
            
        "Попробовать поговорить":   
            $ d2_Al_scene = True
            $ ES_Alisa_comfort_points_SMVIJ += 1
            $ ES_girls_comfort_points_SMVIJ += 1
            me "Алиса, давай спокойно поговорим?"
            show dv shocked pioneer far at cleft
            $ renpy.pause (0.8)
            show us smile pioneer far at cright
            us "Ну вы тут сами разбирайтесь, а я кушать пошла!"
            stop music fadeout 2
            hide us with dissolve
            "Судя по взгляду Леры, она ревнует."
            me "Алиса, ты прости меня за тот случай с подножкой, я тогда был зол."
            show dv rage pioneer far at center with move
            dv "Ну я тоже была зла на тебя!"
            th "Как же ее успокоить? Эх, Алиса. Ты всегда мне нравилась своей манерой, но вот только испытывать её в реальной жизни я точно не желаю."
            me "Давай не будем с тобой ругаться. {w}Наше первое знакомство прошло не очень."
            me "Давай хоть попробуем наладить отношения?"
            "Алиса явно противоречит сама себе. {w}По ней видно, что она не может решить: ударить меня или дать шанс. {w}Если внимательно посмотреть на её плечи, то можно увидеть ангела и дьявола."
            "Она, похоже, пришла к окончательному решению."
            show dv shy pioneer far at center with dissolve
            dv "Семён, прости меня, за руку."
            me "А ты за подножку."
            "Кажется Алиса начала успокаиваться. {w}А вот Лера сейчас кажется убьет меня."
            show dv smile pioneer close at center with dissolve
            dv "Пойдем кушать?"
            me "Я попозже приду, иди без меня. Приятного аппетита."
            dv "Хорошо, спасибо."
            hide dv smile pioneer close at center
            Ler_SM "Ну и что это было?"
            me "Ничего, просто избежал проблем. {w}Ревнуешь?"
            "Лера покраснела слегка."
            "Она взялась за подол юбки и стала мять его в руке."
            Ler_SM "Нет, с чего бы это? {w}Пойдем есть!"
            
    play ambience ambience_dining_hall_full fadeout 2 fadein 1
    scene int_dining_hall_people_day with dissolve
    Ler_SM "Потом мне еду принесёшь, я постою рядом, пока ты кушаешь."
    me "Обязательно Лера, обязательно."
    "Я взял поднос и начал выискивать столик."
    "Свободный оказался лишь рядом с Кристиной."
    show Kristy smile pioneer day at center with dissolve
    Vlr_SM "Привет, ребята."
    me "Привет, Кристя."
    "Мы произнесли это вдвоем."
    Vlr_SM "Лера, что стоишь, возьми стул и присаживайся с нами."
    Ler_SM "Нет, я постою."
    me "Потом с тобой поговорим, Кристина."
    hide Kristy smile pioneer day
    show Kristy normal pioneer day at center
    Vlr_SM "А о чем?"
    Ler_SM "У меня есть одна проблема, я думаю ты это имел в виду, Семён."
    Vlr_SM "Хорошо, я выслушаю вас позже."
    "Звон стаканов разбавляет тишину. Звук вилок и ложек создает хаотичную мелодию, которая настраивает атмосферу."
    th "Лучше бы завести разговор с кем-нибудь. Лучше с Кристной, ибо это будет менее подозрительно."
    th "А стоит ли?"
    menu:
        "Заговорить с Кристиной":
            "Я всё же решил нарушить молчание вокруг нас."
            me "Кристина, как спалось?"
            $ Krst_comfort_SMVIJPNNN += 1
            hide Kristy normal pioneer day
            show Kristy shy pioneer day at center
            "Кристина подняла глаза и посмотрела на меня."
            "Я только сейчас обратил на неё внимание с такого расстояния."
            "Её взгляд можно назвать щенячьим. {w}Она смотрит на меня блестящими глазами, а слезы так и вырвутся наружу."
            "Она смогла совладать с собой и опустила взгляд в тарелку."
            hide Kristy shy pioneer day
            show Kristy normal pioneer day at center
            Vlr_SM "Могло быть и лучше."
            me "А что снилось?"
            Vlr_SM "Не важно."
            "Понял."
            "Я решил, что на этом хватит беседы с Кристиной, и уткнулся в тарелку."
            
            
        "Продолжать есть молча":
            "Лучше не стоит."
            "Когда я ем, я глух и нем. {w}Поэтому лучше помолчу."
            "Довольно интересно наблюдать, как Лера занимает себя, пока мы кушаем."
            "То ногти рассматривает, то юбку из стороны в сторону дергает, то в окно смотрит."
            Ler_SM "Что-то случилось, Сеня?"
            "Ой, заметили."
            me "Да нет, всё нормально."
            "Я сказал шепотом, чтобы не быть услышанным."
            
    "Трапеза была окончена через какое-то время."
    me "Всё, Кристина, я пойду. Спасибо за компанию."
    hide Kristy normal pioneer day
    show Kristy smile pioneer day at center
    Vlr_SM "Хорошо. До встречи, еще увидимся с вами."
    "После этой фразы пара окружающих нас пионеров посмотрели на Кристину с непонимающим взглядом."
    me "Да, до встречи."
    Vlr_SM "Хотя подождите, я уже закончила. Пойдем вместе?"
    "Пионеры уже чуть ли не со стула падают, чтобы услышать речь Кристины."
    me "Да, хорошо."
    hide Kristy smile pioneer day with dspr
    "Пока Кристина относит посуду, я решил взять несколько бутербродов для Леры."
    "Я же не оставлю её в голоде."
    th "А вообще надо придумать какой-то другой способ, потому что неделю одними бутербродами сыт не будешь."
    "Кристина не заставила себя долго ждать и уже подходила к нам."
    show Kristy smile pioneer day at center with dissolve
    Vlr_SM "Ну что, пойдем?"
    SILer_SM_together "Пошли!"
    hide Kristy smile pioneer day with dspr
    "Я первый вышел из столовой. {w}Девочки шли позади и болтали о своём."
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    scene ext_dining_hall_near_day with dissolve
    show mt normal pioneer far at cleft with dissolve
    show Kristy normal pioneer day at center with dissolve
    "Не успели мы выйти, как Ольга Дмитриевна уже ждет нас на пороге."
    th "Вожатая держит какую-то бумагу. Это бегунок, зуб даю."
    mt "Привет, Семён. У меня для тебя задание."
    me "Здравствуйте Ольга Дмитриевна. Да, я готов ко всему."
    "Я сказал улыбаясь и вожатая тоже начала улыбаться."
    show mt smile pioneer far at left 
    mt "Ничего такого, просто обходной лист, ты должен его пройти как можно быстрее!"
    me "Вас понял, будет сделано."
    mt "Постарайся пройти до обеда, а то голодный будешь потом ходить."
    show mt angry pioneer far at left 
    mt "А ты, Кристина, помнишь, что я говорила на линейке?"
    hide Kristy normal pioneer day
    show Kristy shy pioneer day at center 
    Vlr_SM "Да."
    mt "Иди выполняй!"
    hide Kristy shy pioneer day
    show Kristy smile pioneer day at center 
    Vlr_SM "Хорошо."
    "Нотка грусти прозвучала в ее ответе."
    mt "Все идите ребята, не смею задерживать вас."
    scene ext_houses_day with dissolve
    show Kristy normal pioneer day at center with dissolve
    "Мы пришли к домикам и тут Лера сказала."
    Ler_SM "Ладно Семён, иди лист проходи, а я с Кристей пойду."
    hide Kristy normal pioneer day
    show Kristy shy pioneer day at center 
    me "Хорошо, удачи вам девочки."
    Vlr_SM "И тебе удачи, Семён."
    hide Kristy shy pioneer day with dissolve
    th "Ну что ж, куда пойдем?"
    
    $ disable_all_zones()

    $ set_zone("music_club","day2_musclub_SMVIJ")
    $ set_zone("clubs","day2_clubs_SMVIJ")
    $ set_zone("library","day2_library_SMVIJ")
    $ set_zone("medic_house","day2_aidpost_SMVIJ")

    jump day2_map_SMVIJ
    
label day2_map_SMVIJ:
    if day2_map_necessary_done == 4:
        jump day2_main_SMVIJ_mode2
        
    $ show_map()
    
label day2_musclub_SMVIJ:
    if d2_aidpost_smv_vh == False and d2_clubs_smv_vh == False and d2_library_smv_vh == False and d2_muzclub_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_aidpost_smv_vh == True:
        scene ext_aidpost_day with dissolve
    if d2_library_smv_vh == True:
        scene ext_library_day with dissolve
    if d2_muzclub_smv_vh == True:
        scene ext_musclub_day with dissolve
    if d2_clubs_smv_vh == True:
        scene ext_clubs_day with dissolve
    
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    th "Музыки что ли послушать?"
    "Спустя какое-то время я принял окончательное решение и направился в сторону музыкального клуба."
    scene ext_musclub_day with dissolve
    "Добравшись до музыкального клуба я уже мог слышать звуки рояля."
    th "Сейчас мне предстоит знакомство с милой японкой."
    "Её пикантная поза уже всплыла у меня в голове."
    th "А вдруг в этот раз будет всё иначе?"
    th "Есть только один способ проверить."
    th "Эх ну что ж, Семен, пойдем!"
    play sound sfx_open_door_squeak_2
    play ambience ambience_music_club_day fadein 1
    scene int_musclub_day with dissolve
    "Внутри меня ждала целая группа инструментов. {w}Прямо оркестр из одной особы."
    "Я инстинктивно посмотрел под рояль."
    th "NANI?!"
    $ renpy.notify("NANI на японском означает ~Чего?~")
    th "Где Мику?"
    "Вместо неё на полу был только отблеск яркого солнца, от которого не скрыться даже на этом, забытом людьми, местом."
    "И только потом, когда я уже решил осмотреться до меня дошло..."
    th "Как же я могу быть таким не внимательным..."
    show d2_mi_pose_smvij_nn with dissolve
    "Мику была совершенно в другом месте."
    th "Но стоит она всё равно замечательно, не так ли?"
    "Так, стоп. Надо собраться."
    me "Кхм-кхм..."
    "Я решил привлечь к себе внимание."
    mi "Что?!" with vpunch
    hide d2_mi_pose_smvij_nn with dspr
    "Мику пыталась развернуться, но она оступилась."
    th "Вот дурак. Знаешь же, что она неуклюжая."
    "Люди ходить по воздуху не умеют, следовательно, она и повстречалась с чистым, блестящим от натирки и ласки, но твердым полом."
    th "Хорошо, что на неё все книжки не упали."
    "Мику пыталась встать, но я решил помочь."
    show mi sad pioneer close at center with dissolve
    me "Мику, давай я тебе помогу."
    show mi shocked pioneer close at center
    "Мику очень удивилась."
    th "Чего это она?"
    show mi sad pioneer close at center
    "Но буквально через несколько секунд она взяла себя в руки."
    mi "Спасибо."
    hide mi with dspr
    "Я аккуратно помог ей подняться."
    "Вот она на ногах, но она всё всматривается в моё лицо."
    show mi normal pioneer at center with dspr
    mi "А мы раньше встречались?"
    th "Что она имеет в виду?"
    me "Думаю нет."
    show mi smile pioneer at center
    mi "Тогда откуда ты знаешь моё имя?"
    th "Вот черт! Проболтался."
    th "Думай, Семён, думай."
    "..."
    me "Да мне о тебе говорили, когда бегунок давали."
    "Первое, что смог сказать я."
    show mi happy pioneer at center
    mi "Да ладно? {w}Правда? А я думала про меня тут все забыли. Я же тут одна всегда. Нет, правда-правда одна. Алиса только заходит иногда, да ей только гитару настроить или ноты дать."
    mi "Я на всех инструментах играть умею. Честно-честно! Хочешь прямо сейчас покажу? Я тут недавно такую хорошую песню написала, давай сыграю?"
    show mi shocked pioneer at center
    mi "Ой, что же я это не представилась? Меня Мику зовут. Честно-честно."
    show mi smile pioneer at center
    extend " Мой папа русский, а мама японка. У меня папа там что-то в Японии строит, вот так они и познакомились."
    mi "Хотя стой... {w}Ты же уже знаешь моё имя. Зачем тогда я это говорила?"
    show mi happy pioneer at center 
    mi "Ну и ладно. А тебя как зовут? Ты в клуб записаться пришел?"
    th "Ну наконец-то мне слово дали. {w}Спасибо, Мику, я тебя своей речью не разочарую."
    me "Меня зовут Семён. Нет, я пока не пришел записываться. Я еще не все места обошел, поэтому не могу пока решить. Пришел я сюда с бегунком. Подпишешь?"
    show mi smile pioneer at center
    mi "Ой, конечно-конечно. Давай сюда. Я быстро."
    show mi smile pioneer close at center with dspr
    "Мику резким движением пересекла расстояние между нами и забрала у меня листок. "
    hide mi with dspr
    th "Такой скорости даже супер-герои позавидовали бы."
    "Я присел на стульчик в углу этого приятного места и стал ждать."
    "Не прошло и минуты, как она вернулась уже с готовым бегунком."
    th "Это было даже быстрее, чем она забрала у меня листок."
    show mi normal pioneer at center with dissolve
    mi "А вот и я. Держи."
    "Мику протягивает мне листок."
    th "Откуда у неё столько энергии?"
    me "Да... Спасибо."
    "Я взял листок в руки и, сложив пополам, сунул в задний карман шорт."
    show mi smile pioneer at center
    mi "Ну ты приходи, я всегда рада новым людям в моем клубе. Он не совсем мой, конечно, но я тут заведую."
    mi "Может всё-таки ты хочешь, чтобы я тебе сыграла? Музыка красивая получилась правда-правда."
    th "Временем я не ограничен, может стоит попробовать?"
    menu:
        "Послушать музыку":
            $ d2_Miku_plastinka = True
            $ ES_Miku_comfort_points_SMVIJ += 1
            th "А почему бы и нет?"
            me "Давай, я буду не против."
            show mi happy pioneer at center
            mi "Ура! Я мигом за нотами и вернусь."
            hide mi with move
            "Мику, развив первую космическую, удалилась во второе помещение клуба."
            th "Как бы не споткнулась. {w}Шуму было бы много."
            play sound sfx_padenie_miku
            th "Мда..."
            mi "Я в порядке!"
            th "И не сомневаюсь..."
            "Мику вернулась через 20 секунд после инцидента."
            show mi smile pioneer at center with dissolve
            mi "А вот и я."
            mi "Сейчас всё сыграю, не уходи."
            me "Да я и не собирался."
            show mi laugh pioneer at center
            mi "Ну и отлично. Всё, я готова."
            hide mi with dspr
            "Мику подошла к роялю, положила ноты на подставку и положила пальцы на клавиши."
            "Она пытается собраться с мыслями."
            th "Вот минут 5 назад была такая смелая, а сейчас боится."
            "В голове сразу всплыла пословица."
            th "На словах ты Лев Толстой, а на деле..."
            "Не успел я додумать, как Мику начала играть."
            window hide
            play music miku_music_piano fadein 1
            $ renpy.pause (5, hard=True)
            "Пальцы Мику скачут по клавишам, а её волнение ушло в раз."
            "Я редко слушаю такого рода музыку. Да что говорить, я вообще второй раз в жизни вижу, как кто-то играет в живую."
            "Первый раз мне это показала мама."
            window hide
            $ renpy.notify ("Вы можете продолжать слушать музыку, а можете пропустить.")
            ""
            stop music fadeout 2
            "Мику перестала играть. Она поворачивается ко мне."
            play sound sfx_aplauds_miku
            "Я просто не смог сдержать аплодисменты. Руки начали двигаться сами собой."
            show mi shy pioneer at center with dspr
            me "Это было прекрасно."
            mi "Ой, не стоит."
            "Мику засмущалась и опустила взгляд."
            me "Нет, ты это заслужила."
            show mi smile pioneer at center
            mi "Спасибо, мне очень приятно."
            me "За правду спасибо не говорят."
            mi "И что же мне тогда сказать? Благодарю?"
            me "Ну... Можно и так."
            "Я встал со стула и обратился к Мику."
            me "Спасибо за твоё шикарное выступление для меня одного. Я бы остался еще побеседовать, но мне пора."
            mi "Да, я понимаю. Ты заходи, я всегда тут одна. Ну иногда Алиса приходит, конечно, но я тебе уже об этом говорила. Ты подумай о моём предложении, я тебя на любом инструменте научу играть."
#ШУТКА ПОДЛЕЖИТ УДАЛЕНИЮ ПОСЛЕ СОВЕТА
            th "А на кожаной флейте тоже научишь?"
            me "Да, хорошо. Еще раз спасибо."
            mi "Совершенно не за что. До встречи."
            hide mi with dspr
            "Я развернулся и направился к выходу."
        
        
        
        
        "Не слушать музыку":
            th "Не думаю, что это стоит того."
            me "Прости, времени реально мало. Я еще на обед хочу. Давай как-нибудь в другой раз?"
            show mi sad pioneer at center
            mi "Ну ладно, тогда в следующий раз."
            me "Ты на меня не в обиде за это?"
            show mi smile pioneer at center
            mi "Нет, ты что."
            me "Ну хорошо. Тогда я еще зайду."
            mi "Отлично. До скорой встречи."
            hide mi with dissolve
            "Я развернулся и направился к выходу."
            
    
    scene ext_musclub_day with dissolve
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    
    
    $ d2_clubs_smv_vh = False
    $ d2_aidpost_smv_vh = False
    $ d2_library_smv_vh = False
    $ d2_muzclub_smv_vh = True
    
    
    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map_SMVIJ
    
label day2_clubs_SMVIJ:
    if d2_aidpost_smv_vh == False and d2_clubs_smv_vh == False and d2_library_smv_vh == False and d2_muzclub_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_aidpost_smv_vh == True:
        scene ext_aidpost_day with dissolve
    if d2_library_smv_vh == True:
        scene ext_library_day with dissolve
    if d2_muzclub_smv_vh == True:
        scene ext_musclub_day with dissolve
    if d2_clubs_smv_vh == True:
        scene ext_clubs_day with dissolve
    "Я отправился к зданию клубов."
    "Карту я уже знаю наизусть, так что для меня не составит труда дойти туда с закрытыми глазами."
    scene ext_clubs_day with dissolve
    th "Вот я и пришёл. {w}Ну что ж, пойдем знакомиться с гениями робототехники."
    "Так, надеюсь мне не придется вступать к ним в клуб."
    "А если они меня начнут окружать, то в любом случае меня спасет Славя."
    "Наверное с роботом своим возятся сейчас. {w}Придется их отвлечь."
    th "Так, пойдем!"
    scene d5_clubs_robot with dissolve
    "Как я угадал. {w}Для чего им такой робот интересно? {w}На ум лезут только пошлые мысли."
    el "А, ты наверное Семён. Проходи!"
    scene int_clubs_male_day with dissolve
    play ambience ambience_clubs_inside_day fadein 1
    show el normal pioneer far at cleft
    with dissolve
    el "Знакомься, это Шурик!"
    show sh normal_smile pioneer far at cright with dissolve
    sh "Привет, дружище."
    el "О, а ты наверное к нам в клуб пришёл вступать, я прав?"
    sh "Вступай, у нас очень интересно. {w}Мы как раз робота делаем. И тебя научим!"
    me "Да нет, ребят, мне всего лишь обходной лист подписать."
    el "Так а ты вступи, затем подпишем."
    show el laugh pioneer far at cleft
    show sh laugh pioneer far at cright
    "Ну где же Славя, которая должна уже спасать меня?"
    "А вот и она! {w}Моё спасение."
    "Удивительно, что в этот раз всё совпало с оригинальным сюжетом."
    show sl angry pioneer far at center with dissolve
    sl "А что это тут происходит?"
    show sh normal far at cright
    show el normal far at cleft
    sl "Семён, что ты хотел?"
    me "Да, обходной подписать."
    sl "Сейчас все будет."
    "Она взяла у меня обходной лист и подошла к Шурику."
    sl "Подписывай!"
    show sh surprise far at cright
    "Она сказала это в таком тоне, что Шурик немного удивился."
    sh "Х-х-хорошо."
    "Он подписал мне обходной и мы вышли из клубов."
    scene ext_clubs_day with dissolve
    play ambience ambience_boat_station_day fadein 1
    show sl happy pioneer far at center 
    with dissolve
    sl "Вот такие у нас гении тут."
    sl "Они не сильно тебя измучили?"
    "Говоря это она потихоньку приближалась ко мне."
    show sl happy pioneer close at center
    me "Вовсе нет, но спасибо тебе за помощь, я уж думал что никогда не избавлюсь от них."
    "Сказал я улыбнувшись."
    show sl tender pioneer close at center
    sl "Слушай, Семён, а что ты сегодня вечером делаешь?"
    "Этот вопрос ввел меня в ступор."
    "Не уж то она решила меня на свидание позвать? {w}Да нет бред какой-то."
    "Ну нужно как-то отвечать, так что думай Семён."
    menu:
        "Меня Ольга Дмитриевна просила помочь":
            sl "Как жалко, а я хотела тебя гулять позвать."
            show sl sad pioneer close at center
            
        "Ничего не делаю":
            $ d2_SL_svidanka = True
            $ ES_girls_comfort_points_SMVIJ += 1
            sl "Отлично, тогда ничего не планируй!"
            $ ES_Slavya_comfort_points_SMVIJ += 1
            sl "Хочу тебе пару красивых мест показать."
            me "Хорошо, буду с нетерпением ждать этого."
            show sl shy pioneer close at center
            
    me "Слушай я пойду, дела."
    sl "Хорошо, удачи Семён."
    hide sl with dissolve
    "Славя развернулась и пошла в направлении площади."
    th "Ну что, куда теперь?"
    $ d2_clubs_smv_vh = True
    $ d2_aidpost_smv_vh = False
    $ d2_library_smv_vh = False
    $ d2_muzclub_smv_vh = False
            
    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map_SMVIJ

label day2_library_SMVIJ:
    if d2_aidpost_smv_vh == False and d2_clubs_smv_vh == False and d2_library_smv_vh == False and d2_muzclub_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_aidpost_smv_vh == True:
        scene ext_aidpost_day with dissolve
    if d2_library_smv_vh == True:
        scene ext_library_day with dissolve
    if d2_muzclub_smv_vh == True:
        scene ext_musclub_day with dissolve
    if d2_clubs_smv_vh == True:
        scene ext_clubs_day with dissolve
    
    "Я отправился в библиотеку."
    scene ext_library_day with dissolve
    "Наверное дрыхнет во всю."
    "Как бы ее позлить? {w}Ну не знаю, просто разбужу."
    "Время еще терять из-за её сна."
    "Она не заслуживает такого."
    play ambience ambience_library_day fadein 1
    scene int_library_day with dissolve
    un "Ой..."
    th "Господи, я чуть Лену не убил."
    show un scared pioneer close at center with dissolve
    "Она хотела выходить из библиотеки, а я её дверью ударил."
    me "Прости, Лена."
    me "Я не знал что ты тут."
    un "Ничего, со всеми бывает, а мне и не больно вовсе."
    th "Ага, конечно, вон какая шишка вскочила."
    menu:
        "Позаботиться":
            $ ES_Lena_comfort_points_SMVIJ += 1 
            $ d2_LN_pomosh = True
            me "Ничего себе не больно, вон какая шишка вскочила."
            me "Тебе надо к медсестре срочно!"
            me "Сейчас я получу подпись от Жени и пойдем вместе к медсестре."
            show un shy pioneer close at center
            me "Подожди меня снаружи."
            un "Хорошо."
            hide un
            mz "А тебе чего?"
            show mz angry glasses pioneer close at center with dissolve 
            "Видимо не получится позлить."
            "Я настолько шумно открыл дверь, что она проснулась."
            me "Да вот, обходной подписать."
            mz "Давай сюда."
            "Она выхватила у меня обходной и подписала его."
            mz "А теперь вали."
            me "А зачем мне тут оставаться? Бывай."
            stop ambience fadeout 2
            play ambience ambience_camp_center_day fadein 1
            scene ext_library_day with dissolve
            "Как же она меня бесит."
            play music morning fadein 3
            show un normal pioneer close at center with dissolve
            me "Сильно болит?"
            show un surprise pioneer close at center
            un "Нет, уже почти не болит."
            if d2_med_sv_vh == False :
                me "Все равно надо в мед пункт сходить, я там ещё не был, как раз подпишу обходной лист."
                show un shy pioneer close at center
                un "Ну тогда нам по пути. Пойдём?"
                
                
                
            else:
                me "Все равно надо сходить в мед пункт, медсестра как раз там сидит, я недавно подписывал обходной там."
                show un shy pioneer close at center
                un "А ты не опоздаешь другие подписывать?"
                "Я заулыбался."
                me "Нет, не волнуйся."
            
            "Какая же она милая."
            me "Пойдём."
            scene black with dissolve
            "Мы шли с ней медленно."
            "Она взяла меня под руку, потому что у неё кружилась голова."
            "Сильно наверное я её ударил."
            "Какая же она все таки красивая."
            "Мне кажется что стеснение ей даже подходит."
            "Она молчала всю дорогу, но находиться рядом с ней уже значило для меня многое."
            stop music fadeout 2
            scene ext_aidpost_day with dissolve
            "Мы подошли с ней к медпункту."
            "Всю дорогу, Лена смотрела в пол и ничего мне не сказала."
            "Она настолько стеснительная, на сколько я себе это и представлял."
            
            
            
            if d2_med_sv_vh == False :
                show un normal pioneer close at center with dissolve
                un "Пойдём?"
                me "Да, конечно, мне же ещё надо подписать его."
                "С этими словами мы вошли в медпункт."
                play ambience ambience_medstation_inside_day fadeout 1 fadein 2
                scene int_aidpost_day with dissolve
                "Я вошёл первым."
                "Как я и думал, медсестра сидела за столом {w}и заполняла какие-то бумаги."
                me "Здравствуйте."
                show cs normal glasses far at center with dissolve
                cs "Здравствуй, пионер. {w}На что жалуешься?"
                me "Мне обходной подписать надо."
                cs "Ааа, это подождёт, давай мы тебя осмотрим."
                "Не будь со мной Лены..."
                cs "Вижу ты не один пришёл, значит обследование подождёт."
                "Лена обошла меня и подошла к медсестре."
                show un normal pioneer far at cleft with dissolve
                un "Здравствуй Виола."
                cs "Привет, Леночка, ничего себе у тебя шишка."
                cs "Сейчас, я подпишу пионеру обходной и приду к тебе"
                me "Меня Семёном зовут."
                cs "Хорошо, Семён, давай обходной."
                "Она взяла лист, подписала его и сказала."
                cs "Если будут жалобы, обязательно заходи."
                me "Конечно, до свидания."
                "С этими словами я удалился из медпункта."
                
            else:
                show un normal pioneer close at center with dissolve
                un "Пойдёшь?"
                me "Да, давай я тебя провожу."
                un "Хорошо."
                "С этими словами мы вошли в медпункт."
                play ambience ambience_medstation_inside_day fadeout 1 fadein 2
                scene int_aidpost_day with dissolve
                "Я вошёл первым."
                "Как я и думал, Виола сидела за столом {w}и заполняла какие-то бумаги."
                me "Здравствуй, Виола, я вам пациента привел."
                show cs normal glasses far at center with dissolve
                "Лена обошла меня и отправилась ближе к Виоле."
                show un normal pioneer far at cleft with dissolve
                cs "Привет, Леночка, ничего себе у тебя шишка."
                cs "Сейчас мигом исправим."
                cs "Спасибо, Семён, дальше я сама."
                show cs smile far at center
                me "Да, я же уже подписал обходной."
                me "До свидания, Виола."
                cs "Пока, пионер."
            play ambience ambience_boat_station_day fadein 1
            scene ext_aidpost_day with dissolve
            
            if d2_med_sv_vh == False :
                "Странные события, ну да ладно."
                "Вот ещё одна подпись."     
                $ reset_zone("medic_house")
        
        "Ничего не делать":
            $ d2_Lena_nnd == True
            "Ладно, чем я ей помочь то могу?"
            me "Ну ладно, я пойду подпись получу {w}позже увидимся."
            show un shy pioneer close at center
            un "Хорошо."
            hide un 
            "Так и как же будить ее будем?"
            mz "А тебе чего?"
            show mz angry glasses pioneer close at center with dissolve 
            "Видимо не получится позлить."
            "Я настолько шумно открыл дверь, что она проснулась."
            me "Да вот, обходной подписать."
            mz "Давай сюда."
            "Она выхватила у меня обходной и подписала его."
            mz "А теперь вали."
            me "А зачем мне тут оставаться? {w}Бывай."
            play ambience ambience_boat_station_day fadein 1
            scene ext_library_day with dissolve
            "Как же она меня бесит."
            
    
        
    if d2_med_sv_vh == False:
        $ d2_clubs_smv_vh = False 
        $ d2_aidpost_smv_vh = True
        $ d2_library_smv_vh = False
        $ d2_muzclub_smv_vh = False
    else:
        $ d2_clubs_smv_vh = False 
        $ d2_aidpost_smv_vh = True
        $ d2_library_smv_vh = False
        $ d2_muzclub_smv_vh = False
    if d2_Lena_nnd == True:
        $ d2_clubs_smv_vh = False 
        $ d2_aidpost_smv_vh = False
        $ d2_library_smv_vh = True
        $ d2_muzclub_smv_vh = False
    
    
    $ disable_current_zone()
    if d2_med_sv_vh == False:
    
        $ day2_map_necessary_done +=2
    else:
        $ day2_map_necessary_done +=1
    jump day2_map_SMVIJ
    
label day2_aidpost_SMVIJ:
    if d2_aidpost_smv_vh == False and d2_clubs_smv_vh == False and d2_library_smv_vh == False and d2_muzclub_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_aidpost_smv_vh == True:
        scene ext_aidpost_day with dissolve
    if d2_library_smv_vh == True:
        scene ext_library_day with dissolve
    if d2_muzclub_smv_vh == True:
        scene ext_musclub_day with dissolve
    if d2_clubs_smv_vh == True:
        scene ext_clubs_day with dissolve
    
    "Я отправился к Виоле."
    scene ext_aidpost_day with dissolve
    "Найти дорогу мне не составило труда, ведь я знаю этот лагерь как облупленный."
    "Так, надо идти, подпись получить."
    th "Собрались!"
    play sound sfx_knock_door6_closed
    cs "Войдите."
    play ambience ambience_medstation_inside_day fadeout 1 fadein 2
    scene int_aidpost_day with dissolve
    "Виола сидела за столом и разбиралась с какими-то бумагами."
    show cs normal glasses far at center with dissolve
    cs "Привет, пионер, ты новенький наверное?"
    me "Здравствуйте, да я новенький, меня Семёном зовут."
    cs "Прекрасно, а я тебя как раз и ждала, меня Виолой зовут."
    me "Я обходной пришёл подписать."
    cs "Это я знаю, но сперва раздевайся."
    me "Зачем? Я ни на что не жалуюсь."
    cs "Как это зачем? Смотреть тебя будем, мало ли что."
    cs "Раздевайся, раздевайся."
    th "Что же делать?"
    cs "Ну, я жду."
    play sound sfx_open_door_kick
    cs "Кого ещё принесло?"
    show us cry2 pioneer far at cleft with dissolve
    cs "Это что ещё за рана у тебя? {w}Где ты так поранилась?"
    us "Да на пляже."
    "Странно, этого не было в оригинальном сюжете."
    cs "Давай сюда обходной!"
    "Она взяла лист и подписала его."
    cs "Если что болит, сразу ко мне."
    me "Хорошо, я пойду."
    cs "Пока, пионер."
    me "До свидания, Виола."
    play ambience ambience_boat_station_day fadein 1
    scene ext_aidpost_day with dissolve
    "Фух, что вообще тут происходит?"
    "Ладно."
    
    $ d2_clubs_smv_vh = False 
    $ d2_aidpost_smv_vh = True
    $ d2_library_smv_vh = False
    $ d2_muzclub_smv_vh = False
    
    $ d2_med_sv_vh = True
    
    
    $ disable_current_zone()
    $ day2_map_necessary_done +=1
    jump day2_map_SMVIJ
    
label day2_main_SMVIJ_mode2:
    play ambience ambience_camp_center_day fadein 1
    scene ext_square_day with dissolve
    "Итак, я собрал все подписи."
    "Теперь надо Леру с Кристиной найти, а то они загуляли где-то."
    "Было бы проще если бы я слушал на линейке, но что поделать, меня не изменить."
    th "Куда они могли отправиться?"
    menu:
        "Пляж":
            "Я решил, что они вполне могли пойти на пляж."
            "После трудного дня любой захочет расслабиться у берега в теплом песочке."
            scene ext_dining_hall_away_day with dissolve
            $ renpy.pause(1)
            play ambience ambience_boat_station_day fadeout 2 fadein 1
            scene ext_beach_day with dissolve 
            "На пляже было много пионеров."
            "Кто-то плавал, кто-то следил за порядком, но пока не было видно Леры или Кристины."
            "Я решил, что лучшим решением будет встретиться с ними на обеде и отправился к домику."
            play ambience ambience_camp_center_day fadein 1
            
        "Сцена":
            "Сегодня Славя целый день вьётся вокруг меня."
            "Сцена наверняка пустует и пылится."
            "Лера с Кристиной могут вполне убирать сцену. {w}Я направлюсь туда"
            scene ext_library_day with dissolve
            $ renpy.pause(1)
            scene ext_stage_normal_day with dissolve
            "Как-то я прогадал, возле сцены была Алиса."
            if d2_Al_scene:
                th "Пойду пообщаюсь с ней."
                show dv smile pioneer far at center with dissolve
                "Она с усмешкой спросила."
                dv "Что, послушать пришёл?"
                show dv shy pioneer far at center
                me "Ну может быть и так."
                dv "Ну тогда садись, чего пришёл, слушай."
                show dv smile pioneer far at center
                play music alice_guitar fadein 2
                scene d3_dv_scene_2 with dissolve
                "Она играла очень красиво."
                "Не знаю что это за мелодия, но звучит она очень романтично."
                $ renpy.notify ("Вы можете продолжать слушать музыку, а можете пропустить.")
                ""
                stop music fadeout 2
                me "Очень красиво играешь."
                dv "Я знаю."
                me "Ладно, я пойду, меня Ольга Дмитриевна попросила зайти."
                dv "Валяй, на обеде свидимся."
            else:   
                th "Пусть играет себе, а я по тихому уйду."
                
    scene ext_library_day with dissolve
    $ renpy.pause(1)
    scene ext_houses_day with dissolve          
    play sound sfx_dinner_horn_processed
    "Не успел я дойти до нашего домика, как прозвучал горн на обед."
    th "Ну что, потопали на обед?"
    scene ext_dining_hall_away_day with dissolve
    "Я подошёл к столовой и принялся ждать."
    $ renpy.pause(2)
    scene black with dissolve
    $ renpy.pause(2)
    scene ext_dining_hall_near_day with dissolve
    "Я прождал минут 10, но Леры и Кристины не было видно."
    th "Может быть они уже в столовой?"
    "Внезапно ко мне подошла вожатая."
    show mt normal pioneer far at center with dissolve
    mt "Семён, а ты чего сидишь тут?"
    me "Да я вот Кристину жду."
    mt "Её не будет на обеде, я ей слишком сложное задание дала, поэтому она придёт только к ужину."
    "Да что это за задание такое? {w}Где мне теперь искать Леру?"
    "Ладно, ничего не поделать, придётся кушать без них."
    me "Хорошо, тогда пойду в столовую."
    mt "Приятного аппетита."
    play ambience ambience_dining_hall_full fadein 1
    scene int_dining_hall_people_day with dissolve
    "Я вошёл в столовую."
    "Столовая была набита полностью пионерами."
    "Место было лишь рядом с Ульяной и Алисой."
    th "Ну выбора у меня нет."
    "Я взял поднос с едой и направился к столику."
    me "Можно присесть с вами?"
    if d2_Al_scene:
        show us normal pioneer far at cleft with dissolve
        show dv normal pioneer far at cright with dissolve
        dv "Привет, Семён."
        dv "Плюхайся."
        "Она глазами указала на стул рядом."
        "Я послушно взял стул и присел."
        show dv smile pioneer far at cright
        dv "Сказала же, на обеде свидимся. {w}Приятного аппетита."
        me "И вам того же, девочки."
        
        $ renpy.pause(2)
        scene black with dissolve
        $ renpy.pause(2)
        scene int_dining_hall_people_day with dissolve
        show us normal pioneer far at cleft with dissolve
        show dv normal pioneer far at cright with dissolve
        "Я мигом расправился с едой, но девочки все ещё ели."
        me "Ладно девчонки, удачи."
        "Я решил не мешать и удалился из столовой."
    else:
        play music music_list["awakening_power"] fadein 1
        show us normal pioneer far at cleft with dissolve
        show dv rage pioneer far at cright with dissolve
        dv "Ты совсем страх потерял?"
        dv "Ешь стоя."
        "Мне было все равно на её разговоры, поэтому я просто сел к ним за стол."
        show us surp2 pioneer far at cleft
        "Игнорируя их, я закончил трапезу. {w}Позже, я поспешил удалиться из столовой."
        stop music fadeout 2
    
    play ambience ambience_camp_center_day fadeout 2 fadein 1 
    scene ext_dining_hall_near_day with dissolve    
    if d2_SL_svidanka:
        "И тут я вспомнил, что мне ещё предстоит свидание со Славей."
        th "Она сказала вечером, но во сколько это?"
        "Надо найти её и узнать."
        "А вот кстати и Славяна."
        show sl smile pioneer close at center with dissolve
        me "Привет, Славя."
        sl "Привет Семён."
        sl "Слушай, я же забыла сказать тебе во сколько и где мы встречаемся."
        show sl shy pioneer close at center
        sl "Дурочка я, совсем заработалась."
        show sl normal pioneer close at center
        me "Вовсе и не дурочка, просто забыла {w}со всеми бывает."
        show sl smile pioneer close at center
        sl "Ладно, смотри,  после ужина иди на пляж, там и встретимся."
        me "Хорошо, я все понял."
        sl "Ладно, Семён, долг зовёт, я пойду."
        me "До встречи."
        sl "До встречи."
        hide sl with dspr
        "Она встала со скамейки и убежала за столовую."
            
    else:
        "Я сел на скамейку возле столовой и принялся ждать."
            

    $ renpy.pause(2)
    scene black with dissolve
    $ renpy.pause(2)
    scene ext_dining_hall_near_day with dissolve  
    "Так я просидел минут 20."
    "Пока я сидел, все пионеры уже закончили свою трапезу и ушли по делам."
    "Надо было чем-то себя занять, поэтому я решил, что стоит поискать Леру."
    th "Куда пойдем, Семён?"    
    
    $ disable_all_zones()

    $ set_zone("sport_area","day2_sport_area_SMVIJ")
    $ set_zone("boat_station","day2_boat_station_SMVIJ")
    $ set_zone("camp_entrance","day2_camp_entrance_SMVIJ")
    $ set_zone("forest","day2_forest_SMVIJ")

    jump day2_map_poisk_SMVIJ
    
label day2_map_poisk_SMVIJ:
    if day2_poisk_necessary_done == 4:
        jump day2_poisk_SMVIJ_mode2
        
    $ show_map()
    
label day2_sport_area_SMVIJ:
    if d2_sport_area_smv_vh == False and d2_forest_smv_vh == False and d2_boat_station_smv_vh == False and d2_camp_entrance_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_sport_area_smv_vh == True:
        scene ext_playground_day with dissolve
    if d2_boat_station_smv_vh == True:
        scene ext_boathouse_day with dissolve
    if d2_camp_entrance_smv_vh == True:
        scene ext_no_bus with dissolve
    if d2_forest_smv_vh == True:
        scene ext_path_day with dissolve
    
    
    "Может они убирают спортплощадку?"
    "Хотя что они там забыли?"
    "Наша вожатая непредсказуема, поэтому стоит проверить."
    play ambience ambience_soccer_play_background fadeout 1 fadein 2
    scene ext_playground_day with dissolve
    "На площадке было много детворы, но ни Леры, ни Кристины я не увидел."
    "Тут одна фигура подбежала ко мне."
    show us smile pioneer at center with dissolve
    us "О, Семён. А что ты тут забыл?"
    me "Да я тут ищу кое-кого."
    us "Ну это может подождать. Пойдем с нами поиграем?"
    me "Ну... Я не знаю, я давно не играл в футбол."
    show us grin pioneer at center
    us "Ой, да ты что. У нас таких вся команда, кроме меня, конечно. Выделяться не будешь."
    th "Стоит ли? Может всё-таки сыграть чуть-чуть?"
    us "Ну так что, ты идешь?"
    menu:
        "Поиграть":
            $ ES_girls_comfort_points_SMVIJ += 1
            $ ES_Ulya_comfort_points_SMVIJ += 1
            th "А почему бы и нет? Раз она говорит, что там таких же вся команда, то я могу попробовать."
            me "Ну давай, только чуть-чуть."
            show us laugh pioneer at center 
            us "Ура! {w}Давай быстрее на поле!"
            "Я послушно побежал за Ульяной на поле."
            hide us with dspr
            "Вокруг была детвора лет так 12-14, но не больше."
            th "А, ну так это будет легко."
            $ set_mode_nvl()
            "Свисток. Мяч в игре. {w}Так получилось, что мы с Ульяной в разных командах. {w}Ну это не важно, у неё вся команда вафельная, думаю, что я смогу что-то сделать."
            "Инициативу берет на себя команда Ульяны, а если быть точным, то только Ульяна. Она, обводя противников, подходит к воротам, где я уже стою и жду её мяча."
            "УДАР! {w}Мяч прилетает прямо ко мне в руки."
            me "И это всё, что ты можешь?"
            us "Ну я тебе еще покажу."
            "Она попыталась скорчить страшную гримасу, но получилось просто забавно. {w}Я кое-как сдержал смех."
            "Правил у нас не было четких, поэтому мне мои союзники дали право выйти в атаку."
            "Мяч опустился на землю, я уже готов к атаке. {w}Пульсация идет бешеным темпом, то ли от выброса адреналина, то ли от страха облажаться."
            "Плевать, вот и мой момент."
            "Я выхожу с середины поля, отдав пас ближайшему союзнику. {w}Он обработал мяч и ведет его к створу ворот."
            "Обратный пас не заставил себя ждать, мяч летит ко мне. {w}Мяч катится по полю, пролетая сквозь противников. {w}Я взял мяч и теперь буду один, ибо я вышел на финальную стадию."
            "Передо мной стоит маленький, полный мальчик. {w}Мда... Правила дворового футбола: самый толстый на ворота. {w}Я не стал пробивать со всей силы, потому что побоялся попасть в мальчика."
            "Вместо этого я показал, что хочу бить в правый нижний угол. Одного моего взгляда и замаха хватило, чтобы парень подумал так, как я хотел. Он сместился вправо. Именно это мне и было нужно."
            "Я слабенько толкнул мяч в левый угол. Глаза парня чуть не вылетели из орбит. Он понимает, что допустил ошибку, но мяч уже приближается к воротам."
            play sound sfx_soccer_ball_gate
            "Мяч попал в ворота, счет открыт. 1:0 в нашу пользу."
            us "Эй! Так не честно."
            me "Почему-то я ждал этого выкрика."
            us "Ну всё, сейчас ты у меня попляшешь."
            "Я понял, что сейчас она будет стараться изо всех сил, поэтому отбежал чуть назад."
            "Я дал сигнал своему напарнику, что теперь я на воротах. Кивнув, он уступил мне место вратаря."
            nvl clear
            "Свисток, мяч снова в игре. {w}Ульяна дала пас какому-то пареньку. Он очень даже хорош, проходит все степени защиты одна за другой."
            "Пас идет Ульяне, и она с радостью его принимает. {w}С огнём в глазах она прорывает последнею степень защиты и направляется ко мне."
            "Выход один на один, облажаться нельзя. {w}Она подходит ближе и ближе. По моей щеке стекают капли пота, но я стараюсь держать концентрацию."
            show d3_soccer with dspr
            "Ульяна замахивается и мяч отправляется в свободный полет."
            "Я встал в позу и был готов ловить мяч. {w}Мяч летел в девятку, так что я попытался дотянуться... {w}Но не смог. Мяч коснулся моих пальцев и всё равно упал в ворота."
            hide d3_soccer with dspr
            us "Ну что, как теперь петь будешь?"
            me "Мы пока не закончили."
            "Счет 1:1, и только я могу его изменить."
            "Свисток, мяч в игре. {w}Я вспомнил все свои умения, которые мне могли тут пригодиться, напряг все свои мышцы и готов был сносить каждого на пути."
            mi "Семён, покажи им!"
            "Чччт0000000оооооооо? {w}Я посмотрел налево, а там Мику всеми силами пытается поддержать меня. Она уже поговорила с девочкой, которая ведет счет, чтобы быть в курсе событий."
            "Удивительно, что она еще плакат не принесла и шарф не нацепила. {w}Значит сейчас мне надо постараться на все сто процентов."
            "Свисток уже был, а я всё стою, и это было моей первой ошибкой. Толпа голодных пацанов и одна девочка бегут ко мне навстречу с желанием съесть меня живьем."
            "Я отдал пас своему союзнику, а он, понимая что к чему, отдал пас обратно, когда я пробежал через баррикаду из зомби-школьников."
            "Мяч катится по земле и скоро оказывается у меня. Я принимаю его и продвигаюсь вперед."
            "Всё тот же парень стоит на воротах, он не показывает страх, в глазах его одна решимость. {w}Я понял, что сейчас, когда на меня смотрят, я просто не могу облажаться, поэтому я замахнулся так, что аж Мику ахнула."
            "Парень даже не шелохнулся, что меня поразило. На него бежит парень в два раза его выше, замахивается со всей силы, а он даже не моргнул."
            "Я замахнулся и начал ударять, парень прыгнул в бок, желая поймать мяч, но тут он прогадал, я всего лишь замахивался."
            nvl clear
            "Как только парень оказался на земле, мне было достаточно только пнуть мяч в другую сторону, что я и сделал."
            "Мяч катится и катится. {w}Вскоре он остановился за линией, даже не коснувшись сетки."
            "Счёт 2:1 в нашу пользу."
            $ set_mode_adv()
            me "Ну дальше как-нибудь сами, я в вас верю."
            show us normal pioneer at center with dissolve
            us "Эй, ты куда?"
            me "Мне надо поговорить с Мику, да и выдохся я слегка."
            show us grin pioneer at center
            us "Слабак! Ну и валяй."
            hide us with dspr
            "С этими словами Ульяна развернулась и побежала к своей команде."
            "Я, стараясь дышать ровно, подошел к Мику."
            show mi smile pioneer at center with dissolve
            me "Мику, привет еще раз. Ты не видела Кристину?"
            mi "Кристину? Нет, сегодня я её не видела. {w}Кстати, мог бы и детишкам дать поиграть, а то один играл только."
            th "А кто это сейчас поднимал флаги в мою честь? {w}Этих девушек не поймешь."
            me "А ты чего не в клубе, кстати."
            show mi laugh pioneer at center
            mi "Ну не буду же я там сидеть всё время."
            me "Ну да, верно. Ладно, я тогда пойду. До встречи."
            show mi smile pioneer at center
            mi "Удачи. Заходи в клуб, если что."
            me "Договорились."
            hide mi with dspr
            "Я развернулся и направился на дальнейшие поиски."
            
            
            
            
            
            
            
        "Отказаться":
            th "Нет, мне надо Леру искать."
            me "Прости, Уля, надо идти искать Кристину, у меня к ней одно дело."
            $ ES_Lera_comfort_points_SMVIJ += 1
            show us grin pioneer at center
            us "Ну и валяй, а я пошла."
            hide us with dspr
            "Ульяна убежала, а я пошел на дальнейшие поиски."
    
    play ambience ambience_camp_center_day fadein 1
    
    $ d2_sport_area_smv_vh = True
    $ d2_boat_station_smv_vh = False
    $ d2_camp_entrance_smv_vh = False
    $ d2_forest_smv_vh = False
    
    $ disable_current_zone()
    $ day2_poisk_necessary_done +=1
    jump day2_map_poisk_SMVIJ
    
label day2_boat_station_SMVIJ:
    if d2_sport_area_smv_vh == False and d2_forest_smv_vh == False and d2_boat_station_smv_vh == False and d2_camp_entrance_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_sport_area_smv_vh == True:
        scene ext_playground_day with dissolve
    if d2_boat_station_smv_vh == True:
        scene ext_boathouse_day with dissolve
    if d2_camp_entrance_smv_vh == True:
        scene ext_no_bus with dissolve
    if d2_forest_smv_vh == True:
        scene ext_path_day with dissolve
        
    $ renpy.pause(2, hard=True)
    play ambience ambience_boat_station_day fadein 1
    scene ext_boathouse_day with dissolve
    "На причале тоже пусто, пионеров совсем нет, только я один."
    "Я присел на край причала и свесил ноги к воде, смотря в своё отражение на воде."
    "Легкая рябь на воде то дело и пытается исказить его, но это удается ей с трудом."
    "Я провел так в мыслях некоторое время."
    "Пока меня не потревожили..."
    show mt normal pioneer at center with dissolve
    mt "Семён, а что это мы тут прохлаждаемся? Бегунок кто заполнять будет?"
    th "Вот же появляется не в том месте и не в то время... Прямо как призрак."
    me "Да я уже всё заполнил."
    show mt smile pioneer at center
    mt "Тогда давай сюда."
    "Я протянул заполненный листок."
    "Вожатая сложила его пополам и сунула в карман."
    th "Ну, ничего другого я и не ожидал. Может стоило сразу заполнить его от своей руки? Она же всё равно не поверяет."
    if d2_MT_palevo:
        show mt angry pioneer at center
        mt "Семён, а что ты сегодня у склада делал? И почему не остановился?"
        th "Ох блин... Хотя этот разговор всё равно должен был рано или поздно состояться."
        me "А вы мне что-то кричали? Я не слышал, честно."
        "Я решил играть в глухого дурака."
        show mt normal pioneer at center
        mt "Ну ладно, а что ты там делал?"
        me "Я искал умывальники, но потом понял, что пришел совершенно не туда, а потом вдалеке я увидел пионера какого-то, вот и решил у него спросить."
        "Вожатая некоторое время пребывает в ступоре."
        show mt smile pioneer at center
        mt "Ладно, будем считать, что ты меня убедил."
        me "Почему убедил? Я же правду говорю."
        mt "Да верю-верю я тебе, Семён, не волнуйся ты так. Только подозрений добавляешь."
        
        
    mt "Долго тут будешь сидеть?"
    me "Нет, я уже скоро хотел уходить."
    mt "Ну ладно, а я уже пойду, дел еще много."
    me "Да, хорошо."
    hide mt with dspr
    "Вожатая развернулась и ушла по своим делам."
    "Я же остался опять один."
    th "Мне тоже пора выдвигаться."
    "Я встал и сделал маленькую разминку, потому что ноги затекли."
    th "Надо идти дальше."
    play ambience ambience_camp_center_day fadein 1
    
    $ d2_sport_area_smv_vh = False
    $ d2_boat_station_smv_vh = True
    $ d2_camp_entrance_smv_vh = False
    $ d2_forest_smv_vh = False
    
    $ disable_current_zone()
    $ day2_poisk_necessary_done +=1
    jump day2_map_poisk_SMVIJ
    
label day2_camp_entrance_SMVIJ:
    if d2_sport_area_smv_vh == False and d2_forest_smv_vh == False and d2_boat_station_smv_vh == False and d2_camp_entrance_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_sport_area_smv_vh == True:
        scene ext_playground_day with dissolve
    if d2_boat_station_smv_vh == True:
        scene ext_boathouse_day with dissolve
    if d2_camp_entrance_smv_vh == True:
        scene ext_no_bus with dissolve
    if d2_forest_smv_vh == True:
        scene ext_path_day with dissolve
        
    "Точно, они вполне могут быть у ворот. Убирать там или просто лицезреть дали этой локации, потому что полноценным миром это точно не назвать."    
    scene ext_no_bus with dissolve
    "Здесь пусто..."
    "Я осмотрелся по сторонам, ни души."
    "Только ветер треплет волосы и шепчет на ухо что-то непонятное."
    "Мне здесь делать больше нечего, надо бы отправляться."
    
    
    
    $ d2_sport_area_smv_vh = False
    $ d2_boat_station_smv_vh = False
    $ d2_camp_entrance_smv_vh = True
    $ d2_forest_smv_vh = False
    
    $ disable_current_zone()
    $ day2_poisk_necessary_done +=1
    jump day2_map_poisk_SMVIJ

label day2_forest_SMVIJ:
    if d2_sport_area_smv_vh == False and d2_forest_smv_vh == False and d2_boat_station_smv_vh == False and d2_camp_entrance_smv_vh == False :
        scene ext_dining_hall_near_day with dissolve
    if d2_sport_area_smv_vh == True:
        scene ext_playground_day with dissolve
    if d2_boat_station_smv_vh == True:
        scene ext_boathouse_day with dissolve
    if d2_camp_entrance_smv_vh == True:
        scene ext_no_bus with dissolve
    if d2_forest_smv_vh == True:
        scene ext_path_day with dissolve
        
    "А может в лесу задание дали?"
    "Вожатая сегодня всё время твердит о каком-то задании. Если оно сложное, то это точно не уборка какая-то. Надо бы проверить лес."
    play ambience ambience_forest_day fadein 1
    scene ext_path_day with dissolve
    "Я вышел на лесную тропинку и стал осматривать местность."
    "Тишина, только птички украшают эту пустоту."
    th "Может Крикнуть?"
    th "Можно попробовать."
    me "Кристина!!"
    "Эхом это имя отдалось мне..."
    th "Значит пусто..."
    un "Напугал ты меня..."
    "Спустя какое-то время Лена показалась из кустов."
    show un normal pioneer at center
    un "Зачем так кричать?"
    me "Да я просто весь лагерь обыскал, да вот найти Кристину всё никак не могу. Ты её не видела?"
    "Лена только покачала головой."
    "И только потом я заметил в руках у неё блокнот."
    me "А что это?"
    "Я указал пальцем на блокнот."
    show un shy pioneer at center
    un "Это... Просто блокнот, там ничего."
    "Не знаю, какая пчела меня укусила, но я хотел узнать, что в этом блокноте."
    me "А можно мне посмотреть?"
    un "За-зачем?..."
    me "Ну просто интересно. Может и я что-то нарисую."
    show un smile pioneer at center
    un "Только на чуть-чуть."
    "Она трясущимися руками протягивает блокнот."
    "Я взял его и раскрыл на первой странице."
    "Пусто."
    "Вторая страница."
    "Пусто."
    "Третья страница."
    "Пусто."
    "Я решил перемотать на середину."
    "А вот тут уже что-то есть, но написано карандашом."
    show un scared pioneer at center
    un "Не смотри!"
    "Но её слов было не достаточно, я уже давно успел прочитать всё, что было написано на это странице."
    "{i}Он медленно сигару закурил,{/i}"
    "{i}Рука коснулась талии моей,{/i}"
    "{i}Запоминая все мои детали,{/i}"
    "{i}На ушко шёпотом спросил....{/i}"
    "Всего одно четверостишье."
    $ ES_Lena_comfort_points_SMVIJ += 1
    "Лена вытянула у меня блокнот из рук."
    un "Ну я же просила..."
    me "Очень красиво получилось. Я не шучу. Почему не продолжила?"
    show un surprise pioneer at center
    un "Ты серьезно? Мне не нравится этот стих. Да пока вдохновения нет, если честно."
    me "Ну тогда не буду отвлекать, удачи."
    show un smile pioneer at center
    un "Спасибо. И тебе."
    hide un with dspr
    "На этом наш диалог и закончился."
    "Я развернулся и пошел дальше."
    play ambience ambience_camp_center_day fadein 1
    
    
    
    
    
    $ d2_sport_area_smv_vh = False
    $ d2_boat_station_smv_vh = False
    $ d2_camp_entrance_smv_vh = False
    $ d2_forest_smv_vh = True
    
    $ disable_current_zone()
    $ day2_poisk_necessary_done +=1
    jump day2_map_poisk_SMVIJ
    
label day2_poisk_SMVIJ_mode2:
    play ambience ambience_forest_day fadein 1
    scene ext_polyana_day with dissolve
    "Итак я обошёл все места, но так и не нашёл их."
    if d2_SL_svidanka:
        "Я уже опустил руки и решил ждать их после прогулки со Славей."
    else:
        "Я уже опустил руки и решил ждать их после ужина."
    "Скоро должен быть ужин."
    play music spring fadein 2
    "Посижу пожалуй подумаю о жизни."
    "Это место постоянно вызывает поток нескончаемых мыслей, прервать которые может лишь горн на ужин."
    "Итак вот уже второй день я провёл в этом лагере. {w}Тут все не так как я себе представлял, все разные, живые."
    "У каждого какое-то есть своё дело."
    "Каждый из них отличается чем-то друг от друга. {w}Играя в игру дома, я представлял всех куклами, которые играют свою роль."
    "Тут очень много незнакомых мне людей, которые не играют ключевую роль, но как мне кажется - Кристина в моём случае как раз таки странный и ключевой персонаж."
    "Не хотелось бы уходить из этого лагеря, а впрочем ладно. У меня ещё целых 5 дней, надо насладиться вдоволь."
    "Интересно, какое задание у Леры и Кристины, не уж то они ещё на задании, вряд ли, но вполне возможно."
    scene ext_polyana_sunset with dissolve
    stop music fadeout 2
    "Где же ужин? Может я его пропустил?"
    play sound sfx_dinner_horn_processed
    extend " А нет."
    th "Ну что ж, пойдем Семён?"
    play ambience ambience_camp_center_evening fadein 1
    scene ext_square_sunset with dissolve
    $ renpy.pause (2)
    scene ext_dining_hall_away_sunset with dissolve
    play music soft_horn fadein 2
    "Возле столовой столпилось много народу во главе с Ольгой Дмитриевной и что-то буйно обсуждали."
    "Что же случилось?"
    "Неужели девочки пропали."
    "Очень много тревожных мыслей начали посещать меня в этот момент."
    "А если они заблудились в лесу?"
    "Стоит подойти к ним."
    "Не могу сдвинуться с места, очень переживаю, что же случилось?"
    th "Так, Семён, соберись, ничего такого. {w}Пошли!"
    scene ext_dining_hall_near_sunset
    show mt normal pioneer far at center 
    show sl normal pioneer far at cright
    show el normal pioneer far at cleft 
    show dv normal pioneer far at left 
    show us normal pioneer far at left 
    show mi smile pioneer far at right
    with dissolve
    "Мику улыбается."
    stop music fadeout 2
    "Мне стало поспокойнее. {w}Они всего лишь планируют игру в карты."
    el "О, привет Семён."
    el "Ты же будешь в карты играть сегодня?"
    me "Нет, простите, у меня другие планы."
    el "Но как же так. Ты что не умеешь играть?"
    me "Играть я умею."
    me "Я же сказал, у меня просто другие планы."
    sl "Да, я тоже не буду у меня тоже планы есть."
    show el surprise pioneer far at cleft
    "У Электроника пробежало на лице удивление, но потом так же быстро и пропало."
    show el normal pioneer far at cleft
    if d2_SL_svidanka:
        th "Под планами Славя точно имела в виду нашу прогулку."
    else:
        th "Сама пригласила погулять, а теперь у неё планы."
    show mt smile pioneer far at center
    mt "Странно всё это, ну да ладно."
    mt "Итак, значит все остальные играют?"
    Pioners_SMVIJ "Да."
    show mt normal pioneer far at center
    "Ребята ответили хором."
    th "Хм, где же Кристина с Лерой? {w}Что до сих пор не вернулись? {w}Странно это, даже очень."
    mt "Ну тогда идем потчевать, и так уже долго тут торчим."
    play ambience ambience_dining_hall_full fadein 1        
    scene int_dining_hall_people_sunset with dissolve
    "Мы вошли в столовую."
    "Нигде я не видел ни Леры, ни Кристины."
    th "Надеюсь с ними все хорошо! {w}По крайней мере будет время провести вечер с обитателями данного места."
    "Я взял еду и принялся выискивать свободный столик."
    "Свободным столик оказался лишь рядом с Леной и Мику."
    "Забавно, две противоположности за одним столиком."
    "Как они вместе в одном домике уживаются?"
    "Ну что же, выбор не велик."
    show un normal pioneer far at cleft 
    show mi normal pioneer far at cright 
    with dissolve
    me "Можно присяду?"
    show mi smile pioneer far at cright
    mi "Конечно-конечно присаживайся, мест больше нет."
    "Она проговорила это удивительно быстро, я даже подумал что она против, но потом сообразил по её взгляду."
    me "Как ваш день девочки?"
    mi "Очень хорошо, вот новую песенку сочинила, хочешь спою как-нибудь? А вообще скучно одной в клубе, эх если бы кто-то вступил. О чем это я? А у тебя как день?"
    th "Боже, как же быстро."
    show mi normal pioneer far at cright
    me "Замечательно, обошёл весь лагерь, теперь знаю его как свои пять пальцев."
    if d2_LN_pomosh:
        "Все это время Лена украдкой поглядывала на меня."
        "Я тоже начал смотреть на неё."
        "..."
        show un shocked pioneer far at cleft 
        un "Что-то не так?"
        me "Да нет, все хорошо."
        "Сказал я улыбнувшись."
        show un smile pioneer far at cleft
        un "Ну ладно."
        "Она улыбнулась и продолжила кушать."
    else:
        "Все это время Лена просто ела и ничего не говорила."
        "Скорее всего её обидела ситуация с дверью. {w}Хотя нет, мы же нормально общались перед ужином."
        "Ладно, пускай кушает, не буду её отвлекать."
    "Мы закончили трапезу и я вышел прочь из столовой."
    play ambience ambience_camp_center_evening fadeout 2 fadein 1
    scene ext_dining_hall_near_sunset with dissolve
    "Посижу немного, а потом схожу на пляж."
    scene black with dissolve
    $ renpy.pause(1)
    scene ext_dining_hall_near_sunset with dissolve
    "Что-то я засиделся, пора бы уже идти на пляж."
    if d2_SL_svidanka:
        th "Так? А что я Славе скажу?"
        th "О чем мы будем болтать?"
        "Ладно это не важно, главное что проведу вечер не один."
    else:
        "Слава богу я отказался от прогулки. {w}Будет время посидеть - подумать."
    scene ext_square_sunset with dissolve   
    $ renpy.pause(1)
    play ambience ambience_boat_station_day fadeout 2 fadein 1
    $ sunset_time()
    $ persistent.sprite_time = 'sunset' 
    scene ext_beach_sunset with dissolve
    th "Как же тут красиво. {w}Сидя в пыльном городе я бы никогда не понял что есть красота."
    if d2_SL_svidanka:
        th "Скоро должна уже прийти Славя."
        th "Она человек ответственный, так что не придется её долго ждать, я в этом уверен."
        "Ветер легонько поддувает, ослабляя действие жары, которая стала только сильнее с приходом вечера."
        "Я, сам того не замечая, стал рисовать на песке всякие странные фигуры: узоры, цветочки и другое."
        "Всегда хотел научиться рисовать, но мне от природы этого не дано. Каждый раз, когда берусь за карандаш, то не хватает смелости и терпение продолжить рисовать после двух-трех линий, ибо они получаются очень кривыми."
        show sl smile2 dress at center with dissolve
        sl "А у тебя неплохо получается."
        "Я немного пошатнулся от увиденного, но быстро и почти незаметно, вернулся в изначальную позицию."
        me "Не пугай так."
        sl "Я тебя напугала?"
        me "Ну если только чуть-чуть."
        sl "Ладно, в следующий раз учту. Ну что, есть идеи, куда пойти?"
        me "Я же тут новенький, совершенно ничего не знаю. Да и это твоя идея была показать мне красивые места лагеря."
        show sl tender dress at center
        sl "Ой, точно."
        show sl smile dress at center
        extend " Дай подумать."
        "Славя ушла в размышления, но надолго она меня не оставила."
        sl "Точно. Пойдем, я тебе покажу одно красивое место."
        hide sl with dspr
        "Славя развернулась и начала медленно отдаляться, и только подол её платья зовет меня за собой."
        "Я встал с песка, отряхнул шорты и пошел за ней."
        play ambience ambience_camp_center_evening fadeout 2 fadein 1
        scene ext_square_sunset with dissolve
        "Мы оказались на площади, болтая о всём, что не стоит даже упоминания. Кто где вырос, чем занимается и увлекается по жизни."
        "Не подумал бы, что так называемые куклы могут говорить такие вещи и в таких подробностях о себе."
        "Значит здесь всё немного иначе, чем в оригинале, не так ли?"
        "Вдалеке я увидел ту самую фигуру, которую забыть просто невозможно. Лера шла с Кристиной, которая несла какую-то корзину."
        "Я думал их позвать, но потом подумал, что это может стоить мне фингала под глазом."
        "Я немного ускорил шаг. Совсем чуть-чуть, Славя этого даже не заметила."
        "Но именно в этот момент Лера обернулась и увидела нас."
        th "Вот же блин..."
        "Лера смотрит на меня какое-то время, но потом оборачивается и идет дальше вместе с Кристиной, но в этот раз они молчат."
        th "Ну ладно. Потом с ней поговорим."
        
        scene ext_path_sunset with dissolve
        play ambience ambience_forest_evening fadeout 2 fadein 1
        "Славя всё идет рядом со мной и расспрашивает меня о моей жизни."
        th "Сколько же всего она хочет узнать?"
        sl "Вот по этой дорожке я обычно бегаю по утрам. Тут свежий воздух, а роса порой обжигает ноги. Это так приятно."
        me "Угу, могу себе представить."
        "Я уже понимал, куда она ведет, но решил спросить."
        me "А сколько нам еще идти до этого места?"
        sl "Мы уже почти пришли."
        "И правда. То самое место уже виднелось за поворотом."
        scene ext_polyana_sunset with dissolve
        show sl smile2 dress at center with dissolve
        sl "Ну вот мы и пришли."
        "Да, именно это место она и хотела мне показать."
        me "Тут так красиво."
        "Я не соврал. Это место очень красиво, даже несмотря на то, что видел его я кучу раз."
        sl "Я знаю. Я часто тут отдыхаю после пробежки."
        me "И как ты только время находишь для этого?"
        me "Неужели тебе не хочется больше в кровати поваляться?"
        show sl laugh dress at center
        sl "Я уже привыкла. Надо просто держать режим."
        me "А тебе никогда не хотелось расслабиться? Ну, сделать что-то такое, чтобы все были в шоке, что ты так умеешь вообще? Удивить всех."
        show sl smile2 dress at center
        sl "Ну что например?"
        me "Ну..."
        "Я впал в раздумья. А ведь это не так легко придумать занятие подобного рода."
        me "Прогулять линейку, поспать подольше, не слушаться вожатую."
        show sl laugh dress at center
        sl "Ты скажи еще шапку зимой носить и хрустальным сервизом бабушки пользоваться."
        me "Ну да, и это тоже, например."
        show sl smile dress at center
        sl "Нет, такого желания не было."
        me "Странно это. Вроде такая молодая, но детство своё не ценишь."
        sl "Да я бы и не сказала, что уж такой ребенок."
        me "И оно верно."
        hide sl with dspr
        "Мы и дальше продолжили болтать о всякой всячине, пока не стало темнеть."
        play ambience ambience_forest_night fadeout 2 fadein 1
        $ night_time()
        $ persistent.sprite_time = 'night'
        
        scene ext_polyana_night with dissolve
        show sl smile dress at center with dspr
        sl "Пойдем, я тебе еще кое-что покажу."
        me "Ну пошли."
        th "Чем она сможет меня удивить?"
        hide sl with dissolve
        "Славя пошла в том направлении, которого я не видел в игре ранее."
        th "А вот это будет интересно."
        scene ext_path_night with dissolve
        "Мы вышли на дорожку, которая очень сильно напоминала мне ту, с которой мы и пришли."
        "Ходить в лесу ночью не очень комфортно, как по мне. А Славя чувствует себя, как рыба в воде."
        sl "Это не далеко, мы скоро будем."
        me "Да, хорошо."
        scene black with dspr
        $ renpy.pause (3, hard=True)
        scene ext_path_night with dspr
        "Мы идем уже минут 10, но так и не достигли того самого места."
        sl "Мы уже близко. Тебе там понравится."
        "Сказала Славя и улыбнулась мне ярче луны."
        me "Отлично."
        "Я смог сказать только это, чтобы не промолчать совершенно."
        sl "А вот мы и на месте."
        "Как же тут красиво... {w}Я даже присел."
        play music music_list["meet_me_there"] fadein 1
        scene d3_sl_evening with dspr
        "Это место уже было в игре, но в реальности... {w}В реальности оно еще замечательнее."
        "Славя просто стояла сзади меня и смотрела в даль."
        "Луна смотрела на нас двоих сквозь облака, желая дать нам насладиться видами."
        sl "Знаешь, я тут редко бываю. Особенно в такое время. Тут красиво, не так ли?"
        me "Да..."
        "Я просто не мог говорить, всё мое внимание было приковано к темной бездне впереди нас."
        sl "Но днем тут не так красиво. В последнее время я сюда редко прихожу, хотя в начале смены, после того, как вожатая показала мне это место, я часто сюда ходила."
        sl "Кстати, а почему ты приехал к середине смены?"
        me "К середине?"
        sl "Ну да, ты опоздал на целую неделю. Смены в лагерях длятся две недели."
        th "Точно, и что же мне сказать на такое? {w}Пойдем с банального."
        me "Дома были проблемы. Мама приболела, я не мог оставить её одну."
        sl "Какой ты добрый и ответственный."
        "Я незамедлительно начал краснеть."
        me "Спасибо."
        sl "За правду спасибо не говорят."
        th "А вот теперь о мои щеки точно можно было обжечься."
        me "А что же мне тогда сказать? {w}Благодарю?"
        th "Где-то я уже это сегодня слышал."
        sl "Ты еще и умный. Смог так выбраться из ситуации."
        th "Сейчас мне кажется, что мои щеки ярче, чем угли в костре."
        me "Не думал так про себя."
        sl "А почему?"
        me "Не люблю себя нахваливать."
        sl "Хорошая черта. Тоже не люблю людей с высоким о себе мнением. {w}Нужно быть скромным."
        th "Лера тогда идеал для неё."
        sl "Ладно, Семён, пойдём уже. Вожатая точно искать будет, а если еще учитывать, что ты у неё живешь..."
        me "Точно. Лучше уже пойти."
        "Я встал, еще раз посмотрел в даль через плечо и отправился вместе со Славей в лагерь."
        stop music fadeout 2
        scene ext_path_night with dissolve
        $ renpy.pause (2)
        play ambience ambience_camp_center_night fadein 2
        scene ext_square_night with dissolve
        $ renpy.pause (2)
        scene ext_houses_night with dissolve
        "Вот мы и пришли к месту, где должны разойтись."
        show sl smile2 dress at center
        me "Спасибо тебе большое за экскурсию по столь замечательным местам."
        show sl shy dress at center
        sl "Всегда пожалуйста, Семён."
        sl "Ну... Я пойду?"
        me "А? {w}Конечно, я тебя не задерживаю. Да и мне пора."
        show sl smile2 dress at center 
        sl "Хорошо. Спокойной ночи."
        me "Спокойной ночи."
        hide sl with dspr
        th "Ну и мне пора идти."
        "Я развернулся и медленным, спокойным шагом пошел в сторону своего домика."
        th "Сейчас придется объясняться Лере."
        scene ext_house_of_mt_night with dissolve
        "На пороге меня уже ждала Лера."
        Ler_SM "Где ты был?"
        "Я понял, что сейчас будет ругань. И самая настоящая."
        me "Пойдем в другое место, отойдем. Там спокойно и поговорим."
        Ler_SM "Угу."
        "Лера промычала. Она постаралась вложить в этот звук как можно больше пренебрежения и недоверия."
        "Вдвоем мы пошли в сторону нейтрального места, дороги в лес. Я иду впереди, а Лера сзади."
        play ambience ambience_forest_night fadein 2
        scene ext_path_night with dissolve
        "Мы встали на середине дороги. Взгляд Леры сразу уперся в меня."
        Ler_SM "Ну. {w}И где ты был?"
        me "Это я должен тебя спрашивать. Где ты слонялась весь день? Я тут себе оба локтя искусал, пока волновался за тебя. Телефона тут нет, позвонить некуда. Вожатая говорит, что ты на задании, а подробности раскрывать не хочет."
        "Лера сразу побледнела слегка от количества информации, которую я ей выдал."
        Ler_SM "Мы с Кристиной плыли на остров за земляникой."
        me "Зачем?"
        "Это уже стало походить на допрос. Роль фонаря исполняет яркая луна, только в этом и отличие."
        Ler_SM "Что это за допрос такой?"
        th "Как я и думал..."
        me "Мне просто интересно."
        Ler_SM "Это для торта. Вожатая хотела сюрприз сделать."
        me "И на такой объем земляники она послала только Кристину?"
        Ler_SM "Ты про меня вообще забыл за этот день? Она и меня тоже попросила."
        me "Каким это, простите, образом?"
        extend " Ты забыла, что ты тут на правах гостя незваного? Ты, Лера, невидима! Она позвала только Кристину, а вот она уже , в свою очередь, позвала тебя."
        "И только сейчас до меня дошло, что это прозвучало немного грубо."
        Ler_SM "Пусть и так! Теперь ты. Что ты делал с этой блондинкой?"
        me "Она просто показывала мне лагерь. Влюбилась она в меня, непонятно что ли?"
        Ler_SM "Ты еще скажи, что она тебя насильно заставила идти."
        me "Нет, конечно, я добровольно согласился."
        Ler_SM "Всё с тобой понятно..."
        me "А что мне остается делать? Мне нужно как-то сблизиться с обитателями лагеря, чтобы не было худо потом."
        Ler_SM "Так это можно сделать и без свиданий."
        "Я понял, что криками это дело не решишь, поэтому я решил просто спокойно всё объяснить. Это всегда помогало."
        me "Лера, послушай. Я сейчас объяснюсь. Мне надо сблизиться с девушками из лагеря. И не только с ними, кибернетики тоже идут в счет."
        me "Мне надо, чтобы меня признали. В игре это и было условием того, чтобы выйти из этого лагеря, полного циклов."
        me "Мне надо просто освоиться. Если бы ты была на моём месте, ты бы поступила точно также."
        "Лера сразу размяглась. Она поняла, что просто приревновала."
        Ler_SM "Так ты же уже и так знаешь лагерь, зачем тебе эта экскурсия?"
        me "Но остальные не знают, что я знаю лагерь. Именно поэтому я и согласился."
        "Лера покраснела. Она пытается придумать, как загладить свою вину. Это видно сразу."
        Ler_SM "Прости, что сразу наскочила. Я не знала."
        me "Ничего, всё хорошо."
        "Я сразу заключил Леру в свои объятия."
        Ler_SM "Пойдем домой? А то я так устала, с ног валюсь."
        "Промычала Лера мне в грудь."
        me "Пошли, я тоже за этот день с этим бегунком устал."
        "Я нежно отпустил Леру, и мы двинулись домой."
        play ambience ambience_camp_center_night fadein 2
        scene ext_square_night with dissolve
        $ renpy.pause (2)
        scene ext_houses_night with dissolve
        $ renpy.pause (1)
        scene ext_house_of_mt_night_without_light with dissolve
        $ renpy.pause (0.7)
        play ambience ambience_int_cabin_night fadein 2
        scene int_house_of_mt_night2 with dspr
        "Когда мы вошли, Ольга Дмитриевна уже спала."
        th "Хорошо. И докучать не будет насчет отбоя, и Леру смущать не будет. Одни плюсы."
        me "Лера, давай аккуратно. Вожатая спит."
        Ler_SM "Хорошо."
        "Даже не понижая голоса сказала Лера."
        me "Тссс... Я же сказал, тише."
        Ler_SM "Она меня всё равно не СЛЫ-ШИТ."
        "Громко пропела она."
        th "А, точно."
        me "Ну тогда пойдем."
        "Мы аккуратно присели на кровать."
        "Я стал переодеваться, а Лера встала."
        me "Ты чего?"
        Ler_SM "Ты так сумбурно переодеваешься, что скинешь меня с кровати рано или поздно. Поэтому я решила встать."
        "Я просто промолчал."
        "Вещи уже оказались на полу."
        "Лера, дождавшись своей очереди, присела на кровать, ближе к моим ногам, и стала переодеваться."
        "Весь процесс не занял большого количества времени, и вскоре она оказалась у меня под боком со стороны стены."
        Ler_SM "Сегодня был тяжелый день. Спокойной ночи."
        me "Спокойной ночи."
        stop ambience fadeout 2
        scene black with dissolve
        $ renpy.pause (2, hard=True)
        
        
        
        
        
        
        
        
        
    else:
        "Вроде и плохо быть одному, но я даже немного рад, что не пошел сегодня со Славей гулять. Мало ли это выльется во что-то."
        "А Леру я обидеть не хочу."
        th "Уже вечер, а Леры и Кристины всё еще не видно. Где же они, черт бы их побрал? {w}Уж слишком много времени они тратят на это задание."
        th "Пойду погуляю еще. Надо же как-то время убить."
        scene ext_boathouse_sunset with dissolve
        "Я решил, что далеко идти не хочется, вода так и манит меня обратно."
        "Купаться я не хочу, но просто наблюдать..."
        th "Чувствую я, что какое-то событие должно произойти."
        th "Может человек тонуть будет? {w}Или Лера с Кристиной на пляж придут после задания."
        "..."
        "Нет, не угадал я."
        "Во время моих размышлений мне в поле зрения попался приближающийся объект."
        "Внимательно приглядевшись, я понял, что это лодка. А в ней сидят две дамы, и одна из них очень похожа на Леру, а другая на Кристину."
        th "Тут ошибки быть не может."
        th "Это точно они."
        "В это время девушки уже подплыли к берегу настолько, что они заметили меня."
        Ler_SM "Семён!"
        "Я просто поднял руку в жесте приветствия."
        "Девушки уже приплыли, привязали лодку. Я решил идти к ним навстречу."
        show Kristy normal pioneer sunset at center with dissolve
        Vlr_SM "Привет. Не поможешь?"
        "Не услышав даже моего согласия или отказа, она просто вручила мне в руки корзину."
        me "Где вы были весь день?"
        Vlr_SM "На острове."
        me "Что делали?"
        Vlr_SM "Задание выполняли."
        "Она явно не хочет идти на диалог."
        Ler_SM "Мы ходили землянику собирать. Вожатая хочет сделать торт. Только это сюрприз."
        me "Хорошо. А я тут волновался за вас, весь лагерь обыскал, а Ольга Дмитриевна только загадками и говорит."
        hide Kristy normal pioneer sunset
        show Kristy angry pioneer sunset
        Vlr_SM "Пойдемте, голубки. Надо землянику отнести."
        "Сказала Кристина резким тоном."
        hide Kristy angry pioneer sunset with dspr
        "Лера просто посмотрела на меня, подняла и опустила плечи, сказав этим, что она сама не понимает, почему это она так."
        "Кристина уже была впереди нас на шагов 10, поэтому мы решили поспешить."
        scene black with dissolve
        stop ambience fadeout 1
        $ renpy.pause (2, hard=True)
        play ambience ambience_camp_center_evening fadein 2
        scene ext_dining_hall_near_sunset with dissolve
        Ler_SM "Вот и закончили."
        show Kristy normal pioneer sunset with dissolve
        Vlr_SM "Угу. {w}Ладно, ребята, пойду я. Удачи."
        "Кристина просто помахала рукой нам и развернулась."
        hide Kristy normal pioneer sunset with dspr
        Ler_SM "Ну что, как день прошел?"
        me "В страшных муках. Весь день за тебя волновался да с бегунком по лагерю скакал."
        Ler_SM "А у нас интересно прошел. Кристина при тебе почему-то неразговорчивая. При мне она намного общительнее."
        me "Я тоже это заметил. Может поговоришь с ней об этом?"
        Ler_SM "Не стоит торопить события."
        me "Да, оно верно."
        "Повисло неловкое молчание."
        Ler_SM "Уже ночь скоро. Пойдем спать? А то я устала очень."
        me "Да, хорошо. Я тоже вымотался за этот день, так что я не против лечь спать хоть здесь."
        "Лера просто улыбнулась и повела меня за собой."
        play ambience ambience_camp_center_night fadein 1
        scene ext_house_of_mt_night_without_light with dissolve
        me "Хм..."
        Ler_SM "Что такое?"
        me "Вожатая либо спит, либо её нет дома."
        Ler_SM "В любом случае для меня это хорошо. Пошли скорее, иначе тебе придется меня на руках нести, а это будет странно смотреться."
        me "Почему?"
        Ler_SM "Ты забыл, что я невидима?"
        me "Ой, точно. Прости."
        Ler_SM "Ничего."
        "С кокетливой улыбкой она сказала мне это."
        "Я решил, что стоять долго под дверью и разговаривать это, конечно, прекрасно, но как-нибудь в другой раз. Поэтому я открыл дверь."
        play ambience ambience_int_cabin_night fadein 1
        scene int_house_of_mt_night with dissolve
        "Включив свет и убедившись в отсутствии вожатой, я обратился к Лере."
        me "Ну что, давай тогда ты первая переодевайся. Тебе же к стене ложиться."
        Ler_SM "Что ты как дите малое? Сама бы догадалась."
        th "Удивительно, как она может говорить для некоторых задевающие вещи с такой интонацией, что ты совершенно не воспринимаешь это, как что-то обидное."
        "Лера начала переодеваться. В это время я тоже начал снимать рубашку."
        "..."
        "С переодеванием было покончено быстро. Лера уже улеглась в кровать."
        Ler_SM "Семён, выключишь свет?"
        me "Да, конечно."
        scene int_house_of_mt_night2
        th "Свет выключен. Пора и мне в кровать."
        "Я быстрым шагом дошел до кровати и улегся к Лере."
        Ler_SM "Спокойной ночи."
        me "Сладких снов."
        stop ambience fadeout 2
        scene black with dissolve
        window hide
        $ renpy.pause (2, hard=True)
    
    if ES_Lera_comfort_points_SMVIJ >= ES_girls_comfort_points_SMVIJ:
        jump SMVIJ_plane_dream
    else:
        jump SMVIJ_day3
label SMVIJ_plane_dream:
    $ prolog_time()
    play ambience airplane_int fadein 1
    scene plane_dream_int with dissolve
    Devishka_SM "Извините, а вы меня не сфотографируете?"
    th "Чего она хочет?"
    Devishka_SM "Молодой человек?"
    ya_SMVIJ "А? {w}Простите. Да, конечно."
    "Девушка передала мне телефон с включенной камерой."
    "Она отстегивает ремень безопасности, встает и принимает позу для фотографии."
    Devishka_SM "Так нормально?"
    ya_SMVIJ "В самый раз."
    "Улыбнувшись сказал я."
    Personal_SM "Простите, мы заходим на посадку. Не могли бы Вы сесть на своё место?"
    Devishka_SM "Да мне только на одну минуту. Я обещала фотографию сделать."
    Personal_SM "Я настаиваю. Сядтье, пожалуйста на своё место."
    Devishka_SM "Пока мы тут разговариваем, я бы уже давно сделала фотографию и села бы на место."
    "Стюардесса закатила глаза на секунду."
    Personal_SM "Хорошо. Только быстро."
    Devishka_SM "Хорошо."
    "Стюардесса удалилась, скорчив перед этим противную гримасу."
    Devishka_SM "Вот всегда так. {w}Вы готовы?"
    ya_SMVIJ "Да, готов."
    ya_SMVIJ "Птичка вылетит через три..."
    ya_SMVIJ "Два..."
    ya_SMVIJ "Од..." with vpunch
    "Самолет вдруг затрясло и девушка упала на землю."
    "Тряска была настолько сильной, что я даже выронил телефон из рук."
    ya_SMVIJ "Девушка, с Вами всё в порядке?"
    play ambience Padenie fadein 1
    "На борту поднялась паника. Мы все смотрим в иллюминатор."
    "Там огонь."
    ya_SMVIJ "Девушка! Пристегнитесь срочно!"
    scene black with dissolve
    ya_SMVIJ "Девушка!..."
    window hide
    stop ambience fadeout 2
    jump SMVIJ_day3
    
    
    
    
    
        
    
