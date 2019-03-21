def constructString(DigitString, time):
    res = DigitString
    for i in range(time):
        res = res + "$"*(i+1) + res[::-1]
    return res


def get_N_char(N):
    str = constructString("12345", 4)
    #print(str)
    return str[N-1]


time = int(input())
while time > 0:
    time -= 1
    index = int(input())
    print(get_N_char(index))
