#!/usr/bin/python3
import os
import random
import sys
import time


def main():
    random_number = int(sys.argv[1])
    print(f'Child[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
    time.sleep(random_number)
    print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')
    os._exit(random.randint(0, 1))


if __name__ == '__main__':
    main()
