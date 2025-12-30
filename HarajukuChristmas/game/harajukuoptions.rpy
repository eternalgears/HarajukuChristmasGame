label harajukuoptions:
#includes point and click mechanics! replace the menu below with image buttons
#when all image buttons are pressed, then proceed to the visual kei santa label (visualkeisanta)

#after visual kei santa part, then go to apartment_end label
    hide reina
    hide kuma
    
    scene bg harajuku:
        zoom 0.375

    default Parfait = False
    default Lolita = False
    default Gyaru = False

    if Parfait and Lolita and Gyaru:
        jump visualkeisanta
    else:
        call screen shop_selection
    
    screen shop_selection:
        if not Parfait:
            imagebutton:
                xpos 0.1179
                ypos 0.769
                xanchor 0.5
                yanchor 1.0
                hover_sound "audio/reina.wav"
                activate_sound "audio/kuma.wav"
                idle "Parfait_Candles_Idle.png"
                hover "Parfait_Candles_Hover.png"
                action Jump("parfait_candles")
        if not Lolita:
            imagebutton:
                xpos 0.3585
                ypos 1.0039
                xanchor 0.5
                yanchor 1.0
                hover_sound "audio/reina.wav"
                activate_sound "audio/kuma.wav"
                idle "Lolita_Boutique_Idle.png"
                hover "Lolita_Boutique_Hover.png"
                action Jump("lolita_boutique")
        if not Gyaru:
            imagebutton:
                xpos 0.815
                ypos 1.04
                xanchor 0.5
                yanchor 1.0
                hover_sound "audio/reina.wav"
                activate_sound "audio/kuma.wav"
                idle "Gyaru_Boutique_Idle.png"
                hover "Gyaru_Boutique_Hover.png"
                action Jump("gyaru_boutique")

