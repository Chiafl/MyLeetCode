/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* reverseK(struct ListNode* head, int k);

struct ListNode* reverseKGroup(struct ListNode* head, int k){
    if (!head || !head->next){
        return head;
    }
    struct ListNode* temp = head, *newHead;
    int c = k;
    while (c>0){
        if (!temp) return head;
        temp = temp->next;
        c--;
    }
    newHead = reverseK(head, k);
    head->next = reverseKGroup(temp, k);
    return newHead;
}

struct ListNode* reverseK(struct ListNode* head, int k){
    if (!head || !head->next || k<=1){
        return head;
    }
    struct ListNode* newHead = reverseK(head->next, k-1);
    head->next->next = head;
    head->next = 0;
    return newHead;
}

