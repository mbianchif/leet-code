impl Solution {
    #[inline]
    fn div_ceil(a: i32, b: i32) -> i32 {
        (a as f64 / b as f64).ceil() as i32
    }

    fn eat_bananas(piles: &[i32], h: i32, k: i32) -> bool {
        let time = piles.iter().fold(0, |acc, x| acc + Self::div_ceil(*x, k));
        time <= h
    }

    fn search_k(piles: Vec<i32>, h: i32, (a, b): (i32, i32)) -> i32 {
        if a == b {
            return a;
        }

        let mid = (a + b) >> 1;
        let ended = Self::eat_bananas(&piles, h, mid);
        let range = if ended { (a, mid) } else { (mid + 1, b) };
        Self::search_k(piles, h, range)
    }

    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let range = (1, *piles.iter().max().unwrap());
        Self::search_k(piles, h, range)
    }
}
