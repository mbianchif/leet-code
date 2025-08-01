impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let a = n * (n + 1) / 2;

        // O(n)
        let b: i32 = nums.into_iter().sum();
        a - b
    }
}
