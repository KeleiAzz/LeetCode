def task(V, N):
    size = len(V)
    if size < 2:
        return size
    m = {} # latest running time of a task
    current_time = 1 # current time
    for task in V:
        if task not in m: # if a task has not run, just run it
            m[task] = current_time
            current_time += 1
        else:
            if current_time - m[task] > N: # if the latest running time of the task + N < current time, run this task
                m[task] = current_time
                current_time += 1
            else:
                current_time = m[task] + N + 1 # other, forward the time to task + N + 1, run this task
                m[task] = current_time
                current_time += 1
    return current_time - 1

print task([1, 2, 1, 2], 2)
