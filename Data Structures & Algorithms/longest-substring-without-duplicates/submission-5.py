class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        running_start_index = 0
        unique_chars = set()
        for i, char in enumerate(s):
            # duplicate found
            if char in unique_chars:
                #tally
                max_length = max(max_length, len(s[running_start_index:i]))
                
                duplicate_char_index = s[running_start_index:i].index(char) + running_start_index
                # if duplicate_char_index != running_start_index: #not single char remove (keep the duplicate in set, because we're adding a new one)
                for c in s[running_start_index:duplicate_char_index]:
                    unique_chars.discard(c)

                running_start_index = duplicate_char_index + 1
            # else:
            unique_chars.add(char)

        return max(max_length, len(s[running_start_index:len(s)]))

