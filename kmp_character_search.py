import sys
def build_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # 长度
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = build_lps(pattern)
    i = 0  # text 的索引
    j = 0  # pattern 的索引
    count = 0  # 记录匹配次数

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            count += 1
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return count



if __name__ == "__main__":
    str_num = str(sys.argv[1])
    print(kmp_search(str_num,"2023"))
