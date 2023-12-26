# 想研究前一個程式,是怎麼跑的
s = "00111"
N = len(s)
ans = 0
for left in range(N-1):
  print('left:', left, 'i<=left有誰?', end=' ')
  for i in range(N):
    if i<=left: print(s[i], end=' ') # 把 i<=left 的字都印出來
  print('i>left有誰?', end=' ')
  for i in range(N):
    if i>left: print(s[i], end=' ') # 把 i>left 的字都印出來
  print()

''' output 輸出結果
left: 0 i<=left有誰? 0 i>left有誰? 0 1 1 1 
left: 1 i<=left有誰? 0 0 i>left有誰? 1 1 1 
left: 2 i<=left有誰? 0 0 1 i>left有誰? 1 1 
left: 3 i<=left有誰? 0 0 1 1 i>left有誰? 1 
'''