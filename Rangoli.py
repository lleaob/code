def rangoli(size):
    if size < 1 or size > 26:
        return 'NA'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    line = ''
    for char in range(size):
        line += alphabet[char] + '-'
    for char in range(len(line)):
        line += line[-char]

    return line

n = 5
print(rangoli(n))