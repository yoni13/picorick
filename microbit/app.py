def on_button_pressed_a():
    global mode
    mode += 1
    if mode > 5:
        mode = 5
    basic.show_string("" + (wordlist[mode]))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if pinlist[mode] == 1:
        pins.analog_write_pin(AnalogPin.P0, 1000)
        pins.analog_write_pin(AnalogPin.P1, 1000)
        pins.analog_write_pin(AnalogPin.P2, 1)
    if pinlist[mode] == 2:
        pins.analog_write_pin(AnalogPin.P0, 1000)
        pins.analog_write_pin(AnalogPin.P1, 1)
        pins.analog_write_pin(AnalogPin.P2, 1000)
    if pinlist[mode] == 3:
        pins.analog_write_pin(AnalogPin.P0, 1)
        pins.analog_write_pin(AnalogPin.P1, 1000)
        pins.analog_write_pin(AnalogPin.P2, 1000)
    if pinlist[mode] == 4:
        pins.analog_write_pin(AnalogPin.P0, 1)
        pins.analog_write_pin(AnalogPin.P1, 1)
        pins.analog_write_pin(AnalogPin.P2, 1000)
    if pinlist[mode] == 5:
        pins.analog_write_pin(AnalogPin.P0, 1)
        pins.analog_write_pin(AnalogPin.P1, 1)
        pins.analog_write_pin(AnalogPin.P2, 1)
    if pinlist[mode] == 6:
        pins.analog_write_pin(AnalogPin.P0, 1000)
        pins.analog_write_pin(AnalogPin.P1, 1)
        pins.analog_write_pin(AnalogPin.P2, 1)
    basic.show_string("writed" + ("" + str(pinlist[mode])))
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P0, 1000)
    pins.analog_write_pin(AnalogPin.P1, 1000)
    pins.analog_write_pin(AnalogPin.P2, 1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global mode
    mode += -1
    if mode < 0:
        mode = 0
    basic.show_string("" + (wordlist[mode]))
input.on_button_pressed(Button.B, on_button_pressed_b)

mode = 0
pinlist: List[number] = []
wordlist: List[str] = []
wordlist = ["esc", "rick", "anorick", "again", "hh", "4xuan"]
pinlist = [1, 2, 3, 4, 5, 6]
mode = 0
