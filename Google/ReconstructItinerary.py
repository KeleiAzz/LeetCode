# coding=utf-8
from collections import defaultdict
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = defaultdict(list)
        for frm, to in tickets:
            d[frm].append(to)
        for frm in d.keys():
            d[frm].sort()
        stack = ['JFK']
        res = []
        while stack:
            node = stack[-1]
            # res.append(node)
            if d[node]:
                stack.append(d[node].pop(0))
            else:
                res.append(stack.pop())
        res.reverse()
        return res


    def findItinerary2(self, tickets):
        """
        这种效率低些但是比较容易懂,backtracking的方法,每次要加入res时把备选的都试一下,从第一个开始,如果把这个加进去能得到一个正确的
        输出,那就都OK了,如果这个进去不能得到正确输出,那么就从res里拿出来再选下一个放进去试试.
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = defaultdict(list)
        for frm, to in tickets:
            d[frm].append(to)
        for frm in d.keys():
            d[frm].sort()
        total = len(tickets) + 1
        res = ['JFK']
        self.helper(d, 'JFK', res, total, 1)
        return res

    def helper(self, d, cur, res, total, num):
        if num >= total:
            return True
        if cur not in d or not d[cur]:
            return False
        cur_list = d[cur]
        i = 0
        while i < len(cur_list):
            nxt = cur_list.pop(i)
            res.append(nxt)
            if self.helper(d, nxt, res, total, num + 1):
                return True
            res.pop()
            cur_list.append(nxt)
            cur_list.sort()
            i += 1
