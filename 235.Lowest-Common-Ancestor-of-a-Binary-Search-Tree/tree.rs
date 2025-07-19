use std::{cell::RefCell, rc::Rc};

impl Solution {
    fn lca(root: Option<Rc<RefCell<TreeNode>>>, p: i32, q: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(node) = root else {
            return None;
        };

        let mut borrow = node.borrow_mut();
        if borrow.val == p || borrow.val == q {
            drop(borrow);
            return Some(node);
        }

        // O(n)
        let left = Self::lca(borrow.left.take(), p, q);
        let right = Self::lca(borrow.right.take(), p, q);
        drop(borrow);

        if left.is_some() && right.is_some() {
            Some(node)
        } else {
            left.or(right)
        }
    }

    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        let p = p.unwrap().borrow().val;
        let q = q.unwrap().borrow().val;

        // O(n)
        Self::lca(root, p, q)
    }
}
