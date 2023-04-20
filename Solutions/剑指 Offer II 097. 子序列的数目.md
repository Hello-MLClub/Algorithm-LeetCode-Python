# [剑指 Offer II 097. 子序列的数目](https://leetcode.cn/problems/21dk04/)

- 标签：字符串、动态规划
- 难度：困难

## 题目大意

给定两个字符串 `s` 和 `t`。

要求：计算在 `s` 的子序列中 `t` 出现的个数。

## 解题思路

动态规划求解。

定义状态 `dp[i][j]`表示为：以 `i - 1` 为结尾的 `s` 子序列中出现以 `j - 1` 为结尾的 `t` 的个数。

则状态转移方程为：

- 如果 `s[i - 1] == t[j - 1]`，则：`dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]`。即 `dp[i][j]` 来源于两部分：
    - 使用 `s[i - 1]` 匹配 `t[j - 1]`，则 `dp[i][j]` 取源于以 `i - 2` 为结尾的 `s` 子序列中出现以 `j - 2` 为结尾的 `t` 的个数，即 `dp[i - 1][j - 1]`。
    - 不使用 `s[i - 1]` 匹配 `t[j - 1]`，则 `dp[i][j]` 取源于以 `i - 2` 为结尾的 `s` 子序列中出现以 `j - 1` 为结尾的 `t` 的个数，即 `dp[i - 1][j]`。
- 如果 `s[i - 1] != t[j - 1]`，那么肯定不能用 `s[i - 1]` 匹配 `t[j - 1]`，则 `dp[i][j]` 取源于 `dp[i - 1][j]`。

下面来看看初始化：

- `dp[i][0]` 表示以 `i - 1` 为结尾的 `s` 子序列中出现空字符串的个数。把 `s` 中的元素全删除，出现空字符串的个数就是 `1`，则 `dp[i][0] = 1`。
- `dp[0][j]` 表示空字符串中出现以 `j - 1` 结尾的 `t` 的个数，空字符串无论怎么变都不会变成 `t`，则 `dp[0][j] = 0`
- `dp[0][0]` 表示空字符串中出现空字符串的个数，这个应该是 `1`，即 `dp[0][0] = 1`。

然后递推求解，最后输出 `dp[size_s][size_t]`。

## 代码

```Python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        size_s = len(s)
        size_t = len(t)
        dp = [[0 for _ in range(size_t + 1)] for _ in range(size_s + 1)]
        for i in range(size_s):
            dp[i][0] = 1
        for i in range(1, size_s + 1):
            for j in range(1, size_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[size_s][size_t]
```

