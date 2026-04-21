class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # If left character is not alphanumeric, skip it
            if not s[left].isalnum():
                left += 1
                continue
            
            # If right character is not alphanumeric, skip it
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Both characters are alphanumeric, compare them
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
