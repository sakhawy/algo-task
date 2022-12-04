#!/usr/bin/env python3

def helper(l1, l2):
    res = []
    
    while l1+l2:
        if l1[0] < l2[0]:
            res.append(l1.pop(0))
        else:
            res.append(l2.pop(0))

        if not l1:
            res += l2
            break

        if not l2:
            res += l1
            break
    
    return res


def merge(l):
    if len(l) == 1:
        return [l[0]]
    
    l1 = merge(l[:len(l)//2])
    l2 = merge(l[len(l)//2:])

    return helper(l1, l2)

def test():
    assert merge([1, 5,7,3,2]) == [1,2,3,5,7]
    assert merge([100000, 1, -10, 2]) == [-10, 1, 2, 100000]

if __name__ == '__main__':
    test()
