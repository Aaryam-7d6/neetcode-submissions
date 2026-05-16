class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #c = 0
        #a = []
        #if len(nums) == 1:
            #return nums
        #for i in range(len(nums)-1):
             
            #if nums[i] == nums[i+1]:
                #c+=1
                #if nums[i] not in a:
                    #a.append(nums[i])
            #else:
                #return nums
            #if sorted(nums) == nums:
                #return nums
            
        #return a[:k]
        #t = set(nums)
        t = set(nums)
        d = {}
        for i in t:
            d[i] = nums.count(i)
        
        d = sorted(d, key=d.get, reverse=True)
        return d[:k]



            

        