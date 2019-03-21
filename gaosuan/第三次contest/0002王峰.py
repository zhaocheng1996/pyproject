def divisible(N_nums, M_nums):
    res = []
    for m in M_nums:
        count = 0
        for n in N_nums:
            if n % m == 0:
                count += 1
        res.append(count)
    return res


T = int(input())
while T > 0:
    T -= 1
    NM = [int(x) for x in input().split(' ')]
    print(NM)
    N = NM[0]
    M = NM[1]
    N_nums = [int(x) for x in input().split(' ')]
    M_nums = [int(x) for x in input().split(' ')]
    res = divisible(N_nums, M_nums)
    print(' '.join(str(x) for x in res))
