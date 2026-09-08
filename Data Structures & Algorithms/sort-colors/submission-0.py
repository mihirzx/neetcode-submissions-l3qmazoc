class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pizza = len(nums) - 1
        counts = [0,0,0]
        for i in range(pizza + 1):
            counts[nums[i]] += 1
        
        i = 0 
        for n in range(3):
            for _ in range(counts[n]):
                nums[i] = n
                i += 1
