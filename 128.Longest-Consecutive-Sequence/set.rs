use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        // O(n)
        let nums: HashSet<_> = nums.into_iter().collect();
        let mut longest = 0;

        // O(n)
        for num in &nums {
            if !nums.contains(&(num - 1)) {
                let seq_len = (*num..).take_while(|n| nums.contains(n)).count();
                longest = longest.max(seq_len as i32);
            }
        }

        longest
    }
}
