use std::collections::HashMap;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();
        let ops = HashMap::from([
            ("+", (|a, b| a + b) as fn(i32, i32) -> i32),
            ("-", |a, b| a - b),
            ("*", |a, b| a * b),
            ("/", |a, b| a / b),
        ]);

        // O(n)
        for token in tokens {
            match token.parse::<i32>() {
                Ok(num) => stack.push(num),
                Err(_) => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    let result = ops[token.as_str()](a, b);
                    stack.push(result);
                }
            }
        }

        stack.pop().unwrap()
    }
}
