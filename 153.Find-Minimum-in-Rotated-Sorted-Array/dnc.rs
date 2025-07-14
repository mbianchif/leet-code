impl Solution {
    fn dnc(nums: &[i32]) -> i32 {
        if let [only] = nums {
            return *only;
        }

        let mid = nums.len() / 2;
        let l = Self::dnc(&nums[..mid]);
        let r = Self::dnc(&nums[mid..]);
        l.min(r)
    }

    pub fn find_min(nums: Vec<i32>) -> i32 {
        Self::dnc(&nums)
    }
}
