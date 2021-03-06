import time
import board
import busio
import digitalio
import binascii

pin = digitalio.DigitalInOut(board.GP19)
pin.direction = digitalio.Direction.OUTPUT

uart = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=19200)
data = [2, 0x10, 0x20]

pin.value = False
time.sleep(5.0)
pin.value = True

uart.write(bytes(data))
time.sleep(10)
uart.write(bytes(data))
print("Done")
