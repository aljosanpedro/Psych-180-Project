# Main Menu
define main_menu_pause = 0.5
image main_menu_animated:
    "gui/title/left.png"
    pause main_menu_pause
    "gui/title/right.png"
    pause main_menu_pause
    repeat

# Simon
define simon_slow_pause = 0.5
image simon_slow:
    "images/ui/simon/big/left.png"
    pause simon_slow_pause
    "images/ui/simon/big/right.png"
    pause simon_slow_pause
    repeat

define simon_mid_pause = 0.25
image simon_mid:
    "images/ui/simon/big/left.png"
    pause simon_mid_pause
    "images/ui/simon/big/right.png"
    pause simon_mid_pause
    repeat

define simon_fast_pause = 0.1
image simon_fast:
    "images/ui/simon/big/left.png"
    pause simon_fast_pause
    "images/ui/simon/big/right.png"
    pause simon_fast_pause
    repeat
