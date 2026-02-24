n = int(input())
p =0
d=0
c = list(map(int, input().split()))
for i in range(n):
	if c[i] >=1:
		p +=c[i]
	elif c[i] == -1 and p>0:
		p -=1
	elif c[i] == -1 and p == 0:
		d +=1
print(d)
