n, d = map(int, raw_input().strip().split(' '))
numbers = map(int, raw_input().strip().split(' '))
print ' '.join(map(str, numbers[d:] + numbers[:d]))
