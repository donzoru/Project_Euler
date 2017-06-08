a = 2;
n = int(1000000);
t = 0;
a = [];
a.append(0);
a.append(0);
a.append(1);
for i in range(3,n):
	if(i % 2 == 0): a.append(0);
	else : a.append(1);
ans = 0;
for i in range(2,len(a)) :
	if( a[i] == 1) : 
		t=t+1;
		if( t == 10001 ) : 
			ans = i;
			break;
	for j in range(i*i,len(a),2*i):
		a[j]=0;
print(ans);
