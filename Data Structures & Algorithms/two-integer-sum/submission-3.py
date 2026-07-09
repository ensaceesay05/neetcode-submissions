class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, j in enumerate(nums):
            result = target - j

            if result in hashmap:
                return [hashmap [result], i]
            
            hashmap[j] = i