def str_count(s_f, s_s):
    len_f = len(s_f)
    len_s = len(s_s)

    if len_s == 0:
        return len_f + 1

    cnt = 0
    idx = 0

    while (idx + len_s - 1 < len_f):
        if(s_f[idx:idx+len_s] == s_s):
            cnt += 1
            idx += len_s
        else:
            idx += 1

    return cnt

s_full = input('Enter a string: ')
s_sub = input('Enter a substring: ')

cnt = str_count(s_full, s_sub)
cnt_ref = s_full.count(s_sub)

print('My answer: {}'.format(cnt))
print('Correct answer: {}'.format(cnt_ref))