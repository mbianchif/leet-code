impl Solution {
    pub fn get_row(matrix: &[Vec<i32>], target: i32) -> Option<usize> {
        let mut start = 0;
        let mut end = matrix.len();

        while start < end {
            let mid = (start + end) >> 1;
            let left = *matrix[mid].first().unwrap();
            let right = *matrix[mid].last().unwrap();

            if target < left {
                end = mid;
            } else if right < target {
                start = mid + 1;
            } else {
                return Some(mid);
            }
        }

        None
    }

    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let Some(idx) = Self::get_row(&matrix, target) else {
            return false;
        };

        matrix[idx].binary_search(&target).is_ok()
    }
}
