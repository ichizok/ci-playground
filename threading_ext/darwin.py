from ctypes import (
    CDLL,
    POINTER,
    Structure,
    c_int,
    c_uint,
    c_uint32,
    c_void_p,
    byref,
    sizeof
)
from ctypes.util import find_library


class ThreadTimeConstraintPolicy(Structure):
    _fields_ = [
        ("period", c_uint32),
        ("computation", c_uint32),
        ("constraint", c_uint32),
        ("preemptible", c_uint)
    ]


_libc = CDLL(find_library('c'))

THREAD_TIME_CONSTRAINT_POLICY = c_uint(2)

THREAD_TIME_CONSTRAINT_POLICY_COUNT = c_uint(
    int(sizeof(ThreadTimeConstraintPolicy) / sizeof(c_int)))

_libc.pthread_self.restype = c_void_p

_libc.pthread_mach_thread_np.restype = c_uint
_libc.pthread_mach_thread_np.argtypes = [c_void_p]

_libc.thread_policy_get.restype = c_int
_libc.thread_policy_get.argtypes = [
    c_uint,
    c_uint,
    c_void_p,
    POINTER(c_uint),
    POINTER(c_uint)
]

_libc.thread_policy_set.restype = c_int
_libc.thread_policy_set.argtypes = [
    c_uint,
    c_uint,
    c_void_p,
    c_uint
]


def _mach_thread_self():
    return _libc.pthread_mach_thread_np(_libc.pthread_self())


def get_time_constraint_policy(default=False):
    thread = _mach_thread_self()
    policy_info = ThreadTimeConstraintPolicy()
    policy_infoCnt = THREAD_TIME_CONSTRAINT_POLICY_COUNT
    get_default = c_uint(default)

    kret = _libc.thread_policy_get(
        thread,
        THREAD_TIME_CONSTRAINT_POLICY,
        byref(policy_info),
        byref(policy_infoCnt),
        byref(get_default))
    if kret != 0:
        return None
    return {
        'period': int(policy_info.period),
        'computation': int(policy_info.computation),
        'constraint': int(policy_info.constraint),
        'preemptible': bool(policy_info.preemptible),
    }


def set_time_constraint_policy(policy_info):
    thread = _mach_thread_self()
    policy_info = ThreadTimeConstraintPolicy(
        period=c_uint32(policy_info['period']),
        computation=c_uint32(policy_info['computation']),
        constraint=c_uint32(policy_info['constraint']),
        preemptible=c_uint(policy_info['preemptible']),
    )
    policy_infoCnt = THREAD_TIME_CONSTRAINT_POLICY_COUNT

    kret = _libc.thread_policy_set(
        thread,
        THREAD_TIME_CONSTRAINT_POLICY,
        byref(policy_info),
        policy_infoCnt)
    if kret != 0:
        raise OSError(kret)
