class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        groups = {}

        # O(n * klogk)
        for i in range(n):
            key = tuple(sorted(strs[i]))
            anagrams = groups.get(key, [])
            anagrams.append(strs[i])
            groups[key] = anagrams

        # O(n)
        return list(groups.values())
