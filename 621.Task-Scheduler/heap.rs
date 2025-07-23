use std::collections::{BinaryHeap, VecDeque};

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        // O(m)
        let counts = tasks.into_iter().fold([0; 26], |mut field, x| {
            let i = x as usize % field.len();
            field[i] += 1;
            field
        });

        let mut counts: BinaryHeap<_> = counts
            .into_iter()
            .filter_map(|x| (x > 0).then_some(x))
            .collect();

        let mut cooldown = VecDeque::with_capacity(counts.len());
        let mut t = 0;

        // O(m)
        while !counts.is_empty() || !cooldown.is_empty() {
            if let Some(front) = cooldown.front().filter(|(tx, _)| *tx <= t) {
                counts.push(front.1);
                cooldown.pop_front();
            }

            t += 1;
            if let Some(count) = counts.pop().map(|c| c - 1).filter(|&c| c > 0) {
                cooldown.push_back((t + n, count));
            }
        }

        t
    }
}
