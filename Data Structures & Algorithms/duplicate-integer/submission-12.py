class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pizza = set()


        for i in nums:
            if i in pizza:
                return True
            pizza.add(i)
        return False