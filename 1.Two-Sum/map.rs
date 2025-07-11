use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        let mut seen = HashMap::with_capacity(n);

        // O(n)
        for (i, x) in nums.into_iter().enumerate() {
            if let Some(j) = seen.get(&(target - x)) {
                return vec![i as i32, *j];
            }

            seen.insert(x, i as i32);
        }

        Vec::new()
    }
}
