from email._header_value_parser import _check_for_early_dl_end

str = r"abc\n"
print(str)

a = 2.5e-2

print(a)

b = 2.5e2
c = 250.0

print(b)
print(b == c)

print(type(b))

print(isinstance(b, float))

print(3 / 2)

print(1 / 9)
print(3 ** -2)
print(-3 ** 2)
print((-3) ** 2)

print(3 < 4 < 5)
print(3 < 6 < 5)

t = 7
print(3 < t < 8)
print(3 < t < 6)

x = 3
y = 5

small = x if x < y else y
print(small)

assert 3 > 2

for i in str:
    print(i, end='')

print()

for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(2, 5, 2):
    print(i)

print()

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2
    print(i)
