impl Solution {
    pub fn get_descent_periods(prices: Vec<i32>) -> i64 {
        let periods_in_days = |days| days * (days + 1) / 2;
        let mut smooth_periods = 0;
        let n = prices.len();
        let mut l = 1;

        // O(n)
        for r in 1..n {
            if prices[r - 1] != prices[r] + 1 {
                smooth_periods += periods_in_days(r - l + 1);
                l = r + 1;
            }
        }

        (smooth_periods + periods_in_days(n - l + 1)) as i64
    }
}
