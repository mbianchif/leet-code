use std::{cell::RefCell, rc::Rc};

impl Solution {
    fn __good_nodes(root: Option<Rc<RefCell<TreeNode>>>, cap: i32) -> i32 {
        root.map(|mut node| {
            let mut borrow = node.borrow_mut();
            let new_cap = cap.max(borrow.val);

            // O(n)
            let l = Self::__good_nodes(borrow.left.take(), new_cap);
            let r = Self::__good_nodes(borrow.right.take(), new_cap);
            let this = (borrow.val >= cap) as i32;

            l + this + r
        })
        .unwrap_or(0)
    }

    pub fn good_nodes(root: Option<Node>) -> i32 {
        // O(n)
        match root.as_ref().map(|node| node.borrow().val) {
            Some(val) => Self::__good_nodes(root, val),
            None => 0,
        }
    }
}
