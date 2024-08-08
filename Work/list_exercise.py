import time
import random

def read_matrix(n, m):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

num = int(input())
x1 = int(input())
matrix = read_matrix(num-1,3)

# # 进行数据生成以便进行实验
# num = 100000
# num_list = list(range(num))
# matrix = []
# x1 = num_list[0]
# for i in range(1,num):
#     insert_index = random.randint(0,i-1)
#     is_right = random.randint(0,1)
#     matrix.append([num_list[i],num_list[insert_index],is_right])
# print(matrix)

start_time = time.time()

# 通过这个例子熟悉列表索引和列表插入操作
serial_list = []
serial_list.append(x1)

for i in range(1,num):
    if matrix[i-1][2] == 1:
        actual_insert_index = serial_list.index(matrix[i-1][1])+1
    else:
        actual_insert_index = serial_list.index(matrix[i-1][1])
    serial_list.insert(actual_insert_index,matrix[i-1][0])

print(" ".join(map(str,serial_list)))
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
