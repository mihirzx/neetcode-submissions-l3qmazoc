class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums) - 1

        for num in nums:
            mid = (left+right) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
