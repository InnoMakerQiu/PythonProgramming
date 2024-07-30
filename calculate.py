def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10
    # 这里其实只要计算除个位以外的其他位数累加，对于除个位以外的数的影响
    digit = digit_sum//10
    if digit_sum %10 !=0:
        digit+=1
    return digit

def iterations_to_zero(n):
    # 对个位不进行考虑
    iterations = 1
    n = n // 10    
    while n > 0:
        n -= sum_of_digits(n)
        print(n)
        iterations += 1
    return iterations

# 示例
n = 999
result = iterations_to_zero(n)
print(f"需要迭代 {result} 次才能得到预期的结果。")

