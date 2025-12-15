impl Solution {
    const MOD: usize = 10usize.pow(9) + 7;

    pub fn number_of_ways(corridor: String) -> i32 {
        let mut chars = corridor.char_indices();
        let mut find_next_seat = || chars.find_map(|(i, c)| (c == 'S').then_some(i));
        let mut ways = 1;

        // O(n)
        find_next_seat();

        // O(n)
        let Some(mut last_right) = find_next_seat() else {
            return 0;
        };

        // O(n)
        while let Some(left) = find_next_seat() {
            let Some(right) = find_next_seat() else {
                return 0;
            };

            let plants = left - last_right;
            ways = (ways * plants) % Self::MOD;
            last_right = right;
        }

        ways as i32
    }
}
