from cpu_info import *
from mem_info import *
from platform_info import *
from timing_info import *


def sysinfo():
    dmessage(system='dump')
    cpuinfo_disp()
    meminfo_disp()
    platform_disp()


if __name__ == "__main__":
    dmessage(system='dump')
    cpuinfo_disp()
    meminfo_disp()
    platform_disp()
