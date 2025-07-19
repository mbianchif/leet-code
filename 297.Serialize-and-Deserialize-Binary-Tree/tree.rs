use std::{cell::RefCell, rc::Rc};
type Node = Rc<RefCell<TreeNode>>;

struct Codec {}

impl Codec {
    const EMPTY: &'static str = ".";

    fn new() -> Self {
        Self {}
    }

    fn serialize(&self, root: Option<Node>) -> String {
        root.map(|node| {
            let mut node = node.borrow_mut();
            let val = node.val.to_string();
            // O(n)
            let left = self.serialize(node.left.take());
            let right = self.serialize(node.right.take());
            format!("{val} {left} {right}")
        })
        .unwrap_or(String::from(Self::EMPTY))
    }

    fn create_node<'a, I: Iterator<Item = &'a str>>(stream: &mut I) -> Option<Node> {
        let val = stream
            .next()
            .filter(|&num| num != Self::EMPTY)?
            .parse()
            .unwrap();

        let mut tree_node = TreeNode::new(val);
        tree_node.left = Self::create_node(stream);
        tree_node.right = Self::create_node(stream);
        Some(Rc::new(RefCell::new(tree_node)))
    }

    fn deserialize(&self, data: String) -> Option<Node> {
        // O(n)
        Self::create_node(&mut data.split_whitespace())
    }
}
