def on_forever():
    basic.show_leds("""
        # . . . .
                # . . . .
                # . . . .
                # . . . .
                # . . . .
    """)
    basic.show_leds("""
        # . # . .
                # . # . .
                # . # . .
                # . # . .
                # . # . .
    """)
    basic.show_leds("""
        # . # . #
                # . # . #
                # . # . #
                # . # . #
                # . # . #
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                # # # # #
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                # # # # #
                . . . . .
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . . . .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # . # .
                . . . . .
    """)
    basic.show_leds("""
        # . . . #
                . # . # .
                . . . . .
                . # . # .
                # . . . #
    """)
    basic.show_leds("""
        # # . # #
                # . . . #
                . . . . .
                # . . . #
                # # . # #
    """)
    basic.show_leds("""
        # # . # #
                # . . . #
                . . # . .
                # . . . #
                # # . # #
    """)
    basic.show_leds("""
        # # . # #
                # . # . #
                . # # # .
                # . # . #
                # # . # #
    """)
    basic.show_leds("""
        . . . . .
                . . # . .
                . # # # .
                . . # . .
                . . . . .
    """)
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
