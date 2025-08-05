from collections import deque, defaultdict


class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        indegs = defaultdict(int)
        n = len(words)

        # O(n * k)
        g = {ch: [] for word in words for ch in word}

        # O(n * k)
        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            k = min(len(w1), len(w2))

            j = 0
            while j < k and w1[j] == w2[j]:
                j += 1

            if j < k:
                g[w1[j]].append(w2[j])
                indegs[w2[j]] += 1
            elif len(w1) > len(w2):
                return ""

        # O(v)
        q = deque(v for v in g if indegs[v] == 0)

        # O(v + e)
        result = []
        while q:
            v = q.popleft()
            result.append(v)

            for w in g[v]:
                indegs[w] -= 1
                if indegs[w] == 0:
                    q.append(w)

        return "".join(result) if len(result) == len(g) else ""
