from machine import UART

uart = UART(0, 115200)                         
uart.init(115200, bits=8, parity=None, stop=1) 

# RED Unlimited
red_unlimited = bytearray('\xBB\x00\x03\x00\x01\x01\x7E\x7B\x9A')
uart.write(red_unlimited)  # write 1 character

while True: 
    print(uart.read())