use std::{
    cmp::{Ordering, Reverse},
    collections::BinaryHeap,
};

impl PartialOrd for ListNode {
    fn partial_cmp(&self, b: &ListNode) -> Option<Ordering> {
        Some(self.cmp(b))
    }
}

impl Ord for ListNode {
    fn cmp(&self, b: &ListNode) -> Ordering {
        self.val.cmp(&b.val)
    }
}

impl Solution {
    pub fn merge_k_lists(lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        // O(n)
        let mut nodes: BinaryHeap<_> = lists.into_iter().flatten().map(Reverse).collect();
        let mut head = ListNode::new(0);
        let mut tail = &mut head;

        // O(Nlogn)
        while let Some(Reverse(mut node)) = nodes.pop() {
            if let Some(next) = node.next.take() {
                nodes.push(Reverse(next));
            }

            tail = tail.next.insert(node);
        }

        head.next
    }
}
