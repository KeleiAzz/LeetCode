__author__ = 'keleigong'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A > E and B > F and G > C and H > D:
            return (G - E) * (H - F)
        if A < E and B < F and G < C and H < D:
            return (C - A) * (D - B)
        if E > C or G < A or F > D or B > H:
            return (C - A) * (D - B) + (G - E) * (H - F)
        a = [A, E, C, G]
        a.sort()
        a = a[2] - a[1]
        b = [B, D, F, H]
        b.sort()
        b = b[2] - b[1]
        return (C - A) * (D - B) + (G - E) * (H - F) - a * b