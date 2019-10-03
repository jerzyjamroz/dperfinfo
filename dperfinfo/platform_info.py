###### Platform info and distribution of a Linux machine.
import platform
import sys


def platform_disp():
    print(platform.uname())
    print(platform.linux_distribution())
    print('python ' + str(sys.version_info))
    print('\n'.join(sys.path))

if __name__ == "__main__":
    platform_disp()