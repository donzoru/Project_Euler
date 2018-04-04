n = 2**1000
ans = int(0)
while n :
	ans = ans + n % 10
	n //= 10
print(ans)