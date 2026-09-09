class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # k: set('char'), v: List(str)

        for word in strs:
            counter = Counter(word)
            anagrams[frozenset(counter.items())].append(word)
        
        return list(anagrams.values())


