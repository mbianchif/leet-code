from collections import defaultdict, deque


class Solution:
    def ladderLength(self, begin: str, end: str, word_list: list[str]) -> int:
        # O(v)
        if end not in word_list:
            return 0

        word_list.append(begin)
        patterns = defaultdict(list)
        words = defaultdict(list)
        k = len(begin)

        # O(v * k)
        for word in word_list:
            for i in range(k):
                pattern = word[:i] + "*" + word[i + 1 :]
                patterns[word].append(pattern)
                words[pattern].append(word)

        q = deque([begin])
        distances = {begin: 1}

        # O(v * k + e)
        while q:
            v = q.popleft()
            if v == end:
                return distances[v]

            for pattern in patterns[v]:
                for w in words[pattern]:
                    if w not in distances:
                        distances[w] = distances[v] + 1
                        q.append(w)

        return 0
