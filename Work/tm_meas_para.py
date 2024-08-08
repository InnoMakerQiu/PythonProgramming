import time
# 通过实验结果发现，python打印的效率很低，所以建议通过字符串叠加的方式，然后再最后一起打印
num = int(input())
start_time = time.time()

result = ""  # 用于存储结果的字符串

for i in range(0, num):
    if 2 * i < num:
        result += str(2 * (num - 1 - i)) + "\n"  # 进行字符串叠加并添加空格分隔
    else:
        result += str(2 * i) + "\n"  # 进行字符串叠加并添加空格分隔

print(result)

end_time = time.time()
execution_time = end_time - start_time
print(execution_time)