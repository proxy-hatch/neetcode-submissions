class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        e.g., 
        aba
        abba
        a
        """
        no_whitespace = "".join(char for char in s if char.isalnum()).lower()
        n = len(no_whitespace)

        for i in range(n//2):
            if no_whitespace[i] != no_whitespace[n-1-i]:
                return False
        
        return True
