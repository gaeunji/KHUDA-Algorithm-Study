
def check(str):
	check = False # true면 아님
	for i in range(len(str)):
		if str[i] == str[(len(str)-1)-i]:
			check = False
		else:
			check = True
			return check
	return check
			

M = int(input())
for j in range(M):
	N = int(input())
	arr = [input().strip() for _ in range(N)]

	found = False
	for i in range(N):
		for j in range(N):
			if i != j:
				new = list(arr[i]) + list(arr[j])
				rev = list(arr[j]) + list(arr[i])
				if(check(new) == False):
					answer = "".join(new)
					print(answer)
					found = True
					break
				elif(check(rev) == False):
					answer = "".join(rev)
					print(answer)
					found = True
					break
		if found:
			break
	if not found:
		print(0)
			
