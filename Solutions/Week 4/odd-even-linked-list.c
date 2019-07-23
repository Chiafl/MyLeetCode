/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* oddEvenList(struct ListNode* head){
    struct ListNode* oddHead = calloc(1,sizeof(struct ListNode));
    struct ListNode* odd = oddHead;
    struct ListNode* evenHead = calloc(1,sizeof(struct ListNode));
    struct ListNode* even = evenHead;
    char b = 0;
    while (head){
        if (b==0){
            odd->next = head;
            odd = odd->next;
            b = 1;
        }
        else{
            even->next = head;
            even = even->next;
            b = 0;
        }
        head = head->next;
    }
    even->next = 0;
    odd->next = evenHead->next;
    head = oddHead->next;
    free(oddHead);
    free(evenHead);
    return head;
}

