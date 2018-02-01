from machine import UART

uart = UART(0, 115200)                         
uart.init(115200, bits=8, parity=None, stop=1) 

# RED Unlimited
red_unlimited = "\xBB\x00\x36\x00\x05\x02\x00\x00\x00\x00\x7E\x22\x0D"
uart.write(red_unlimited)  # write 1 character

while True: 
    print(uart.read())