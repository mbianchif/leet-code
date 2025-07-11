use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap},
};

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;

        // O(n)
        let counts = nums.into_iter().fold(HashMap::new(), |mut acc, x| {
            *acc.entry(x).or_default() += 1;
            acc
        });

        // O(n * logk)
        let mut top = BinaryHeap::new();
        for (num, count) in counts {
            top.push((Reverse(count), num));
            if top.len() > k {
                top.pop();
            }
        }

        // O(k)
        top.into_iter().map(|(_, num)| num).collect()
    }
}
