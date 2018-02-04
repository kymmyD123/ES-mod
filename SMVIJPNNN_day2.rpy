init:
    image ext_warehouse_day = "mods/SMVIJPNNN/image/bg/ext_warehouse_day.jpg"
    image int_warehouse_day = "mods/SMVIJPNNN/image/bg/int_warehouse_day.png"
    image lineup = "mods/SMVIJPNNN/image/cg/day2/d2_lineup.jpg"
    
    $ Ler_SM = Character(u'Лера', color="99FF99", what_color="E2C778")
    $ Pioners_SMVIJ = Character(u'Пионеры', color ="#009966", what_color = "E2C778")
    $ SILer_SM_together = Character(u'Семён и Лера', color="00cc00", what_color="E2C778")
    
    $ Vlr_SM = Character(u'Кристина', color="660066", what_color="E2C778")
    
    $ bus_engine = "mods/SMVIJPNNN/music/bus_engine.mp3"
    $ nobody_secret = "mods/SMVIJPNNN/music/nobody_secret.mp3"
    $ Sakura = "mods/SMVIJPNNN/music/Sakura.mp3"
    $ morning = "mods/SMVIJPNNN/music/morning.mp3"
    $ soft_horn = "mods/SMVIJPNNN/music/soft_horn.mp3"
    $ spring = "mods/SMVIJPNNN/music/spring.mp3"
    $ silent_garden = "mods/SMVIJPNNN/music/silent_garden.mp3"
    $ Saya = "mods/SMVIJPNNN/music/Saya.mp3"
    
    $ ES_Alisa_comfort_points_SMVIJ = 0
    
    $ ES_Lena_comfort_points_SMVIJ = 0
    
    
    $ d2_clubs_smv_vh = False
    $ d2_muzclub_smv_vh = False
    $ d2_library_smv_vh = False
    $ d2_aidpost_smv_vh = False
    
    
    $ d2_MT_palevo = False
    $ d2_SL_svidanka = False
    $ d2_LN_pomosh = False
    
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
    "Пусть я и вижу это очень часто, но в данном месте, где лучи солнца освещают её полузакрытые глаза, она выглядит потрясающе."
    me "Ты очень прекрасно выглядишь!"

    Ler_SM "Спасибо, Сенечка."
    "Она покраснела."
    me "Как ты спала? Что тебе снилось?"
    "Лера задумчиво посмотрела на меня и её настроение переменилось. {w}Она стала грустной и все время смотрела в сторону."
    Ler_SM "Я не помню, извини."
    th "Она что-то скрывает, ладно."
    "Я не стал её допрашивать, ведь она только проснулась, да и делать этого особо не хотелось, поэтому я сказал."
   
    me "Ладно, пойдем на линейку, опоздание неприемлимо."
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
    "Я решил молчать далее, так как было бы глупо если бы меня заметили,разговаривающим с самим собой."
    "А вот и Ольга Дмитриевна."
    show mt normal pioneer at center with dissolve
    mt "Итак пионеры, начнем линейку."
    mt "Сегодня у нас в планах..."
    "Я не стал её слушать, ведь я итак знаю что мне делать в этом лагере."
    scene lineup with dissolve
    $ set_mode_nvl()
    "Меня мучало много вопросов. {w}Один из них - это почему Кристина видит Леру, а остальные нет."
    "Ответ на этот вопрос так и не найден. {w}И будет ли вообще?"
    "Да и некоторые сцены тоже нарушены. Я прекрасно понимаю, что не все мои действия соответствуют Семёну в игре, но это всё равно слишком."
    "Вот возьмём пример : я сегодня вышел из домика рано утром, задолго до начала линейки. {w}А где же Славя?"
    "Ведь она всегда бегает по утрам и не изменяет своим традициям и привычкам."
    "Да взять ту же Лену. {w}Где она была весь день? Я должен был увидеть её вечером на скамейке возле Генды, но я её не видел."
    "Это, конечно, можно списать на то, что расстояние было большое и я просто мог её не увидеть, но я бы не сказал, что у меня плохое зрение. Я бы даже сделал себе комплемент, что у меня самое лучшее зрение в этом лагере."
    "Ну и переходим к главной загадке всего лагеря - Кристина."
    "Первое - почему она видит Леру? {w}Должна же быть какая-то причина этому. Она так же попала в лагерь, как и мы? Она что-то на подобие пионера? {w}Или может даже Юли?"
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
            
        "Пройти мимо сделав вид, что незаметил":
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
    show Kristy smile pioneer at center with dissolve
    Vlr_SM "Привет, ребята."
    me "Привет, Кристя."
    "Мы произнесли это вдвоем."
    Vlr_SM "Лера, что стоишь, возьми стул и присаживайся с нами."
    Ler_SM "Нет, я постою."
    me "Потом с тобой поговорим, Кристина."
    show Kristy normal pioneer at center with dissolve
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
            "Кристина подняла глаза и посмотрела на меня."
            "Я только сейчас обратил на неё внимание с такого расстояния."
            "Её взгляд можно назвать щенячим. {w}Она смотрит на меня блестящими глазами, а слезы так и вырвутся наружу."
            "Она смогла совладать с собой и опустила взгляд в тарелку."
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
            "Я сказал шопотом, чтобы не быть услышаным."
            
    "Трапеза была окончена через какое-то время."
    me "Всё, Кристина, я пойду. Спасибо за компанию."
    Vlr_SM "Хорошо. До встречи, еще увидимся с вами."
    "После этой фразы пара окружающих нас пионеров посмотрели на Кристину с непонимающим взглядом."
    me "Да, до встречи."
    Vlr_SM "Хотя подождите, я уже закончила. Пойдем вместе?"
    "Пионеры уже чуть ли не со стула падают, чтобы услышать речь Кристины."
    me "Да, хорошо."
    "Пока Кристина относит посуду, я решил взять несколько бутербродов для Леры."
    "Я же не оставлю её в голоде."
    th "А вообще надо придумать какой-то другой способ, потому что неделю одними бутербродами сыт не будешь."
    "Кристина не заставила себя долго ждать и уже подходила к нам."
    Vlr_SM "Ну что, пойдем?"
    SILer_SM_together "Пошли!"
    "Я первый вышел из столовой. {w}Девочки шли позади и болтали о своём."
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    scene ext_dining_hall_near_day with dissolve
    show mt normal pioneer far at cleft with dissolve
    show Kristy normal pioneer at center with dissolve
    "Не успели мы выйти, как Ольга Дмитриевна уже ждет нас на пороге."
    th "Вожатая держит какую-то бумагу. Это бегунок, зуб даю."
    mt "Привет, Семён. У меня для тебя задание."
    me "Здравствуйте Ольга Дмитриевна. Да, я готов ко всему."
    "Я сказал улыбаясь и вожатая тоже начала улыбаться."
    show mt smile pioneer far at cleft 
    mt "Ничего такого, просто обходной лист, ты должен его пройти как можно быстрее!"
    me "Вас понял, будет сделано."
    mt "Постарайся пройти до обеда, а то голодный будешь потом ходить."
    show mt angry pioneer far at cleft with dissolve
    mt "А ты, Кристина, помнишь, что я говорила на линейке?"
    show Kristy shy pioneer at center with dissolve
    Vlr_SM "Да."
    mt "Иди выполняй!"
    show Kristy smile pioneer at center with dissolve
    Vlr_SM "Хорошо."
    "Нотка грусти прозвучала в ее ответе."
    mt "Все идите ребята, не смею задерживать вас."
    scene ext_houses_day with dissolve
    show Kristy normal pioneer at center with dissolve
    "Мы пришли к домикам и тут Лера сказала."
    Ler_SM "Ладно Семён, иди лист проходи, а я с Кристей пойду."
    show Kristy shy pioneer at center with dissolve
    me "Хорошо, удачи вам девочки."
    Vlr_SM "И тебе удачи, Семён."
    th "Ну чтож, куда пойдем?"
    
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
    
    play ambience ambience_camp_center_day fadeout 2 fadein 1
    th "Музыки что ли послушать?"
    "Спустя какое-то время я принял окончательное решение и направился в сторону музыкального клуба."
    scene ext_musclub_day with dissolve
    "Добравшись до музыкального клуба я уже мог слышать звуки рояля."
    th "Сейчас мне предстоит знакомство с милой японкой."
    "Её пикантная поза уже всплыла у меня в голове."
    th "А вдруг в этот раз будет всё иначе?"
    th "Есть только один способ проверить."
    th "Эх ну чтож, Семен, пойдем!"
    play sound sfx_open_door_squeak_2
    play ambience ambience_music_club_day fadein 1
    scene int_musclub_day with dissolve
# ЗДЕСЬ НАДО ПОСТАВИТЬ MI(2) ИЗ ПАПКИ "СПРАЙТЫ НЕ ИЗ БЛ"
    ""
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
    "Я отправился к зданию клубов."
    "Карту я уже знаю наизусть, так что для меня не составит труда дойти туда с закрытыми глазами."
    scene ext_clubs_day with dissolve
    th "Вот я и пришёл. {w}Ну чтож, пойдем знакомиться с гениями робототехники."
    "Так, надеюсь мне не придется вступать к ним в клуб."
    "А если они меня начнут окружать, то в любом случае меня спасет Славя."
    "Наверное с роботом своим возятся сейчас. {w}Придется их отвлечь."
    th "Так, пойдем!"
    scene d5_clubs_robot with dissolve
    "Как я угадал. {w}Для чего им такой робот интересно? {w}На ум лезут только пошлые мысли."
    el "А, ты наверное Семён. Проходи!"
    scene int_clubs_male_day  
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
    scene ext_clubs_day
    show sl happy pioneer far at center 
    with dissolve
    sl "Вот такие у нас гении тут."
    sl "Они не сильно тебя измучали?"
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
    
    "Я отправился в библиотеку."
    scene ext_library_day with dissolve
    "Наверное дрыхнет во всю."
    "Как бы ее позлить? {w}Ну не знаю, просто разбужу."
    "Время еще терять из за её сна."
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
            scene ext_library_day with dissolve
            "Как же она меня бесит."
            play music morning fadein 3
            show un normal pioneer close at center with dissolve
            me "Сильно болит?"
            show un surprise pioneer close at center
            un "Нет, уже почти не болит."
            if d2_med_sv_vh == False :
                "ЗДЕСЬ НУЖНО ПРОПИСЫВАТЬ ТО, ЧТО БЫЛО БЫ ЕСЛИ СЕМЕН ЕЩЕ НЕ БЫЛ В МЕДПУНКТЕ."
                me "Все равно надо в мед пункт сходить, я там ещё не был, как раз подпишу обходной лист."
                show un shy pioneer close at center
                un "Ну тогда нам по пути. Пойдём?"
                
                
                
            else:
                "ЗДЕСЬ НУЖНО ПРОПИСЫВАТЬ ТО, ЧТО БЫЛО БЫ ЕСЛИ СЕМЁН УЖЕ БЫЛ В МЕДПУНКЕ."
                me "Все равно надо сходить в мед пункт, медсестра как раз там сидит, я недавно подписывал обходной там."
                show un shy pioneer close at center
                un "А ты не опоздаешь другие подписывать?"
                "Я заулыбался."
                me "Нет, не волнуйся."
            
            "Какая же она милая."
            me "Пойдём."
            scene d3_un_forest with dissolve
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
            "Эх Лена, знала бы ты что я чувствую по отношению к тебе."
            
            
            if d2_med_sv_vh == False :
                "ЗДЕСЬ НУЖНО ПРОПИСЫВАТЬ ТО, ЧТО БЫЛО БЫ ЕСЛИ СЕМЕН ЕЩЕ НЕ БЫЛ В МЕДПУНКТЕ."
                show un normal pioneer close at center with dissolve
                un "Пойдём?"
                me "Да, конечно, мне же ещё надо подписать его."
                "С этими словами мы вошли в медпункт."
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
                show cs normal glasses close at center 
                me "Меня Семёном зовут."
                cs "Хорошо, Семён, давай обходной."
                "Она взяла лист, подписала его и сказала."
                cs "Если будут жалобы, обязательно заходи."
                me "Конечно, до свидания."
                "С этими словами я удалился из медпункта."
                
            else:
                "ЗДЕСЬ НУЖНО ПРОПИСЫВАТЬ ТО, ЧТО БЫЛО БЫ ЕСЛИ СЕМЁН УЖЕ БЫЛ В МЕДПУНКЕ."
                show un normal pioneer close at center with dissolve
                un "Пойдёшь?"
                me "Да, давай я тебя провожу."
                un "Хорошо."
                "С этими словами мы вошли в медпункт."
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
                
            scene ext_aidpost_day with dissolve
            
            if d2_med_sv_vh == False :
                "ЗДЕСЬ НУЖНО ПРОПИСЫВАТЬ ТО, ЧТО БЫЛО БЫ ЕСЛИ СЕМЕН ЕЩЕ НЕ БЫЛ В МЕДПУНКТЕ."
                "Странные события, ну да ладно."
                "Вот ещё одна подпись."     
                $ reset_zone("medic_house")
        
        "Ничего не делать":
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
            me "А зачем мне тут оставаться? Бывай."
            scene ext_library_day with dissolve
            "Как же она меня бесит."
    
        
        
    $ d2_clubs_smv_vh = False 
    $ d2_aidpost_smv_vh = False
    $ d2_library_smv_vh = True
    $ d2_muzclub_smv_vh = False
    
    
    $ disable_current_zone()
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
    
    "Я отправился к Виоле."
    scene ext_aidpost_day with dissolve
    "Найти дорогу мне не составило труда, ведь я знаю этот лагерь как облупленный."
    "Так, надо идти, подпись получить."
    th "Собрались!"
    play sound sfx_knock_door6_closed
    cs "Войдите."
    scene int_aidpost_day with dissolve
    "Виола сидела за столом и разбиралась с какими-то бумагами."
    show cs normal glasses far at center with dissolve
    cs "Привет, пионер, ты новенький наверное?"
    me "Здравствуйте, да я новенький, меня Семёном зовут."
    cs "Прекрастно, а я тебя как раз и ждала, меня Виолой зовут."
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
    scene ext_square_day with dissolve
    "Итак, я собрал все подписи."
    return