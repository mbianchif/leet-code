use std::{cmp::Reverse, collections::BinaryHeap};

struct MedianFinder {
    lo: BinaryHeap<i32>,
    hi: BinaryHeap<Reverse<i32>>,
}

impl MedianFinder {
    fn new() -> Self {
        Self {
            lo: BinaryHeap::new(),
            hi: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        // O(logn)
        self.lo.push(num);

        let &lo = self.lo.peek().unwrap();
        if let Some(&Reverse(hi)) = self.hi.peek() {
            if lo > hi {
                // O(logn)
                self.lo.pop();
                self.hi.push(Reverse(lo));
            }
        }

        if self.lo.len() > self.hi.len() + 1 {
            // O(logn)
            self.lo.pop();
            self.hi.push(Reverse(lo));
        }

        if self.hi.len() > self.lo.len() + 1 {
            // O(logn)
            let Reverse(hi) = self.hi.pop().unwrap();
            self.lo.push(hi);
        }
    }

    fn find_median(&mut self) -> f64 {
        let &a = self.lo.peek().unwrap();
        let Some(&Reverse(b)) = self.hi.peek() else {
            return a as f64;
        };

        let lo = self.lo.len();
        let hi = self.hi.len();

        if lo - hi == 1 {
            return a as f64;
        }

        if hi - lo == 1 {
            return b as f64;
        }

        (a + b) as f64 / 2.0
    }
}
