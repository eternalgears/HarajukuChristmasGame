label gyaru_boutique:

    $ Gyaru = True
    jump harajukuoptions
    scene bg gyaru boutique with slow_dissolve
    play sound "audio/store_bell.wav"

    show reina happy with dissolve

    pause
    stop sound

    play music "audio/fashion store!.mp3" fadein 2.5
    r "WOAHHHH!!"
    "Rows holding fluffy accessories and racks with gyaru-like clothing fill the store atmosphere."
    show reina happy at right with easeinright
    
    show kuma happy at left with easeinleft
    
    k "I knew you'd like the store."
    r "There is so much in here!"
    k "Oooo~ I've been meaning to show you it. Come on, let's go look over here."
    show reina neutral
    
    show kuma neutral
    
    "We hustle over to a rack containing shoulderless shirts. I can already picture how cute Kuma would look in them."

    show reina happy
    r "Wow this shirt looks really pretty! And it's {i}sooo soft.{/i}"
    r "What do you think, Kuma?"

    show kuma talking

    k "Hm? Let me see."
    play sound "audio/clothing_sound.wav"
    pause

    show kuma happy
    stop sound
    
    k "Wow it really is. I like the texture on it."
    r "That's good! This seems like something that you would wear."
    show kuma talking

    k "Are ya sure? I wasn't totally set on this one because I already have plenty of shoulderless shirts."
    r "Absolutely! A new shirt changes the base outfit right? So then, you would have a new outfit to accessorize!"
    k "Hmm... you do have a point."
    show kuma happy
    
    k "I think I will buy it. I can pair this one with one of my mini skirts."
    r "Yaa~y!"

    "We continue looking through the store, scouting for accessories, skirts, etc."

    show reina talking

    r "Sooo.. you come here often with your gyaru friends?"
    k "Yes! Every few months or so we pay the store a visit and buy the newest releases."

    show reina happy

    r "That's really nice!"
    r "When was the last time you were here?"
    show kuma talking
    k "A little while ago actually."
    k "I have a friend who I used to come here often with, but she's been swamped with college work lately so we haven't seen each other in a while."
    show reina talking
    r "Oh... that's unfortunate. Hopefully you get to see her sometime soon!"
    show kuma happy
    k "Me too. Even so, it is nice to visit this boutique again. {w}With you."
    show reina happy
    r "Awwww... stop that! You're such a flirt!"

    "We walk around for a bit before landing on a rack of magazines, sorted by genre."

    k "Oh my godd!! I've been looking for these fashion magazines for a while now. I can't believe they had them here."
    r "Ooooo these look interesting..."

    show reina laughing
    "I scan through the magazines. {w}I notice a particular one and chuckle to myself."

    show kuma talking
    k "What's so funny?"
    r "No no, I'm not laughing at you! I'm just remembering our collab back in high school."

    #flashback transition to high school

    scene white with slow_dissolve
    scene bg bedroom dark with dissolve

    "After a long tiring day of school, I've finally made it home..."
    show reina neutral with dissolve
    r "Eugh..."
    show reina surprised
    r "Crap, I forgot I still have to finish that essay!"
    r "Uuu... I have to start now!"

    show reina neutral

    "After a while of tedious work, I suddenly hear a notification sound from my phone."

    r "Hm?"

    show reina surprised
    r "HUH???"

    r "I got a DM from Kuma??"
    r "The popular gyaru influencer on Kinsta?? THE Kuma??"
    show reina happy
    r "I can't believe this is happening!!"
    "I close the doc tab (that has my essay due at 11:59PM.)"
    "Work can wait!"


    # in text
    show reina neutral at right with easeinright
    
    nvl clear

    k_nvl "hey! this is kuma reaching out! i have been looking for someone who wears lolita fashion to be in my upcoming magazine issue."
    k_nvl "and since we are moots and all..."
    k_nvl "you seem like just the person for it! let me know if you want to collab! no pressure tho ^_^"

    # exit text (doesn't go back to center of screen tho... TODO)
    show reina happy:
        ease 0.5 xpos 0.5

    r "AAAAAAAAAAHHH!!!!!"
    r "AAAAAAAAAAAAAAAAAHHHHHHHHH!!!!!!!!!!!"
    r "I can't believe this is happening??"
    r "Me? Me out of all people?! I can't believe this??"
    r "I HAVE TO ACCEPT!!!"

    # change scene for photoshoot
    scene bg harajuku city with slow_dissolve

    show reina neutral at right with easeinright
    
    show kuma neutral at left with easeinleft

    "A few days later, we were able to meet up for the photo shoot and take photos together."

    show kuma happy

    k "Thank ya so so much for doing this with me! This is just what I needed for the magazine issue."

    show reina happy

    r "No no, thank you for featuring me!"

    "Kuma and I said our goodbyes and parted ways. She told me that she was gonna finish the magazine issue and publish it in the upcoming weekend."

    # transition? here
    scene pink with slow_dissolve
    scene bg bedroom dark with slow_dissolve

    show reina neutral

    "A few weeks had passed by since I did the photoshoot with Kuma."
    show reina happy
    "I've been in contact with her since the photoshoot and we finally became friends irl!"
    # ding sound effect
    play sound "audio/phone buzz.wav"
    queue sound "audio/phone buzz.wav"
    "Buzz buzz..."

    r "Oh! It looks like I got a text from her!"

    # in text
    show reina neutral at right with easeinright

    nvl clear

    k_nvl "hey reina"
    r_nvl "What's up?"
    k_nvl "have u heard any rumors going around lately?"
    r_nvl "Not that I know of, why?"
    k_nvl "well um one of my magazine rivals started a rumor we are dating... (^_^;)"

    show reina surprised

    r_nvl "WHAT???"
    k_nvl "yeah..."
    k_nvl "im sorry you got dragged into this mess."

    show reina happy

    r_nvl "No no! It's nothing you should put the blame on yourself for."
    r_nvl "The rumors will go away eventually so let's not worry too much! :3"
    k_nvl "yeah! ur right! ^_^"
    k_nvl "btw, would u wanna hang out sometime tomorrow?"
    r_nvl "Sure!!!"
    k_nvl "kk. cya then!"

    show reina happy:
        ease 0.5 xpos 0.5

    "Tomorrow after school, Kuma is scheduled to come over to my apartment."
    "Even though we are friends, I'm really scared."
    "I still can't believe I'm friends with Kuma. She's so bold... cute... and fashionable... "
    show reina surprised
    "I don't want those rumors to mess up the bond that we have."

    scene bg bedroom morning with dissolve
    
    show reina talking with dissolve
    r "K-Kuma!"

    show reina talking at right with easeinright
    show kuma happy at left with easeinleft

    k "Reina!"

    "Of course, I scrubbed my room clean like a maniac before she came here."

    show kuma talking

    k "Woww. Your room is real organized."

    show reina happy

    r "Really?? Thank you so much."

    show kuma laughing

    k "Haha! There's no need to thank me."

    show kuma talking

    "Time flew by as we chatted about many things, like our love for fashion and the fashion magazines we've been keeping up with."
    "It got to a point where we also talked about our past, going into how we got into our fashion sub-styles."

    k "I think I gotta head out soon..."
    show reina talking

    r "Oh that's okay! I should probably get to doing my homework."
    k "Well see ya soon."
    show reina happy
    r "Byeeeee!"

    # transition AGAIN
    scene pink with slow_dissolve
    "A few months later..."
    scene bg bedroom dark with slow_dissolve
    
    show reina neutral with dissolve
    "I rushed back home to finish my homework so that I could call Kuma."
    "I was locked in on a physics question when I heard a buzz from my phone."

    #in Text

    show reina neutral at right with easeinright

    k_nvl "hey. can we talk rn?"

    # in person 
    show reina neutral:
        ease 0.5 xpos 0.5

    "There were so many things running through my head for what she could've meant."
    "She seems serious."

    #in Text
    show reina neutral at right with easeinright

    r_nvl "Yeah sure!"

    #on call - assuming that only reina shows up since it's a call
    show reina talking:
        ease 0.5 xpos 0.5

    r "What's up? Did something happen?"
    k "Umm..."
    k "I've been meaning to tell you this for a while now but... {w}I have feelings for you, Reina."
    k "I love how you're so passionate about fashion design. You could go on and on about certain fabrics and sewing patterns."
    k "And you're so cute, fun, kind, a lot of things. It's so hard not to like you!"
    k "I really love your presence! Just everything!"
    k "Would you like to go out on a date sometime...?"

    show reina surprised
    r "Is this real life?? Oh my gosh..."
    show reina happy
    r "Kuma, I think you're amazing as well!! I would gladly go on a date with you!"

    # in person

    "We talked a little while longer and then we eventually got off our call to do homework."
    r "Hehehehhehe..."
    r "Huuuhuuu..."
    # note: make the screaming dialogue text smaller to show that her voice is muffled (possibly by a pillow)
    # as a voice bleep this would be really funny
    show reina laughing
    r "{size=20}AAAAAAAAAAAAAAAAAHHHHH!!!!"
    r "{size=20}I can't believe I am going on a date with Kuma!!"

    # present time (end flashback)

    scene white with slow_dissolve
    scene bg gyaru boutique with slow_dissolve

    show reina talking at right with easeinright
    show kuma neutral at left with easeinleft
    
    r "Even now, I can't believe I am dating you!"
    show kuma happy

    k "Oh stop that..."
    # blushing happy reina here
    show reina happy

    r "Aww..."
    r "We've gone on so many amazing dates after that though!"
    r "I'm so happy to be with you!"
    k "I'm happy to be with ya too..."
    show kuma talking

    k "Come on, let's go get a few more things then head out."
    r "Yes ma'am!"

    jump harajukuoptions
