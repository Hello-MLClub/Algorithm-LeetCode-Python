# [剑指 Offer II 075. 数组相对排序](https://leetcode.cn/problems/0H97ZC/)

- 标签：数组、哈希表、计数排序、排序
- 难度：简单

## 题目大意

给定两个数组，`arr1` 和 `arr2`，其中 `arr2` 中的元素各不相同，`arr2` 中的每个元素都出现在 `arr1` 中。

要求：对 `arr1` 中的元素进行排序，使 `arr1` 中项的相对顺序和 `arr2` 中的相对顺序相同。未在 `arr2` 中出现过的元素需要按照升序放在 `arr1` 的末尾。

注意：

- `1 <= arr1.length, arr2.length <= 1000`。
- `0 <= arr1[i], arr2[i] <= 1000`。

## 解题思路

因为元素值范围在 `[0, 1000]`，所以可以使用计数排序的思路来解题。

使用数组 `count` 统计 `arr1` 各个元素个数。

遍历 `arr2` 数组，将对应元素`num2` 按照个数 `count[num2]` 添加到答案数组 `ans` 中，同时在 `count` 数组中减去对应个数。

然后在处理 `count` 中剩余元素，将 `count` 中大于 `0` 的元素下标依次添加到答案数组 `ans` 中。

## 代码

```Python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0 for _ in range(1010)]
        for num1 in arr1:
            count[num1] += 1
        res = []
        for num2 in arr2:
            while count[num2] > 0:
                res.append(num2)
                count[num2] -= 1

        for num in range(len(count)):
            while count[num] > 0:
                res.append(num)
                count[num] -= 1

        return res
```

