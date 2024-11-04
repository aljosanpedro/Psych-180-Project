# SET-UP

# Disable help keys (i.e. Esc)
define _game_menu_screen = None

# Image Transforms
transform char:
    zoom 0.7
    offset (-180,20)
transform bg_nora_old:
    zoom 0.7
transform bg_nora_new:
    zoom 0.6
transform bg_senpai:
    zoom 1.1
transform bg_resto_evening:
    zoom 0.4
transform bg_resto_cafe:
    zoom 0.9

# Characters
# Mascot
define simmer_color = "#CD5F2A"
define kulo = Character("Kulo", color=simmer_color)
# Boys
define geo = Character("Geo", color="#609AD2")
define pao = Character("Pao", color="#212630")
# Girls
define lily = Character("Lily", color="#61575A")
define bianca = Character("Bianca", color="#C3A393")

# Transitions
define swipe_speed = 0.2
define swipe_left = CropMove(swipe_speed, "slideawayleft")
define swipe_right = CropMove(swipe_speed, "slideawayright")
define entrance = Dissolve(0.5)
define q_fade = Dissolve(0.1)

# $ because was defined in gui.rpy
$ new_screen = PushMove(0.3, "pushup")
define scroll_up = PushMove(0.75, "pushup")

# Phone
define player_phone = Character("Aljo", color=simmer_color, kind=nvl, callback=Phone_ReceiveSound)
# Mascot
define kulo_phone = Character("Kulo", color="#CD5F2A", kind=nvl, callback=Phone_SendSound)
# Boys
define geo_phone = Character("Geo", color="#609AD2", kind=nvl, callback=Phone_SendSound)
define pao_phone = Character("Pao", color="#212630", kind=nvl, callback=Phone_SendSound)
# Girls
define lily_phone = Character("Lily", color="#61575A", kind=nvl, callback=Phone_SendSound)
define bianca_phone = Character("Bianca", color="#C3A393", kind=nvl, callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = None

# Global Vars
define story = ""

define gender = ""

define name = "Aljo"
define player = Character("[name]")

# Labels
label start:
    call tips.reset
    jump intro

# intro -> profile -> swipe -> chat -> date -> decide -> ending

label end:
    # DEAR FUTURE SELF:
    # WE ENDED ON CHAT.CHOOSE BEFORE CHOOSING A MATCH TO CHAT WITH!

    return
