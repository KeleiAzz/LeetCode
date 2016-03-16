def minCostII(costs):
    if not costs:
        return 0
    pre = costs[0][:]
    now = costs[0][:]
    k = len(costs)
    for i in range(1, len(costs)):
        for j in range(k):
            now = min(pre[:j] + pre[j+1:]) + costs[i][j]
        pre = now[:]
    return min(now)

def minCostIII(costs, neighbors):
    '''
    House neighbors are in a adjacent list. when calculating new costs, pick houses not in current house's adjacent list.
    :param costs:
    :return:
    '''
    if not costs:
        return 0
    pre = costs[0][:]
    now = costs[0][:]
    k = len(costs)
    for i in range(1, len(costs)):
        for j in range(k):
            now = min(pre[x] for x in range(k) if x not in neighbors[j]) + costs[i][j]
        pre = now[:]
    return min(now)
