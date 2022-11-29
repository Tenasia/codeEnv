import pyfirmata
import time


board = pyfirmata.Arduino('COM4')

iterator = pyfirmata.util.Iterator(board)
iterator.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

while True:
    sw = digital_input.read()
    if sw == True:
        led.write(1)
    else:
        led.write(0)
    time.sleep(1)
    