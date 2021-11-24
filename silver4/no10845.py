import sys


def m_cmd(a, b=0):
    if a == 'push':
        queue.append(b)
    elif a == 'front':
        if queue:
            return queue[0]
        else:
            return -1
    elif a == 'back':
        if queue:
            return queue[-1]
        else:
            return -1
    elif a == 'size':
        return len(queue)
    elif a == 'pop':
        if queue:
            return queue.pop(0)
        else:
            return -1
    elif a == 'empty':
        if queue:
            return 0
        else:
            return 1


N = int(input())
queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        print(m_cmd(cmd[0]))
    else:
        if m_cmd(cmd[0], int(cmd[1])) is None:
            continue
        else:
            print(m_cmd(cmd[0], int(cmd[1])))
