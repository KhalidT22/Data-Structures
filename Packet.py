import sys
data = list(map(int, sys.stdin.read().split()))

def packet_process(data):
    S = data[0]
    n = data[1]
    buffer = []
    finish_times = []
    if len(data) <3:
        return
    end_time = data[2] +  data[3]
    cur_arrival_time = data[2]
    result_list = []
    for i in range(1,n+1):
        check = True

        if  len(buffer) < S:

            if i == 1:

                buffer.append(cur_arrival_time)
                finish_times.append(end_time)
            elif cur_arrival_time == data[2*i]:

                buffer.append(end_time)
                end_time = end_time + data[2*i+1]
                finish_times.append(end_time)
            elif end_time < data[2*i]:

                buffer.append(data[2*i])
                cur_arrival_time = data[2*i]
                end_time = data[2*i]  + data[2*i+1]
                finish_times.append(end_time)
            else:

                buffer.append(end_time)
                cur_arrival_time = data[2*i]
                end_time = end_time + data[2*i + 1]
                finish_times.append(end_time)


            result_list.append(buffer[-1])
        else:

                for packet in finish_times:
                    if packet <=  data[2*i]:

                        buffer.pop(0)
                        finish_times.pop(0)

                        if cur_arrival_time == data[2*i]:

                            buffer.append(end_time)
                            end_time = end_time + data[2*i + 1]
                            finish_times.append(end_time)

                        elif end_time < data[2*i]:

                            buffer.append(data[2*i])
                            cur_arrival_time = data[2*i]
                            end_time = data[2*i] + data[2*i + 1]
                            finish_times.append(end_time)
                        else:

                            buffer.append(end_time)
                            cur_arrival_time = data[2*i]
                            end_time = end_time + data[2*i + 1]
                            finish_times.append(end_time)

                        if check:

                            result_list.append(buffer[-1])
                            check = False
                        break

                if check :
                    result_list.append(-1)
        if i ==n:
            for j in range(0,len(result_list)):
                print(result_list[j])

packet_process(data)





