def delete_duplicates(s):
    a = s.split(" ")
    a = set(a)
    result = ' '.join(a)
    return result


print(delete_duplicates('yellow grey white yellow black grey grey red'))