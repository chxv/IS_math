#!/usr/bin/env python3
#-*-coding=utf8-*-

# 最大公因数
import sys

def get_maxCommonFactor(a, b):
    '''
    输出计算最大公因数的全过程
    辗转相除（广义欧几里得除法）
    :param a:  factor A
    :param b:  factor B
    :return: None
    '''
    if a < b:
        a, b = b, a
    while True:
        remainder = a % b  # 余数
        quotient = a // b  # 商
        print(f'{a} = {b} * {quotient} + {remainder}')
        if remainder == 0:
            print('the greatest common factor is ', b)
            break
        a = b
        b = remainder

def get_process_variable(a, b):
    '''
        获得中间变量并保存在process列表中
        process保存每一步的商和余(商是计算下一步用不上的)
        return: process
    '''
    if a < b:
        a, b = b, a
    process=[(a,b)]
    while True:
        remainder = a % b  # 余数
        quotient = a // b  # 商
        process.append((quotient, remainder))
        if remainder == 0:
            break
        a=b
        b=remainder
    return process

def print_process(process):
    a=process[0][0]
    b=process[0][1]
    for i in process[1:]:
        print(f' {a} = {b} * {i[0]} + {i[1]} ')
        a=b
        b=i[1]
    # 最后的答案为最后一个a=b*q+r中的b,即倒数第二个process的余
    print('the great common factor is {}'.format(process[-2][1]))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        a = int(input())
        b = int(input())
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    a=abs(a)
    b=abs(b)
    p=get_process_variable(a,b)
    print_process(p)

