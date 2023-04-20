# [剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

- 标签：数组、双指针、排序
- 难度：简单

## 题目大意

给定一个整数数组 `nums`。

要求：将奇数元素位于数组的前半部分，偶数元素位于数组的后半部分。

## 解题思路

定义快慢指针 `slow`、`fast`，开始时都指向 `0`。

- `fast` 向前搜索奇数位置，`slow` 指向下一个奇数应当存放的位置。
- `fast` 不断进行右移，当遇到奇数时，将该奇数与 `slow` 指向的元素进行交换，并将 `slow` 进行右移。
- 重复上面操作，直到 `fast` 指向数组末尾。

## 代码

```Python
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1

        return nums
```

