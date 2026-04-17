class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # assign each letter a unique prime number
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        maps = {}
        for word in strs:
            # multiply primes for each letter — anagrams produce same product
            key = 1
            for c in word:
                key *= primes[ord(c) - 97]  # ord('a') = 97, precomputed
            
            if key in maps:
                maps[key].append(word)
            else:
                maps[key] = [word]
        
        return list(maps.values())