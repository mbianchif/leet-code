use std::{cmp::Reverse, collections::BinaryHeap};

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let k = k as usize;
        let partial_len = |v: &[i32]| v[0].pow(2) + v[1].pow(2);

        // O(n)
        let heap: BinaryHeap<_> = points
            .into_iter()
            .map(|v| (Reverse(partial_len(&v)), v))
            .collect();

        // O(klogn)
        (0..k)
            .scan(heap, |heap, _| heap.pop().map(|(_, v)| v))
            .collect()
    }
}
