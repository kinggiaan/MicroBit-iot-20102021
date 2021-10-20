def on_button_pressed_a():
    radio.send_string(".")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("done")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == ".":
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
    elif receivedString == "/":
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        basic.pause(500)
        basic.clear_screen()
    else:
        basic.show_icon(IconNames.YES)
        basic.pause(500)
        basic.clear_screen()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("/")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
basic.show_string("MORSE")
basic.show_icon(IconNames.HEART)

def on_forever():
    pass
basic.forever(on_forever)
