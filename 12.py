def calu(n):
	t = int(n**0.5)
	ans = int(1)
	for i in range ( 2 , t ):
		tem = int(1);
		while( n%i == 0 ):
			tem = tem + 1
			n /= i
		ans = ans*tem
	return ans
sum = int(0)
for i in range ( 1 , 100000000 ):
	sum += int(i)
	if( calu(sum) >= 500) :
		print(sum);
		break;
		
