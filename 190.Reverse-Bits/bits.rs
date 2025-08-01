impl Solution {
    pub fn reverse_bits(x: i32) -> i32 {
        (0..16).fold(0, |acc, i| {
            let j = 31 - i;

            let a = (x >> i) & 1;
            let b = (x >> j) & 1;

            acc | (b << i) | (a << j)
        })
    }
}
