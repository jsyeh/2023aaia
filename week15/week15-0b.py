# SOIT106_ADVANCE_012
a = list(map(int, input().split() ))

ans = 0
for b in a:
	if b == a[-1]: 
	ans += 1

print(ans-1)