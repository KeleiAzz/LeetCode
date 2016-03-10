class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return -1

        is_negative = True if numerator * denominator < 0 else False
        if numerator < 0:
            numerator *= -1
        if denominator < 0:
            denominator *= -1

        #before .
        before = str(numerator / denominator)
        remain = numerator % denominator
        print before, remain
        #after .
        remain_index_map = {}
        after = ''
        while remain != 0:
            #calculate one time
            numerator = remain * 10
            after += str(numerator / denominator)
            print after
            #add remain to remain_index_map
            remain_index_map[remain] = len(after) - 1

            #refresh remain
            remain = numerator % denominator
            #check whether loop occurs
            if remain in remain_index_map:
                break

                #loop not detected, iterate to next iteration

        #loop exists
        if remain:
            repeate_start_idx = remain_index_map[remain]
            after = after[:repeate_start_idx] + '(' + after[repeate_start_idx:] + ')'

        #combine before and after part
        res = ''
        if is_negative:
            res = '-'

        if after == '':
            res += before
        else:
            res += (before + '.' + after)

        return res


s = Solution()

print s.fractionToDecimal(235, 37)