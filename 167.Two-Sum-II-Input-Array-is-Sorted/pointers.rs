use std::collections::HashMap;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let (mut i, mut j) = (0, numbers.len() - 1);

        // O(n)
        while i < j {
            let sum = numbers[i] + numbers[j];
            if sum < target {
                i += 1;
            } else if sum > target {
                j -= 1;
            } else {
                return vec![1 + i as i32, 1 + j as i32];
            }
        }

        Vec::new()
    }
}
