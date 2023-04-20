class UnionFind:
    def __init__(self, n):                          # 初始化
        self.fa = [i for i in range(n)]             # 每个元素的集合编号初始化为数组 fa 的下标索引
        self.rank = [1 for i in range(n)]           # 每个元素的深度初始化为 1
    
    def find(self, x):                              # 查找元素根节点的集合编号内部实现方法
        while self.fa[x] != x:                      # 递归查找元素的父节点，直到根节点
            self.fa[x] = self.fa[self.fa[x]]        # 隔代压缩优化
            x = self.fa[x]
        return x                                    # 返回元素根节点的集合编号

    def union(self, x, y):                          # 合并操作：令其中一个集合的树根节点指向另一个集合的树根节点
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:                        # x 和 y 的根节点集合编号相同，说明 x 和 y 已经同属于一个集合
            return False
        
        if self.rank[root_x] < self.rank[root_y]:   # x 的根节点对应的树的深度 小于 y 的根节点对应的树的深度
            self.fa[root_x] = root_y                # x 的根节点连接到 y 的根节点上，成为 y 的根节点的子节点
        elif self.rank[root_y] > self.rank[root_y]: # x 的根节点对应的树的深度 大于 y 的根节点对应的树的深度
            self.fa[root_y] = root_x                # y 的根节点连接到 x 的根节点上，成为 x 的根节点的子节点
        else:                                       # x 的根节点对应的树的深度 等于 y 的根节点对应的树的深度
            self.fa[root_x] = root_y                # 向任意一方合并即可
            rank[y] += 1                            # 因为层数相同，被合并的树必然层数会 +1
        return True

    def is_connected(self, x, y):                   # 查询操作：判断 x 和 y 是否同属于一个集合
        return self.find(x) == self.find(y)