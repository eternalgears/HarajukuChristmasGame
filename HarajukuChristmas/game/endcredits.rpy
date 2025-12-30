label endcredits:
    play music "audio/endcredits.mp3" fadein 0.5
    scene white with slow_dissolve
    show text "Hii!! The end!! (>_<)" 
    with slow_dissolve
    pause
    show text "{size=50}{color=#FF96B0}Concept Artists!{/size}{/color}\nChloe Choi\nAitana"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Writers!{/size}{/color}\n{i}Lead Writer{/i} - Jaden Nguyen\n{i}Writer{/i} - Braden Buell\n{i}Writer{/i} - Katie Sanchez"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Artists!{/size}{/color}\n{i}Backgrounds{/i} - Chloe Choi\n{i}CGs{/i} - Bao-Nhi Nguyen\n{i}Sprites{/i} - Gabriela Montante\n{i}School BG{/i} - Mazie Berry\n{i}UI{/i} - Jaden Nguyen"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Programming!{/size}{/color}\nJaden Nguyen\nGrace Seeberger"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Music!{/size}{/color}\nNicolas Hermoza\nKiran Dinakaran"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Game Testers!{/size}{/color}\nAiden Clary\nNicolas Hermoza\nMaxwell Ali\nKiran Dinakaran"
    with dissolve
    $ renpy.pause(4.0)
    show text "{size=50}{color=#FF96B0}Project Manager!{/size}{/color}\nJaden Nguyen"
    with dissolve
    $ renpy.pause(4.0)
    show text "Thank you for playing our game!! ^_^"
    with dissolve
    pause
    show text "Please continue to support {color=#FF96B0}Studio Yurika!!{/color}\n{i}Weaving games full of yuri and love!{/i}"
    with dissolve
    pause
    hide text with dissolve
    with Pause(1)
    return

