def compute(n):
    return lambda x: x*n

result = compute(8)

print(f'the result is {result(1)}')