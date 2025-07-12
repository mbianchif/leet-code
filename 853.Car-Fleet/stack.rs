impl Solution {
    fn time_till_end((pos, speed): (i32, i32), end: i32) -> f32 {
        (end - pos) as f32 / speed as f32
    }

    pub fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
        // O(n)
        let mut cars: Vec<_> = position.into_iter().zip(speed).collect();

        // O(nlogn)
        cars.sort_unstable_by_key(|car| car.0);

        // O(n)
        let mut last = None::<f32>;
        cars.into_iter().rev().fold(0, |fleets, car| {
            let curr = Self::time_till_end(car, target);

            if !last.map(|l| l < curr).unwrap_or(true) {
                return fleets;
            }

            last = Some(curr);
            fleets + 1
        })
    }
}
