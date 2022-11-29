import pyfirmata
import time

board = pyfirmata.Arduino('COM4')

iterator = pyfirmata.util.Iterator(board)
iterator.start()

board.digital[10].mode = pyfirmata.INPUT

timer = 0

while timer < 10:
    sw = board.digital[10].read()

    if sw == True:
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)
    
    
    time.sleep(1.0)
    timer += 1

print(timer)


