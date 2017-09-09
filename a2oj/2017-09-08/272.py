from sys import stdin

first = True
for line in stdin:
    chars = list(line)
    for i in range(len(chars)):
        if chars[i]=='"':
            if first:
                chars[i]="``"
            else:
                chars[i]="''"
            first = not first
    print(''.join(chars[:-1]))