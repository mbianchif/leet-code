impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut start = 0;
        let mut end = nums.len();

        while start < end {
            let mid = (start + end) >> 1;
            if nums[mid] < target {
                start = mid + 1;
            } else if nums[mid] > target {
                end = mid;
            } else {
                return mid as i32;
            }
        }

        -1
    }
}
