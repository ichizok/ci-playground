#!/usr/bin/env python3
import os
from subprocess import Popen, PIPE
from fcntl import fcntl, F_GETFL, F_SETFL
from itertools import count

def set_nonblock(fd):
    flags = fcntl(fd, F_GETFL)
    flags |= os.O_NONBLOCK
    fcntl(fd, F_SETFL, flags)

p = Popen(['sleep', '30'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
fd = p.stdin.fileno()

set_nonblock(fd)

for i in count():
    try:
        os.write(fd, b'a')
    except BlockingIOError:
        i -= 1
        p.kill()
        break

print("pipe write blocked after {} bytes ({} KiB)".format(i, i//1024))
