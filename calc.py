import matrix

def dot(A,B):
	n=len(A);
	m=len(B)
	cal=0
	temp=[]
	answer=[[] for i in range(n)]
	for i in range(n):
		for j in range(m):
			for k in range(m):
				cal^=A[i][k]&B[k][j]
			temp.append(cal)
			cal=0
		answer[i]=temp
		temp=[]
	return answer
	
	
def printmatrix(matrix):
	for i in range(0,len(matrix)):
		print matrix[i]

def gfunc(n,temp):
	temp=calculat(n,matrix.matrix30,temp)
	output=[]
	#print temp
	for i in range(30):
		output.append(temp[i][1]^temp[i][13]^(temp[i][13]&temp[i][1]))
	for i in range(30):
		for j in range(i+1,30):
			output.append((temp[i][1]&temp[j][13])^(temp[i][13]&temp[j][1]))
	return output,temp

	
def calculat(n,matrixcalc,temp):
	for i in range(0,n):
		temp=dot(temp,matrixcalc)
	return temp

def solve( ma):
	#printmatrix(ma)
	global m; m = ma 
	n = len( m )
	n2=len(m[1])
	print n,len(m[1])
	i = 0; j = 0; row_pos = 0; col_pos = 0; ik = 0; 
	mik = True;    
	while( ( row_pos < n ) and( col_pos < n2 ) ):
		mik=True
		ik=row_pos
		for i in range( row_pos, n ):  
			if m[i][col_pos] :  
				mik = False
				ik = i  
				break
		if mik:  
			col_pos = col_pos + 1
			continue  
		if( ik != row_pos ):  
			m[row_pos],m[ik]=m[ik],m[row_pos]
		for i in range(0,n):
			if i != row_pos and m[i][col_pos]:  
				j = n2-1   
				while( j >= col_pos ):  
					m[i][j] ^=m[row_pos][j]  
					j = j - 1   
		row_pos = row_pos + 1; col_pos = col_pos + 1  
	return 1  



	
output="0000101000011101001101011101101111011111010101110111010110111111101111101000111011110110111111111010111010000011010000011011011110100100100110110110111010001000001000101011100010011110110110111011100111101111111011111110111011111111111110101110101000011101001110010110111101011001111010010001111111010010000011011100110011111111101110111000111101111010111010100111000010100110110101101101111101111111100110111000111111101010101110101110110111011110010010101011011101111111110111110100001111111111101000011011001101011100010011011011000111110111011101111110011111110101111101101100111111011111101111111110110011110100110111111101101001011111101001101011110001010110111001010111101011101010111111101111111111100111100111111110001111011010001111111011101001000010000010010100101010111111111100001100111101110011001011010101110111110001111011101010011111111011111111010001011100010110101001100110110111010100011110001111111100101111000011100010111101100011111101001010000001111011000111010101101110011110010000011111011101111000000111101001100111000100110101000011000100100001100001111110111011100101111010011100110000010011010101010011111111000010011010000111101011100101111111011110111101101110111111101101000101110011111011001110110010010101000011011001011100101000110111110010111111101001010110001110000111100111011101101010110101101100011100100010111101010110011101111101001101111111000111110111010010100101001101110101000101100001000000001001011001100011111110110110111000001110011000011011100110011101000101111011011001101001100011011110001011111110101001001111101101011111101011100100111110001110110011111011100111101010110101111011011"
length=len(output)
count=-1
j=0
temp=matrix.matrix30
calcuarr=[[] for i in range(1000)]
answer=[]



for i in range(length):
	count+=1
	if output[i]=='1':
		answer,temp=gfunc(count,temp)
		count =0
		answer.append(1)
		# print answer
		calcuarr[j]=answer
		j+=1
solve(calcuarr)
# print m[:30]
for i in range( 0, 30):  
	 print "x[%d] = %d" % (i, m[i][len( m[1])-1])  	


	
	
# printmatrix(matrix.matrix30)
# printmatrix(matrix.matrix50)
# printmatrix(matrix.matrix100)

{ 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1 };