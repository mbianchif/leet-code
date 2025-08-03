use std::collections::{BinaryHeap, HashMap};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = nums.len();

        // O(n)
        let init = HashMap::<_, usize>::with_capacity(n);
        let counts = nums.into_iter().fold(init, |mut acc, x| {
            *acc.entry(x).or_default() += 1;
            acc
        });

        // O(n)
        let mut heap: BinaryHeap<_> = counts.into_iter().map(|(x, count)| (count, x)).collect();

        // O(k * logn)
        (0..k).scan(heap, |h, _| h.pop().map(|(_, x)| x)).collect()
    }
}
