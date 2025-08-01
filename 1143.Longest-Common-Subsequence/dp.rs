impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let (n, m) = (text1.len(), text2.len());
        let text1 = text1.as_bytes();
        let text2 = text2.as_bytes();

        // O(m)
        let mut prev = vec![0; m + 1];
        let mut curr = vec![0; m + 1];

        // O(n * m)
        for i in 1..=n {
            for j in 1..=m {
                curr[j] = if text1[i - 1] == text2[j - 1] {
                    1 + prev[j - 1]
                } else {
                    prev[j].max(curr[j - 1])
                };
            }

            (prev, curr) = (curr, prev);
        }

        prev[m]
    }
}
