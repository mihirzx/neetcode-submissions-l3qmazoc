class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = {}

        for num in nums:
            map1[num] = 1 + map1.get(num,0)

        sorted_items = sorted(map1.items(), key=lambda x: x[1], reverse=True)
        result = []
        for item in sorted_items[:k]:
            result.append(item[0])
        return result