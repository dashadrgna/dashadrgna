def reformat_string(s):
    a = s[:len(s) // 2]
    a_1 = s[len(s) // 2:]
    a = a[::-1]
    a_1 = a_1[::-1]
    result = a + a_1
    return result.lower()


print(reformat_string('Hello'))
print(reformat_string('Data'))
