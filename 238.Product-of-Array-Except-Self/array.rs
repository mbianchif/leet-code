impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let prevs = nums.iter().scan(1, |state, x| {
            let tmp = *state;
            *state *= x;
            Some(tmp)
        });

        // O(n)
        let posts = nums
            .iter()
            .rev()
            .scan(1, |state, x| {
                let tmp = *state;
                *state *= x;
                Some(tmp)
            })
            .collect::<Vec<_>>()
            .into_iter()
            .rev();

        // O(n)
        prevs.zip(posts).map(|(prev, post)| prev * post).collect()
    }
}
