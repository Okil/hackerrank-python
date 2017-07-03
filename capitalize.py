text = '132 456 Wq  m e'
split = text.split(' ')
string = ''
for i in range(0, len(split)):
    result = split[i].capitalize()
    split[i] = result
print(' '.join(split))
