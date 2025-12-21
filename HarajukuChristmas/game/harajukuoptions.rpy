label harajukuoptions:
#includes point and click mechanics! replace the menu below with image buttons
#when all image buttons are pressed, then proceed to the visual kei santa label (visualkeisanta)

#after visual kei santa part, then go to apartment_end label
    scene bg harajuku city with slow_dissolve

    default Parfait = False
    default Lolita = False
    default Gyaru = False

    if Parfait and Lolita and Gyaru:
        jump visualkeisanta
    
    # "if not [Variable]" is how to show/hide options for screen
    # doesn't work with menu, so leaving it as is until we get harajuku bg for imagebuttons
    menu:
        #if not Parfait:
        "Parfait Candles":
            $ Parfait = True
            jump parfait_candles
        #if not Lolita:
        "Lolita Fashion Boutique":
            $ Lolita = True
            jump lolita_boutique
        #if not Gyaru:
        "Gyaru Fashion Boutique":
            $ Gyaru = True
            jump gyaru_boutique

