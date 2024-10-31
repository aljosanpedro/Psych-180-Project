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
define kulo = Character("Kulo", color="#CD5F2A")
# Boys
define geo = Character("Geo", color="#609AD2")
define pao = Character("Pao", color="#212630")
# Girls
define lily = Character("Lily", color="#61575A")
define bianca = Character("Bianca", color="#C3A393")

# Inputs
define name = ""
define player = Character("[name]")

# Transitions
define swipe_speed = 0.2
define swipe_left = CropMove(swipe_speed, "slideawayleft")
define swipe_right = CropMove(swipe_speed, "slideawayright")

define scroll_speed = 0.75
define scroll_up = PushMove(scroll_speed, "pushup")

# Phone
define n_nvl = Character("Nighten", kind=nvl, image="nighten", callback=Phone_SendSound)
define e_nvl = Character("Eileen", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

# Labels
label start:
    jump intro

# intro -> profile -> swipe -> chat -> date -> decide -> ending

label end:
    return
