def encode_str(s):
    a = s[:len(s) // 2]
    b = s[len(s) // 2:]
    b = b[::-1]
    result = ''
    for i in range(len(a)):
        result = result + a[i] + b[i]
    return result


def decode_str(s1):
    a1 = s1[::2]
    b1 = s1[1::2]
    b1 = b1[::-1]
    return a1 + b1


print(encode_str('sandwich'))
print(decode_str('shacnidw'))