import math
a = 600851475143;
ans = 0;
t = int(a**0.5 + 1);
for i in range(2,t):
	if( a % i == 0) :
		ans = max(ans,i);
		while( a % i ==0 ) :
			a /= i;
if(a > 1): ans = max(ans,a);
print(ans);