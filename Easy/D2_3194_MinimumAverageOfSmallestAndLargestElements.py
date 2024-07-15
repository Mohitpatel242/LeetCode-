class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        b=len(nums)/2
        l = []
        for i in range(len(nums)):
            if len(nums)==0:
                break    
            if len(nums)==1:
                b = nums[0]/2
                l.append(b)
                break   
            a = (nums[0] + nums[-1])/2
            if a%2==0.0:
                l.append(int(a))
            else:
                l.append(a)
            nums.pop(0)
            nums.pop(-1)
        l.sort()
        return l[0]
                