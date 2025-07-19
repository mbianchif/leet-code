use std::{cell::RefCell, collections::VecDeque, rc::Rc};

type Node = Option<Rc<RefCell<TreeNode>>>;

impl Solution {
    fn get_nodes(queue: &mut VecDeque<(usize, Node)>) -> Vec<(usize, i32)> {
        let Some((lvl, node)) = queue.pop_front() else {
            return vec![];
        };

        let mut ret = match node {
            None => vec![],
            Some(root) => {
                let mut borrowed = root.borrow_mut();
                queue.push_back((lvl + 1, borrowed.left.take()));
                queue.push_back((lvl + 1, borrowed.right.take()));
                vec![(lvl, borrowed.val)]
            }
        };

        // O(n)
        ret.append(&mut Self::get_nodes(queue));
        ret
    }

    pub fn level_order(root: Node) -> Vec<Vec<i32>> {
        // O(n)
        let nodes = Self::get_nodes(&mut VecDeque::from([(0, root)]));
        let Some(levels) = nodes.last().map(|(lvl, _)| *lvl + 1) else {
            return vec![];
        };

        // O(logn)
        nodes
            .into_iter()
            .fold(vec![Vec::new(); levels], |mut acc, (lvl, val)| {
                acc[lvl].push(val);
                acc
            })
    }
}
