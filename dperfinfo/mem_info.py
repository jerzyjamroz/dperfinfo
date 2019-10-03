# Memory Info of a Linux machine.

from __future__ import print_function
from collections import OrderedDict


def meminfo_get():
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo


def meminfo_disp():
    # global meminfo
    meminfo = meminfo_get()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))


if __name__ == "__main__":
    meminfo_disp()
