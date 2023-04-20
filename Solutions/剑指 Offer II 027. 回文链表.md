# [剑指 Offer II 027. 回文链表](https://leetcode.cn/problems/aMhZSa/)

- 标签：栈、递归、链表、双指针
- 难度：简单

## 题目大意

给定一个链表的头节点 `head`。

要求：判断该链表是否为回文链表。

## 解题思路

利用数组，将链表元素依次存入。然后再使用两个指针，一个指向数组开始位置，一个指向数组结束位置，依次判断首尾对应元素是否相等，若都相等，则为回文链表。若不相等，则不是回文链表。

## 代码

```Python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        p1 = head
        while p1 != None:
            nodes.append(p1.val)
            p1 = p1.next
        return nodes == nodes[::-1]
```

