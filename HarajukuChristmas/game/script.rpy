# The script of the game goes in this file.

# voice bleeps
init python:
    def reina_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/reina.wav", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def kuma_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/kuma.wav", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

    def santa_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show":
            renpy.sound.play("audio/santa.wav", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Reina", image = "reina", cb_name="reina", color="#ffffff", style="reina_text", callback = CallbackList(reina_sound, name_callback))
define k = Character("Kuma", image = "kuma", cb_name="kuma", color="#ffffff", style="kuma_text", callback = CallbackList(kuma_sound, name_callback))

# npc characters

define v = Character("Santa", image = "santa", cb_name = "santa", color="#ffffff", style="santa_text", callback = CallbackList(santa_sound, name_callback))
define c = Character("Clerk", color="#ffffff", style="santa_text", callback = name_callback)


# nvl characters
define r_nvl = Character("Reina", kind = nvl, image = "reina", callback = Phone_SendSound)
define k_nvl = Character("kuma~ :33", kind = nvl, callback = Phone_ReceiveSound)

# Sprite groups 
layeredimage reina1:
    #at sprite_highlight('reina')
    group emotion:
        attribute neutral default:
            "reina_neutral.png"
        attribute talking:
            "reina_talking.png"
        attribute smiling:
            "reina_smiling.png"
        attribute shocked:
            "reina_shocked.png"
        attribute laughing:
            "reina_laughing.png"

layeredimage kuma1:
    #at sprite_highlight('kuma')
    group emotion:
        attribute neutral default:
            "kuma_neutral.png"
        attribute talking:
            "kuma_talking.png"
        attribute smiling:
            "kuma_smiling.png"
        attribute shocked:
            "kuma_shocked.png"
        attribute laughing:
            "kuma_laughing.png"

image reina = LayeredImageProxy("reina1", transform=sprite_highlight("r"))
image kuma = LayeredImageProxy("kuma1", transform=sprite_highlight("k"))

# defaults 
default preferences.text_cps = 40
define slow_dissolve = Dissolve(1.0)
define medium_dissolve = Dissolve(0.7)
#define sprite_dissolve = Dissolve(0.3)
define config.nvl_list_length = None
#define config.say_attribute_transition = sprite_dissolve
default preferences.fullscreen = False
default preferences.skip_unseen = False

# transforms 
transform right:
    xalign 0.9
    yalign 0.1

transform left:
    xalign 0.1
    yalign 0.1

transform center:
    xalign 0.5
    yalign 0.1

#i was on something with these yaligns
transform Rlower:
    xalign 0.95
    yalign -0.8

transform Llower:
    xalign 0.05
    yalign -0.8

# images
image white = "#fff"
image pink = "#ffd9d9"

# outline text
style reina_text:
    outlines [(4, "#FFB1A3", 0, 0)]

style kuma_text:
    outlines [(4, "#fca67e", 0, 0)]

style santa_text:
    outlines [(4, "#b52a2a", 0, 0)]

label splashscreen:
    scene white
    play sound "audio/splash.wav"
    scene bg splash with dissolve
    with Pause(1)
    $ renpy.pause()

    scene white with slow_dissolve

    show text "{size=40}{color=#CC5E5E}Made for the Winter Visual Novel Jam 2025.{/size}{/color}"
    with slow_dissolve
    $ renpy.pause()
    hide text with dissolve
    with Pause(1)

    return

########### GAME START ########
label start:

    scene pink with dissolve
    play music "audio/apt-ost.mp3" fadein 2.5
    r "Hmm hmmm~"
    r "Just gotta get it over here.."

    scene bg apartment with slow_dissolve:
        zoom 0.375
    show reina neutral at center with dissolve:
        zoom 0.2
    "I flick the mascara up a little more, making sure it curls up just the way I want it to."
    "Today’s the big day! {w}I’m gonna spend a nice Christmas date with my girlfriend."

    r talking "Hehe… Kuma is gonna love this one…"

    # phone notification sound effect here

    r laughing "AAHHHH!!!!!!!!"
    r "KUMAAAA!!!!!!!"

    show reina laughing at right with easeinright
    # texting portion (put proper texting conventions for coders)

    k_nvl "haiiii ^_^"
    nvl_narrator "kuma~ :33 poked you."
    k_nvl "hiiii reinaaa"
    k_nvl "u preparing for the date?"
    nvl_narrator "You poked kuma~ :33."
    r_nvl neutral "Ya :3"
    r_nvl "You also ready?"
    r_nvl smiling "I can’t wait to see you :33"
    k_nvl "ummm"
    k_nvl "im already here"
    k_nvl "(^_^;)"
    r_nvl shocked "WHAT"
    r_nvl "I’m almost done!"
    r_nvl smiling "I’ll be there"
    r_nvl ":)) !!!"
    k_nvl "cyaaa"
    k_nvl ">_<"

    # texting portion ends
    show reina neutral:
        ease 0.5 xalign 0.5

    r "Whew…"
    r laughing "She’s 30 minutes early to a date?? That’s not like her!"
    r talking "I’ve got to get my game on!"
    "I swiftly add the finishing touches to my makeup and put on my cute bow heels."
    r neutral "..."
    r smiling "I’ve got to add a photo for Kinsta!"

    # photo snapping sound effects
    "(snaps some photos)"
    r neutral "Let’s go!"

    #replace the line below with harajuku music later
    scene bg harajuku with slow_dissolve:
        zoom 0.375
    
    "The streets of Harajuku are filled with people in every corner. There’s some festive jazzy music among the constant chatter."

    show reina neutral at right with easeinright:
        zoom 0.2
    r "Kuma said to meet at this corner.."
    show kuma neutral at left with easeinleft:
        zoom 0.2
    k "Reinaaa?"
    r smiling "Ah!"
    # sound effect of hugging and cg should be here

    window hide
    scene cg hug with slow_dissolve
    pause

    r "KUUUMMAAA!!!"
    k "Ghk…!"

    # panning transition for hug
    window auto hide
    show cg hug with slow_dissolve:
        subpixel True ypos 1.23 zoom 1.32 
        xpos 0.46 
        linear 3.35 xpos 0.63 
    with Pause(3.45)
    show cg hug with slow_dissolve:
        pos (0.63, 1.23) 
    window auto show


    "I hugged her tight. It feels like I’m holding a cloud since we’re both wearing fluffy jackets."
    k "You’re squeezing me!"
    r "Huhu~"

    scene bg harajuku with slow_dissolve:
        zoom 0.375
    show reina talking at right:
        zoom 0.2
    show kuma neutral at left:
        zoom 0.2

    r "Oooo… I didn’t think that gyarus could have winter wear too. The leopard print coat looks soo cute on you!"
    r laughing "Cute and gyaru as ever!"
    k smiling "Wahhh… thank ya, thank ya."
    k talking "Your coord is so cute too~"
    k neutral "Hopefully it ain’t too much trouble to get a Christmas print JSK?"
    r shocked "I stayed up at 12 am bidding with this other lolita online to get it…"
    r "Since it’s in season and all!"
    k shocked "Yikes…"
    k smiling "It looks like ya would’ve been cuter in it anyway."
    r smiling "You’re such a flirt…"
    r laughing "OKAY!!!"
    r laughing "LETS GO!!!"
    k laughing "Yeah!"

    hide reina with dissolve
    hide kuma with dissolve

    jump harajukuoptions
