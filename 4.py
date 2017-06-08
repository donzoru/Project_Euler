import math
ans = 0;
for i in range(100,999) :
	for j in range(i+1,999) :
		a = i * j;
		s = str(a);
		n = 0;
		for k in range(0,int(len(s)/2)):
			if( s[k] == s[int(len(s))-k-1] ) : n=n+1;
		if ( n == int(len(s) / 2) ) : ans = max(ans,a);
print(ans);