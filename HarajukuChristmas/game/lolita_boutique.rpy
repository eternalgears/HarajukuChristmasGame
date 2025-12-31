label lolita_boutique:
    $ Lolita = True
    #Enter Lolita Fashion Boutique
    play music "audio/lolitaboutique.mp3" fadein 1.5
    scene bg lolitaboutique with slow_dissolve:
        zoom 0.375
    show reina laughing at right:
        zoom 0.2
    show kuma neutral at left:
        zoom 0.2
    with easeinleft
    r "EEEEKK!! This place is really packed!"
    k talking "Well ya know.. it is the holiday season..."
    r smiling"Hmm... well you know what this calls for?"
    k neutral "Oh?"
    r laughing "SALESSSS!!"
    "Kuma glances around the store before grasping my hand, leading me to the sales rack."
    "She picks out a blouse and holds it against my chest."
    k talking "Woahh... wouldja look at that."
    k smiling "This blouse looks real similar to the blouse ya wore when I followed ya on Kinsta..."
    r shocked "EH?? {w}You remember something like that?"
    k laughing "Yup!! I have a perfect recollection of ya even before our first interaction hehe..."
    r neutral "Oh gosh..."
    r smiling "I only remember up until I posted my photos..."
    scene white with slow_dissolve
    "Back then..."
    # Enter flashback (black fade in fade out to backstory cg)
    play music "audio/crowd.mp3" fadein 2.5 fadeout 2.0
    scene bg classroom with slow_dissolve
    "I sit isolated in the back of the classroom, eavesdropping on my classmates' chatter about their after school plans and the newest console release."
    window hide
    scene cg flashback with slow_dissolve
    pause

    r "(Sigh...)"
    "I stared at the clock, waiting for the school bell to start."
    "Tick...{w}tick...{w}tick..."

    # insert school bell sound
    play sound "<volume 5.0>audio/school.mp3"
    with Pause(10.583)

    scene bg classroom with slow_dissolve
    stop music fadeout 20.0
    "Students rushed out of the classroom at the first sound of the bell, probably eager to be first at the nearest arcades and cafes."
    "I waited for the crowd to die down before I finally made my way out the door."
    play music "audio/winter.wav" fadein 5.0 fadeout 5.0
    scene white with slow_dissolve
    "The cold breeze on the walk home made me shiver uncontrollably."
    r "Ah...I wish I had brought a thicker jacket."
    "The sound of the snow crunching beneath my boots was enough to distract me from the harsh wind." 
    "I hurried to the front door of my house and threw it open."
    play music "audio/lolitaboutique.mp3" fadein 1.5
    scene pink with slow_dissolve
    r "I’m homeee!!"
    "I made my way up the stairs to my room and shut the door to begin my magical transformation!!"
    scene bg apartment with slow_dissolve:
        zoom 0.375
    r "Where’d I put that new petticoat..."
    "I managed to throw on every piece and completed my makeup without a hassle."
    r "Nowww... for the finishing touch!"
    "I carefully grabbed my headpiece and tied it."
    r "Perfect!"
    # photo snapping sfx
    window hide
    play sound "<volume 4.0>audio/photo.wav"
    with Pause(1.0)
    play sound "<volume 4.0>audio/photo.wav"
    with Pause(1.0)
    play sound "<volume 4.0>audio/photo.wav"
    with Pause(1.0)
    "I take many photos, making sure they are positioned correctly to the camera. I have to show my outfit at the best angles, after all!"
    r "This looks like enough..."
    "I scrolled through my gallery and carefully chose which photos to upload."
    "Finally, I set the post caption to ‘Pray for miniature moon ♡’"
    scene pink with dissolve


    # Change to present
    scene bg lolitaboutique with slow_dissolve:
        zoom 0.375
    show reina neutral at right:
        zoom 0.2
    show kuma neutral at left:
        zoom 0.2
    with sprite_dissolve

    r "Ehhh... that’s all I can remember..."
    k smiling "Don’t worry bout’ it! I remember the rest."
    "Kuma rushes over to another rack and sorts through all the jumperskirts until she finds a really familiar one."
    "That’s definitely the jumperskirt that I wore with that post!!"
    r shocked "WAAAAHHH??? They still sell this here?"
    r neutral "I guess it never went out of style..."
    k smiling "Thanks to {i}my{/i} help hehe..."
    k neutral "I wasn’t president of the fashion club in high school for nothing..."

    # To Kuma’s flashback
    scene white with slow_dissolve
    k "When we met, I remember..."
    with Pause(1.0)
    play music "<volume 0.5>audio/crowd.mp3" fadein 1.5 fadeout 2.0
    scene bg classroom with slow_dissolve
    "I stood in between many of my club officer friends in front of a classroom."
    stop music fadeout 20.0
    with hpunch
    k "Aaaand that concludes the club meeting!!"
    k "If you guys have any questions about the upcoming fashion swap meet, please let me know!"
    "I waited for everyone to leave the classroom and then sat at an empty desk."
    "As I clicked on the search bar, I was reminded of who I had looked up earlier that day."
    "A rising small lolita fashion Kinsta creator who posts a lot of intricate lolita coords."
    k "Reina..."
    "My heart sped up from just seeing her name on the search history."
    "I clicked on the account and saw that she made a new post!"
    "‘Pray for miniature moon ♡’"
    k "Lolita style is just so cool..."
    "I swiped through all the photos and just stared in awe."
    "With a trembling finger, I liked her new post and {i}even followed her.{/i}"
    k "Should I just go the full mile and repost as well?"
    k "As we’re both fashion influencers... surely she won’t find it odd..."
    k "Plus that skirt is supes cute."
    "With my mind struggling to choose the right decision, I decided to stick to my intuition and repost."

    # Back to present 
    scene bg lolitaboutique with slow_dissolve:
        zoom 0.375
    show reina laughing at right:
        zoom 0.2
    show kuma smiling at left:
        zoom 0.2
    with sprite_dissolve

    play music "audio/lolitaboutique.mp3"
    r "Oh! I remember that now!!"
    r smiling "That jumperskirt (even though it is the most expensive one I own) is one of my favorite pieces!! I was starting to gain traction on Kinsta because of it."
    r "I still wasn’t popular enough to get Kinsta monetization money... so I would go months without being able to buy lolita pieces."
    r neutral "Being a lolita is already an expensive lifestyle as it is, so I clung to that piece a lot and posted it all the time."
    r smiling "At some point I was getting tired of that jumperskirt. Untillll..."
    k neutral "Until?"
    r laughing "The most popular and cutest fashionista started following me!!"
    "I looked at Kuma and realized that even the simplest of compliments were still enough to make her blush."
    k smiling "I really... {w}wanted to compliment you but I wasn’t bold enough to DM you immediately..."
    k neutral "I decided reposting was the next best thing."
    k talking "I don’t know if you ever realized the impact my repost made, but my fans really loved your jumperskirt."
    r neutral "Of course I noticed! I just didn’t think it would have such an impact that it would keep it in stores years later."
    r smiling "Honestly... I don’t think you know the impact that singular repost had on me."
    r talking "Your repost made tons of kind people comment on my post and it helped me regain the confidence I had."
    k neutral "What do you mean? I thought you loved that thing to death."
    r neutral "Well..."
    r shocked "At that point in time, I was thinking of giving up that lifestyle."
    r "Everything in my life kept going wrong and I was starting to let go of the things I held close to me."
    r smiling "Then... the day you followed me!"
    r laughing "I didn’t have the best day at school... so seeing that notification was like a reminder.."
    r "A reminder that if you withstand the most brutal moments of your life..."
    r "Something uplifting and equally as intense will eventually come along."
    r smiling "Even if it feels like you’ve been fighting forever, if you keep going, one day it’ll feel like you’ve been feeling euphoric forever!"
    k smiling "I forgot how contrasting our high school lives were."
    k talking "It felt like I had a thriving high school life."
    k "I had many friends, fans on Kinsta, and I was running a successful magazine at such a young age as well."
    k "It felt like I had everything I wanted in my life, but I always felt like I was missing something."
    k "Though, I could never pinpoint what I was missing until I had it."
    k smiling "Seeing you on Kinsta brought a feeling I’d never encountered before and hasn’t been replicated since."
    k laughing "I can still feel the adrenaline rush sometimes. Not even the rival magazines’ drama has made me feel so on edge."
    r neutral "The emotion sounds similar to what I felt that day..."
    r "Despite the weather being cold and harsh that night, your follow made me forget all about it. It truly brought me such great warmth."
    "Kuma held my hands, holding my gloves with care. Her eyes looked into me deeply."
    k neutral "Just to be clear..."
    k "I love being in your presence, Reina." 
    k talking "I’d trade years of my lifespan if it meant I could spend a minute with you. This life means nothing if I can’t spend the rest of it with you."
    show reina talking
    "I couldn’t do much except blush and look away, unable to withstand her stare."
    "A whole lifespan? She can't be serious."
    r laughing "Honestly you... you got so confident all of a sudden..."
    show kuma smiling 
    "Her once serious expression transformed into her usual smile. Still holding hands, we stepped out of the store with our fastening hearts."

    scene bg harajuku with medium_dissolve:
        zoom 0.375
    play music "audio/apt-ost.mp3" fadein 1.5

    jump harajukuoptions
    # note to self: change this to harajuku options
