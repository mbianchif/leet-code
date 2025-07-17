impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let (mut min_price, mut max_profit) = (prices[0], 0);

        // O(n)
        for price in prices {
            max_profit = max_profit.max(price - min_price);
            min_price = min_price.min(price);
        }

        max_profit
    }
}
