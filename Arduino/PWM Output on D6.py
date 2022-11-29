import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
lenPin = board.get_pin('d:6:p')

print('Starting to output PWM Signal')
while True:
    for i in range(0, 101, 4):
        lenPin.write(i/100)
        time.sleep(0.05)
    time.sleep(1)
    for i in range(100, -1, -4):
        lenPin.write(i/100)
        time.sleep(0.05)
    time.sleep(1)