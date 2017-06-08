e = 4000000;
a = 1;
b = 2;
ans = 2;
while( (a < e) and (b < e) ) :
	a = a+b;
	if( a % 2 ==0 ) : ans += a;
	b = a+b;
	if( b % 2 ==0 ) : ans += b;
print(ans);	