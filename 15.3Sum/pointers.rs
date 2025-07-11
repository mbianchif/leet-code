use std::{collections::HashSet, iter::FromIterator};

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut triplets = HashSet::new();

        // O(nlogn)
        nums.sort();

        // O(n^2)
        for (start, num) in nums.iter().enumerate() {
            if let Some(prev) = nums.get(start - 1) {
                if prev == num {
                    continue;
                }
            }

            let target = -num;
            let mut i = start + 1;
            let mut j = nums.len() - 1;

            // O(n)
            while i < j {
                let sum = nums[i] + nums[j];
                if sum < target {
                    i += 1;
                } else if sum > target {
                    j -= 1;
                } else {
                    let left = nums[i];
                    let right = nums[j];
                    triplets.insert(vec![*num, left, right]);

                    while i < j && nums[i] == left {
                        i += 1;
                    }

                    while i < j && nums[j] == right {
                        j -= 1;
                    }
                }
            }
        }

        // O(n)
        Vec::from_iter(triplets)
    }
}
