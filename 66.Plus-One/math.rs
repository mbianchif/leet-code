impl Solution {
    pub fn plus_one(mut digits: Vec<i32>) -> Vec<i32> {
        // O(n)
        for num in digits.iter_mut().rev() {
            if *num < 9 {
                *num += 1;
                return digits;
            }

            *num = 0;
        }

        digits.insert(0, 1);
        digits
    }
}
