
n = int(input())
data = [int(i) for i in input().split()]
m = int(input())

def max_window(data):
    useful = []
    max_list = []


    for i in range(0,m):

        while len(useful) > 0 and data[i] >=  data[useful[-1]]:
            useful.pop()
        useful.append(i)

    for i in range(m,n):
        max_list.append(data[useful[0]])

        while  len(useful) > 0 and  useful[0] <= i-m:
            useful.pop(0)

        while len(useful) > 0 and data[i] >= data[useful[-1]]:
            useful.pop()
        useful.append(i)
    max_list.append(data[useful[0]])
    print(*max_list)

max_window(data)

