use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut words: HashMap<_, Vec<String>> = HashMap::new();

        // O(n * klogk)
        for word in strs {
            let mut arr: Vec<_> = word.chars().collect();
            arr.sort();

            words.entry(arr).or_default().push(word);
        }

        // O(n)
        words.into_values().collect()
    }
}
