label visualkeisanta:
    # (visual kei santa part shows up when reina and kuma are done with going everywhere in harujuku)
    scene pink with slow_dissolve
    pause
    scene bg harajuku with slow_dissolve:
        zoom 0.375

    show bg harajuku:
        zoom 0.375

    show reina neutral at right:
        zoom 0.2
    show kuma talking at left:
        zoom 0.2
    with sprite_dissolve
    
    k "Mannn... I'm beat."

    r smiling "Hmm~ Hmm~"
    k "You're so cheerful for spending almost 200k yen today."
    r "Yeah? You spent like 80k today, right?"
    k "Mhm. I'm quite worried about our married future."
    k "We gotta save up as much as we can for a nice home together..."
    k smiling "Whaddya say, Reina? Should we save money starting now?"
    
    r shocked "M-MARRIED??"
    r "Are we getting married??"

    k neutral "..."
    
    k smiling "Come on! Let's go home!"
    r "Wait a second Kuma..."
    "Kuma tugged on my hand, gesturing me to go home. She's clearly trying to distract me from her out of nowhere marriage proposal!"

    r "Just you wait a second Kuma!"

    stop music
    show santa neutral at center:
        zoom 0.2
    v "{cps=10}Ho ho ho..."
    show reina shocked at altright:
        zoom 0.2
    show kuma smiling at altleft:
        zoom 0.2
    with ease

    r neutral "Eh?"
    play music "audio/santa1.mp3" fadein 2.5
    v "{cps=10}Merry... Christmas..."

    k shocked "Ah.. that's..."
    v "Can you take a video for me? I need to send it to Mrs. Claus..."

    r talking "S-sure!"
    k talking "{size=24} I know this guy." # smaller text for whispering

    "The strange man hands me his phone, which was already recording."

    v "..."

    r neutral "..."
    k neutral "..."
    v "........"
    show reina shocked
    show kuma shocked
    show santa shouting
    v "MINNASANN" with hpunch
    v "KONNICHI WAAARRRTS"
    v "YYYUUUUWAARTS" with hpunch
    v "HAJIMETE" with hpunch
    v "HA{w}JI{w}METEE" with hpunch
    v neutral "Seven El*ven." with slow_dissolve
    v shouting "DE{w}DE{w}DE{w} ONIGIRI" with hpunch
    v "KAI MASTER"
    v "JA{w}JA{w}JA{w}JA{w}JA{w}JA{w}JA{w}JA" with hpunch
    v "ITDAKIMASUUUU!!!!" with hpunch
    r "..."
    k neutral "Um..."
    k talking "Let's go, Reina."
    hide kuma with dissolve
    hide reina with dissolve
    v "OOIISSHIII DESSSUUUUUUU{nw}" with hpunch
    jump apartment_end
