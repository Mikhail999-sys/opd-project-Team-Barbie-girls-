#Персонажи и город
define GG = Character("[ggname]", color="#c8ffc8")
define city = Character("[ggcity]", color="#c8ffc8")
define antonmom = Character('Мама Антона', color="#c8ffc8")
define granny = Character('Бабуля', color="#c8ffc8", image="granny")
define aris = Character("[Ggirl]",color="000000", image="aris")
define teacher = Character('Преподаватель',color="333333",image="teacher")
#Музыка
define audio.trainmusic = "music/trainmusic.mp3"
define audio.musicmorning = "music/musicmorning.mp3"
define audio.musickitchen = "music/musickitchen.mp3"
#Звуки
define audio.dindon = "sounds/dindon.mp3"
define audio.dreamDown = "sounds/dreamDown.mp3"
define audio.grannyshocking = "sounds/grannyshocking.mp3"
define audio.trainOpen = "sounds/trainOpen.mp3"
define audio.trainMagic = "sounds/trainMagic.mp3"
define audio.soundbear = "sounds/soundbear.mp3"
define audio.soundkitchen = "sounds/soundkitchen.mp3"
define audio.soundlaugh = "sounds/soundlaugh.mp3"
#Концовка баллы
define score = 0
define teacherangry = 0

init:
    $left2 = Position(xalign=0.3,yalign=1.0)
    $desk = Position(xalign=0.5,yalign=0)
    
# Игра начинается здесь:
label start:
    camera:
        perspective True
    scene bg black with dissolve
    window hide
    pause
    
    scene bg disc with dissolve
    window hide
    pause
    
    scene bg head with dissolve
    window hide
    pause
    
    scene bg name1 with dissolve
    window hide
    pause
    
    scene bg black with dissolve
    $ ggname = renpy.input("Меня зовут", default ="Антон").strip()
    if ggname == "":
        $ ggname = "Антон"
    $ ggcity = renpy.input("Я приехал из", default ="Копейска").strip()
    if ggcity == "":
        $ ggcity = "Копейска"


    
    "У меня есть семья, сестра учится в Москве, папа лежит в больнице..."
    show antonmom with dissolve:
        xalign -0.6 yalign 1.0
        
    "Также есть мама, которая не хочет уезжать из [ggcity]."
    hide antonmom with dissolve
    
    "Я обычный первокурсник, ничем особенным не выделяюсь, не люблю привлекать внимание, хотя часто помогаю людям."
    "Я не решительный и порой неуклюжий, учёба не легко даётся. Но у меня появилось предчувствие, что скоро всё измениться…"
    scene act1 with dissolve
    window hide
    pause
    
    play sound trainMagic
    pause 1.5
    scene train11 with dissolve

    GG "(Где я, что это за место? Как я тут оказался?!)"
    GG "(Нужно сохранять спокойствие, паника ничем не поможет…)"
    
    scene train21 with dissolve
    GG "(За окнами появились здания, я слышу приближение людей.)"
    
    play sound trainOpen
    pause 1.0
    scene train31 with dissolve
    GG "(Толпа людей зашла передо мной, но я не могу разглядеть их лица.)"
    play music trainmusic fadein 1.5
    GG "(Похоже, что я нахожусь в поезде и мы начали движение. Я никогда не был здесь раньше, но атмосфера мне что-то напоминает…)"
    GG "(Нужно подойти ближе к окнам, может я смогу узнать, где я нахожусь?)"
    
    scene train41 with dissolve
    GG "(Я даже предположить не могу, где я сейчас, но кажется, что я нахожусь не в городе.)"
    "???" "Внучок, не поможешь бабушке?"
    
    show granny sad with moveinright
    
    GG "(Передо мной появилась бабушка, я её впервые вижу, похоже, что она чем-то расстроена.)"
    GG "Конечно, чем я могу вам помочь?"
    
    granny speak "У меня плохая память, я еду домой, но уже не помню, какие станции мы проехали, подскажи пожалуйста, какая будет следующая станция?"
    show granny sad
    GG "Простите, но я и сам не знаю название следующей станции, подождите секунду, я спрошу у людей и скоро к вам вернусь."

    scene train51 with dissolve
    pause 1.5
    menu:
        "Помочь бабушке?"
        
        "(Я и так боюсь разговаривать с незнакомцами, а эта обстановка довольна жуткая, лучше не рисковать и сказать, что я не смог узнать…)":
            jump scared
        
        "(Мне страшно, но я должен спросить. Я не могу бросить бабушку в беде…)":
            jump helped
    return

label scared:
    
    scene train41 with dissolve
    show granny sad
    
    GG "Извините, но я не смог узнать название следующей станции."
    
    granny shock1 "Я всё видела, ты даже не подходил ни к кому, чтобы спросить. Почему ты предложил свою помощь, если не можешь сделать что-то настолько простое?"
    GG "Но вы первые ко мне обратились, я не мог отказать вам."
    
    stop music fadeout 1
    
    granny shock2 "Тебя в детстве не воспитывали? Тебе совсем бабушку не жаль? Неудачник, ничтожество! Сейчас такое бездарное поколение растёт! Сгинь с глаз моих!"
    play sound grannyshocking
    pause 0.6
    show granny crazy1 with vpunch
    pause 0.3
    
    scene bg black with dissolve
    play sound dindon
    window hide
    pause
    play sound dreamDown
    scene hotel morning with dissolve
    pause 0.3
    GG "(Ай, неудачно упал…)"
    GG "(Слава богу, это всего лишь был кошмар, но он был слишком реалистичным…)"
    GG "(Если будильник уже прозвенел, сколько же сейчас времени?)"
    GG "(Чёрт, надо поторопиться и выходить.)"
    scene bg black with dissolve
    window hide
    jump scene3
    
label helped:
    $ score += 1
    GG "Кто-нибудь, подскажите пожалуйста, какая следующая станция?!"
    GG "(Может стоило подойти к кому-нибудь, а не орать на весь вагон…)"
    
    scene train61 with dissolve
    
    "???" "Следующая станция Коборо."
    
    GG "Спасибо!"
    
    scene train41 with dissolve
    show granny sad with dissolve
    
    GG "Бабушка, я узнал, что следующая станция Коборо."
    
    granny speak "Похоже что я уже проехала свою станцию, досадно…"
    show granny sad
    
    GG "Давайте я помогу вам добраться до дома?"
    GG "(Хотя я и сам без понятия где я…)"
    
    granny speak "Не переживай внучок, я доберусь сама, спасибо за твою помощь, всего тебе хорошего."
    stop music fadeout 1
    scene train11 with dissolve
    play sound trainMagic
    pause 0.3
    GG "(Снова этот же звук, что происходит?)"
    scene bg black with dissolve
    play sound dindon
    window hide
    pause
    scene hotel morning with dissolve
    pause 0.3
        
    GG "(Видимо это был всего лишь сон, но он был слишком реалистичным…)"
    
    GG "(Если будильник уже прозвенел, сколько же сейчас времени?)"
    
    GG "(Ой, надо поторопиться и выходить.)"
    
    scene bg black with dissolve
    window hide
    jump scene3
    
label scene3:    
    scene vuzmorning1 with dissolve
    play music musicmorning fadein 1.0
    
    GG "(На улице весьма хорошая погода, вот бы прогуляться после пар.)"
    
    GG "(После 9-ого класса, я ещё не знал, чего хочу, поэтому решил дойти до 11-ого класса и к счастью, я тогда познакомился с интересной профессией «гейм-дизайнер»)"
    
    GG "(Мне понравилась идея создавать собственные игровые миры, механики, концепции, определять сеттинг игры. Я думаю, что это очень интересная работа!)"
    
    GG "(Один из нужных навыков гейм-дизайнера это воображение, я только начал его развивать, но у меня уже есть плоды.)"

    GG "(Например, я могу с лёгкостью представить, что передо мной какое-то животное.)"

    scene vuzmorningbear
    play sound soundbear
    
    GG "(Ого, как реалистично!)"
    
    GG "(Даже подозрительно реалистично…)"
    
    GG "(Пожалуй, сегодня я пойду другой дорогой.)"
    stop music fadeout 1.0
    scene bgblack2 with dissolve
    pause 0.5
    scene vuzkitchen2 with dissolve
    play music musickitchen
    
    GG "(Ничего не меняется, те же люди, та же атмосфера, опять приходится покупать самую дешёвую еду, когда же в моей жизни что-то начнёт меняться…)"
    
    GG "(Я только сел за стол и тут же услышал, как кто-то окликнул меня)"
    
    play sound soundkitchen
    
    show aris gloomy1 at left2 with moveinleft
    
    "???" "Эй, ты! Чего такой кислый, сидишь тут один, никаких друзей нет что ли?"
    
    show aris gloomy2 at left2
    
    GG "(Ко мне впервые подошли, чтобы познакомиться, на вид и не скажешь, но я рад этому.)"
    
    GG "Как тебя зовут?"
    
    $ Ggirl = renpy.input("Эту девушку зовут:", default ="Айрис").strip()
    if Ggirl == "":
        $ Ggirl = "Айрис"
    
    aris proud1 "Я вторая принцесса королевства Э́льдии, Бо́реас Де Ла́ри [Ggirl], но ты можешь называть меня просто [Ggirl]."
    
    aris proud2 "Как же зовут тебя?"
    
    menu:
    
        "Как повести себя?"
        
        "(Почему бы мне не подыграть ей?)":
            jump played
        
        "(У неё синдром восьмиклассника? Пожалуй, представлюсь как обычно.)":
            jump besimple
    return
    
label played:
    $ score += 1
    GG "Я старший сын императора Ричарда, Но́тас Грейрат [ggname], но ты можешь называть меня просто [ggname]."
    
    show aris surprise1 
    
    "..."
    
    show aris surprise2
    
    "..."
    
    aris sly1 "Ого, у тебя тоже голубая кровь? Приятно познакомиться [ggname]."
    
    aris speak1 "Я тут мимо проходила и увидела твою кислую рожу."
    
    aris angry1 "Меня это взбесило!"
    
    aris speak2 "Поэтому пришла исправить это."
    play sound soundlaugh
    "(Ты засмеялся)"
    
    
    GG "Я думаю, что у тебя получилось."
    
    show aris surprise3 at left2
    
    "..."
    
    show aris shy1 at left2
    
    "..."
    
    jump scene3_1
    
    
    

label besimple:
    
    GG "Моё имя [ggname]"
    
    aris gloomy2 "..."
    
    aris gloomy1 "Я сегодня решила заняться благотворительностью, поэтому сяду рядом с тобой, можешь меня не благодарить."
    
    jump scene3_1

label scene3_1:
    "" "[score]"
    show aris speak3 at left2
    
    "[ggname] и [Ggirl] начали общаться и узнали, что они с одного направления."
    
    aris speak3 "Так ты тоже хочешь стать гейм-дизайнером, почему ты решил выбрать эту профессию?"
    
    show aris norm1 at left2
    
    GG "Ну... Просто я хотел бы создавать…"
    
    aris sly2 "Ты чего такой неуверенный, боишься меня? Я обычно не кусаюсь."
    
    GG "(Мне не послышалось? Она сказала обычно?)"
    
    show aris norm1 at left2
    
    GG "Я всегда был увлечен компьютерными играми. Меня привлекает возможность создавать собственные миры и истории, которые заставляют людей переживать разные эмоции."
    
    GG "А почему ты выбрала гейм-дизайн?"
    
    aris speak4 "Я люблю рисовать, придумывать дизайн игрового мира и дизайн персонажей!"
    
    GG "Это здорово! Спасибо, что поговорила со мной, мне стало лучше."
    
    aris shy2 "Не стоит благодарности..."
    
    show aris shy3 
    
    "..."
    
    aris speak5 "Я пошла по королевским делам, увидимся позже…"
    
    hide aris with moveoutleft
    
    GG " (Приятно осознавать, что это не последняя наша встреча.)"
    jump scene4
   
    label scene4:
    stop music
    play music classmusic fadein 1.0
    scene bgchair with dissolve

    GG "(Нам говорили, что сегодня у нас будет новый преподаватель на замену прежнему, интересно, что же случилось с тем преподавателем?)"
   
    scene bgdesk with dissolve

    show teacher happy at desk
    pause

    teacher speak1 "Всем привет! С сегодняшнего дня я буду заменять вашего преподавателя по гейм-дизайну."
    
    "" "Студенты: А что случилось с предыдущим преподавателем?"
    
    teacher sad1 "..."
    
    teacher speak2 "Он попал в больницу в тяжёлом состоянии…"
    
    show teacher sad
    
    teacher speak3 "Но не переживайте, врачи дают утешительный прогноз."
    
    show teacher normal
    
    "" "Студенты: (шепчутся между собой) Как думаешь, что с ним могло случиться, может он попал в дтп или на него напали?"
    
    show teacher sad2
    
    GG "(Наш прошлый преподаватель добрый и приятный человек, не вериться, что кто-то хотел нанести ему вред.)"
    
    teacher speak4 "Ребята, я понимаю, что вам хочется обсудить этот инцидент, но давайте перейдём к занятию."
    
    teacher speak1 "Я не знаю, насколько вы хорошо поняли кто такой гейм-дизайнер, поэтому сегодня ещё раз поговорим об этой замечательной профессии!"
    
    show teacher happy
    
    menu:
        "Что будем делать?"
        
        "(Я хочу послушать преподавателя, может смогу узнать что-то новое?)":
            jump learn
            
        "(Я хочу посидеть в телефоне «мемы, комиксы»)":
            jump lazyshit
    return

label learn:
    $score += 1
    
    teacher speak1 "Уважаемые студенты, сегодня я хочу поделиться с вами увлекательным миром профессии гейм-дизайнера."
    
    teacher speak1 "Эта профессия — это не только возможность создавать игры, но и вдохновлять миллионы людей по всему миру."
    
    teacher speak1 "Гейм-дизайнеры — это творческие волшебники, которые объединяют искусство, технологии и воображение для того, чтобы воплотить уникальные и захватывающие миры в игровой форме."
    
    teacher speak1 "Они отвечают за создание концепции игры, геймплея, персонажей, уровней и всего, что делает игровой процесс увлекательным и уникальным."
    
    teacher speak3 "Эта профессия требует не только технических навыков в программировании и использовании специализированных инструментов, но и креативности, умения работать в команде и понимания желаний игроков."
    
    teacher speak1 "Гейм-дизайнеры должны быть готовы к постоянному обучению и развитию, так как игровая индустрия постоянно эволюционирует и требует новых идей."
    
    teacher speak1 "Работа гейм-дизайнера — это уникальная возможность воплотить свои идеи в жизнь, создать что-то удивительное и вдохновляющее для миллионов игроков по всему миру."
    
    teacher speak1 "Если у вас есть страсть к творчеству, желание развиваться и создавать что-то уникальное, то профессия гейм-дизайнера может стать вашим увлекательным и призванием."
    teacher speak1 "Может у кого-то есть вопросы?"
    
    menu:
        "Что спросить?"
        
        "Какие языки программирования изучать для гейм-дизайна?":
            jump language
        "Можно узнать подробнее про работу в команде?":
            jump teamwork
        "Как геймдизайнер может набросать концепт для специалиста, который, например занимается звуком, если сам в этом не разбирается?":
            jump soundtrouble
        "(У меня нет вопросов.)":
            jump noquestions
    return
    
label questions:
    teacher speak1 "Ещё вопросы?"
    menu:
        "Что спросить?"
        
        "Какие языки программирования изучать для гейм-дизайна?":
            jump language
        
        "Можно узнать подробнее про работу в команде?":
            jump teamwork
        
        "Как геймдизайнер может набросать концепт для специалиста, который, например занимается звуком, если сам в этом не разбирается?":
            jump soundtrouble
        
        "(У меня нет вопросов.)":
            jump noquestions
    return
    
label language:
    $ teacherangry += 1
    
    teacher speak1 "Рекомендую изучать С# или Lua. Если говорить про движки, то наиболее подходящий движок для гейм-дизайна — Unity, а там используется C#."
    
    teacher speak3 "В крупной компании гейм-дизайнера могут попросить написать скрипты, а это Lua. В любом случае это объектно-ориентированное программирование — без него никуда."
    jump questions
    
label teamwork:
    $ teacherangry += 1
    
    teacher speak1 "Геймдизайнер много взаимодействует с людьми — устно или письменно. Встречаются разные сотрудники — интроверты и экстраверты. И геймдизайнеру нужно уметь доносить свои мысли до всех — разными способами."
    
    teacher speak3 "Это не только устное общение, но и умение «нарисовать» быстро что-то для художника в виде заметки или «написать» программисту задачу на понятном ему языке."
    
    teacher speak1 "Также коммуникативные навыки геймдизайнеру нужны для защиты идей и ведения переговоров. Геймдизайнер даёт задачи всей команде, многие процессы завязаны на нём — это большая ответственность."
    
    jump questions
    
label soundtrouble:
    $ teacherangry += 1
    
    teacher speak1 "Нужно разбираться в смежных областях хотя бы на базовом уровне: познакомиться с терминологией, ограничениями."
    
    teacher speak1 "Приведу пример. Допустим, геймдизайнеру нужен звук захлопывания двери. Задачу он может сформулировать по-разному. Может просто сказать саунд-дизайнеру «Мне нужен звук захлопывания двери», а может добавить: «в таком-то диапазоне по децибелам, формат выходного файла такой-то, ограничение по длительности такое-то, а максимальная громкость вот такая»."
    
    jump questions
    
label lazyshit:
    
    GG "(Сомневаюсь, что смогу узнать что-то новое…)"
    
    scene bgphone with dissolve
    
    GG "(Я слышал, что если поставить Дениса Борисовича на главный экран, то удача улыбнётся.)"
    
    GG "(Чем же заняться, я хочу почитать какие-нибудь грустные комиксы или же полистать мемы.)"
    
    stop music fadeout 1.0
    
    $ renpy.movie_cutscene("images/videophone.ogv")
## КРИНЖ
    jump cringe
label cringe:    
    scene bg black
    stop music
    menu:
        "Что выбрать?"
        
        "Мемы":
            jump mems
        "Комиксы":
            jump comics
        "Убрать телефон":
            jump scene4_1
    return
label mems: 
    play music musicmoon
    
    menu:
        "Что выбрать?"
        "Мемы(20 штук)":
            jump mems1
        "Депрессивные мемы":
            jump sadmems
        "Хватит телефона":
            jump cringe
    return
label mems1:
    scene mem1
    pause
    "" "(Теперь понятно, почему на каком-то участке загрузка быстрее, а на каком-то медленнее!)"
    scene mem2
    pause
    "" "(Как видят коматозное состояние любители майнкрафта.)"
    scene mem3
    pause
    "" "(Интересное совпадение…)"
    scene mem4
    pause
    "" "(Этот парень был из тех, кто просто любит чинить кондиционеры.)"
    scene mem5
    pause
    "" "(Да ну, не может быть таких ситуаций.)"
    scene mem6
    pause
    "" "(«Перевод - Первый язык программирования был придуман в 1956 году. Программисты до 1956 года:»)(Первые программисты бедняжки.)"
    scene mem7
    pause
    "" "(Не думаю, что эта авантюра закончиться хорошо.)"
    scene mem8
    pause
    "" "(Мем смешной, ситуация страшная…)"
    scene mem9
    pause
    "" "(Пациент пытался обмануть математику.)"
    scene mem10
    pause
    "" "(У меня максимум голова кружилась после такого.)"
    scene mem11
    pause
    "" "(Это будет ваше первое и последнее использование данного пылесоса.)"
    scene mem12
    pause
    "" "(Интересно, как она выкрутилась потом.)"
    scene mem13
    pause
    "" "(«Перевод – Я не могу перестать плакать от этой книги»)(Как я её понимаю, сам пытался изучать С++, но пришлось бросить это дело.)"
    scene mem14
    pause
    "" "(Это напомнило, что мой отец в больнице, мне нужно больше учиться, чтобы поскорее начать зарабатывать, почему я тогда снова вместо этого листаю мемы…)"
    scene mem15
    pause
    "" "(Когда игра перестала быть игрой.)"
    scene mem16
    pause
    "" "(Представляю лица тех, кто по привычке хлопнул комара.)"
    scene mem17
    pause
    "" "(Не люблю таких людей, которые мешают разговору по телефону. Она получила по заслугам.)"
    scene mem18
    pause
    "" "(Сам попадаю в такие ситуации, но обычно выхожу победителем.)"
    scene mem19
    pause
    "" "(На каждый глупый вопрос найдётся свой глупый ответ.)"
    scene mem20
    pause
    "" "(Пожалуй, хватит на сегодня мемов…)"
    jump mems
label sadmems:
    scene sadmem1
    pause
    "" "(Я бы сделал всё, чтобы вернуться в то время…)"
    scene sadmem2
    pause
    "" "(Почти всё в точку, однако я бы не назвал своих родителей проблемой, наоборот, благодаря им, я продолжаю учиться и не опускать руки.)"
    scene sadmem3
    pause
    "" "(Судьба всех забытых кукол…)"
    scene sadmem4
    pause
    "" "(Никогда не задумывался об этом, а ведь правда...+ 1 к фобиям.)"
    scene sadmem5
    pause
    "" "(Я бы почитал историю этого персонажа.)"
    jump mems
label comics:
    play music musiccomics
    scene bg black
    menu:
        "ЧТО ЖЕ ВЫБРАТЬ?"
       
        "Кот и смерть":
            jump catdeath
        "Кошки и солнышко":
            jump catsun
        "Любимая игрушка":
            jump lovetoy
        "Последний заплыв":
            jump lastswim
        "Приют":
            jump priut
        "Скажи привет хомячку":
            jump sayhi
        "Собачка Зевс":
            jump zeus
        "Щенок и блогеры":
            jump dogandb
        "Вернуться назад":
            jump cringe

    return            
label catdeath:
    scene cat1
    pause
    window hide
    scene cat2
    pause
    window hide
    scene cat3
    pause
    window hide
    scene cat4
    window hide
    pause
    scene ccat1
    pause
    window hide
    scene ccat2
    pause
    window hide
    scene ccat3
    pause
    window hide
    scene ccat4
    pause
    window hide
    scene ccat5
    pause
    window hide
    scene ccat6
    pause
    window hide
    scene ccat7
    pause
    window hide
    scene ccat8
    pause
    window hide
    scene ccat9
    pause
    "" "(Замечательная бабушка…)"
    scene cccat1
    pause
    window hide
    scene cccat2
    pause
    window hide
    scene cccat3
    pause
    window hide
    scene cccat4
    pause
    window hide
    scene cccat5
    pause
    window hide
    scene cccat6
    pause
    window hide
    scene cccat7
    pause
    window hide
    scene cccat8
    pause
    window hide
    scene cccat9
    pause
    window hide
    scene cccat10
    pause
    "" "(Вот и закончилась эта история про чёрного кота, надеюсь, что у бабушки всё будет хорошо.)"
    jump comics
label catsun:
    scene sun1
    pause
    window hide
    scene sun2
    pause
    window hide
    scene sun3
    pause
    window hide
    scene sun4
    pause
    window hide
    scene sun5
    pause
    "" "(Всегда стоит делиться с близкими людьми, пока такая возможность не исчезла…)"
    jump comics
label lovetoy:
    scene toy1
    pause
    window hide
    scene toy2
    pause
    window hide
    scene toy3
    pause
    window hide
    scene toy4
    pause
    window hide
    scene toy5
    pause
    window hide
    scene toy6
    pause
    window hide
    scene toy7
    pause
    window hide
    scene toy8
    pause
    window hide
    scene toy9
    pause
    window hide
    scene toy10
    pause
    "" "(Такая глубокая тоска – цена за то, как сильно кого-то любили…)"
    scene ttoy1
    pause
    window hide
    scene ttoy2
    pause
    window hide
    scene ttoy3
    pause
    window hide
    scene ttoy4
    pause
    window hide
    scene ttoy5
    pause
    window hide
    scene ttoy6
    pause
    window hide
    scene ttoy7
    pause
    window hide
    scene ttoy8
    pause
    window hide
    scene ttoy9
    pause
    window hide
    scene ttoy10
    pause
    window hide
    jump comics
label lastswim:
    scene shark1
    pause
    window hide
    scene shark2
    pause
    window hide
    scene shark3
    pause
    window hide
    scene shark4
    pause
    window hide
    scene shark5
    pause
    window hide
    scene shark6
    pause
    window hide
    scene shark7
    pause
    window hide
    scene shark8
    pause
    window hide
    scene shark9
    pause
    window hide
    scene shark10
    pause
    window hide
    jump comics
label priut:
    scene shelter1
    pause
    window hide
    scene shelter2
    pause
    window hide
    scene shelter3
    pause
    window hide
    scene shelter4
    pause
    window hide
    scene shelter5
    pause
    window hide
    scene shelter6
    pause
    window hide
    scene shelter7
    pause
    window hide
    scene shelter8
    pause
    window hide
    scene shelter9
    pause
    "" "(Я так рад, что она решила подарить ему дом, даже если не надолго…)"
    jump comics 
label sayhi:
    scene hum1
    pause
    window hide
    scene hum2
    pause
    window hide
    scene hum3
    pause
    window hide
    scene hum4
    pause
    window hide
    scene hum5
    pause
    window hide
    scene hum6
    pause
    window hide
    scene hum7
    pause
    window hide
    scene hum8
    pause
    window hide
    scene hum9
    pause
    "" "(Бедный хомячок…)"
    jump comics
label zeus:
    scene zeus1
    pause
    window hide
    scene zeus2
    pause
    window hide
    scene zeus3
    pause
    window hide
    scene zeus4
    pause
    window hide
    scene zeus5
    pause
    window hide
    scene zeus6
    pause
    window hide
    scene zeus7
    pause
    window hide
    scene zeus8
    pause
    window hide
    scene zeus9
    pause
    window hide
    scene zzeus1
    pause
    window hide
    scene zzeus2
    pause
    window hide
    scene zzeus3
    pause
    window hide
    scene zzeus4
    pause
    window hide
    scene zzeus5
    pause
    window hide
    scene zzeus6
    pause
    window hide
    scene zzeus7
    pause
    window hide
    scene zzeus8
    pause
    "" "(Очень трогательная история...)"
    jump comics
label dogandb:
    scene puppy1
    pause
    window hide
    scene puppy2
    pause
    window hide
    scene puppy3
    pause
    window hide
    scene puppy4
    pause
    window hide
    scene puppy5
    pause
    window hide
    scene puppy6
    pause
    window hide
    scene puppy7
    pause
    "" "(Одно дело совершать добрые поступки ради своей выгоды, другое дело притворяться, что совершаешь добрые поступки… )"
    jump comics      
label noquestions:   
 
    if teacherangry >4:
        teacher speak1 "Вы что долбаебы зачем столько раз переспрашивать?"
    if teacherangry <3:
        $ score -= 1
    "" "[score]"
    
    jump scene4_1
    
label scene4_1:
    scene bgdesk with dissolve
    
    show teacher speak1 at desk 
    
    teacher speak1 "Всем спасибо за сегодняшнее занятие, буду ждать вас на следующем!"
    
    scene bgchair
    
    GG "(Так, какие у меня сейчас планы?)"

    
    