impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let (n, m) = (word1.len(), word2.len());
        let word1 = word1.as_bytes();
        let word2 = word2.as_bytes();

        // O(m)
        let mut curr = vec![0; m + 1];
        let mut prev: Vec<_> = (0..=m).collect();

        // O(n * m)
        for i in 1..=n {
            curr[0] = i;

            // O(m)
            for j in 1..=m {
                curr[j] = if word1[i - 1] == word2[j - 1] {
                    prev[j - 1]
                } else {
                    1 + prev[j - 1].min(prev[j]).min(curr[j - 1])
                }
            }

            (curr, prev) = (prev, curr)
        }

        prev[m] as i32
    }
}
