﻿init:

    $ mods["SMVIJPNNN_label_1"]=u"Вставьте имя сами."
    $ Ler_SM = Character(u'Лера', color="99FF99", what_color="E2C778")
    image bus_410 = "mods/SMVIJPNNN/image/bus_410.jpg"
    image busbus = "mods/SMVIJPNNN/image/busbus.jpg"
    image semen_room_clear = "mods/SMVIJPNNN/image/semens-room.jpg"
    image camp-s-frombus = "mods/SMVIJPNNN/image/camp-s-frombus.jpg"
    image 18-disclaimer = "mods/SMVIJPNNN/image/18-disclaimer.jpg"
    $ bus_engine = "mods/SMVIJPNNN/image/bus_engine.mp3"
    $ ES_girls_comfort_points_SMVIJ = 0
    $ ES_Lera_comfort_points_SMVIJ = 0
    
   
label SMVIJPNNN_label_1:
    play music music_list["i_dont_blame_you"] fadein 2
    window hide 
    scene 18-disclaimer with dissolve
    $ renpy.pause (3)
    scene semen_room_clear with dissolve
    "Ранее утро за окном, а мы не спим."
    "На улице темно, ведь это зима."
    "На часах 6 утра."
    "Свет из дальних окон пробивается в нашем и оставляет след."
    "Тишину в комнате разбавляет только шум куллера да милое посапывание Леры."
    th "Нам пора."
    me "Лера..."
    "Я нежно дотронулся до её плеча."
    me "... Нам пора идти."
    Ler_SM "М?..."
    me "Вставай, иначе на поезд опоздаем."
    Ler_SM "Я что, уснула?"
    "Я удивлен, как весь её макияж не расплылся, пока она так мило сопела на моём плече."
    me "Да, ты хотела присесть и уснула."
    Ler_SM "Прости."
    "Я встал и потянул плавным движением Леру за собой."
    "Взяв сумки, мы направились к выходу."
    play music music_list["raindrops"] fadeout 1 fadein 2
    scene bus_stop with dissolve
    "Мы медленным и размеренным шагом двигались к остановке."
    "Шум окружающих машин не мог заглушить хруст снега под ногами."
    "Держась за теплую руку, я понимаю, что это утро не может быть испорчено."
    "Пусть мы и встали сегодня рано, я вдоволь насладился её энергией."
    "Мы пришли на остановку, не сказав друг другу ни слова."
    "Да нам и не нужно, мы просто наслаждаемся моментами, проведенными вместе."
    "Придя на остановку, я решил немного потревожить окружающую нас тишину."
    me "Ну вот мы и пришли."
    "Лера подняла глаза и с улыбкой сказала:"
    Ler_SM "Да я могла бы и сама догадаться."
    $ set_mode_nvl()
    "Встретились мы с Лерой давно. Это было года три назад. {w}Она поступила в институт, где я учился на втором курсе."
    "Мы сразу начали общаться легко. Между нами не было стены робости и стеснения."
    "У нас совершенно одинаковые вкусы, у нас нет разногласий. С её родителями я познакомился через полгода отношений."
    "Они приняли меня легко, потому что внешне я вызывал доверие."
    "Встретив Леру, я позабыл, что такое одиночество. Каждую минуту свободного времени мы проводили вместе."
    "Раньше я просто был один и...."
    $ set_mode_adv()
    Ler_SM "Ты слышал, что я сказала?"
    "Лера вывела меня из раздумий о прошлом."
    Ler_SM "Эй, ты в порядке?"
    me "Да, прости. Просто задумался."
    Ler_SM "И о чем же ты думаешь?"
    "Я не нашелся, чего сказать, поэтому я сказал самую настоящую правду..."
    me "Я думал о нас."
    "Лера расплылась в широкой улыбке и хотела меня поцеловать, но шум мотора приближающегося автобуса прервал нас."
    window hide
    scene bus_410 with dissolve
    $ renpy.pause (1)
    stop music fadeout 2
    play ambience bus_engine fadein 2
    scene busbus with dissolve
    "Тряска в автобусе уже напоминала нам поезд."
    "Шум мотора заменял стук колес о шпалы."
    me "Лера, ты можешь поспать. Нам всё равно на конечной выходить."
    Ler_SM "Угу."
    "Уставшая и еле державшая глаза открытыми Лера промычала сквозь зубы своё согласие."
    "Она плавно положила свою голову мне на плечо и сразу заснула."
    "Она заснула моментально. {w}Я даже не заметил."
    "Тряска в автобусе всё больше напоминала мне о том, что я тоже уставший."
    th "Нам всё равно на конечной..."
    "Прошептал я, и мои слова были проглочены шумом двигателя."
    show blink
    "Глаза начали слипаться и я медленно начал проваливаться в нибытие."
    stop ambience fadeout 2
    scene black
    hide blink
    $ backdrop = "days"
    $ new_chapter(1, u"День превый.")
    $ persistent.sprite_time = 'day'
    $ day_time()
    play ambience ambience_camp_entrance_day fadein 2
    scene black
    "Мне снился хороший сон. Мы с Лерой плавали в озере."
    "Оно очень напоминало мне озеро из той игры..."
    "Тут я почувствовал толчок в плечо."
    Ler_SM "Сеня, вставай. Где мы?!"
    "В её голосе явно чувствовалась тревога. Что могло случиться? {w}Мы же должны были выйти на конечной."
    "Я нехотя открыл глаза "
    scene int_bus with flash
    play music music_list["no_tresspassing"] fadein 2
    extend "и не поверил."
    th "Неужели мы попали в…"
    "Я посмотрел в глаза Лере. В них я видел страх и не понимание происходящего."
    Ler_SM " Где мы, Сема?"
    "Я не мог сказать ей правду. {w}По крайней мере сейчас."
    "Я схватил Леру за руки. На глазах её уже накатываются слезы."
    me "Лера, просто подыграй мне. Я отвечу на все твои вопросы позже."
    Ler_SM "Подыграть где? Я ничего не понимаю, Сеня."
    "Она сжала мою руку и бросилась в мои объятия."
    me "Всё хорошо, это закончится. Очень быстро, ты даже не заметишь."
    "Не мог же я ей сказать, что мы тут можем остаться навечно из-за непонятных циклов."
    Ler_SM "Хорошо, я постараюсь."
    scene camp-s-frombus with dissolve
    me "Вот смотри, сейчас через эти ворота к нам выйдет девушка. {w}Она думает, что мы новенькие в этом пионерском лагере."
    "На лице Леры я уже увидел долю удивления."
    Ler_SM "Пионерский?"
    scene int_bus with dissolve
    me "Я же сказал, что все вопросы потом."
    "Сказал я с улыбкой."
    "Лера кивнула и продолжила слушать меня, выходя из автобуса."
    scene ext_camp_entrance_day with dissolve
    me "Тебе нужно будет подыграть, как будто мы действительно приехали в этот лагерь. Идет?"
    "Лера кивнула и смахнула слезу с лица."
    me "А вот и она."
    stop music fadeout 2
    play music music_list["she_is_kind"] fadein 2
    "Я услышал шаги за воротами."
    show sl pioneer normal at center with dissolve 
    sl "Привет. Ты, наверное, новенький?"
    th "Ты? Может она оговорилась?"
    me "Да, мы новенькие. А тебя кто-то за нами послал?"
    show sl surprise pioneer at center
    "Славя недоумевающе посмотрела на меня, а потом за мои плечи."
    "Она явно в замешательстве."
    sl "Эм..."
    show sl pioneer smile at center
    extend "Ну меня послала вожатая. Как мне к тебе обращатсья?"
    me "Семен."
    "Я указал в сторону ладонью, желая представить Леру, но она решила сделать это сама."
    Ler_SM "А меня Лера."
    "Славя всё так же стояла на месте. Она сделала вид, будто не заметила, что Лера что-то сказала."
    show sl pioneer normal at center
    sl "А меня Славяна зовут. Все зовут меня Славя, поэтому и ты зови."
    show sl pioneer smile at center
    "Славя улыбнулась и посмотрела прямо мне в глаза."
    "Всё это время она не замечает Леру."
    th "Она что, специально?"
    th "Да быть такого не может. Славя всегда была доброй и отзывчивой, она просто не могла так поступить. Тем более в начале."
    "Я схватил Леру за руку."
    "Лера посмотрел на меня глазами полными уверенности. Примерно несколько минут назад она плакала, но, видимо, то, что Славя её не замечала, разожгло в ней огонь и она захотела заявить о себе."
    sl "Ну пойдем. Вожатая тебя уже, наверное, заждалась."
    "Я просто не мог выдержать подобной наглости!"
    stop music fadeout 2
    hide sl pioneer smile at center
    show sl pioneer normal far at center
    "Как только она хотела зайти за ворота, я спросил."
    me "Почему ты с ней так обращаешься? Неужели ты её не видишь? Или ты делаешь это специально?"
    show sl scared pioneer far at center
    sl "Ты о чем?"
    "Дрожащим голосом спросила Славя."
    "По её лицу было видно, что она не врет. Она явно не понимает, о чем идет речь."
    th "Что же тут творится? Она её не видит?"
    me "Прости, просто переутомился после поездки. У меня в кармане хомячок."
    show sl smile pioneer far at center 
    sl "Ой, а можно посмотреть?"
    me "Прости, не могу. Она боится новых людей, поэтому мой карман может стать мокрым."
    show sl sad pioneer far at center
    $ renpy.pause (1)
    show sl smile pioneer far at center
    "Славя сначала погрустнела, а потом сменила свою грусть ясной и красивой, женственной улыбкой."
    sl "Понимаю. Ладно, пойдем."
    hide sl
    "Как только Славя ушла за ворота, я обернулся к Лере."
    "Я шепотом сказал ей"
    me "Я сам не понимаю, что это. Веди себя как обычно, представляйся людям, заводи разговор. Мы должны понять, что происходит."
    "Лера просто кивнула, но мою руку не отпустила."
    sl "Ну ты где там?"
    me "Иду-иду, Славя."
    "Мы ускорили шаг с Лерой."
    scene ext_clubs_day with dissolve
    "Мы пересекли ворота. В глаза сразу бросаются клубы."
    "Правда после клубов взгляд сам падает на персону рядом."
    show un shy pioneer at cright with dissolve
    "Она смотрит на меня. Наши взгляды пересекаются."
    "Лера смотрит на неё, но Лена её как будто тоже не видит."
    me "Смотри, что сейчас будет."
    "Сказал я шопотом Лере."
    Ler_SM "Ты о чем?"
    "В полный голос спросила Лера. Она явно хочет, чтобы её заметили."
    me "Просто смотри."
    play music music_list["eat_some_trouble"] fadein 2
    "Лера поворачивается в сторону Лены."
    show us grin sport at left with dspr
    "И прямо по прогнозу появляется Ульянка. В руке она уже держала знакомого мне кузнечика."
    show us smile sport at center with move
    "Хватило всего пары секунд и Ульяна пересекла расстояние между ними."
    show d1_grasshopper with dspr
    un "УИИИИИИИИИИИИИ!!!" with vpunch
    "Лена завизжала так, что стекла могли треснуть в любую секунду."
    us "Ахахахах."
    "Ульяна, заливаясь хохотом, убежала прочь."
    hide d1_grasshopper
    scene ext_clubs_day
    show un scared pioneer at cright
    show sl angry pioneer at cleft
    with dissolve
    "Ульяны уже и след простыл."
    stop music fadeout 2
    sl "Вот Ульяна... {w}Лена, ты в порядке?"
    show un shy pioneer at cright
    un "Д-да..."
    "Лена всё еще дрожала, но она смогла хоть как-то произнести своё согласие."
    show sl normal pioneer at cleft
    sl "Эх... {w}Семён, это Лена. {w}Лена, это Семён. Новенький."
    Ler_SM "А меня зовут Лера!"
    "Чуть ли не криком отозвалась она, чтобы напомнить о своём присутствии."
    un "П-приятно познакомиться, Семён."
    th "Да они это, бл*ть, специально?!"
    "Лена уже не может стерпеть. Слезы катятся по её щекам."
    me "Извините, но мне нужно обратно в автобус. Кажется, я забыл одну вещицу. Она довольно важна для меня."
    show sl smile pioneer at cleft
    show un normal pioneer at cright
    sl "Да, конечно. Мы подождем тебя здесь."
    me "Спасибо. Я постараюсь быстрее."
    "Я развернулся и проследил, чтобы Лера пошла прямо за мной."
    scene ext_bus with dissolve
    "Как только мы второй раз пересекли ворота, я пошел в автобус."
    "Лера молча шла за мной."
    "Слезы капали, но никто их не видел. {w}Кроме меня."
    scene int_bus with dissolve
    me "Лера, послушай меня."
    "Я обнял её, стараясь утешить из всех сил."
    me "Я сам не понимаю, что здесь происходит. Просто дай меня немного времени, я постараюсь во всём разобраться."
    Ler_SM "Да как ты разберешься? {w}Я тут явно лишняя!"
    me "Не смей говорить так!" 
    me "Ты для меня тут главная мотивация выбраться отсюда."
    me "Все мои мысли сейчас заняты тем, чтобы объяснить тебе то, что с нами происходит, но я сам понимаю лишь малую долю."
    me "Как и договорились, мы сейчас знакомимся с лагерем, а потом мы с тобой уйдем в одно красивое место, где я тебе всё расскажу. Всё, что знаю я."
    me "А возможно нам кто-то поможет."
    Ler_SM "Кто?"
    "Лера явно была на пределе."
    me "Это будет сюрпризом."
    "Я поцеловал Леру в лоб."
    th "Надеюсь, это её хоть чуть-чуть приободрит."
    "И, кажется, это сработало."
    "Лера обняла меня ещё сильнее."
    me "Всё будет хорошо."
    Ler_SM "Да, я верю тебе."
    "Сказала Лера без малейшей доли сарказма."
    me "Нам пора. Иначе нас искать станут."
    Ler_SM "Ты имел в виду тебя?"
    "Лера говорит это с натянутой улыбкой, но я прекрасно вижу, что ей не легко справиться с подобным."
    me "Ну да..."
    "Я схватил её за руку и потащил из автобуса."
    scene ext_camp_entrance_day with dissolve
    $ renpy.pause (1.5)
    scene ext_clubs_day with dissolve
    me "Вот и я, простите, что заставил ждать."
    show sl smile pioneer at center with dissolve
    sl "Ничего. Ничего не забыл?"
    me "На этот раз всё. Можем отправляться дальше."
    "Славя кивнула и направилась в сторону площади."
    scene ext_square_day with dissolve
    Ler_SM "А сколько тут всего девушек?"
    me "Всего 9, считая персонал. По крайней мере столько расскрыто в игре. Здесь может быть больше."
    show sl surprise pioneer far at cright with dspr
    sl "Ты что-то сказал?"
    me "А? {w}Да нет, тебе показалось."
    sl "Ну ладно. Мы уже почти пришли."
    me "Спасибо."
    scene ext_houses_day with dissolve
    Ler_SM "Тут красиво, не так ли?"
    me "Угу. Ты даже представить себе не можешь, как тут порой красиво бывает."
    "Славя посмотрела на меня через плечо, но я уже перестал говорить к этому времени."
    sl "Наверное опять показалось."
    "Сказала Славя шопотом."
    "Я сделал вид, что не заметил её слова."
    "Хотя это действительно странно. Со стороны может показаться, что я разговариваю сам с собой."
    scene ext_house_of_mt_day with dissolve
    sl "Вот мы и пришли."
    play sound sfx_knock_door6_closed
    "Славя постучала в двери."
    mt "Открыто."
    "Славя открыла дверь и вошла, взглядом приглашая меня в дом."
    Ler_SM "Мне тоже идти?"
    me "Ты теперь всегда рядом со мной, что бы не случилось."
    "Я сделал первый шаг в домой, а за мной последовала Лера."
    play ambience ambience_int_cabin_day fadeout 2 fadein 1
    scene int_house_of_mt_day 
    show mt normal pioneer at center
    show sl normal pioneer at right
    with dissolve
    mt "Славя, спасибо. Можешь идти."
    sl "Хорошо."
    hide sl with dissolve
    "Славя покиинула дом, аккуратно, почти бесшумно, закрыв дверь."
    mt "Привет, Семён. {w}Мы долго тебя ждали. Как была поездка?"
    me "Да я не знаю, если честно. Я почти всю дорогу проспал."
    "Лера поняла, что ей стоять всё равно бесполезно, поэтому она присела на кровать."
    show mt smile pioneer at center 
    mt "Вот оно как. Ладно, сейчас я пойду посмотрю тебе форму. Посиди пока здесь."
    "Именно во время этой фразы Лера начала корчить рожи."
    "У неё это всегда получается хорошо, и даже в такой напряжно, не знакомой ситуации я просто не смог сдержать смех."
    me "Да, хорошо."
    "Сказал я сквозь смех."
    show mt normal pioneer at center 
    mt "Я сказала что-то смешное?"
    me "Нет, просто вспомнилось кое-что."
    mt "Ну ладно. Посиди здесь пока, я скоро вернусь."
    hide mt with dissolve
    "Ольга Дмитриевна ушла, закрыв за собой дверь."
    me "Ну зачем ты так? Мне сейчас не легче."
    "Сказал я с улыбкой на лице, поэтому никакого ощущения серьезности в моем лице не было."
    Ler_SM "Ну а чем мне еще заняться?"
    "И тут у меня в одном месте заиграло детство."
    me "Слушай, а ты можешь взаимодействовать с объектами?"
    "Лера была ошарашена подобным вопросом."
    Ler_SM "Ну я не знаю, не было пока случая."
    me "Но не смотря на это простынь под тобой проминается."
    Ler_SM "Да, так и есть. А к чему был этот вопрос?"
    me "Ну а ты сама догадайся. Кто любит у нас разыгрывать других? Будучи невидимым, можно столько всего придумать."
    "На лице Леры сначала проскользнула грусть, но она тут же сменилась яркой улыбкой, способной прожечь всё, что угодно."
    Ler_SM "А ты прав."
    "Лера впала в раздумья."
    Ler_SM "Столько мыслей в голове сразу. Как мы попали сюда? Для чего мы здесь?"
    me "Цикл идет уже не так, как раньше. В игре он был другой. Нас проводила Славя, а такого там не было. Нас не встретила Алиса."
    Ler_SM "Кто? Цикл? Алиса?"
    me "Немного терпения. {w}Я расскажу тебе всё позже."
    me "Но сейчас должна прийти Ольга и сказать, что домиков свободных нет, поэтому я буду спать в её домике. Она отдаст мне форму, а потом скажет, что дел для меня сегодня нет, поэтому я могу прогуляться по лагерю."
    Ler_SM "Понятно."
    "Как только Лера закончила говорить, двери распахнулись и вожатая вошла."
    show mt normal pioneer at center with dissolve
    mt "А вот и твоя форма."
    "Она всучила мне в руки сложенную одежду."
    mt "Кстати, я даже не представилась. Меня Ольга Дмитриевна зовут."
    me "Очень приятно."
    mt "Домиков свободных нет, так что будешь спать со мной. Вернее, в моём домике."
    th "У кого что болит..."
    me "Да, хорошо."
    hide mt with dspr
    "Вожатая подошла к тумбочке."
    "Она достала оттуда связку ключей."
    "Отделив один ключ, она отдала его мне."
    show mt smile pioneer at center with dspr 
    mt "Держи, теперь это и твой домик. Спать будешь на этой кровати."
    "Вожатая указала на кровать, где сидела Лера."
    "Лера съежилась, потому что ладонь вожатой указывала прямо на неё."
    show mt surprise pioneer at center 
    mt "Ох... А почему это простынь помята?"
    show mt normal pioneer at center
    mt "Ну теперь это твоя кровать, так что ты и поправь."
    me "Хорошо, я поправлю."
    mt "Ну и отлично. Я пойду по делам. Ты переоденься. Хоть чуть-чуть будешь похож на порядочного пионера."
    me "Хорошо."
    mt "И да, сегодня дел на тебя нет, так что погуляй по лагерю, познакомься с ребятами. Я уверена, они тебя примут хорошо."
    me "Прямо так и поступлю. Спасибо."
    "Я посмотрел на Леру со взглядом типа"
    th "Я был прав."
    Ler_SM "Да ты у нас местная Ванга."
    mt "Ну всё, я пошла. Если что-то будет нужно, то обращайся ко мне или Славе. Да и другие ребята тоже тебе помогут."
    hide mt with dspr
    "После этих слов Ольга Дмитриевна вышла из дома, прикрыв дверь."
    me "Вот и всё. Сейчас я переоденусь и мы с тобой отправимся в одно место."
    Ler_SM "Какое место?"
    me "Терпение, Лера, терпение. {w}Всё успеется."
    "Я начал переодеваться."
    "Лера всё это время смотрела на меня и не отводила взгляда."
    me "Ты во мне сейчас дырку взглядом прожжешь."
    "Лера засмущалась и отвела взгляд."
    me "Ой, да ладно. Чего ты там не видела."
    Ler_SM "Ну да..."
    "Сказала Лера, смотря в окно."
    Ler_SM "А у нас сейчас такого точно нет..."
    me "Ты о чем?"
    "К этому моменту я уже переоделся и начал завязывать галстук."
    Ler_SM "Я о погоде. Солнце, никакого дождя. Тишина да и только."
    me "А... {w}Так вот ты о чем."
    "А галстук всё отказывается слушаться. Он то и дело выскальзывает из рук."
    "Лера посмотрела на меня и улыбнулась."
    Ler_SM "Эх, растяпа. {w}Давай помогу."
    "Лера встала с кровати и направилась ко мне."
    "Она взяла в руки галстук и начала вязать узел на моей шее."
    th "У неё точно получится лучше. {w}Авось и Ольга похвалит."
    "Остался только последний штрих, и узел будет готов."
    play sound sfx_knock_door6_closed
    "В дверь постучалась и тут же вошла "
    show sl surprise pioneer far at center with dissolve
    extend "Славя."
    sl "А... {w}А как это?"
    "Лера всё стояла и держала мой галстук. Со стороны это выглядело, как будто концы его леветируют."
    "Только спустя время до Леры дошло и она отпустила галстук."
    sl "Как? Что это было? {w}Ты фокусник?"
    "А вот и решение проблемы пришло само."
    me "Ну да, практикуюсь."
    show sl smile pioneer far at center 
    sl "Ух ты! А покажешь еще раз?"
    th "Ну что же, придется."
    me "Да, сейчас попробую еще раз."
    "Я начал махать руками вокруг Леры и бормотать всякую чушь."
    me "Сим салабим, ахалай махалай, галстук взлетай."
    "Лера всё это время просто ржет. {w}Вот прямо в открытую. {w}Без доли стеснения."
    "И только когда я задел Леру своими движениями, она поняла, что делать."
    th "Ну наконец-то..."
    "Лера схватила концы галсутка и начала поднимать и опускать их."
    "Я всё продолжал махать руками, а Лера всё сильнее смеялась."
    th "Ну ладно, хватит."
    "Я аккуратно дотронулся до Леры, чтобы дать ей знак, что стоит прекратить."
    "Она так и сделала, но смеяться не перестала."
    th "Эх... Надо бы её проучить."
    hide sl
    show sl surprise pioneer at center with dspr
    sl "Вау, это замечательно. Только ты галсутк не завязал до конца. "
    show sl smile pioneer at center
    extend "Давай помогу."
    th "Вот чёрт. А Лера не будет ревновать?"
    menu:
        "Позволить Славе завязать":
            $ ES_girls_comfort_points_SMVIJ += 1
            hide sl
            show sl smile pioneer close at center with dspr
            "Славя подошла ко мне и полностью развязала галстук."
            th "Неужели ей не нравится, как Лера изначально завязала?"
            "Галстук в её руках сияет от лучей солнца и отражает их мне в глаза."
            "Славя четкими движениями завязывает узел."
            "Её действия быстры, но нежны. Она делает это очень аккуратно."
            "Лера всё это время смотрит то на меня, то на Славю."
            "Я подмигнул ей, надеясь, что она приободрится."
            sl "Что-то не так?"
            th "Черт, заметила."
            me "Да нет, просто в глаз что-то попало."
            "А вот это уже точно расстроило Леру."
            "Галстук уже был готов. Он четко сидел на моей белой рубашке."
            hide sl
            show sl normal pioneer at center with dspr
            "Славя отошла на несколько шагов."
            me "Спасибо большое."
            show sl shy pioneer at center 
            sl "Не за что."
            me "Так а зачем ты приходила, кстати?"
            show sl normal pioneer at center
            sl "Да я к Ольге Дмитриевне."
            me "Ну, как видишь, её тут нет. Она ушла буквально несколько минут назад, как ты пришла. Сказала, что у неё дела."
            sl "Хорошо, спасибо."
            hide sl with dspr 
            "Славя ушла, оставив нас с Лерой в напряжной обстановке."
        
        "Оставить это Лере":
            $ ES_Lera_comfort_points_SMVIJ += 1
            me "Да нет, спасибо. Я и сам могу."
            show sl normal pioneer at center
            sl "Ну как скажешь."
            me "Кстати, а зачем ты зашла?"
            th "Уж не поверю, что ко мне."
            sl "Да я к Ольге Дмитриевне."
            me "Ну, как видишь, её тут нет. Она ушла буквально несколько минут назад, как ты пришла. Сказала, что у неё дела."
            sl "Хорошо, спасибо."
            hide sl with dspr 
            "Славя ушла, оставив нас с Лерой наедине."

    me "А из тебя выйдет не плохая ассистентка. {w}Может нам тут своё шоу устроить?"
    
    if ES_girls_comfort_points_SMVIJ == 1:
        Ler_SM "Ну нет, как-нибудь в другой раз."
        "Лере явно не понравилось то, что я позволил Славе сделать это."
    else:
        Ler_SM "А почему бы и нет. {w}Сможешь удивить их."
        
        
    me "Ладно, а теперь, как я и обещал, я расскажу тебе всё, что я знаю. {w}Пошли."
    "Лера кивнула и пошла за мной."
    play ambience ambience_camp_center_day fadeout 1 fadein 2
    scene ext_house_of_mt_day with dissolve
    "Мы вышли из домика. В глаза сразу ударил солнечный цвет."
    "Я закрыл дверь на ключ, который мне дала вожатая, и мы пошли по направлению поляны."
    scene ext_houses_day with dissolve
    $ renpy.pause (1)
    scene ext_path_day with dissolve
    $ renpy.pause (1)
    scene ext_path2_day with dissolve
    $ renpy.pause (1)
    scene ext_polyana_day with dissolve
    "Всю дорогу до поляны мы молчали. Это была вынужденная мера, потому что сейчас середина дня и большенство пионеров находятся на улице."
    "Они явно смотрели бы на меня, как на идиота."
    "У Леры терпение вышло."
    Ler_SM "Ну и что ты хочешь мне сказать? Что ты мне расскажешь?"
    me "Хорошо, присядь. Разговор будет долгим."
    $ set_mode_nvl()
    me "Помнишь, я еще дома тебе говорил про игру Бесконечное лето? {w}Так вот, мы попали прямо в игру. Сейчас кратко расскажу сюжет."
    me "Главный герой игры — одинокий молодой человек Семён. Он живёт за счёт случайных фрилансовых заказов и проводит большую часть своего времени в интернете на анонимных имиджбордах. В один зимний день Семён отправляется на встречу выпускников, садится в автобус марки «ЛиАЗ», 410-го маршрута, где засыпает, а просыпается летом, в «Икарусе», у ворот летнего пионерлагеря «Совёнок».Обнаружив, что он чудесным образом переместился не только в пространстве, но и во времени, попав из зимы 2008 года в лето 1980-х, Семён старается разобраться, как и для чего он тут очутился, почему стал выглядеть как 17-летний подросток и как ему вернуться обратно в свой мир. Однако вскоре он сближается с другими пионерами (а особенно — с пионерками) и оказывается с головой захвачен вихрем лагерной рутины. Семёна ждут семь насыщенных дней, в течение которых ему предстоит узнать, является ли для него случившееся шансом начать новую жизнь или же наказанием, способным обернуться нескончаемым кошмаром."
    Ler_SM "И да, всё как у нас. {w}Только Семён там был один, а в этот раз мы попали вместе."
    scene ext_polyana_sunset with dissolve
    me "Да, в этом и странность. И что забавно, так это то, что тебя никто не видит."
    nvl clear
    "Лере явно не понравилось то, как я выразился."
    Ler_SM "Ну тебе-то да, забавно, а вот мне совершенно не весело."
    me "Лера, мы со всем разберемся, я тебе обещаю."
    "Я хотел взять Леру за руку, но не успел. Она приложила их к лицу и начала плакать."
    me "Ну Лера, прекрати."
    play ambience ambience_camp_center_evening fadeout 2 fadein 1
    play sound sfx_bush_leaves
    $ set_mode_adv()
    "Мы услышали звук в кустах и обернулись к источнику звука."
    th "Кто-то в кустах, это точно."
    dvp "Ну я же говорила, что он клюнет."
    usp "Ага. {w}Ахахах."
    "Спустя несколько секунд из-за кустов показались две фигуры."
    play music music_list["i_want_to_play"] fadein 2
    show dv normal pioneer at cleft
    show us normal pioneer at cright
    with dissolve
    "Это были две проказницы. {w}Встречайте, Алиса и Ульяна собственной персоной."
    dv "О, какие люди. Я тебя тут раньше не видела. Это ты тот новенький, про каторого говорила Уля?"
    show us angry pioneer at cright
    us "Не называй меня так!"
    show dv grin pioneer at cleft
    dv "Ну что молчишь? Язык проглотил?"
    me "Да, новенький. Семёном кличут."
    show dv normal pioneer at cleft
    show us normal pioneer at cright
    dv "И что это мы тут делаем в одиночестве?"
    me "Да так, решил побыть один."
    dv "Ну ладно, дай хоть руку пожму. В знак приветствия, так сказать."
    th "Добром это не кончится..."
    "Она протягивает руку, а я машинально делаю то же самое."
    dv "Приятно познакомиться, Семён."
    "Мы пожали руки и девочки начали уходить."
    play music music_list["eat_some_trouble"] fadeout 2 fadein 1
    hide us
    hide dv
    show dv smile pioneer far at cleft
    show us laugh pioneer far at cright
    "Но Ульяна не сдержалась и смех вырвался из её уст."
    th "Что-то тут не так..."
    Ler_SM "Сёма, твоя рука."
    me "М?"
    "Я посмотрел на свою руку."
    me "АЛИСА!" with hpunch
    show us normal pioneer far at cright
    show dv angry pioneer far at cleft
    dv "Что? Надо быть внимательнее!. {w}Да и вообще, откуда ты моё имя знаешь?"
    me "Услышал, пока вы с Ульяной шли сюда."
    show dv normal pioneer at cleft
    dv "Ладно, бывай, Дурачелло."
    me "Ах ты..."
    "Прошипел я сквозь зубы."
    hide us
    hide dv
    with dspr
    "Девочки развернулись и пошли в сторону лагеря."
    play music music_list["awakening_power"] fadeout 2 fadein 1
    Ler_SM "Ну уж нет, я тебе это так с рук не спущу!"
    "Лере хватило доли секунды, чтобы оказаться перед Алисой."
    "Подножка не заставила себя долго ждать и Алиса упала на землю."
    show dv angry pioneer far at cleft with dissolve
    dv "Ах ты... {w}А ну иди сюда!"
    th "Ох черт..."
    "Даже и подумать не успел, как мои ноги сами понесли меня прочь."
    "Лера, сдерживая смех, побежала за мной."
    
    
    
    


    