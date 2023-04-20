# [剑指 Offer II 084. 含有重复元素集合的全排列 ](https://leetcode.cn/problems/7p8L0Z/)

- 标签：数组、回溯
- 难度：中等

## 题目大意

给定一个可包含重复数字的序列 `nums` 。

要求：按任意顺序返回所有不重复的全排列。

## 解题思路

这道题跟「[剑指 Offer II 083. 没有重复元素集合的全排列](https://leetcode.cn/problems/VvJkup/)」不一样的地方在于增加了序列中的元素可重复这一条件。这就涉及到了去重。先对 `nums` 进行排序，然后使用 visited 数组标记该元素在当前排列中是否被访问过。若未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。

然后再递归遍历下一层元素之前，增加一句语句进行判重：`if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue`。

然后进行回溯遍历。

## 代码

```Python
class Solution:
    res = []
    path = []

    def backtrack(self, nums: List[int], visited: List[bool]):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue

            if not visited[i]:
                visited[i] = True
                self.path.append(nums[i])
                self.backtrack(nums, visited)
                self.path.pop()
                visited[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        self.path.clear()
        nums.sort()
        visited = [False for _ in range(len(nums))]
        self.backtrack(nums, visited)
        return self.res
```

