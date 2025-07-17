impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        // O(n)
        let s = s.into_bytes();
        let mut field = [false; 256];
        let mut l = 0;

        // O(n)
        (0..s.len()).fold(0, |max, r| {
            let ch_r = s[r] as usize;

            while field[ch_r] {
                field[s[l] as usize] = false;
                l += 1;
            }

            field[ch_r] = true;
            max.max((r - l) as i32)
        })
    }
}
