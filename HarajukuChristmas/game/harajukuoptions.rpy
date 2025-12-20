label harajukuoptions:
#includes point and click mechanics! replace the menu below with image buttons
#when all image buttons are pressed, then proceed to the visual kei santa label (visualkeisanta)

#after visual kei santa part, then go to apartment_end label
    scene bg harajuku city with slow_dissolve

    $ default Parfait = False
    $ default Lolita = False
    $ default Gyaru = False

    menu:
        if Parfait and Lolita and Gyaru:
            jump visualkeisanta
        else:
            if not Parfait:
                "Parfait Candles":
                    jump parfait_candles
            if not Lolita:
                "Lolita Fashion Boutique":
                    jump lolita_boutique
            if not Gyaru:
                "Gyaru Fashion Boutique":
                    jump gyaru_boutique

