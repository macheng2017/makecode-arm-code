aAxis = 0
call_servo()
def on_button_pressed_a():
    global aAxis
    aAxis +=10
    call_servo()
input.on_button_pressed(Button.A, on_button_pressed_a)
def call_servo():
    robotbit.geek_servo2_kg(robotbit.Servos.S1, aAxis*4)

def show_led():
    basic.show_number(aAxis)

def on_forever():
    show_led()
basic.forever(on_forever)

def on_button_pressed_a2():
    global aAxis
    aAxis -=10
    call_servo()

input.on_button_pressed(Button.B, on_button_pressed_a2)