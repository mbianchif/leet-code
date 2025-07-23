use std::{cmp::Reverse, collections::BinaryHeap};

struct KthLargest {
    heap: BinaryHeap<Reverse<i32>>,
    k: usize,
}

impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut kth = Self {
            heap: BinaryHeap::with_capacity(nums.len()),
            k: k as usize,
        };

        // O(nlogk)
        for x in nums {
            kth.add(x);
        }

        kth
    }

    fn add(&mut self, val: i32) -> i32 {
        let heap = &mut self.heap;

        // O(logk)
        heap.push(Reverse(val));
        if heap.len() > self.k {
            // O(logk)
            heap.pop();
        }

        heap.peek().unwrap().0
    }
}
