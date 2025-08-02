def generate_incrementer(start):
    num = start
    def incrementer():
        nonlocal num
        num += 1
        return f'p{num}'
    return incrementer
incrementer = generate_incrementer()
print(incrementer())
