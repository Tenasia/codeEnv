import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led = board.get_pin('d:11:p')

while True:
    analog_value = analog_input.read()
    if analog_value != None:
        led.write(analog_value)
    time.sleep(0.1)