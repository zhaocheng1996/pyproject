def cow_years(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return cow_years(n-1) + cow_years(n-2)


T = int(input())
while T > 0:
    N = input()
    T -= 1
    num = cow_years(int(N))
    print(num)
