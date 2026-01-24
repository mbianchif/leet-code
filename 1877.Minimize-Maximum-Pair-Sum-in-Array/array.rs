impl Solution {
    pub fn min_pair_sum(mut nums: Vec<i32>) -> i32 {
        // O(nlogn)
        nums.sort_unstable();

        let mid = nums.len() >> 1;
        let (front, back) = nums.split_at(mid);

        // O(n)
        front
            .iter()
            .zip(back.iter().rev())
            .map(|(f, b)| f + b)
            .max()
            .unwrap_or_default()
    }
}
