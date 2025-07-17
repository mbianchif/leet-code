struct Solution {}

use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut dq = VecDeque::with_capacity(k);
        let mut mxs = Vec::new();

        // O(n)
        for i in 0..nums.len() {
            if dq.front().map_or(false, |&front| front + k <= i) {
                dq.pop_front();
            }

            while dq.back().map_or(false, |&back| nums[back] < nums[i]) {
                dq.pop_back();
            }

            dq.push_back(i);
            if i >= k - 1 {
                mxs.push(nums[dq[0]]);
            }
        }

        mxs
    }
}

fn main() {
    println!("Hello, world!");
}

/*

    [[1, 4, 2], 3,  5]  4
    [1, [4, 2,  3], 5]  4
    [1,  4,[2,  3,  5]] 5

*/
