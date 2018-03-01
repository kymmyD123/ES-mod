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
    
    
    