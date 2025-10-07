use std::collections::{BTreeSet, HashMap};

impl Solution {
    pub fn avoid_flood(rains: Vec<i32>) -> Vec<i32> {
        let n = rains.len();

        // O(n)
        let mut ans = vec![-1; n];
        let mut sunny_days = BTreeSet::new();
        let mut rain_days = HashMap::with_capacity(n);

        // O(nlogn)
        for (day, &lake) in rains.iter().enumerate() {
            if lake == 0 {
                sunny_days.insert(day);
                ans[day] = 1;
                continue;
            }

            if let Some(&rain_day) = rain_days.get(&lake) {
                let Some(&sunny_day) = sunny_days.range(rain_day + 1..).next() else {
                    return Vec::new();
                };

                sunny_days.remove(&sunny_day);
                ans[sunny_day] = lake;
            }

            rain_days.insert(lake, day);
        }

        ans
    }
}
