def all_variants(text):
    for x in range(len(text)):
        for j in range(len(text) - x):
            yield text[j: j + x + 1]

a = all_variants("abc")
for i in a:
    print(i)