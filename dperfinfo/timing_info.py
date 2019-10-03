from functools import wraps
from time import time
import datetime


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        # print 'func:%r args:[%r, %r] took: %2.6f sec' % (f.__name__, args, kw, te-ts)
        print '%r %2.9f s' % (f.__name__, te-ts)
        return result
    return wrap


def dmessage(**kwargs):
    # st = inspect.stack()[1]
    # print '%s:%d %s()' % (st[1], st[2], st[3])
    # for k, v in kwargs.items():
    #    print '%s: %s' % (k, v)
    print datetime.datetime.now().isoformat() + " " + str(kwargs.items())


def demo():
    dmessage(testattr="SSSSSSSS")


if __name__ == '__main__':
    demo()
