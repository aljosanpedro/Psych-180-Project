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
define blank = Character("Simmer", color=simmer_color)
define kulo = Character("Kulo", color=simmer_color)
define kali = Character("Kali", color=simmer_color)
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

$ new_screen = PushMove(0.3, "pushup")
define scroll_up = PushMove(0.75, "pushup")

# Phone
# Mascot
define kulo_phone = Character("Kulo", color="#CD5F2A", kind=nvl, callback=Phone_SendSound)
# Boys
define geo_phone = Character("Geo", color="#609AD2", kind=nvl, callback=Phone_SendSound)
define pao_phone = Character("Pao", color="#212630", kind=nvl, callback=Phone_SendSound)
# Girls
define lily_phone = Character("Lily", color="#61575A", kind=nvl, callback=Phone_SendSound)
define bianca_phone = Character("Bianca", color="#C3A393", kind=nvl, callback=Phone_SendSound)

define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_SendSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# Global Vars
define story = ""

define gender = ""
define mascot = blank

define name = ""
define player = Character("[name]")

# Labels
label start:
    call tips.reset
    jump intro

# intro -> profile -> swipe -> chat -> date -> decide -> ending

label end:
    return
