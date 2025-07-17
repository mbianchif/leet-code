#include <stdbool.h>

struct ListNode {
    struct ListNode *next;
};

bool hasCycle(struct ListNode *head) {
    if (!head) {
        return false;
    }

    struct ListNode *slow = head;
    struct ListNode *fast = head;

    // O(n)
    while (true) {
        if (!fast) return false;
        fast = fast->next;
        
        if (!fast) return false;
        fast = fast->next;

        slow = slow->next;
        if (slow == fast) {
            return true;
        }
    }

    return false;
}
