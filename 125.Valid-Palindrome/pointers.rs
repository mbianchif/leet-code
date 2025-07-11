impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        if s.is_empty() {
            return true;
        }

        let mut chars = s
            .chars()
            .filter_map(|c| c.is_ascii_alphanumeric().then_some(c.to_ascii_lowercase()));

        // O(n)
        while let (Some(front), Some(back)) = (chars.next(), chars.next_back()) {
            if front != back {
                return false;
            }
        }

        true
    }
}
