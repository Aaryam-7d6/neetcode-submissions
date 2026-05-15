class Solution:
    def reverse(self, x: int) -> int:
        s = 1 if x>=0 else -1
        #a = str(x)
        #b = a[::-1]
        #c = int(b)
        r = int(str(abs(x))[::-1]) * s
        if r < -2147483648 or r > 2147483647:
            return 0
        return r