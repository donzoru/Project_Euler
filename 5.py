def gcd(a,b):
	if( b == 0 ) :
		return a;
	else : 
		return gcd( b,a%b);
def lcm(a,b):
	return int(a/gcd(a,b)*b);
ans = 1;
for i in range(2,20) :
	ans = lcm(ans,i);
	
print(ans);