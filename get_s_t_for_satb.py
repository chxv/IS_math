#!/usr/bin/env python3
#-*-coding=utf8-*-

'''
    求整数s, t 使得 s*a+t*b = (a, b)
    其中a, b 已知

    配合广义欧几里得除法
'''
import maxCommonFactor
import sys

def bezout(p):
    '''
        通过广义欧几里得的公式计算步骤
        推导贝祖等式的计算步骤
        直接输出结果
        return: None
    '''
    great_factor=p[-2][-1]
    a=p[0][0]
    b=p[0][1]
    print(f'由广义欧几里得的计算方法可知:\n{great_factor} = ', end='')
    
    l = len(p)
    S, T = 1, 0
    
    if l > 3:
        i=l-2
        _s = -p[i][0]
        _b = p[i-1][1]
        _t = 1
        _a = p[i-2][1]
        equal = f'{_s} * {_b} + {_a}'  # 一个b的内部展开 
        S, T = S * _s + T, S
        print(f'\t{equal}')
 
    for i in range(l-3,1,-1):
        # (-q) * b + a
        # 临时变量s,b,t,a表示当前未展开的式子s*b+t*a
        _s = -p[i][0]
        _b = p[i-1][1]
        _t = 1
        _a = p[i-2][1]
        equal = f'{_s} * {_b} + {_a}'  # 一个b的内部展开 

        print(f'\t{S} * ({equal}) + {T} * {_b} ')
        S, T = S * _s + T, S
        print(f'\t{S} * {_b} + {T} * {_a}')
        
   # for之后的一次运算
    i=1
    _s = -p[i][0]
    _b = p[i-1][1]
    _t = 1
    _a = p[i-1][0]  # <- 唯一与循环内不同的地方
    equal = f'{_s} * {_b} + {_a}'
    print(f'\t{S} * ({equal}) + {T} * {_b} ')
    S, T = S * _s + T, S
    print(f'\t{S} * {_b} + {T} * {_a}')
 
    print('\n s,t 分别为  ',S,T)    


if __name__ == "__main__":
    if len(sys.argv) < 3:
        a = int(input())
        b = int(input())
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    a=abs(a)
    b=abs(b)
    # 在求最大公因数时已经使得a>b
    p=maxCommonFactor.get_process_variable(a,b)
    maxCommonFactor.print_process(p)
    bezout(p)

