class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d={
            "0" : "+",
            "1": "",
            "2": ["a","b", "c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w","x","y","z"],
            "*" : "",
            "#" : ""
        }

        if digits == "":
            return[]
        
        if len(digits) == 1:
            return d[digits]
        
        a = []
        #r = []
        r=[""]
        

        for i in digits:
            a.append(d[i])

        #for i in a[0]:
            #for j in a[1]:
                #r.append(i+j)
        #l = len(a)
        #i,j=a[0],a[0]
        #while l >= 0:
        #         a.append(a[i]+a[j])
        #         i+=1
        #         j+=1
        #         l-=1
        for i in digits:
            nr=[]
            for j in r:
                for k in d[i]:
                    nr.append(j+k)
            r = nr
        return r