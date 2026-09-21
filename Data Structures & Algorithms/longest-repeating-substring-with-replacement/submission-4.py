class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Intuition:
        Iterating thru the string once, a few possible decisions:
        1. s[i-1] != s[i]: start new str
        2. s[i-1] != s[i]: use up a k
        3. s[i-1] != s[i]: no more k left. tally
        3. s[i-1] == s[i]: count++

        BABBAAA
        k = 1

        BABABBBBBAA
        BABXBBBBB
            BBBBB

        BXBXBB
        BXBB


        AAABABB


        max = 3
        BABABBBBBAA
             |
        - B, 3, 0
        - B, 2, 1

        """
        i_of_substr_with_k_left = set()
        # k: the index of substr beginning char
        # v: (repeating_char, length, remaining k)
        substr_map = {}
        max_length = 0

        def update_substrs(char):
            for idx in list(i_of_substr_with_k_left):
                substr = substr_map[idx]
                if substr[0] == char:
                    substr_map[idx] = (substr[0], substr[1] + 1, substr[2])
                else:  # use a k
                    substr_map[idx] = use_a_k_or_tally_substr(substr, idx)

        def use_a_k_or_tally_substr(substr: tuple[str, int, int], idx: int):
            if substr[2] == 0:  # tally
                nonlocal max_length
                max_length = max(substr[1], max_length)
                i_of_substr_with_k_left.remove(idx)
                return None
            else:  # use a k
                return (substr[0], substr[1] + 1, substr[2] - 1)

        for i, char in enumerate(s):
            update_substrs(char)
            if i == 0 or char != s[i - 1]:
                # consider it as a new substr
                substr_map[i] = (char, 1, k)
                i_of_substr_with_k_left.add(i)

        # final tally
        for idx in i_of_substr_with_k_left:
            substr = substr_map[idx]
            # try to use up any remaining k by extending to the left
            max_length = max(substr[1] + min(idx, substr[2]), max_length)
        return max_length
