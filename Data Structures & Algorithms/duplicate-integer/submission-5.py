class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        le = len(nums)
        for i in range(le-1):
            if nums[i] == nums[i-1] or nums[i] == nums[i]:
                return True
            else:
                return False
        '''
        #n = sorted(nums)
        '''
        for num in nums:
            #if n[num] == n[num - 1] or n[num] == n[num + 1]:
            #if n[num] == n[num]:
            if n[num] == n[num] or n[num] == n[num - 1] or n[num] == n[num + 1]:
                return True
            else:
                return False
        '''
        '''
        y = len(n) - 1
        #while y < 0:
        for i in range(y):
            if n[i] == [num for num in n] :
                return True
            else:
                return False
                '''
        
        #n = sorted(nums)
        #y = len(n)
        #z = None
        #while y < 0:
        '''for i in range(nums):
            for j in range(i):
                if nums[i] == nums[j]:
                    return True
                else:
                    return False
                    '''
            #a = n[i]
            #b = n[i-1]
            #c = n[i+1]
            #if a == [num for num in n] :
            #if a == b or a == [num for num in n]:
                #z = True
            #else:
                #z = False
        #a = len(nums)
        #b = sorted(nums)
        #c = set(b)
        #i = 1
        #for i in range(a):
            #if c[i] == b[i]:
                #return False
            #if i == nums[i+1]:
                #return False
            #else:
                #return True
        #return z
        #return True
        #return False
        return len(nums) != len(set(nums))

