# [剑指 Offer II 036. 后缀表达式](https://leetcode.cn/problems/8Zf90G/)

- 标签：栈、数组、数学
- 难度：中等

## 题目大意

给定一个字符串数组 `tokens`，表示「逆波兰表达式」，求解表达式的值。

## 解题思路

栈的典型应用。遍历字符串数组。遇到操作字符的时候，取出栈顶两个元素，进行运算之后，再将结果入栈。遇到数字，则直接入栈。

## 代码

```Python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                stack.append(int(1 / stack.pop() * stack.pop()))
            else:
                stack.append(int(token))
        return stack.pop()
```

