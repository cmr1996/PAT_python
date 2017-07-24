N = int(input())

for i in range(N):
  NUM = input().split(' ')
  A = int(NUM[0])
  B = int(NUM[1])
  C = int(NUM[2])
  if A > C - B:
    print("Case #%d: true" %(i+1))
  else:
    print("Case #%d: false" %(i+1))