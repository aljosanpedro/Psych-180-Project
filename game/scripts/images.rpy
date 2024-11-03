# Main Menu
define main_menu_pause = 0.67 / 2

image main_menu_anim:
    "gui/title/kulo/left.png"
    pause main_menu_pause
    "gui/title/kulo/right.png"
    pause main_menu_pause
    repeat

# App
define slow_pause = 0.5
define mid_pause = 0.25
define fast_pause = 0.1

image kulo_slow:
    "images/ui/mascot/kulo/left.png"
    pause slow_pause
    "images/ui/mascot/kulo/right.png"
    pause slow_pause
    repeat

image kulo_mid:
    "images/ui/mascot/kulo/left.png"
    pause mid_pause
    "images/ui/mascot/kulo/right.png"
    pause mid_pause
    repeat

image kulo_fast:
    "images/ui/mascot/kulo/left.png"
    pause fast_pause
    "images/ui/mascot/kulo/right.png"
    pause fast_pause
    repeat
