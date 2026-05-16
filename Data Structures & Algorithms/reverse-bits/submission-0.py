class Solution:
    def reverseBits(self, n: int) -> int:
        #if n < 0:
        #    return 0
        #x = str(n)[::-1]
        #y = int(x,2)
        #y = int(x)
        #r = str((n))[::-1]
        #return y
        b = format(n, '032b')
        return int(b[::-1], 2)
