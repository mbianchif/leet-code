use std::{cell::RefCell, rc::Rc};

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        root.map(|node| {
            {
                let mut borr = node.borrow_mut();
                let left = borr.left.take();
                let right = borr.right.take();

                // O(n)
                borr.right = Self::invert_tree(left);
                borr.left = Self::invert_tree(right);
            }

            node
        })
    }
}
