at = input('Enter arrival times i.e 0 1 2 3 :')
arrival_time = [int(x) for x in at.split(' ')]
bt = input('Enter burst times i.e 3 5 6 :')
burst_times = [int(x) for x in bt.split(' ')]
prior = input('Enter priority i.e 1 2 3:')
priorities =  [int(x) for x in prior.split(' ')]

times = list(zip(arrival_time,burst_times,priorities))
sorted_times = sorted(times,key=lambda x : x[2])


print(sorted_times)


turnaround_time = []
waiting_time = []
start = []
finish = []
for i,(a,b,p) in enumerate(sorted_times):
    if i == 0:
        start.append(0)
        waiting_time.append(0)
        f = a + b
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

