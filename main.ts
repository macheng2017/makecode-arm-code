let aAxis = 0
call_servo()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    aAxis += 10
    call_servo()
})
function call_servo() {
    robotbit.GeekServo2KG(robotbit.Servos.S1, aAxis * 4)
}

function show_led() {
    basic.showNumber(aAxis)
}

basic.forever(function on_forever() {
    show_led()
})
input.onButtonPressed(Button.B, function on_button_pressed_a2() {
    
    aAxis -= 10
    call_servo()
})
