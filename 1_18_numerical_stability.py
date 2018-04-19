"""Softmax."""

a = 1000000000
b = 0.000001
for i in range(1000000):
    a = a + b
a = a - 1000000000
print(a)

