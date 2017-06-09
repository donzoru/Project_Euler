n = 2000002
a = [0,0,1];
for i in range(3,n): 
	if( i % 2 == 0 ):a.append(0);
	else : a.append(1);
for i in range(2,int(n**0.5+1)):
	if( a[i]==1 ) : 
		for j in range ( i*i,n,2*i ):
			a[j] = 0;
ans = 0;
for i in range( 2, n ) :
	if( a[i] == 1 ) : ans += i;
print(ans);
