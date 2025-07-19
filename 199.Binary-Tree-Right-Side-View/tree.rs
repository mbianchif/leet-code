use std::{cell::RefCell, rc::Rc};

impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let Some(root) = root else {
            return Vec::new();
        };

        let mut root = root.borrow_mut();
        let l = root.left.take();
        let r = root.right.take();

        // O(n)
        let mut l = Self::right_side_view(l);
        let mut r = Self::right_side_view(r);
        r.extend(l.drain(r.len().min(l.len())..));

        let mut ret = vec![root.val];
        ret.append(&mut r);
        ret
    }
}
