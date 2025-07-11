use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let (n, m) = (s.len(), t.len());

        if n != m {
            return false;
        }

        // O(n)
        let mut counts: HashMap<_, usize> =
            s.chars().fold(HashMap::with_capacity(n), |mut acc, x| {
                *acc.entry(x).or_default() += 1;
                acc
            });

        // O(n)
        for x in t.chars() {
            let Some(count) = counts.get_mut(&x) else {
                return false;
            };

            *count -= 1;
            if *count == 0 {
                counts.remove(&x);
            }
        }

        counts.is_empty()
    }
}
