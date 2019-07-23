// struct ListNode {
//     int val;
//     struct ListNode *next;
// };
 
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* slow = 0;
    struct ListNode* fast = head;
    while (fast){
        head = fast;
        fast = (*fast).next;
        (*head).next = slow;
        slow = head;
    }
    return head;
}

