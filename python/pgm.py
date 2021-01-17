def even(num):
	if(num%2==0):
		return true
	else:
		return false
L=[]
i=0
while(i<=4):
	print("enter an element")
	num=int(input())
	L.insert(i,num)
	i=i+1
k=list(filter(even,L))
print(k)