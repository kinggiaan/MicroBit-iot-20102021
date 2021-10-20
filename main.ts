input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString(".")
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendString("done")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    if (receivedString == ".") {
        basic.showLeds(`
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        `)
        basic.pause(500)
        basic.clearScreen()
    } else if (receivedString == "/") {
        basic.showLeds(`
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        `)
        basic.pause(500)
        basic.clearScreen()
    } else {
        basic.showIcon(IconNames.Yes)
        basic.pause(500)
        basic.clearScreen()
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("/")
})
radio.setGroup(1)
basic.showString("MORSE")
basic.showIcon(IconNames.Heart)
basic.forever(function on_forever() {
    
})
