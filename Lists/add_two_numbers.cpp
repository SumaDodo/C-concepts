/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
      int carry = 0;
      ListNode h(0);
      ListNode* cur = &h;
      while(l1!=NULL || l2 != NULL || carry !=0)
      {
        int l1val = l1?l1->val:0;
        int l2val = l2?l2->val:0;
        if(l1) l1 = l1->next?l1->next:NULL;
        if(l2) l2 = l2->next?l2->next:NULL;
        ListNode* n = new ListNode(l1val+l2val+carry);
        cur->next = n;
        cur = n;
        carry = n->val/10;
        n->val = n->val%10;
      }
      return h.next;
        }
};
