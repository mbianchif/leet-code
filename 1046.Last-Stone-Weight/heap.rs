use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        // O(n)
        let mut heap = BinaryHeap::from(stones);

        // O(nlogn)
        while heap.len() > 1 {
            // O(logn)
            let one = heap.pop().unwrap();
            let two = heap.pop().unwrap();
            let leftover = one - two;

            if leftover > 0 {
                // O(logn)
                heap.push(leftover);
            }
        }

        heap.pop().unwrap_or(0)
    }
}
