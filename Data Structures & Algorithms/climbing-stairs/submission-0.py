class Solution:
    def climbStairs(self, n: int) -> int:
        ways_one, ways_two = 1, 1

        for _ in range(n - 1):
            temp_ways_one = ways_one
            ways_one = ways_one + ways_two
            ways_two = temp_ways_one

        return ways_one