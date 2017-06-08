t = 1000;
flag = 0;
for i in range(1,t):
	for j in range(i+1,t):
		for k in range ( j+1,t):
			a = i ** 2 + j ** 2;
			b = k**2; 
			if(b > a) : break;
			print(a,b);
			if( (a == b) and (i+j+k==1000 )):
				print(i*j*k);
				flag = 1;
				break;
		if(flag==1) :break;
	if(flag==1) :break;
			