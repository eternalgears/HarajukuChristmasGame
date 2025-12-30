label apartment_end:
    play music "audio/apartmentend.mp3" fadein 0.5
    scene bg apartmentend with slow_dissolve:
        zoom 0.375
    $ renpy.pause(1.0)
    show reina neutral at right with slow_dissolve:
        zoom 0.2
    show kuma neutral at left with slow_dissolve:
        zoom 0.2
    "We’re back in my bedroom... In the middle is a kotatsu for the both of us to sleep in for the night. A staple for the ending of all Christmas dates!"
    "More importantly..."
    r talking "What was that all about?"
    k talking "Oh, the guy earlier? {w}He just does that a lot around here."
    r neutral "No! I mean... yeah he’s crazy."
    r shocked "But more than that!"
    r "What is this talk about us getting {i}married?{/i}"
    k neutral "Ohhh that... {w}do ya not wanna get married to me?"
    show reina shocked at right with vpunch:
        zoom 0.2
    r "OF COURSE I WANT TO BE MARRIED TO YOU!!! {w}I LOVE YOU!!!!"
    r "I’m just so shocked!"
    r "Whenever I think of marriage, I think of proper adults who have everything figured out."
    r "People who are in love... people who are mature about everything..."
    r "It sometimes feels like I’ll never be able to reach that part of my life."
    r laughing "Umm... actually I don’t know if I phrased that right."
    r smiling "Sorry."
    k "Reina..."
    k shocked "You know, I didn’t mean to put the ‘future’ pressure on ya like that."
    k talking "Everything takes a step at a time and that’s okay! We don’t have to rush into things."
    r talking "I know... but.."
    r neutral "I can’t help but be scared about what’s to come for the future."
    r shocked "Everything’s been going so well in my life right now!"
    r "I have lolita friends, a decent following on Kinsta, manageable college work... an amazing girlfriend..." 
    r "But there was a time where I was alone. {w}I used to be really lonely and overly anxious in high school, you know?"
    r "I can’t help but feel like that again when the future is brought up because what if this all ends...?"
    r "What if I stop wearing lolita fashion and you stop being a gyaru??"
    r "Will something happen to us?{nw}"
    r laughing "I’m sorry- I know this is too much and I feel like I’m ruining the mood{nw}"
    k shocked "Reina!"
    "Kuma squeezed my hand. I can feel her warmth through my gloves."
    k neutral "Ya already know this by now, but change is an inevitable part of our lives."
    k "There’s lots of things that could change by the next day."
    k talking "Like, if the past me knew that I was dating you, then she woulda passed out cold on the floor."
    r neutral "Seriously?"
    k smiling "Of course."
    k "That doesn’t mean that we’ll ever be apart. I swear."
    k talking "Plus... we would be supes cute fashion grandmas."
    r laughing "Oh you..."
    r "I just said that I was afraid of the future and you mention us being GRANDMAS."
    k laughing "Wait...but wouldn’t it be cute tho?"
    k smiling "People would look at us and say \"Omg! It’s the lolita and gyaru grandmas!!\""
    r smiling "Hehehe... That does sound fun."
    # reina smiling blushing sprite
    "Kuma gestures over to the kotatsu in the corner with a grin."
    k laughing "Get over here! Let’s cuddle!"
    r laughing "Wait!! We’re still in our outfits!"
    k smiling "Oh right.."

    scene black with slow_dissolve
    "After we both got changed into our pajamas, we immediately went to cuddle in the kotatsu."
    window hide
    scene cg apartmendend with slow_dissolve
    pause
    r "..."
    k "I know it’s hard to believe me right now."
    k "It’s going to be okay, Reina."
    r "Kuma..."
    r "Ugh...sorry for being such a downer on our Christmas date! We’re supposed to be really happy right now!"
    k "I’m pretty happy right now."
    r "Really?"
    k "Yeah! I got to be on a Christmas date with my cute girlfriend and then cuddle with her at the end."
    r "Oh... in that case I’m happy too!!"
    window auto hide
    show cg apartmentend with medium_dissolve:
        subpixel True zoom 1.63 
        parallel:
            xpos 0.53 
            linear 1.75 xpos 0.41 
        parallel:
            ypos 1.52 
            linear 1.76 ypos 1.48 
    with Pause(1.86)
    show cg apartmentend with medium_dissolve:
        pos (0.41, 1.48) 
    window auto show
    "I giggled into her chest. I feel bad about having her reassure me but... she seems to really enjoy this moment."
    "The blanket’s warmth and the sound of her heartbeat was all that I needed after such a long day."


    return
