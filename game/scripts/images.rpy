label images:

    label .setup:
        define main_menu_pause = (0.67 / 2)
        define main_menu_zoom = (1 / 2.5)
        define main_menu_left = "gui/main_menu/left.png"
        define main_menu_right = "gui/main_menu/right.png"

        define kulo_slow_pause = 0.5
        define kulo_mid_pause = 0.25
        define kulo_fast_pause = 0.1
        define kulo_left = "images/ui/app/anim/left.png"
        define kulo_right = "images/ui/app/anim/right.png"
    label .animations:
        image main_menu_anim:
            main_menu_left
            zoom(main_menu_zoom)
            pause main_menu_pause
            main_menu_right
            zoom(main_menu_zoom)
            pause main_menu_pause
            repeat


        image kulo_slow:
            kulo_left
            pause kulo_slow_pause
            kulo_right
            pause kulo_slow_pause
            repeat

        image kulo_mid:
            kulo_left
            pause kulo_mid_pause
            kulo_right
            pause kulo_mid_pause
            repeat

        image kulo_fast:
            kulo_left
            pause kulo_fast_pause
            kulo_right
            pause kulo_fast_pause
            repeat