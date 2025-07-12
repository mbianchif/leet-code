impl Solution {
    pub fn daily_temperatures(temps: Vec<i32>) -> Vec<i32> {
        let mut stack = Vec::with_capacity(temps.len());

        // O(n)
        let mut ans = vec![0; temps.len()];

        // O(n)
        for (i, &temp) in temps.iter().enumerate() {
            while stack
                .last()
                .map(|&top| temps[top] < temp)
                .unwrap_or_default()
            {
                let top = stack.pop().unwrap();
                ans[top] = (i - top) as i32;
            }

            stack.push(i);
        }

        ans
    }
}
