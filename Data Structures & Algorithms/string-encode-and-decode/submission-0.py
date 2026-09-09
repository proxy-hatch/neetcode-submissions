class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#" and j < len(s):
                j += 1
            length = int(s[i:j])
            i = j+1+length
            result.append(s[j+1:i])
            
        return result