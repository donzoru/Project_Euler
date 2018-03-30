import math
memo = {}
def collatz(x):
	x = int(x)
	if not x in memo:
		if x == 1:
			memo[x] = 1;
		elif x % 2 == 0: 
			memo[x] = collatz(x//2) + 1
		else :
			memo[x] = collatz(3*x+1) + 1
	return memo[x]
maxx = int(0)
ans = 0
for i in range( 2, 1000001 ):
	t = collatz(i)
	if( t > maxx ) : 
		maxx = t
		ans = i
print(ans)