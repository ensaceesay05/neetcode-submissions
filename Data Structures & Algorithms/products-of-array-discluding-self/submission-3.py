class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        
        for i in range(n):
            l, r = 0, n - 1
            curr = 1
            while l <= r:
                if l == i:   # skip the current index
                    l += 1
                    continue
                if r == i:   # skip the current index
                    r -= 1
                    continue
                
                if l == r:   # when they meet in the middle
                    curr *= nums[l]
                    l += 1
                    r -= 1
                else:        # take both ends
                    curr *= nums[l] * nums[r]
                    l += 1
                    r -= 1
            res.append(curr)
        
        return res
