use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        let parenthesis = HashMap::from([('}', '{'), (']', '['), (')', '(')]);

        // O(n)
        for c in s.chars() {
            if let Some(&paren) = parenthesis.get(&c) {
                if stack.pop() != Some(paren) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        stack.is_empty()
    }
}
