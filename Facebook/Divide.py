def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    max_int = 2147483647
    min_int = -2147483648
    if dividend == min_int and divisor == -1:
        return max_int
    signal = 1
    if dividend < 0:
        signal = -signal
    if divisor < 0:
        signal = -signal
    dividend, divisor = abs(dividend), abs(divisor)
    res = 0
    while dividend >= divisor:
        d, times = divisor, 1
        # print d,
        while d <= dividend:
            d <<= 1
            times <<= 1
        d >>= 1
        times >>= 1
        res += times
        dividend -= d
        print dividend
    return res * signal

print divide(84837,23)