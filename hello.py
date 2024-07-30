import sys

def mySqrt(x: int) -> int:
    if x < 2:
        return x  # 0 和 1 的情况直接返回
    
    left, right = 0, x
    
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right  # 当搜索结束时，right 指向的就是整数部分的平方根

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            x = int(sys.argv[1])
            result = mySqrt(x)
            print(f"输入的数字 {x} 的平方根的整数部分是: {result}")
        except ValueError:
            print("输入的不是有效的整数，请重新输入")
    else:
        print("请输入一个整数作为参数")