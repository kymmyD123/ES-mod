﻿


label SMVIJ_day3:
    $ backdrop = "days"
    $ new_chapter(3, u"День третий.")
    $ day_time()
    $ persistent.sprite_time = "day"
    
    play ambience ambience_int_cabin_day fadein 2
    scene int_house_of_mt_day with dissolve
    "До сих пор думаю, что сплю в своей кровати. Но это далеко не так."
    "Уже двое полных (ну почти) суток я нахожусь по адресу непонятно где. Время : ранее утро. Дата : неизвестно."
    "Солнце пробивается сквозь закрытые шторы, надеясь меня разбудить."
    th "Но мне так не хочется вставать..."
    mt "Семён, вставай!"
    th "Только не это. {w}Ну еще пять минут."
    mt "Вставай говорю."
    me "Мама, ну еще пять минуточек."
    "Я сквозь одеяло, в которое был окутан, услышал, как она саркастично прыснула."
    mt "Ну уж нет, ты у меня проснешься сам."
    "Доклад Семёна Персунова: ко мне приближается женщина и хочет что-то со мной сделать. Предположение: разбудить (но это не точно)"
    "Звук дергнания штор полностью подтвердил мою теорию."
    "Солнце даже сквозь тонкое одеяло достигает меня и приказывает проснуться."
    th "Я так легко не дамся!"
    "Перевернувшись на другой бок я стал храпеть. {w}Специально."
    mt "Это тебя не спасёт."
    "Она открыла форточку и теперь прохладный, еще не до конца нагретый воздух нападает с другого фронта."
    me "Ну Ольга Дмитриевна, еще 5 минуточек..."
    mt "Вставай давай! Настоящий пионер не просыпает!"
    me "Значит запишите меня в список плохих мальчиков."
    th "Как же это звучит..."
    mt "Ну всё..."
    th "Видимо я попал."
    "Главный враг моего сна переходит в режим наступательной атаки. {w}Ольга Дмитриевна уже не играет со мной в шутки. Она толкает меня."
    "Да так, что я могу перевернуться в любую минуту."
    th "А этого допустить нельзя."
    mt "Семён, я не щучу. Что ты, как маленький ребенок? Мало того, что линейку проспал, так еще и эта сцена."
    th "ЧТООО000ооо...?"
    "Мигом выскочив из-под одеяла и описав в воздухе пару красивых, акробатических элементов, я приземлился на кровать, прикрываясь только одной подушкой."
    th "Как я её успел схватить вообще?"
    show mt angry pioneer at center with dissolve
    "Передо мной стоит Ольга Дмитриевна. Руки в боки, страшный, грозный взгляд."
    th "Чувствую будет больно."
    me "Как я проспал? А будильник почему не сработал?"
    mt "Так это ты его выключил да не заметил."
    me "Как так-то?..."
    me "Каюсь, виноват. Больше такого не повторится."
    show mt normal pioneer at center
    mt "Надеюсь. Настоящий пионер никогда себя так не ведет."
    me "Да, это точно."
    "И тут я заметил кое-что странное."
    me "А где Лера?"
    show mt surprise pioneer at center 
    mt "Какая Лера?"
    th "Вот черт... В слух сказал. Утром мозги еще не на полную катушку работают."
    th "Думай, думай..."
    me "А? {w}Мне что, это приснилось тогда?"
    show mt normal pioneer at center
    mt "Кто тебе снился?"
    me "Да... Неважно. {w}Точно приснилось."
    mt "Ну ладно. В любом случае, надеюсь что это был первый и последний раз."
    me "Да, конечно, Ольга Дмитриевна. Больше такого не повторится."
    show mt smile pioneer at center
    mt "Отлично. Завтрак ты тоже пропустил, так что будешь завтракать один."
    me "А мне можно разве так?"
    th "Я прекрасно знаю, что можно, но спросить всё равно надо. Не всё в этом мире идет так, как в той игре."
    mt "Да, можно. Вот только если поварихи добрые. Но если у них плохое настроение, то придется уворачиваться от столовых приборов."
    th "В голове сразу всплыла сцена из Матрицы."
    me "Тогда я пойду. Спасибо."
    mt "Я тоже пойду. После завтрака найди меня, у меня есть к тебе разговор."
    me "Что я еще натворил, даже не выбравшись толком из кровати?"
    show mt normal pioneer 
    mt "Нет, ничего ты не сделал, вот в этом и дело. Потом поговорим. Одевайся, а я пошла. До встречи."
    me "Угу."
    hide mt with dissolve
    "Вожатая покинула домик, и теперь я могу с облегчением вздохнуть."
    th "Надо же так накосячить с самого утра. Ладно, надо одеваться и идти искать Леру."
    "Я быстро заправил постель, оделся и вышел наружу."
    play ambience ambience_camp_center_day fadein 2
    scene ext_house_of_mt_day with dissolve
    "На улице уже большая часть пионеров прогуливается, лагерь живет."
    th "Надо бы пойти умыться."
    "Поняв, что я вышел из домика слишком рано, я зашел обратно, схватил пакет с банными принадлежностями и, закрыв двери на ключ, пошел в сторону умывальников."
    "По пути мелькают знакомые лица."
    scene ext_houses_day with dissolve
    "Вот Алиса идет по своим делам. Дальше можно заметить маленькие косички фиолетового цвета, скромно болтающиеся из стороны в сторону."
    "Ульяна где-то играет, Женя в библиотеке с утра сидит, это точно."
    "И вот только я один, проспавший."
    Ler_SM "Семён."
    "Знакомый, теплый голос пронзил меня сонного."
    "Лера подбежала ко мне и обняла меня."
    Ler_SM "С добрым утром."
    me "С добрым утром."
    Ler_SM "Ты куда?"
    me "Я на умывальники; проспал."
    Ler_SM "Тогда я с тобой."
    me "Да я и не против."
    "Шопотом сказал я."
    "Вместе мы пошли принимать водные процедуры."
    "По пути мы не встретили больше ни одного знакомого лица."
    scene black with dissolve
    $ renpy.pause (2, hard=True)
    scene ext_washstand_day with dissolve
    Ler_SM "Как поспал?"
    play ambience sfx_water_sink_stream fadein 0.4
    me "Отлично. Вот только проспал. Почему ты меня не разбудила? И вообще, куда пошла утром рано?"
    Ler_SM "Вот так много вопросов с утра..."
    "Лера встала в позу, руки в боки, губки бантиком."
    me "Да не, просто интересно."
    "Лера посмотрела в мои заспанные глаза."
    Ler_SM "Ты умываться собираешься? А то кран открыл, а смотришь на меня."
    me "И точно..."
    "Первая горсть воды полетела мне в лицо."
    Ler_SM "Вот и отлично. А то утром ты сам не свой. Страшно на тебя смотреть."
    me "Ну спасибо."
    "Сквозь воду я сказал это."
    "Лера кокетливо засмеялась и, прикрыв губы ладонью, произнесла."
    Ler_SM "Да я же шучу. Ты мне и в таком состоянии нравишься."
    me "Только нравлюсь?"
    "Я даже сам улыбнулся от этой фразы."
    Ler_SM "Ну..."
    "Лера опустила глаза и смотрит себе в ноги."
    Ler_SM "Больше..."
    me "Что больше?"
    "Лера сделала шаг в мою сторону. {w}Она поцеловала меня в щеку и вернулась на место."
    Ler_SM "Так понятнее?"
    "Её красные, румяные щеки бросаются в глаза."
    me "Всё стало предельно ясно."
    "Я улыбнулся её в ответ."
    Ler_SM "Давай умывайся быстрее."
    me "А мы куда-то спешим?"
    Ler_SM "Вожатая хочет тебя видеть, забыл?"
    me "А ты откуда знаешь?"
    th "Действительно, откуда она знает? Мне очень интересно."
    Ler_SM "У вас форточка была открыта. Твоё пробуждение должно быть слышал весь лагерь."
    me "Как же стыдно..."
    Ler_SM "Да не, было забавно."
    me "Хех. Это 'Да не' ты от меня взяла, не так ли?"
    Ler_SM "Ну а от кого же?"
    "В улыбке Леры можно было утонуть. Прямо как в её глазах."
    me "Ладно. Я помолчу немного, надо зубы почистить."
    Ler_SM "Хорошо."
    "Сказала Лера и сорвала одуванчик."
    "В это время я погрузился в свои мысли."
    "Так часто бывает, когда я принимаю подобного рода процедуры."
    "Почему в лагере не бывает дождя?"
    "Почему именно я попал в Совёнок?"
    "Почему мы вдвоем?"
    "Почему именно мы?"
    "Почему моё имя совпадает с именем персонажа из игры?"
    "Почему... Почему... Почему..."
    "Слишком много вопросов, но так мало ответов."
    "Именно ответы на эти вопросы я пытаюсь найти у себя в голове, но пока безрезультатно."
    "Можно представить, что вокруг меня сейчас пустота... Настолько я сейчас оторвался от настоящего. А что считать настоящим? {w}Этот мир или тот?"
    Ler_SM "...вместе?"
    "Куски фраз Леры всё таки пробили мой барьер мыслей."
    me "Фто?"
    "Не вытащив изо рта зубную щетку, я попытался произнести хоть что-то похожее на слово 'Что'."
    Ler_SM "Давай проведем этот день вместе? Больше никого."
    me "Да я только с радостью. Как ты хочешь это сделать?"
    Ler_SM "Ну... Сегодня же танцы будут."
    me "Точно... Танцы. Сегодня же третий день."
    me "И ты предлагаешь мне с тобой танцевать при всех?"
    Ler_SM "А ты так меня стесняешься?"
    me "Да я не об этом. Тебя не видят, забыла?"
    Ler_SM "Да не забыла я. Дай поиздеваться."
    "Лера сделала улыбочку, потянув пальцами уголки губ вверх."
    me "Ну ладно. Только чуть-чуть. Так что ты предлагаешь?"
    Ler_SM "Это ты должен мне предлагать. Ты же знаешь этот лагерь куда лучше меня."
    me "Ну... Да, это так."
    me "Давай потом об этом поговорим тогда? Ближе к танцам? Я просто кушать хочу."
    Ler_SM "Давай. У тебя есть время придумать место."
    me "Хорошо. Тогда я пойду завтракать. Ты уже, кстати, завтракала?"
    Ler_SM "Да, уже покушала. Спасибо, мама."
    me "Да не за что, доченька."
    Ler_SM "Прекрати."
    "Лера легонько толкнула меня в плечо."
    me "Сама же начала."
    Ler_SM "Мне можно, а тебе нет."
    "Сделав ту же улыбочку при помощи пальцев, она смотрит на меня, наклонив голову."
    me "Ладно. Я тогда пойду. Я тебя найду тогда. Где ты будешь сегодня?"
    Ler_SM "Не знаю."
    "Лера пожала плечами."
    Ler_SM "С Кристиной буду гулять, наверное."
    me "Хорошо. Тогда я тебя найду."
    play sound sfx_close_water_sink
    stop ambience
    play ambience ambience_camp_center_day fadein 0.7
    Ler_SM "Договорились."
    Ler_SM "Ну я пойду тогда. До встречи, мой принц."
    me "Еще увидимся, принцесса."
    "Лера подмигнула и, развернувшись и демонстративно согнув одну ножку в колене, пошла в сторону лагеря."
    th "Пора бы и мне идти."
    "Неспешно собрав все вещи в пакет я пошел к домику."
    scene ext_houses_day with dissolve
    "На улице уже позднее утро, лагерь живет в полную мощь. Ни одного спящего существа не осталось в этом лагере, я могу быть уверен в этом."
    "Каждый пионер проходит мимо меня. Каждый идет в паре, все общаются. И только я один выделяюсь."
    "Да и даже если бы я шел не один, то я бы всё равно выделялся. И рассказывать почему не стоит."
    scene ext_square_day with dissolve
    th "Половину пути я уже прошел."
    "Живот урчит, но есть сильно я не хочу. Всегда нет аппетита по утрам. Я воспринимаю это больше как необходимость, чем желание."
    "Поэтому приходится есть через силу."
    "Смотря себе под ноги я и не заметил, что рядом со мной постоянно идет чья-то тень."
    "Приподняв голову и взглянув направо, я увидел Лену."
    show un shy pioneer at center with dissolve
    un "Д-доброе утро..."
    me "Доброе утро и тебе, Лена. Что-то случилось?"
    un "Нет. Просто хотела спросить, куда ты идешь?"
    me "Сначала домой, а потом завтракать."
    show un normal pioneer at center 
    un "Так почти все уже позавтракали."
    me "Почему почти все? Действительно все, кроме меня."
    un "Еще и я."
    me "Как так? Я же видел тебя сегодня утром, ты шла с линейки."
    un "Я пришла к самому концу. Потом сделала вид, что иду со всеми."
    me "Так ты тоже проспала?"
    show un smile pioneer at center
    un "Угу."
    me "Тогда пойдем завтракать вместе?"
    show un shy pioneer at center
    un "Б-буду рада твоей компании..."
    me "Приятно слышать, я тоже буду рад."
    "Лена краснеет всё больше с каждой моей фразой."
    "В данный момент я могу сравнить её румянец только с персиком. Он тоже такой нежный, но не обжигающий."
    me "Ты со мной до моего домика пройдешься или сразу в столовой встретимся?"
    un "Я пойду с тобой, если ты не против."
    me "Нет, совершенно не против."
    un "Тогда пойдем."
    hide un with dspr
    "Лена пошла вперед меня."
    th "Ну ладно, пусть будет так."
    scene ext_house_of_mt_day with dissolve
    me "Ну вот мы и пришли."
    show un normal pioneer at center with dissolve
    un "Угу."
    "Я достал ключ из кармана и, засунув его в скважину, открыл дверь."
    hide un with dspr
    "Я зашел в домик, положил вещи в тумбочку и вернулся обратно."
    "Дверь со скрипом поддалась ключу и закрылась."
    me "Ну что, пойдем завтракать вместе?"
    show un shy pioneer at center with dissolve
    un "А?"
    show un smile pioneer at center
    extend " Ну да, пошли."
    show un surprise pioneer at center 
    me "Как пойдем?"
    un "В-всмысле?"
    show un normal pioneer at center
    me "Через площадь?"
    un "Д-да, давай через площадь."
    scene ext_square_day with dissolve
    $ renpy.pause(1)
    scene ext_dining_hall_away_day with dissolve
    $ renpy.pause(1)
    scene ext_dining_hall_near_day with dissolve
    "Всю дорогу мы шли и разговаривали на разные темы."
    "Я узнал, что Лена живет не подалеку от лагеря в каком-то городке, правда ли это?"
    "Возможно, ведь я ничего не знаю об этом мире, может быть это какая-то параллельная вселенная."
    "А может быть она просто врет мне."
    show un surprise pioneer at center with dissolve
    un "С-семен, ты чего задумался? Уже минуты 2 стоишь."
    me "Прости, да так, задумался о своем, ну что пойдем кушать."
    show un shy pioneer at center
    un "Д-да."
    scene int_dining_hall_day with dissolve
    show un normal pioneer at center with dissolve
    me "Как же тут пусто и тихо."
    un "А? Д-да."
    me "Пойдем еду брать, вся столовая в нашем распоряжении."
    show un shy pioneer at center
    "Кажется её немного смутила эта фраза."
    "Мы взяли еду и двинулись выбирать столик."
    "Решили направиться к самому дальнему столику, который был у окна."
    un "Ааай."
    "Я посмотрел на Лену, {w}Она лежала на полу, а вся еда была разбросана по столовой."
    me "Лена ты впорядке?"
    "Оказалось что она споткнулась он ножку стола."
    un "Д-да, только ушиблась немного. О боже, моя еда..."
    show un sad pioneer at center
    un "Ничего страшного, попробую попросить ещё."
    me "Ладно, буду ждать тебя за столиком."
    hide un 
    "Я сел и принялся её ждать."
    "Видно было, как Лена что-то бурно обсуждала с поварихой, как я понимаю она осталась без еды."
    "Она разочарованно шла к нашему столику."
    show un cry pioneer at center
    un "Она сказала, что еда уже кончилась и что я сама виновата во всем этом."
    "Печально, чтоже делать?"
    menu:
        "Отдать Лене свою еду":
            $ ES_Lena_comfort_points_SMVIJ += 1
            me "Лена не плачь, держи мою порцию."
            show un surprise pioneer at center
            un "Н-нет, ты чего? Это твоя еда! Я-я сама виновата во всем этом."
            me "Раз ты не хочешь брать мою порцию полностью, то давай тогда хотя бы пополам поделим?"
            show un shy pioneer at center
            un "Н-ну, не знаю даже, лишать тебя завтрака."
            me "Я же сказал, поделим пополам, ничего страшного, до обеда все равно не долго осталось."
            un "Л-ладно, хорошо."
            show un normal pioneer at center
            "Мы дружно принялись есть наши порции."
            "Ели мы молча, но мне было приятно находиться с ней, пусть она и молчала."
            scene black with dissolve
            $ renpy.pause(1)
            scene int_dining_hall_day with dissolve
            show un smile pioneer at center with dissolve
            un "Спасибо, Семён, благодаря тебе я не осталась голодной."
            me "Я всегда готов выручить тебя."
            show un shy pioneer at center
            "Кажется я вновь её смутил, боже что я за человек такой."
            un "Мне убраться тут надо, а ты иди, тебя Ольга Дмитриевна искала же."
            me "Давай я тебе помогу?"
            un "Н-нет, ты итак много для меня сделал уже."
            me "Да мне не сложно."
            show un normal pioneer at center
            un "Нет, иди. Я настаиваю."
            me "Ладно, как скажешь."
            me "Удачи тебе, Лена."
            un "Спасибо, С-семен."
                    
        "Ничего не делать":
            $ ES_Lera_comfort_points_SMVIJ += 1
            me "Не плачь, до обеда не долго осталось."
            un "Умеешь ты утешить."
            hide un
            "Лена обидчиво фыркнула и пошла убирать разбросанную по столовой еду и разбитую посуду."
            th "Может зря я так? {w}Аай да ладно, все равно Лера бы не одобрила если бы я поухаживал за ней."
            "Я молча ел уткнувшись носом в свою тарелку."
            scene black with dissolve
            $ renpy.pause(1)
            scene int_dining_hall_day with dissolve
            "Я настолько увлеченно ел, что даже не заметил как Лена ушла из столовой."
            "Трапеза была закончена и я решил немедля уходить из столовой, ведь ещё надо успеть к Ольге Дмитриевне."
            
    "Я отнес посуду и удалился из столовой."
    scene ext_dining_hall_near_day with dissolve
    "Так и где мне искать Ольгу Дмитриевну?"
    th "Думай, думай, думай..."
    "Точно, наверное у домика лежит."
    scene ext_dining_hall_away with dissolve
    $ renpy.pause(1)
    scene ext_square_day with dissolve
    $ renpy.pause(1)
    scene ext_house_of_mt_day with dissolve
    th "Как я угадал? Лежит себе в гамаке, отдыхает."
    "Я подошел к ней."
    show mt normal pioneer at center with dissolve
    mt "Пришел таки. Чего так долго?"
    mt "Впрочем не важно."
    mt "Знаешь зачем я тебя звала?"
    me "Нет, но наверное что-то важное."
    th "Опять нотации будет читать. Про пионеров и так далее."
    mt "Да, это очень важно. Мне Славя рассказала что ты фокусник."
    me "Да, практикуюсь немного, а что такое?"
    mt "Так вот, сегодня у нас вечером будет проходить конкурс талантов и мы бы очень хотели, чтобы ты показал нам фокусы."
    th "Так, что серьезно, было бы нехорошо не посоветоваться с Лерой, но думаю она будет не против."
    me "Ну ладно, я не против."
    mt "Вот и отлично, сейчас на сцене проходит репетиция, ты можешь присоединиться и показать участвующим свои способности."
    me "Это отлично, сейчас же туда пойду."
    show mt smile pioneer at center
    mt "Я приду смотреть вечером, так то у тебя будет время подготовиться, чтобы удивить меня."
    me "Понял, ну тогда я пойду."
    mt "Иди, ребята как раз тебя ждут."
    "Я решил немедля найти Леру."
    scene ext_houses_day with dissolve
    th "Так и где её искать?"
    Ler_SM "Сема!"
    th "Не пришлось, она сама нашла меня."
    me "Лера, иди сюда, нужно поговорить."
    Ler_SM "Что случилось?"
    me "Ольга Дмитриевна..."
    Ler_SM "Предложила тебе учавствовать в конкурсе талантов, да я знаю, я только за."
    "Что? Как она узнала? А впрочем потом спрошу."
    me "Ну тогда, нам нужно срочно идти репетировать на сцену."
    Ler_SM "Пойдем."
    "Мы взялись за руки и медленно, прогулочным шагом, пошли к сцене."
    "Шли мы молча, а впрочем, как я уже говорил, нам и не надо слов, чтобы понимать друг друга."
    scene ext_library_day with dissolve
    $ renpy.pause(1)
    scene ext_stage_normal_day with dissolve
    me "Ну вот мы и пришли."
    "Сказал я шепотом."
    Ler_SM "Будто я и не заметила."
    "Её улыбка шикарна."
    
    
    
    