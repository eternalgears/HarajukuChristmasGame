label gyaru_boutique:

    $ Gyaru = True
    scene bg gyaru boutique with slow_dissolve:
        zoom 0.375
    play music "audio/gyaru boutique.mp3" fadein 2.5
    play sound "audio/store_bell.wav"

    show reina smiling at center with dissolve:
        zoom 0.2

    with Pause(1.0)
    stop sound

    r "WOAHHHH!!"
    "Rows holding fluffy accessories and racks with gyaru-like clothing fill the store atmosphere."
    show reina smiling at right with easeinright:
        zoom 0.2
    
    show kuma smiling at left with easeinleft:
        zoom 0.2
    
    k "I knew you'd like the store."
    r "There is so much in here!"
    k "Oooo~ I've been meaning to show you it. Come on, let's go look over here."
    show reina neutral
    
    show kuma neutral
    
    "We hustle over to a rack containing shoulderless shirts. I can already picture how cute Kuma would look in them."

    r smiling "Wow this shirt looks really pretty! And it's {i}sooo soft.{/i}"
    r "What do you think, Kuma?"

    k talking "Hm? Let me see."
    play sound "audio/clothing_sound.wav"
    with Pause(1.0)
    
    k smiling "Wow it really is. I like the texture on it."
    r "That's good! This seems like something that you would wear."

    k talking "Are ya sure? I wasn't totally set on this one because I already have plenty of shoulderless shirts."
    r "Absolutely! A new shirt changes the base outfit right? So then, you would have a new outfit to accessorize!"
    k "Hmm... you do have a point."
    
    k smiling "I think I will buy it. I can pair this one with one of my mini skirts."
    r "Yaa~y!"

    "We continue looking through the store, scouting for accessories, skirts, etc."

    r talking "Sooo.. you come here often with your gyaru friends?"
    k "Yes! Every few months or so we pay the store a visit and buy the newest releases."

    r smiling "That's really nice!"
    r "When was the last time you were here?"
    k talking "A little while ago actually."
    k "I have a friend who I used to come here often with, but she's been swamped with college work lately so we haven't seen each other in a while."
    r talking "Oh... that's unfortunate. Hopefully you get to see her sometime soon!"
    k smiling "Me too. Even so, it is nice to visit this boutique again. {w}With you."
    r smiling "Awwww... stop that! You're such a flirt!"

    "We walk around for a bit before landing on a rack of magazines, sorted by genre."

    k "Oh my godd!! I've been looking for these fashion magazines for a while now. I can't believe they had them here."
    r "Ooooo these look interesting..."

    show reina laughing
    "I scan through the magazines. {w}I notice a particular one and chuckle to myself."

    k talking "What's so funny?"
    r smiling "No no, I'm not laughing at you! I'm just remembering our collab back in high school."

    #flashback transition to high school
    scene pink with slow_dissolve
    "A year ago..."
    scene white with slow_dissolve
    scene bg apartment with dissolve:
        zoom 0.375

    "After a long tiring day of school, I've finally made it home..."
    show reina neutral at center with dissolve:
        zoom 0.2
    r "Eugh..."
    r shocked "Crap, I forgot I still have to finish that essay!"
    r "Uuu... I have to start now!"

    scene pink with slow_dissolve
    with Pause(1.0)
    scene bg apartment with dissolve:
        zoom 0.375
    show reina neutral at center with dissolve:
        zoom 0.2
    play sound "audio/phone_notification.mp3"
    with Pause(1.0)
    "After a while of tedious work, I suddenly hear a notification sound from my phone."

    r "Hm?"

    show reina shocked with hpunch
    r "HUH???"

    r "I got a DM from Kuma??"
    r "The popular gyaru influencer on Kinsta?? THE Kuma??"
    r laughing "I can't believe this is happening!!"
    show reina smiling
    "I close the doc tab (that has my essay due at 11:59PM.)"
    "Work can wait!"


    # in text
    show reina smiling at right with easeinright
    
    nvl clear

    k_nvl "hey! this is kuma reaching out! i have been looking for someone who wears lolita fashion to be in my upcoming magazine issue."
    k_nvl "and since we are moots and all..."
    k_nvl "you seem like just the person for it! let me know if you want to collab! no pressure tho ^_^"

    # exit text
    show reina laughing:
        ease 0.5 xalign 0.5

    r "AAAAAAAAAAHHH!!!!!"
    r "AAAAAAAAAAAAAAAAAHHHHHHHHH!!!!!!!!!!!"
    r "I can't believe this is happening??"
    r "Me? Me out of all people?! I can't believe this??"
    r "I HAVE TO ACCEPT!!!"

    # change scene for photoshoot
    scene pink with slow_dissolve
    with Pause(1.0)
    play sound "<volume 4.0>audio/photo.wav"
    with Pause(1.5)
    play sound "<volume 4.0>audio/photo.wav"
    with Pause(1.5)
    play sound "<volume 4.0>audio/photo.wav"
    with Pause (1.5)
    "A few days later, we were able to meet up for the photo shoot and take photos together."
    scene bg harajuku with slow_dissolve:
        zoom 0.375

    show reina smiling at right:
        zoom 0.2
    show kuma smiling at left:
        zoom 0.2
    with sprite_dissolve

    k "Thank ya so so much for doing this with me! This is just what I needed for the magazine issue."

    r "No no, thank you for featuring me!"

    "Kuma and I said our goodbyes and parted ways. She told me that she was gonna finish the magazine issue and publish it in the upcoming weekend."

    # transition? here
    scene pink with slow_dissolve
    scene bg apartment with slow_dissolve:
        zoom 0.375

    show reina neutral at center with dissolve:
        zoom 0.2

    "A few weeks had passed by since I did the photoshoot with Kuma."
    show reina smiling
    "I've been in contact with her since the photoshoot and we finally became friends irl!"
    # ding sound effect
    # TODO: two options!! either vibrate (match with "buzz") or notification ping sound
    #play sound "audio/phone_vibrate.mp3"
    play sound "audio/phone_notification.mp3"
    "Buzz buzz..."

    r "Oh! It looks like I got a text from her!"

    # in text
    show reina smiling at right with easeinright

    nvl clear

    k_nvl "hey reina"
    r_nvl "What's up?"
    k_nvl "have u heard any rumors going around lately?"
    show reina neutral
    r_nvl "Not that I know of, why?"
    k_nvl "well um one of my magazine rivals started a rumor we are dating... (^_^;)"

    show reina shocked

    r_nvl "WHAT???"
    k_nvl "yeah..."
    k_nvl "im sorry you got dragged into this mess."

    show reina smiling

    r_nvl "No no! It's nothing you should put the blame on yourself for."
    r_nvl "The rumors will go away eventually so let's not worry too much! :3"
    k_nvl "yeah! ur right! ^_^"
    k_nvl "btw, would u wanna hang out at your place sometime tomorrow?"
    k_nvl "no pressure tho! im just asking since we've hung out a few times"
    r_nvl "Sure!!!"
    k_nvl "kk. cya then!"

    show reina neutral:
        ease 0.5 xalign 0.5

    "Tomorrow after school, Kuma is scheduled to come over to my apartment."
    "Even though we are friends, I'm really scared."
    "I still can't believe I'm friends with Kuma. She's so bold... cute... and fashionable... "
    show reina shocked
    "I don't want those rumors to mess up the bond that we have."

    scene pink with slow_dissolve
    with Pause(0.5)
    "The next day..."
    scene bg apartment with slow_dissolve:
        zoom 0.375
    
    show reina talking at center with dissolve:
        zoom 0.2
    r "K-Kuma!"

    show reina talking at right with easeinright:
        zoom 0.2
    show kuma smiling at left with easeinleft:
        zoom 0.2

    k "Reina!"

    "Of course, I scrubbed my room clean like a maniac before she came here."

    k talking "Woww. Your room is real organized. Supes cute!!"

    k smiling "I love all the H*ts*ne M*ku merch!!"

    r smiling "Really?? Thank you so much."

    k laughing "Haha! There's no need to thank me."

    scene pink with slow_dissolve
    with Pause(1.0)
    "Time flew by as we chatted about many things, like our love for fashion and the fashion magazines we've been keeping up with."
    "It got to a point where we also talked about our past, going into how we got into our fashion sub-styles."

    scene bg apartment with slow_dissolve:
        zoom 0.375
    show reina talking at right:
        zoom 0.2
    show kuma talking at left:
        zoom 0.2
    with sprite_dissolve
    k talking "I think I gotta head out soon..."

    r talking "Oh that's okay! I should probably get to doing my homework."
    k "Well see ya soon."
    r smiling "Byeeeee!"

    # transition AGAIN
    scene pink with slow_dissolve
    with Pause(1.0)
    scene bg apartment with slow_dissolve:
        zoom 0.375
    "A few months later..."
    
    show reina neutral at center with dissolve:
        zoom 0.2
    "I rushed back home to finish my homework so that I could call Kuma."
    play sound "audio/phone_notification.mp3"
    with Pause(1.0)
    "I was locked in on a physics question when I heard a buzz from my phone."

    #in Text

    show reina neutral at right with easeinright

    # dramatic stop music scene
    stop music fadeout 1.0
    k_nvl "hey. can we talk rn?"

    # in person 
    show reina shocked:
        ease 0.5 xalign 0.5

    "There were so many things running through my head for what she could've meant."
    "She seems serious."

    #in Text
    show reina neutral at right with easeinright

    r_nvl "Yeah sure!"
    k_nvl "actually"
    k_nvl "are you free to call?"
    r_nvl talking "Yeah!"
    play music "audio/phone_notification.mp3"
    nvl_narrator "kuma~ :33 is calling you."
    stop music
    #on call - assuming that only reina shows up since it's a call
    show reina talking:
        ease 0.5 xalign 0.5

    r "What's up? Did something happen?"
    k "Umm..."
    k "I've been meaning to tell you this for a while now but... {w}{size=24}ohhh my god...{/size}"
    r smiling "It's okay Kuma! I won't judge."
    k "I have feelings for you."
    show reina shocked at center with hpunch
    r "EHHH??"
    k "I love how you're so passionate about fashion design. You could go on and on about certain fabrics and sewing patterns."
    show reina smiling
    k "And you're so cute, fun, kind, a lot of things. It's so hard not to like you!"
    k "I really love your presence! Just everything!"
    k "Would you like to go out on a date sometime...?"

    play music "audio/gyaru boutique.mp3" fadein 2.5

    r shocked "Is this real life?? Oh my gosh..."
    r laughing "Kuma, I think you're amazing as well!! I would gladly go on a date with you!"

    # in person
    scene pink with slow_dissolve
    with Pause(0.5)
    "We talked a little while longer and then we eventually got off our call to do homework."
    scene bg apartment with dissolve:
        zoom 0.375
    show reina talking at center with dissolve:
        zoom 0.2
    r "Hehehehhehe..."
    r smiling "Huuuhuuu..."
    # note: make the screaming dialogue text smaller to show that her voice is muffled (possibly by a pillow)
    # as a voice bleep this would be really funny
    show reina laughing at center with hpunch
    r "{size=24}AAAAAAAAAAAAAAAAAHHHHH!!!!"
    r "{size=24}I can't believe I am going on a date with Kuma!!"

    # present time (end flashback)

    scene white with slow_dissolve
    with Pause(1.0)
    scene bg gyaru boutique with slow_dissolve:
        zoom 0.375

    show reina talking at right:
        zoom 0.2
    show kuma neutral at left:
        zoom 0.2
    with sprite_dissolve

    r "Even now, I can't believe I am dating you!"

    k smiling "Oh stop that..."
    # blushing happy reina here

    r smiling "Aww..."
    r "We've gone on so many amazing dates after that though!"
    r "I'm so happy to be with you!"
    k "I'm happy to be with ya too..."

    k talking "Come on, let's go get a few more things then head out."
    r "Yes ma'am!"

    scene bg harajuku with slow_dissolve:
        zoom 0.375
    play music "audio/apt-ost.mp3" fadein 1.5

    jump harajukuoptions
