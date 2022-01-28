import time
import timeit
import sys


def set_rt():
    import platform
    if platform.system() == 'Darwin':
        from threading_ext import darwin
        policy_info = darwin.get_time_constraint_policy()
        policy_info['preemptible'] = False
        darwin.set_time_constraint_policy(policy_info)


def sleep(ms):
    n = int(1000 / ms)
    ms /= 1000
    for _ in range(n):
        time.sleep(ms)


def tt(ms, n):
    t = timeit.timeit(lambda: sleep(ms), timer=time.perf_counter_ns, number=n)
    s = t / (n * 10**9)
    print('{}x sleep {}ms'.format(int(1000 / ms), ms))
    print('  Elapsed = {}'.format(s))
    print('  Unit    = {}'.format(s / int(1000 / ms)))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'rt':
        set_rt()

    loop = 3
    tt(1, loop)
    tt(10, loop)
    tt(50, loop)
    tt(100, loop)
    tt(1000, loop)
