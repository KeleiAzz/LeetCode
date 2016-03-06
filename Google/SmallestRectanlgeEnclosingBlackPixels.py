class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        top = self.checkRow(image, 0, x, True)
        bottom = self.checkRow(image, x + 1, len(image), False)
        left = self.checkCol(image, 0, y, top, bottom, True)
        right = self.checkCol(image, y + 1, len(image[0]), top, bottom, False)
        return (bottom - top ) * (right - left)


    def checkRow(self, image, i, j, opt):
        while i != j:
            m = (i + j) >> 1
            if ('1' in image[m]) == opt:
                j = m
            else:
                i = m + 1
        return i


    def checkCol(self, image, i, j, top, bottom, opt):
        while i != j:
            m = (i + j) / 2
            if any(image[k][m] == '1' for k in xrange(top, bottom)) == opt:
                j = m
            else:
                i = m + 1
        return i