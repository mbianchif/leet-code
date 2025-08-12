class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        def bt(i, path, sentences):
            if i == len(s):
                sentences.append(" ".join(path))
                return sentences

            for w in wordDict:
                m = len(w)
                if s[i : i + m] == w:
                    path.append(w)
                    bt(i + m, path, sentences)
                    path.pop()

            return sentences

        # O(2^n)
        return bt(0, [], [])
