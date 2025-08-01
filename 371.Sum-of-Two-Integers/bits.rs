impl Solution {
    fn bin_sum(a: bool, b: bool, carry: bool) -> (bool, bool) {
        let xor = a ^ b;
        let and = a & b;

        let tmp = carry & xor;
        (xor ^ carry, and | tmp)
    }

    pub fn get_sum(a: i32, b: i32) -> i32 {
        (0..32)
            .scan(0, |carry, x| {
                let a = a & (1 << x) != 0;
                let b = b & (1 << x) != 0;

                let (a, b) = Self::bin_sum(a, b, *carry == 1);

                *carry = b as i32;
                Some(a as i32)
            })
            .enumerate()
            .fold(0, |acc, (i, x)| acc | (x << i))
    }
}
