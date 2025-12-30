label visualkeisanta:
    # (visual kei santa part shows up when reina and kuma are done with going everywhere in harujuku)

    show bg harajuku:
        zoom 0.375

    show reina neutral at right with easeinright:
        zoom 0.2
    
    show kuma talking at left with easeinleft:
        zoom 0.2
    
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
    "Kuma tugged on my hand, as if she was distracting me from her out of nowhere marriage proposal."

    r "Just you wait a second Kuma!"

    stop music
    show santa neutral at center:
        zoom 0.2
    v "{cps=10}Ho ho ho..."

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
    v "MINNESANN {w}KONNICHI WAAARRRTS" with hpunch
    v "YYYUUUUWAARTS"
    v "HAJIMETE"
    v "HA{w}JI{w}METEE"
    v neutral "Seven Eleven."
    v shouting "DE{w}DE{w}DE{w} ONIGIRI"
    v "KAI MASTER"
    v "JAJAJAJAJAJAJAJA{nw}"
    v "ITDAKIMASUUUU!!!!" with hpunch
    r "..."
    k "Um..."
    k "Let's go, Reina."
    hide kuma with dissolve
    hide reina with dissolve
    v "OOIISSHIII DESSSUUUUUUU{nw}" with hpunch
    jump apartment_end
