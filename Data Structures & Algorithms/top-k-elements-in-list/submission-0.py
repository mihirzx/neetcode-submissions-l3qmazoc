class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]


        for num in nums:
            count[num] = count.get(num,0) + 1
        for nums, c in count.items():
            freq[c].append(nums)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for nums in freq[i]:
                res.append(nums)
                if len(res) == k:
                    return res
                    

            


