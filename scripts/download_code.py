import os
import subprocess
import sys
from utils import *


def main():
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".py"): 
            download = ['ampy','--port', serial_ports()[0], 'put',os.path.join(sys.argv[1], filename)]
            print(download)
            process = subprocess.Popen(download, shell=True, stdout=subprocess.PIPE)
            process.wait()

    print('Done!')

if __name__ == '__main__':main()