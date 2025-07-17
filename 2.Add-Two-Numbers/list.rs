impl Solution {
    pub fn add_two_numbers(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut l3 = None;
        let mut iter = &mut l3;
        let mut leftover = 0;

        // O(n)
        loop {
            let mut sum = 0;
            if let Some(node) = l1 {
                sum += node.val;
                l1 = node.next;
            }

            if let Some(node) = l2 {
                sum += node.val;
                l2 = node.next;
            }

            sum += leftover;
            leftover = sum / 10;
            sum -= leftover * 10;

            match iter {
                None => *iter = Some(Box::new(ListNode::new(sum))),
                Some(node) => node.val = sum,
            }

            if (l1.is_none() && l2.is_none() && leftover == 0) {
                break;
            }

            if let Some(node) = iter {
                node.next = Some(Box::new(ListNode::new(0)));
                iter = &mut node.next;
            }
        }

        return l3;
    }
}
