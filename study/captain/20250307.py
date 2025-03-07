a = 13
b = bin(a)
c = oct(a)
d = hex(a)
print(a, b, c, d)
print(int(b, 2))
print(int(c, 8))
print(int(d, 16))

# 방법 1
n = a
arr = []
while n > 0:
    arr.append(n % 3)
    n //= 3
ans = ''.join(map(str, arr[::-1]))
print(ans)

# 방법 2
ans = ''
n = a
while n > 0:
    n, rest = divmod(n, 3)
    ans += str(rest)
print(ans[::-1])

# 되돌리기
print(int(ans, 3))


print(13 & 9)
print(13 | 9)
print(13 ^ 9)
print(10 << 2)