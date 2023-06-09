at = input('Enter arrival times i.e 0 1 2 3 :')
arrival_time = [int(x) for x in at.split(' ')]
bt = input('Enter burst times i.e 3 5 6 :')
burst_times = [int(x) for x in bt.split(' ')]

times = list(zip(arrival_time,burst_times))
sorted_times = sorted(times,key=lambda x : x[1])


turnaround_time = []
waiting_time = []
start = []
finish = []
for i,(a,b) in enumerate(sorted_times):
    if i == 0:
        start.append(a)
        wt = start[i] - a
        waiting_time.append(wt)
        f = start[i] + b
        finish.append(f)
        tat = finish[i] - a
        turnaround_time.append(tat)
    else:
        start.append(finish[i-1])
        wt = start[i] - a
        waiting_time.append(wt)
        f = start[i] + b
        finish.append(f)
        tat = finish[i] - a
        turnaround_time.append(tat)

print('Start time :',start)
print('Finish time :',finish)
print('Turnarounds : ',turnaround_time)
print('Waiting : ',waiting_time)
print('Avg  turnaround : ',sum(turnaround_time) / len(arrival_time))
print('Avg waiting : ',sum(waiting_time)  / len(arrival_time))

