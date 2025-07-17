#include <stdlib.h>

struct ListNode {
    struct ListNode *next;
};

struct ListNode *removeNthFromEndRec(struct ListNode *head, int *n) {
    if (!head) return NULL;

    // O(n)
    head->next = removeNthFromEndRec(head->next, n);
    if (!--*n) {
        struct ListNode *tmp = head->next;
        free(head);
        return tmp;
    }

    return head;
}

struct ListNode *removeNthFromEnd(struct ListNode *head, int n) {
    return removeNthFromEndRec(head, &n);
}
