#!/usr/bin/env python3
# -*-coding=utf8-*-

'''
    获得 a，b间的所有素数 prime number
'''


def get_prime_num(a, b):
    # 筛法求素数
    if a > b:
        a, b = b, a

    shai = [0 for _ in range(0, b+1)]
    for i in range(2, b+1):
        if shai[i] == 0:  # 如果当前i是素数
            for j in range(i + i, b+1, i):  # 所有i的倍数都是合数
                shai[j] = 1
    a = 2 if a < 2 else a
    return [i for i in range(a, b+1) if shai[i] == 0]


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        a = int(input())
        b = int(input())
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    a = abs(a)
    b = abs(b)
    result = get_prime_num(a, b)
    print(result)
