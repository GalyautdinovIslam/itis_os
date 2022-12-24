#!/usr/bin/python3
import os
import sys
import random


def fork():
    pid = os.fork()
    if pid != 0:
        print(f'Parent[{os.getpid()}]: I ran children process with PID {pid}.')
    else:
        random_str_number = str(random.randint(5, 10))
        os.execl('./child.py', './child.py', random_str_number)


def main():
    n = int(sys.argv[1])
    for c in range(n):
        fork()
    while n > 0:
        pid, status = os.wait()
        status = os.waitstatus_to_exitcode(status)
        if pid != 0:
            print(f'Parent[{os.getpid()}]: Child with PID {pid} terminated. Exit Status {status}.')
            if status == 0:
                n -= 1
            else:
                fork()
    os._exit(os.EX_OK)


if __name__ == '__main__':
    main()
