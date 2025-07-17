impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let (list1, list2, mut node) = match (list1, list2) {
            (None, None) => return None,
            (Some(mut node1), Some(node2)) if node1.val < node2.val => {
                (node1.next.take(), Some(node2), node1)
            }
            (list1, Some(mut node)) => (list1, node.next.take(), node),
            (Some(mut node), list2) => (node.next.take(), list2, node),
        };

        // O(n)
        node.next = Self::merge_two_lists(list1, list2);
        Some(node)
    }
}
