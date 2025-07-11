class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1

        # O(n)
        while i < j:
            ss = numbers[i] + numbers[j]

            if ss < target:
                i += 1
            elif ss > target:
                j -= 1
            else:
                return [i + 1, j + 1]

        return []
