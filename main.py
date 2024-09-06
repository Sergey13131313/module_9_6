import itertools as it


def all_variants(text):
    l = len(text)
    begin = 0
    step = 1
    while step <= l:
        yield text[begin:begin + step]
        begin += 1
        if (begin + step) > l:
            step += 1
            begin = 0


a = 'abc'

result = all_variants(a)
for x in result:
    print(x)
