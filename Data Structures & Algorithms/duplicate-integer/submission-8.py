class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     list = set()

     for i in nums:
        if i not in list:
            list.add(i)
        else:
            return True
     return False