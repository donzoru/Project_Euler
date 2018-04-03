a = []
for i in range ( 0, 41 ):
	a.append([])
	a[i].append( int(1) )
	for j in range ( 1,41 ):
		a[i].append( int(0) )
for i in range ( 1, 41 ):
	for j in range ( 1 , 41 ):
		a[i][j] = a[i-1][j] + a[i-1][j-1]
print( a[40][20] )