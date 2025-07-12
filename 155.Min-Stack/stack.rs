struct MinStack {
    inner: Vec<i32>,
    min: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        Self {
            inner: Vec::new(),
            min: Vec::new(),
        }
    }

    fn push(&mut self, val: i32) {
        self.inner.push(val);
        let min = self.min.last().map(|l| val.min(*l)).unwrap_or(val);
        self.min.push(min);
    }

    fn pop(&mut self) {
        self.inner.pop();
        self.min.pop();
    }

    fn top(&self) -> i32 {
        *self.inner.last().unwrap()
    }

    fn get_min(&self) -> i32 {
        *self.min.last().unwrap()
    }
}
