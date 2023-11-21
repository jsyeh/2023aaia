# SOIT107_Base_006
x, y = list(map(int, input().split() ))

# 要小心空格、跳行、格式, 要看右下角黃色的錯誤差別, 並補齊錯誤
if x==y: 
	print( 'Enter two numbers:  It is a square ' , end='')
else:
	print( 'Enter two numbers:  It is not a square ' , end='')
