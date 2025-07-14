use std::collections::HashMap;

struct TimeMap {
    map: HashMap<String, Vec<(String, i32)>>,
}

impl TimeMap {
    fn new() -> Self {
        Self {
            map: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.map.entry(key).or_default().push((value, timestamp));
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        let Some(v) = self.map.get(&key) else {
            return String::new();
        };

        let idx = match v.binary_search_by(|(_, stamp)| stamp.cmp(&timestamp)) {
            Err(0) => return String::new(),
            Ok(idx) => idx,
            Err(idx) => idx - 1,
        };

        v[idx].0.clone()
    }
}
