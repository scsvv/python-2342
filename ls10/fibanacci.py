def fibanacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a 
        a, b = b, a + b

# for num in fibanacci(10):
#     print(num)


def read_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()


for line in read_file("/workspaces/python-2342/text.txt"):
    print(line)