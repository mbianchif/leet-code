impl Solution {
    fn count_ones(mut n: i32) -> i32 {
        let mut ones = 0;

        // O(logn)
        while n > 0 {
            ones += n & 1;
            n >>= 1;
        }

        ones
    }

    pub fn count_bits(n: i32) -> Vec<i32> {
        // O(2^b)
        (0..=n).map(Self::count_ones).collect()
    }
}
