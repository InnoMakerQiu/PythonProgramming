# 现在请求你维护一个数列，要求提供以下两种操作：
# 1、 查询操作。
# 语法：Q L
# 功能：查询当前数列中末尾 LL 个数中的最大的数，并输出这个数的值。
# 限制： L 不超过当前数列的长度。(L>0)
# 2、 插入操作。
# 语法：A n
# 功能：将 n 加上 t，其中 t 是最近一次查询操作的答案（如果还未执行过查询操作，则 t=0)，并将所得结果对一个固定的常数 D 取模，将所得答案插入到数列的末尾。
# 限制：n 是整数（可能为负数）并且在长整范围内。
# 注意：初始时数列是空的，没有一个数。

# 线段树需要有哪些性质
# 线段树的结构原理，

class SegmentTree:
    def __init__(self):
        """初始化线段树"""
        self.n = 0  # 当前数列长度
        self.tree = []
        self.last_query_result = 0  # 记录最近一次查询结果

    def build(self):
        """根据当前长度构建线段树"""
        if self.n > 0:
            self.tree = [0] * (2 * self.n)
            for i in range(self.n - 1, 0, -1):
                self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        """更新数列中的某个值，并更新线段树"""
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l):
        """查询末尾 L 个数中的最大值"""
        left = self.n - l + 1 + self.n
        right = self.n + self.n
        result = -float('inf')
        
        while left < right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                result = max(result, self.tree[right])
            left //= 2
            right //= 2

        self.last_query_result = result  # 记录最近一次查询的结果
        return result

    def add(self, n, D):
        """插入操作，将 n 加上最近一次查询结果并取模后插入到数列中"""
        value = (n + self.last_query_result) % D
        if self.n == len(self.tree) // 2:  # 如果树的容量已满，则扩展
            self.tree.extend([0] * (self.n))
        
        self.n += 1
        self.update(self.n - 1, value)

# 示例使用
D = 1000  # 假设固定常数 D = 1000

# 创建线段树
seg_tree = SegmentTree()

# 执行插入操作
seg_tree.add(5, D)  # 插入 5
seg_tree.add(10, D)  # 插入 10

# 查询末尾 2 个数中的最大值
print("Query result:", seg_tree.query(2))  # 输出 10

# 执行插入操作，n = 20
seg_tree.add(20, D)  # 插入 (20 + 10) % 1000 = 30

# 查询末尾 3 个数中的最大值
print("Query result:", seg_tree.query(3))  # 输出 30
