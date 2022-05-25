def replace_charancters(s):
    a = s.replace('g', 'G').replace('G', 'g', 1)
    return a


print(replace_charancters('In the hole in the ground there lived a grey ghost'))