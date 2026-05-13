class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        output = False
        a = set(s)
        b = set(t)
        #c = a-b
        d = list(s)
        e = list(t)
        count = 0
        if len(s) == len(t):
            #if [c for c in s ] == [ a for a in t]:
                #output = True
                #return output
            #if [c for c in s ] != [ a for a in t]:
                #output = True
                #return output
            #if c == set():
            if a==b and all(d.count(h) == e.count(h) for h in a):
                output = True
                return output

            else:
                #output = True
                return output
        
        else:
            return output