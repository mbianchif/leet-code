impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let (mut a, mut b) = (0, cost[0]);

        // O(n)
        for &v in cost.iter().skip(1) {
            let curr_cost = v + a.min(b);
            (a, b) = (b, curr_cost);
        }

        a.min(b)
    }
}
