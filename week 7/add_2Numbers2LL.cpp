/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = NULL, *last = NULL;
        int carrier = 0;
        
        while (l1 != NULL || l2 != NULL) {
            ListNode *result = new ListNode;
            
            int num1 = (l1==NULL)? 0:l1->val;
            int num2 = (l2==NULL)? 0:l2->val;
            
            result->val = num1 + num2 + carrier;
            
            if (result->val >9) {
                result->val = result->val % 10;
                carrier = 1;
            }
            else {
                carrier = 0;
            }
            
            if (head==NULL) {
                head = result;
                last = result;
            } else {
                
                last->next = result;
                last = result;
            }
            
            if(l1!=NULL) {
                l1 =  l1->next;
            }
            if(l2!=NULL) {
                l2 =  l2->next;
            }
        }
        
        if(carrier==1) {
            ListNode *lastCarrier = new ListNode(carrier);
            last->next = lastCarrier;
            last = lastCarrier;
        }
        return head;
    }
};
