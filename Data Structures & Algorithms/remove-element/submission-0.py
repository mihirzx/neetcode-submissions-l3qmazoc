class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k

        

        ## when the current value of the index != val, replace it at the start by using k as a pointer. So we are moving all the non values of val at the start 