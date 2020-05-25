string = 'Make a program that has some sentence on input and ' \
         'returns a dict containing all unique words as keys and the' \
         ' number of occurrences as values.'
a = string.split(' ')
b = set(a)
c = {x: a.count(x) for x in b}
print(c)
