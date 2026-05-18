class Solution:

    def encode(self, strs: List[str]) -> str:
       s = ""
       for i in strs:
        i+="\n"
        s+=i

        
       return s 

    def decode(self, s: str) -> List[str]:
        s = s.split("\n")
        s.pop()
        return s
