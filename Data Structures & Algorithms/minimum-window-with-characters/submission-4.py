class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Intuition (2 ptrs):
        1. keep extending the window (r ptr) to find all the chars
        2. keep shrinking l until we find the shortest
        3. repeat: shrink the leftmost useful and extend until we find its replacement.
        4. keep replacing the optimal solution as we find them, until we finish the string

        Input: s = "OYXXAZUZODYXZV", t = "XYZ" #YXXAZ should be ignored
        Output: "YXZ"
        """
        # edge cases
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        if t in s:
            return t
        
        t_counter = Counter(t)
        missing = sum(t_counter.values())

        counting_substrs = []
        return_value = ""
        l, r = 0, 0
        for r, char in enumerate(s):
            if char in t_counter:
                # only decrement missing if we NEED this char; otherwise simply keeping track of the count that we HAVE
                if t_counter[char] > 0:
                    missing -= 1
                t_counter[char] -= 1
                
                # got all the chars, time to shrink
                if missing == 0:
                    # shrink l until we lose leftmost match
                    while missing == 0:
                        if s[l] in t_counter:
                            t_counter[s[l]] += 1
                            
                            # we no longer have enough. Tally shortest solution
                            if t_counter[s[l]] > 0:
                                missing = 1
                                if r - l + 1 < len(return_value) or return_value == "":
                                    return_value = s[l : r + 1]
                        l += 1
        return return_value

        """
        Intuition (keeping track of multiple trials):
        1. if we see one, keep extending window to find the rest
        2. if we see an extra (found > count(t[char])), we can let it and anything useless in between go to shorten window
        We can complete this in O(n)

        Input: s = "OYXXAZUZODYXZV", t = "XYZ" #YXXAZ should be ignored
        Output: "YXZ"
        """
