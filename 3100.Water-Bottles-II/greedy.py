class Solution:
    def maxBottlesDrunk(self, bottles: int, exchange: int) -> int:
        drunk, empty = 0, 0

        # O(n)
        while bottles > 0:
            drunk += bottles
            empty += bottles
            bottles = 0

            while empty >= exchange:
                empty -= exchange
                bottles += 1
                exchange += 1

        return drunk
