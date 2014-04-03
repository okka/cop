"""
1
1
0
1
1
0
1
0
1
0
1
1
1
1
1
1
1
1
0
1
0
1
1
0
1
0
1
0
0
1
0
0
0
0
1
0
0
0
1
0
0
1
0
0
0
0
0
0
1
0
0
1
0
0
0
1
0
0
0
0
1
0
0
0
0
0
1
1
0
0
0
1
"""
mat = {}
"""
mm = input("m: ") 
nn = input("n: ") 

m = (int)(mm)
n = (int)(nn)
"""
m=8
n=9

i=1
j=1
while (i <= m):
	while (j <= n):
		mat[(i, j)] = input()
		j = j + 1
	i = i + 1
	j = 1

tam = {}
i=1
j=1
while (i <= m):
	while (j <= n):
		print(mat[(i, j)], end=' ')
		
		j = j + 1
	print(" ")	
	i = i + 1
	j = 1


i=1
j=1

ss = {}
while (i <= m):
	S = set()
	while (j <= n):
		if ((int)(mat[(i, j)])==1):
			S.add(j)
		
		j = j + 1
	ss[i] = S
	
	i = i + 1
	j = 1
print(' ')
print("ensemble des colones non zero de chaque ligne!")
print(' ')
print(ss)

gr = {}
i=1
j=1
cot = 1
ch = {}
cc = {}
stt = ""
while ((j < m) and (cot == 1)):
	st = str(j)
	while (i < m):
		gr[(i,1)] = ss[j]-ss[i+1]
		gr[(i,2)] = ss[j]&ss[i+1]
		gr[(i,3)] = ss[i+1]-ss[j]
		if((gr[(i, 1)] != set()) and (gr[(i, 2)] != set()) and (gr[(i, 3)] != set())):
			st = st + str(i+1)
			
		i = i + 1 
	"""cot"""
	if (len(st) == 1):
		
		stt = stt + str(j)
		ch[j] = ""+str(ss[j])
		j = j + 1
	elif (len(st) == 2):
		
		stt = stt + str(j)
		ch[j] = ""+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])
		ch[j+1] = ""+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])
		j = j + 2

	elif (len(st) == 3) : 
			
		stt = stt + str(j)
		if ((len(ss[j]&ss[j+2])<len(ss[j]&ss[j+1]))and(len(ss[j]&ss[j+2])<len(ss[j+1]&ss[j+2]))):
			ch[j] = ""+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])+str(ss[j+2]-(ss[j+1]|ss[j]))
			ch[j+1] = ""+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])+str(ss[j+2]-(ss[j+1]|ss[j]))
			ch[j+2] = ""+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])+str(ss[j+2]-(ss[j+1]|ss[j]))
		elif((len(ss[j]&ss[j+2])>len(ss[j]&ss[j+1]))or(len(ss[j]&ss[j+2])>len(ss[j+1]&ss[j+2]))):
			ch[j] = ""+str(ss[j+2]-(ss[j+1]|ss[j]))+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])
			ch[j+1] = ""+str(ss[j+2]-(ss[j+1]|ss[j]))+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])
			ch[j+2] = ""+str(ss[j+2]-(ss[j+1]|ss[j]))+str(gr[(j, 1)])+str(gr[(j, 2)])+str(gr[(j, 3)])
		j = j + 3
		
	i = j

kk=1
kkk=1
while (kk<=len(ch)):
	while(kkk<=len(ch)):
		if (len(ch[kk])<len(ch[kkk])):
			chh=ch[kk]
			ch[kk]=ch[kkk]
			ch[kkk]=chh
		
		kkk=kkk+1
	kk=kk+1
	kkk=kk

print(' ')
print("ensemble des partition des colones de gauche à droite!")
print(' ')
print(ch)

print(' ')

cch = ""

k=len(ch)
while (k>0):
	cchh=""
	cchhh=""
	cchh=ch[k]
	kk=1
	kkk=1
	while (kk<len(cchh)):
		if ((cchh[kk]!='{')and(cchh[kk]!='}')and(cchh[kk]!=',')and(cchh[kk]!=' ')):
			cchhh=cchhh+cchh[kk]
			kkk=kkk+1
		kk=kk+1
	cch=cch+cchhh
	k=k-1
"""
print(cch)
"""


"""print(gr)"""
subs = {}
i=1
k=1
while (i<m):
		j = 1
		while (j <= 3):
			subs[(k)]=gr[(i, j)]
			k=k+1
			j=j+1
		i = i + 1

sets = {}
i=1
j=1
d=0
k=1
l=1
sch =""
inis = False
isin = set()
while (d<len(cch)):
	setofset = {}
	o=0+(int)(cch[d])
	inis=False
	if (o in isin):
		inis = True
	k=1
	i=1
	while (i<m):
		j = 1
		while (j <= 3):
			if ((o in gr[(i, j)])and (inis==False) ):
				setofset[k] = gr[(i, j)]
				isin.add(o)
				k=k+1
			j=j+1
		i = i + 1
	k=1
	kk=1
	while (k<=len(setofset)):
		while (kk<=len(setofset)):
			if (len(setofset[k])>len(setofset[kk])):
				per=setofset[k]
				setofset[k]=setofset[kk]
				setofset[kk]=per

			kk=kk+1
		k=k+1

	if (inis==False):
		sets[l]=setofset[1]
		sch = sch + str(sets[l])
		if (len(sets[l])>1):
			isin=isin|sets[l]
		
		l=l+1
	d=d+1

"""
print(sets)
print(sch)
"""
k=1
kk=1
ssch = ""
while (k<len(sch)):
	if ((sch[k]!='{')and(sch[k]!='}')and(sch[k]!=',')and(sch[k]!=' ')):
		ssch=ssch+sch[k]
		kk=kk+1
	k=k+1
"""
print(ssch)
"""
perm=""
i=len(ssch)
i=i-1

while (i>=0):
	perm=perm + ssch[i]
	i=i-1
"""
print(perm)
"""

res = {}
i=1
j=1

while (i <= m):
	while (j <= n):
		o=(int)(perm[j-1])
		tam[(i, j)]=mat[(i, o)]
		print(tam[(i, j)], end=' ')
		j = j + 1
	
	print(" ")	
	i = i + 1
	j = 1
	
k=0
i=1
j=1
p=1
kk=1
while (i <= m):
	lis=""
	while (j <= n):
		p=tam[(i, j)]
		lis=lis+str(p)	
		j = j + 1
	
	mis={}
	while (k<len(lis)):
		if (lis[k]!='0'):
			mis[kk]=k+1
			kk=kk+1
		k=k+1
	l=len(mis)
		
	res[i]=(mis[1], mis[l])
	
	i = i + 1
	j = 1
	k=0
	kk=1
print(' ')
print("ensemble des interval de 1 consecutive de chaque ligne!")
print(' ')
print(res)