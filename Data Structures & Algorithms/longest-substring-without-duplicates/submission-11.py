class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimal
        Intuition: instead of maintaining a set, maintain a hash table with value as the last seen index
        """
        # max_length = 0
        # running_start_index = 0
        # seen_chars = {}
        # for i, char in enumerate(s):
        #     # duplicate found
        #     if char in seen_chars:
        #         seen_index = seen_chars[char]
        #         if seen_index >= running_start_index: # otherwise don't care
        #             # tally
        #             max_length = max(max_length, len(s[running_start_index:i]))
        #             running_start_index = seen_index + 1

        #     seen_chars[char] = i

        # return max(max_length, len(s[running_start_index : ]))


        """
        Intuition:
        1. keep a set to store unique chars in substr
        2. when found duplicate, calc max, start at new non-duplicate, and maintain set.
        """
        max_length = 0
        running_start_index = 0
        unique_chars = set()
        for i, char in enumerate(s):
            # duplicate found
            if char in unique_chars:
                # tally
                max_length = max(max_length, len(s[running_start_index:i]))

                duplicate_char_index = s[running_start_index:i].index(char) + running_start_index
                # not single char remove (keep the duplicate in set, because we're adding a new one)
                if duplicate_char_index != running_start_index:
                    for c in s[running_start_index:duplicate_char_index]:
                        unique_chars.discard(c)

                running_start_index = duplicate_char_index + 1
            else:
                unique_chars.add(char)

        return max(max_length, len(s[running_start_index:]))
