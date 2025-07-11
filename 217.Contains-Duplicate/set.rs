use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut set = HashSet::with_capacity(nums.len());

        // O(n)
        !nums.into_iter().all(|x| set.insert(x))
    }
}
