# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
def read4(buf):
    pass

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        count = 0
        while n > 0:
            buf4 = [''] * 4
            l = read4(buf4)
            if not l:
                return count
            for i in range(l):
                if buf4[i] != '' and n > 0:
                    buf[count] = buf4[i]
                    count += 1
                    n -= 1

        return count
