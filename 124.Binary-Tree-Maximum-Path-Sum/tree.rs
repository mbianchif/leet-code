use std::cell::RefCell;
use std::rc::Rc;

type Link = Rc<RefCell<TreeNode>>;

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Link>,
//   pub right: Option<Link>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }

impl Solution {
    // Value given in description.
    const DEFAULT: i32 = -1000;

    pub fn max_path_sum(root: Option<Link>) -> i32 {
        let mut m = Self::DEFAULT;
        // O(n)
        Self::dfs(root.as_ref(), &mut m);
        m
    }

    fn dfs(root: Option<&Link>, m: &mut i32) -> i32 {
        root.map(|link| {
            let mut node = link.borrow();
            // O(n)
            let l = Self::dfs(node.left.as_ref(), m);
            let r = Self::dfs(node.right.as_ref(), m);
            let val = node.val;

            let ret = val.max(val + l).max(val + r);
            *m = (*m).max(l).max(r).max(val + l + r).max(ret);
            ret
        })
        .unwrap_or(Self::DEFAULT)
    }
}
