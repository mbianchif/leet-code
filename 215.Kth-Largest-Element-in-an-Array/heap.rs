use std::{cmp::Reverse, collections::BinaryHeap};

impl Solution {
    pub fn find_kth_largest(nums: Vec<i32>, k: i32) -> i32 {
        // O(n)
        let mut heap: BinaryHeap<_> = nums.into();

        // O(klogn)
        for _ in 1..k {
            heap.pop();
        }

        // O(log(n - k))
        heap.pop().unwrap()
    }
}
