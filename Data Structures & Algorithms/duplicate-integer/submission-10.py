class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seek = {}
        for i in nums:
            if i in seek:
                return True
            seek[i] = True
        return False
    
        