#THIS IS A TEST TEXT,TEST
def get_pat_index(text, pat):
    text_len = len(text)
    pat_len = len(pat)
    i = 0
    res = []
    while i <= text_len - pat_len:
        pre = i
        for j in range(pat_len):
            if text[pre] == pat[j]:
                pre += 1
            else:
                break

        if j+1 == pat_len:
            res.append(pre - pat_len)
        i += 1
        j = 0

    return res

Text = "THIS IS A TEST TEXT"
pat = "TEST"
res = get_pat_index(Text,pat)
print(res)

# N = int(input())
# while N > 0:
#     N -= 1
#     Text, pat = input().split(',')
#     res = get_pat_index(Text, pat)
#     print(' '.join(str(x) for x in res))
