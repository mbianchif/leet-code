impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let ls = height.iter().scan(0, |state, &x| {
            let prev = *state;
            *state = prev.max(x);
            Some(prev)
        });

        // O(n)
        let rs = height
            .iter()
            .rev()
            .scan(0, |state, &x| {
                let next = *state;
                *state = next.max(x);
                Some(next)
            })
            .collect::<Vec<_>>()
            .into_iter()
            .rev();

        // O(n)
        height
            .iter()
            .zip(ls.zip(rs))
            .fold(0, |acc, (h, (l, r))| acc + (l.min(r) - h).max(0))
    }
}
