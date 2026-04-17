import numpy as np
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        
        for word in strs:
            # convert whole word to numpy array in one C call
            arr = np.frombuffer(word.encode(), dtype=np.uint8)
            # bincount does the entire count in one vectorized C loop
            counts = np.bincount(arr - 97, minlength=26).astype(np.uint8)
            maps[counts.tobytes()].append(word)
        
        return list(maps.values())