a = 0
b = 0
palindrom = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        s = str(product)
        if s == s[::-1]:
            if product > palindrom:
                palindrom = product

print palindrom