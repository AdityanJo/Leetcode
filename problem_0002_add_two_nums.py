class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # res=ListNode(0)
        n1=''
        n2=''
        while l1!=None:
            n1+=str(l1.val)
            l1=l1.next
        while l2!=None:
            n2+=str(l2.val)
            l2=l2.next
        res=str(int(n1[::-1])+int(n2[::-1]))
        out=ListNode(0)
        head=out
        print(res)
        for i in range(len(res)):
            out.val=res[::-1][i]
            # print(i)
            # print(len(res))
            if i == len(res)-1:
                out.next=None
                break
            out.next=ListNode(0)
            out=out.next
        return head
        # return head_res
