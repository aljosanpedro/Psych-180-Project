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
define simon = Character("Simon", color="#CD5F2A")
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
define swipe_speed = 0.3

define swipe_left = CropMove(swipe_speed, "slideawayleft")
define swipe_right = CropMove(swipe_speed, "slideawayright")
define swipe_up = PushMove(0.3, "pushup")

define profile_swipe = swipe_up

# Labels
label start:
    jump intro

# intro -> profile -> swipe -> chat -> date -> decide -> ending

label end:
    return
