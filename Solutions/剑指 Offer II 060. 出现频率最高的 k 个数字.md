# [剑指 Offer II 060. 出现频率最高的 k 个数字](https://leetcode.cn/problems/g5c51o/)

- 标签：数组、哈希表、分治、桶排序、计数、快速选择、排序、堆（优先队列）
- 难度：中等

## 题目大意

给定一个整数数组 `nums` 和一个整数 `k`。

要求：返回出现频率前 `k` 高的元素。可以按任意顺序返回答案。

## 解题思路

- 使用哈希表记录下数组中各个元素的频数。时间复杂度 $O(n)$，空间复杂度 $O(n)$。
- 然后将哈希表中的元素去重，转换为新数组。时间复杂度 $O(n)$，空间复杂度 $O(n)$。
- 利用建立大顶堆，此时堆顶元素即为频数最高的元素。时间复杂度 $O(n)$，空间复杂度 $O(n)$。
- 将堆顶元素加入到答案数组中，并交换堆顶元素与末尾元素，此时末尾元素已移出堆。继续调整大顶堆。时间复杂度 $O(log{n})$。
- 调整玩大顶堆之后，此时堆顶元素为频数第二高的元素，和上一步一样，将其加入到答案数组中，继续交换堆顶元素与末尾元素，继续调整大顶堆。
- 不断重复上步，直到 k 次结束。调整 k 次的时间复杂度 $O(nlog{n})$。

总体时间复杂度 $O(nlog{n})$。

因为用的是大顶堆，堆的规模是 N 个元素，调整 k 次，所以时间复杂度是 $O(nlog{n})$。
如果用小顶堆，只需维护 k 个元素的小顶堆，不断向堆中替换元素即可，时间复杂度为 $O(nlog{k})$。

## 代码

```Python
class Solution:
    # 调整为大顶堆
    def heapify(self, nums, nums_dict, index, end):
        left = index * 2 + 1
        right = left + 1
        while left <= end:
            # 当前节点为非叶子节点
            max_index = index
            if nums_dict[nums[left]] > nums_dict[nums[max_index]]:
                max_index = left
            if right <= end and nums_dict[nums[right]] > nums_dict[nums[max_index]]:
                max_index = right
            if index == max_index:
                # 如果不用交换，则说明已经交换结束
                break
            nums[index], nums[max_index] = nums[max_index], nums[index]
            # 继续调整子树
            index = max_index
            left = index * 2 + 1
            right = left + 1

    # 初始化大顶堆
    def buildMaxHeap(self, nums, nums_dict):
        size = len(nums)
        # (size-2) // 2 是最后一个非叶节点，叶节点不用调整
        for i in range((size - 2) // 2, -1, -1):
            self.heapify(nums, nums_dict, i, size - 1)
        return nums

    # 堆排序方法（本题未用到）
    def maxHeapSort(self, nums, nums_dict):
        self.buildMaxHeap(nums)
        size = len(nums)
        for i in range(size):
            nums[0], nums[size - i - 1] = nums[size - i - 1], nums[0]
            self.heapify(nums, nums_dict, 0, size - i - 2)
        return nums

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计元素频数
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        # 使用 set 方法去重，得到新数组
        new_nums = list(set(nums))
        size = len(new_nums)
        # 初始化大顶堆
        self.buildMaxHeap(new_nums, nums_dict)
        res = list()
        for i in range(k):
            # 堆顶元素为当前堆中频数最高的元素，将其加入答案中
            res.append(new_nums[0])
            # 交换堆顶和末尾元素，继续调整大顶堆
            new_nums[0], new_nums[size - i - 1] = new_nums[size - i - 1], new_nums[0]
            self.heapify(new_nums, nums_dict, 0, size - i - 2)
        return res
```

