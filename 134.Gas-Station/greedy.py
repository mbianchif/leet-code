class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        acc, tank, start = 0, 0, 0

        # O(n)
        for i in range(n):
            tank += gas[i] - cost[i]
            acc += gas[i] - cost[i]
            if tank < 0:
                start = (i + 1) % n
                tank = 0

        return start if acc >= 0 else -1
