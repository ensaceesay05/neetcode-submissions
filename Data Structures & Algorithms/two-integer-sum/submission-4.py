class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            result = target - n

            if result in hashMap:
                return [hashMap[result], i]
            
            hashMap[n] = i