impl Solution {
    pub fn largest_rectangle_area(heights: Vec<i32>) -> i32 {
        let mut stack: Vec<(_, _)> = Vec::with_capacity(heights.len());

        // O(n)
        let max = heights.iter().enumerate().fold(0, |mut max, (x, &y)| {
            let mut start = x;

            while stack.last().map(|top| y < top.1).unwrap_or(false) {
                let (xs, ys) = stack.pop().unwrap();
                let area = (x - xs) as i32 * ys;
                max = max.max(area);
                start = xs;
            }

            stack.push((start, y));
            max
        });

        // O(n)
        stack.into_iter().fold(max, |max, (x, y)| {
            let area = (heights.len() - x) as i32 * y;
            max.max(area)
        })
    }
}
