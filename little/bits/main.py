import sys
from little.bits import log
from little.bits.configs import wake_me_device_id
from little.bits.http import do_post

__author__ = 'charlie'


def main(args):
    log.log("Processing %d arguments\n%s" % (len(args), str(args)))
    if "wake_me" in args:
        wake_me()


def wake_me():
    percent = "75"
    duration_ms = str(60 * 1000)
    do_post(device_id=wake_me_device_id, percent=percent, duration_ms=duration_ms)


if __name__ == "__main__":
    main(sys.argv)