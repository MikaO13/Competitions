for _ in range(int(input())):
	n=int(input())
	a=sorted(list(map(int,input().split())))
	ans=0
	for i in range(n):
		if a[i]<=i+1:
			ans=i+1
	print(ans+1)