impl Solution {
    pub fn hamming_weight(mut n: i32) -> i32 {
        let mut ones = 0;

        // O(logn)
        while n > 0 {
            ones += n & 1;
            n >>= 1;
        }

        ones
    }
}
