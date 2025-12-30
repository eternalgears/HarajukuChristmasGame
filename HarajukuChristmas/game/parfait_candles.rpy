label parfait_candles:
    scene bg parfaitcandles with slow_dissolve:
        zoom 0.375
    play music "audio/parfaitcandles.mp3" fadein 0.5
    window hide
    $ renpy.pause(1.9)
    #making parfait candles has a cg and several transitions per "parfait making" steps
    $ Parfait = True
    "*ring ring*"
    show reina neutral at right with slow_dissolve:
        zoom 0.2
    show kuma neutral at left with slow_dissolve:
        zoom 0.2
    k talking "Ooouh..."
    k smiling "Is this a dessert making place?"
    r smiling "Kind of!"
    r "I saw this once in a Moi-même-Moitié video where Mana-sama and Aoki Misako made parfait candles!"
    k neutral "Huh? Whozzat again?"
    # reina thinking sprite
    r talking "Mana-sama is that one pretty doll from Malice Mizer...."
    k talking "The real beautiful one with the blue hair and curls?"
    r laughing "Yeah!"
    r smiling "And Aoki is a pretty popular lolita model! Most well known and influential lolita if you ask me."
    r "Ahhhh... I aspire to be like them someday..."
    k smiling "I gotcha! That’s why we gotta get ultra famous from our influencing life."
    r shocked "But they’re like! World-wide famous!"
    k neutral "I dunno if those would count as world-wide."
    r smiling "Everyone knows lolita fashion because of them..."
    r laughing "Even the people overseas!"
    k "Huh..."
    k talking "I always wondered how people overseas knew about lolita fashion..."
    k "I was scrolling Kinsta the other day and saw an American with Yamanba makeup."
    r talking "Woahhh... the influencer pressure is getting close to me!"
    k smiling "Right? Maybe we are a part of spreading the culture."
    r smiling "That’s.. so..."
    r laughing "COOOL!!!"
    "Suddenly, everyone stares at us. We definitely disturbed their candle making peace."
    k talking "We should probably get started on those candles."
    r neutral "I’m down!"

    # parfait candles clerk: c

    c "Welcome in! How many people?"
    r "Two please!"
    c "Right this way."

    # transition pink fade in then fade out
    scene pink with slow_dissolve
    $ renpy.pause(1.0)
    scene bg parfaitcandles with slow_dissolve:
        zoom 0.375
    show reina neutral at Rlower with slow_dissolve:
        zoom 0.2
    show kuma neutral at Llower with slow_dissolve:
        zoom 0.2
    # drag and drop mechanic here?

    "{i}Step one: choose the jelly cube like gel wax.{/i}"

    "I stare long and hard at the various gel wax colors to choose from."
    r talking "Which jelly cubes...."
    k smiling "I got the blue and purple ones with gel wax."
    r laughing "Then I’ll take the pink and orange ones!"
    # kuma smiling sprite
    k "Those colors kinda remind me of our outfits."

    window hide
    scene cg parfaitcandles with slow_dissolve
    pause
    "{i}Step two: dip the gel wax in glitter and place them in the glass.{/i}"

    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.7, 0.88) zoom 2.03
    "I carefully dip the jelly cubes into the glitter. The cubes absorb the glitter with its stickiness."
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.38, 0.7) zoom 1.63 
    k "Oh my god... my nails got a bit of glitter on them..."
    r "Are you okay??"
    k "Ya of course, of course! Don’t worry bout’ them."
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.5, 0.6) zoom 1.74 
    r "You sure? Those nails must’ve cost a lot..."
    k "It’s okay! Really."

    scene bg parfaitcandles with slow_dissolve:
        zoom 0.375
    show reina neutral at Rlower with dissolve:
        zoom 0.2
    show kuma neutral at Llower with dissolve:
        zoom 0.2
    "{i}Step three: add melted wax to the glass.{/i}"

    "The melted wax, which was provided to us by the staff just now, is in a creamer dispenser."
    "I hold the creamer in both of my hands and pour the wax gently into the glass, watching the liquid float down slowly."
    r smiling "It’s like syrup.."
    k talking "I really want parfaits now."
    r laughing "I get what you mean!"
    k neutral "Can we get parfaits after this...?"
    r neutral "Yeah!!"

    scene cg parfaitcandles with slow_dissolve
    "{i}Step four: Add your color of choice to the wax.{/i}"

    "The staff hurriedly came over and provided us with dried wax and some color dye."
    show cg parfaitcandles with medium_dissolve:
        subpixel True pos (0.4, 1.04) zoom 1.69 
    "I pick out the pink color dye, while Kuma gets the blue color dye."
    "Now we just have to mix the dye and the dry wax."
    "Swirl swirl swirl...."
    k "This is surprisingly really fun."
    k "Have ya done this before?"
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.5, 0.6) zoom 1.74 
    r "Nope!"
    r "I’m glad the first time I get to make them is with you!"

    scene cg parfaitcandles with slow_dissolve
    "{i}Step five: Create the ice cream scoop.{/i}"

    show cg parfaitcandles with medium_dissolve:
        subpixel True pos (0.4, 1.04) zoom 1.69 
    "With the dried wax now colored, we have to get it out of the cup (that we just mixed the color in with) and put it in the scooper."
    "I use a popsicle stick and scrape the wax out with it."
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.38, 0.7) zoom 1.63 
    "Kuma looks like she’s having a hard time getting the wax out of the cup.."
    r "Is the cup hard to grasp?"
    k "Hot hot hot!!"
    r "K-kuma?? Did you get burnt??"
    k "Haah..."
    scene cg parfaitcandles with slow_dissolve
    "I don’t see any visible burn marks on Kuma, thankfully."
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.38, 0.7) zoom 1.63 
    k "Can ya help me with this?~"
    r "Right away!"
    scene cg parfaitcandles with slow_dissolve
    "I reach over and use her popsicle stick to get the wax out of the cup. This wax seems a bit harder than mine."
    "I put the wax into the scooper, molding it into an ice cream shape scoop."
    r "It’s kind of difficult to get the wax into the scooper."
    k "You get me..."

    scene bg parfaitcandles with slow_dissolve:
        zoom 0.375
    show reina neutral at Rlower with dissolve:
        zoom 0.2
    show kuma neutral at Llower with dissolve:
        zoom 0.2
    "{i}Step six: Put the ice cream scoops on top.{/i}"

    "Now that we have our wax ice cream scoops, it’s time to put them into the parfait glass!"
    "Kuma rotates the parfait glass, seemingly proud of her creation."
    k talking "I’m seeing the vision..."
    r laughing "Right? Right?"
    k neutral "I wouldn’t want to use this as a real candle."
    r smiling "Let’s save it then! As a souvenir for today’s Christmas date!" 

    scene cg parfaitcandles with slow_dissolve
    "{i}Step seven: Place the whipped cream and sprinkles.{/i}"

    "{i}Note: it is not actually edible whipped cream and sprinkles. Just decorations for the candle!{/i}"
    show cg parfaitcandles with medium_dissolve:
        subpixel True pos (0.4, 1.04) zoom 1.69 
    "We swirl (again) around the whipped cream on the sides of the parfait glass and top it off with the sprinkles."
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.38, 0.7) zoom 1.63 
    k "Woahh.. this made me realize that I’ve never really baked anything."
    r "I can teach you!"
    k "Oh really? Thank ya Reina!"
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.5, 0.6) zoom 1.74 
    r "You’d have to take your nails off for that though..."
    k "Yikes... well if it’s for you then I could."

    scene cg parfaitcandles with slow_dissolve
    "{i}Step eight: Add toppings.{/i}"
    show cg parfaitcandles with medium_dissolve:
        subpixel True anchor (0.7, 0.88) zoom 2.03 
    "There’s so many toppings to choose from! From stars, hearts, smileys..."
    scene cg parfaitcandles with slow_dissolve
    k "I got these cute heart ones!"
    r "Me too! ^_^"
    r "Kuma! Get the cherries too!"
    k "Roger that."
    # transition black fade in fade out
    scene pink with slow_dissolve
    scene bg parfaitcandles with slow_dissolve:
        zoom 0.375
    show reina neutral at right with dissolve:
        zoom 0.2
    show kuma neutral at left with dissolve:
        zoom 0.2
    r laughing "It’s done!!"
    "My parfait has pink liquid wax, with a purple scoop! There’s bows, hearts, and bells to show that it’s a one of a kind Christmas parfait."
    k smiling "Cute, cute as always Reina."
    r smiling "^_^"
    r neutral "And let me see yours..."

    # kumas messy ugly parfait candle here
    "A messed up blue parfait candle with mismatched ornaments.. It looks gloomy compared to the one that I made."

    r laughing "Oh my gosh!!"
    r "It’s so so cute!!"

    # writers note: blind leading the blind

    k laughing "Thank ya, thank ya."
    k talking "I was thinking about Mana-sama while making this. Y’know with the blue and purple."
    r smiling "Huhu~"
    r talking "You got an eye for style..."
    "I snap some photos of our finished parfait candles. So cute!"
    k neutral "Parfaits now? Pleeease."
    r laughing "Alright, alright!"

    play music "audio/apt-ost.mp3" fadein 1.5
    scene bg harajuku with slow_dissolve:
        zoom 0.375
    show reina neutral at right with slow_dissolve:
        zoom 0.2
    show kuma neutral at left with slow_dissolve:
        zoom 0.2

    k "Oh my god... that triple strawberry sundae parfait was so good.."
    r "I’m stuffed..."
    k talking "You got the mini parfait though?"
    r talking "Yeah but there was a lot on it!"
    r neutral "It had twice the amount of strawberries and chocolate that yours had!"
    k "Yeah, yeah... and half the calories of mine apparently."
    r laughing "We could’ve shared!"
    k smiling "You have a point..."
    k "Where to next, Reina?"

    hide reina with dissolve
    hide kuma with dissolve

    jump harajukuoptions