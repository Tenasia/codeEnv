import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()


analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:13:o')

while True:
    analog_value = analog_input.read()

    if analog_value != None:
        delay = analog_value + 0.01
        led.write(1)
        time.sleep(delay)
        led.write(0)
        time.sleep(delay)
    else:
        time.sleep(0.1)