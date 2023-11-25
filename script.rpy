#Персонажи и город
define GG = Character("[ggname]", color="#c8ffc8")
define city = Character("[ggcity]", color="#c8ffc8")
define antonmom = Character('Мама Антона', color="#c8ffc8")
define granny = Character('Бабуля', color="#c8ffc8", image="granny")
define aris = Character("[Ggirl]",color="000000", image="aris")
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

init:
    $left2 = Position(xalign=0.3,yalign=1.0)
    
# Игра начинается здесь:
label start:

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
    
        "Подыграем?"
        
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
    
    aris shy2 "Не стоит благодарности!"
    
    show aris shy3 
    
    "..."
    
    aris speak5 "Я пошла по королевским делам, увидимся позже…"
    
    hide aris with moveoutleft
    
    GG " (Приятно осознавать, что это не последняя наша встреча.)"
    
    stop music
    pause