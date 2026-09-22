class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Intuition: 
        permutation is a sequence shuffled up in order
        1. have a sliding window over s2, move right one by one with len(s1)
        2. Compare chars with s1 against s2_window. If identical, return true.
        DS: {k: char, v: count} i.e., Counter
        Input: s1 = "abc", s2 = "lecabee"
        """
        s1_chars = Counter(s1)
        window_length = len(s1)
        s2_window_chars = Counter(s2[:window_length])
        if s1_chars == s2_window_chars:
            return True
        
        for i in range(window_length, len(s2)):
            char_to_be_removed = s2[i-window_length]

            if s2_window_chars[char_to_be_removed] == 1:
                del s2_window_chars[char_to_be_removed]
            else:
                s2_window_chars[char_to_be_removed] -= 1
            
            s2_window_chars[s2[i]] += 1

            if s1_chars == s2_window_chars:
                return True

        return False