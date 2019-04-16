# solution 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 自己定义的ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_dic = {}
        result = []
        counter = 0
        while (l1 or l2):
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            _sum = l1_val + l2_val
            if counter in result_dic.keys():  # input [1], [9, 9]
                _sum += result_dic[counter]
            if _sum >= 10:
                result_dic[counter] = _sum % 10
                result_dic[counter + 1] = 1  # 进位
            else:
                result_dic[counter] = _sum
            # else:
            #    result_dic[counter] += _sum
            counter += 1
        for i in range(len(result_dic.keys())):
                result.append(result_dic[i])
        return result

