from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        
        for word in strs:
            # count chars directly into a bytearray (faster than list of ints)
            count = bytearray(26)
            for c in word.encode():  # encode once, iterate bytes not chars
                count[c - 97] += 1   # 97 = ord('a'), hardcoded saves a call
            maps[bytes(count)].append(word)  # bytes hashes faster than tuple
        
        return list(maps.values())