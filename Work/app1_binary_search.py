import time

# 小明一共有 N 块巧克力，其中第 i 块是 Hi×Wi 的方格组成的长方形。为了公平起见，
# 小明需要从这 N 块巧克力中切出 K 块巧克力分给小朋友们。切出的巧克力需要满足：
# 1. 形状是正方形，边长是整数;
# 2. 大小相同

# 使用二分法进行求解，确定好left，right的变化即可
# 第一次解答这道题没有成功，没有思考清楚left以及right应该怎么正确变化，这个循环是否能够正常结束

N,K = map(int,input().split())
h_list,w_list = [],[]
for i in range(N):
    h,w = map(int,input().split())
    h_list.append(h)
    w_list.append(w)

start_time = time.time()
def is_enough(n:int):
    sum = 0
    for i in range(N):
        a=h_list[i]//n
        b=w_list[i]//n
        sum += a*b
        if sum >= K:
            return True
    return False   

def binary_search(left,right):
    while left < right:
        # print(left,right)
        mid = (right+left)//2
        if is_enough(mid):
            left = mid +1
        else:
            right = mid
    return left-1

print(binary_search(1,100000))

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)

