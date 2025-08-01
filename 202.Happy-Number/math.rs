use std::collections::HashSet;

impl Solution {
    fn next(mut n: i32) -> i32 {
        let mut sum = 0;

        // O(logn)
        while n != 0 {
            let x = n % 10;
            sum += x.pow(2);
            n /= 10;
        }

        sum
    }

    pub fn is_happy(mut n: i32) -> bool {
        let mut steps = HashSet::new();

        // O(logn)
        while !steps.contains(&n) {
            if n == 1 {
                return true;
            }

            steps.insert(n);

            // O(logn)
            n = Self::next(n);
        }

        false
    }
}
