import os
import signal
import sys
import time

def signal_n_times(pid, sig, n=1):
    for i in range(n):
        os.kill(pid, sig)
        time.sleep(0.25)


def round(pid, signals, n):
    for i in range(len(signals)):
        signal_n_times(pid, signals[i], n[i])
    os.kill(pid, signal.SIGINT)
    time.sleep(0.5)

def offset(prev, curr):
    new = []
    for i in range(len(prev)):
        new.append((curr[i] - prev[i]) % 9)
    # print new
    return new


if __name__ == '__main__':
    pid = int(sys.argv[1])
    signals = [signal.SIGQUIT,
               signal.SIGABRT,
               signal.SIGTRAP,
               signal.SIGTSTP,
               signal.SIGCONT,
               signal.SIGUSR1,
               signal.SIGUSR2]
    start = [1, 1, 1, 1, 1, 1, 1]
    # Round 1
    n1 = [3, 5, 1, 4, 3, 1, 2]
    round(pid, signals, offset(start, n1))
    # Round 2
    n2 = [6, 3, 1, 3, 2, 2, 5]
    round(pid, signals, offset(n1, n2))
    # Round 3
    n3 = [1, 3, 3, 6, 4, 7, 9]
    round(pid, signals, offset(n2, n3))
    # Round 4
    n4 = [8, 2, 6, 1, 7, 3, 1]
    round(pid, signals, offset(n3, n4))
    time.sleep(1.5)
    # Round 5
    n5 = [2, 4, 7, 7, 3, 6, 9]
    round(pid, signals, offset(n4, n5))
