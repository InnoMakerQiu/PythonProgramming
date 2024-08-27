class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.n = n

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        sum_ = 0
        while i > 0:
            sum_ += self.bit[i]
            i -= i & -i
        return sum_

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
    

# Example usage:
arr = [1, 7, 3, 0, 7, 8, 3, 2, 6, 2]
n = len(arr)
fenwick = FenwickTree(n)

# Build the tree
for i in range(n):
    fenwick.update(i + 1, arr[i])

# Query the sum of the first 5 elements (1-based index)
print(fenwick.query(5))  # Output: 18 (1 + 7 + 3 + 0 + 7)

# Update the 3rd element (arr[2]) by adding 5
fenwick.update(3, 5)

# Query again after update
print(fenwick.query(5))  # Output: 23 (1 + 7 + 8 + 0 + 7)