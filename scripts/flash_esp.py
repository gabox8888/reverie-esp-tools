from utils import *
import subprocess
import sys

def main():
    erase = ['esptool','--port', serial_ports()[0], 'erase_flash']
    flash = ['esptool','--port', serial_ports()[0], '--baud', '115200', 'write_flash', '--flash_size=detect', '0',sys.argv[1]]
    process = subprocess.Popen(erase, shell=True, stdout=subprocess.PIPE)
    process.wait()
    process = subprocess.Popen(flash, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)

if __name__ == '__main__':main()
