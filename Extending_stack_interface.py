import sys


def extend_stack(n):
    stack = []
    maxvals = []

    for i in range(n):
        data = sys.stdin.readline().split()

        if data[0] == "push":
            val = int(data[1])
            stack.append(val)
            if len(maxvals) == 0 or maxvals[len(maxvals)-1] <= val:
                maxvals.append(val)
        elif data[0] == "pop":
           val = stack.pop()
           if val == maxvals[len(maxvals) -1]:
               maxvals.pop()
        else:
            print(maxvals[len(maxvals)-1])

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    extend_stack(n)