def on_button_pressed_a():
    global mode
    mode += 1
    if mode > 5:
        mode = 5
    basic.show_string("" + (wordlist[mode]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mode
    mode += -1
    if mode < 0:
        mode = 0
    basic.show_string("" + (wordlist[mode]))
input.on_button_pressed(Button.B, on_button_pressed_b)

connected = 0
mode = 0
wordlist: List[str] = []
wordlist = ["esc", "rick", "anorick", "again", "hh", "4xuan"]
pinlist = [0, 1, 2, 3, 4, 5]
mode = 0
pins.analog_write_pin(AnalogPin.P0, 787)
if pins.analog_read_pin(AnalogPin.P0) == 787:
    connected = 1
    basic.show_string("ok")
else:
    basic.show_string("failed")
