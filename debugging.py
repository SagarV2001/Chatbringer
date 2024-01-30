# def move(si,sj,hs):
#     print(f'{si} {sj}')
#     if (si,sj) in hs:
#         return MAX
#     hs.add((si,sj))
#     min_dis = dic.get((si,sj))
#     if min_dis:
#         return min_dis
#     if matrix[si][sj] == 1:
#         dic[(si,sj)] = MAX
#         return MAX
#     fi,fj = si+mi,sj+mj
#     ri,rj = si+mj,sj-mi
#     li,lj = si-mj,sj+mi
#     di,dj = si-mi,sj-mj
#     if (fi==ei and fj==ej) or (ri==ei and rj==ej) or (li==ei and lj==ej) or (di==ei and dj==ej):
#         dic[(si,sj)] = 1
#         return 1
#     ans = MAX
#     if fi<n and fi>=0 and fj<m and fj>=0:
#         ans = min(ans,move(fi,fj,set(hs)))
#     if ri<n and ri>=0 and rj<m and rj>=0:
#         ans = min(ans,move(ri,rj,set(hs)))
#     if li<n and li>=0 and lj<m and lj>=0:
#         ans = min(ans,move(li,lj,set(hs)))
#     if di<n and di>=0 and di<m and dj>=0:
#         ans = min(ans,move(di,dj,set(hs)))
#     dic[(si,sj)] = ans+1
#     return ans+1
#
#
# MAX = 9999999
# n,m = (int(x) for x in input().split())
# matrix = []
# for i in range(n):
#     matrix.append([int(x) for x in input().split()])
# starti,startj = (int(x) for x in input().split())
# ei,ej = (int(x) for x in input().split())
# mi,mj = (int(x) for x in input().split())
# dic = {}
# if starti == ei and startj == ej:
#     result = 0
# else:
#     result = move(starti,startj,set())
#     result = result if result!=MAX else -1
# print(result,end=' ')
#
#
#


# value_di = {}
# def execute(line):
#
#     if 'is' in line:
#         exp = line.split(' ')[-1]
#         ops = ['<','>','!=','==','>=','<=']
#         for op in ops:
#             if len(exp.split(op))>1:
#                 var1,var2 = exp.split(op)
#                 val1,val2 = value_di.get(var1),value_di.get(var2)
#                 res = f'{val1}{op}{val2}'
#                 res = eval(res)
#                 return res
#         return False
#     else:
#         if 'print' in line:
#             print(value_di.get(line.split(' ')[-1]))
#         return True
# script=[]
# inp = input()
# while 'print' in inp or 'is' in inp or 'si' in inp or 'Yes' in inp or 'No' in inp:
#     script.append(inp)
#     inp = input()
# variables = [x for x in inp.split(' ')]
# values = [int(x) for x in input().split(' ')]
# di={}
# for j in range(len(variables)):
#     value_di[variables[j]] = values[j]
# st=[]
# i=0
# while i < len(script):
#     line = script[i]
#     if 'is' in line:
#         st.append(('is',i))
#     if 'No' in line:
#         st.append(('No',i))
#     if 'Yes' in line:
#         st.append(('Yes',i))
#     if 'si' in line:
#         st.append(('si',i))
#         res = []
#         popped = st.pop()
#         while 'is' not in popped:
#             res.append(popped)
#             popped = st.pop()
#         di[popped[1]] = res
#     i+=1
# i=0
# while i < len(script):
#     line = script[i]
#     if execute(line):
#         if 'No' in line:
#             while 'si' not in line:
#                 i+=1
#                 line = script[i]
#         i += 1
#     else:
#
#         if di.get(i) and di.get(i)[0][0]=='No':
#             i = di.get(i)[0][1]+1
#         elif di.get(i) and len(di.get(i))>1 and di.get(i)[1][0]=='No':
#             i = di.get(i)[1][1]+1
#         elif di.get(i) and len(di.get(i))>2 and di.get(i)[2][0]=='No':
#             i = di.get(i)[1][1]+1
#         if di.get(i) and di.get(i)[0][0]=='si':
#             i = di.get(i)[0][1]+1
#         elif di.get(i) and len(di.get(i))>1 and di.get(i)[1][0]=='si':
#             i = di.get(i)[1][1]+1
#         elif di.get(i) and len(di.get(i))>2 and di.get(i)[2][0]=='si':
#             i = di.get(i)[1][1]+1

# value_di = {}
# def execute(line):
#     if 'is' in line:
#         exp = line.split(' ')[-1]
#         ops = ['<', '>', '!=', '==', '>=', '<=']
#         for op in ops:
#             if len(exp.split(op)) > 1:
#                 var1, var2 = exp.split(op)
#                 val1, val2 = value_di.get(var1, 0), value_di.get(var2, 0)
#                 return eval(f'{val1} {op} {val2}')
#         return False
#     else:
#         if 'print' in line:
#             print(value_di.get(line.split(' ')[-1]))
#         return True
#
# script=[]
# inp = input()
# while 'print' in inp or 'is' in inp or 'si' in inp or 'Yes' in inp or 'No' in inp:
#     script.append(inp)
#     inp = input()
# variables = [x for x in inp.split(' ')]
# values = [int(x) for x in input().split(' ')]
# di={}
# for j in range(len(variables)):
#     value_di[variables[j]] = values[j]
# st=[]
# i=0
# while i < len(script):
#     line = script[i]
#     if 'is' in line:
#         st.append(('is',i))
#     if 'No' in line:
#         st.append(('No',i))
#     if 'Yes' in line:
#         st.append(('Yes',i))
#     if 'si' in line:
#         st.append(('si',i))
#         res = []
#         popped = st.pop()
#         while 'is' not in popped:
#             res.append(popped)
#             popped = st.pop()
#         di[popped[1]] = res
#     i+=1
#
# i = 0
# while i < len(script):
#     line = script[i]
#     if execute(line):
#         if 'No' in line:
#             while 'si' not in line:
#                 i += 1
#                 line = script[i]
#         i += 1
#     else:
#         for condition in di.get(i):
#             if condition[0] == 'No':
#                 i = condition[1] + 1
#             elif condition[0] == 'si':
#                 i = condition[1] + 1


from collections import deque
def move(matrix,si,sj,ei,ej,mi,mj):
    n, m = len(matrix), len(matrix[0])
    q = deque([((si,sj), 0)])
    hs = set([(si,sj)])
    while q:
        (si, sj), distance = q.popleft()
        if (si, sj) == (ei,ej):
            return distance
        for di, dj in [(mi, mj), (mj, -mi), (-mi, -mj), (-mj, mi)]:
            ni, nj = si + di, sj + dj
            if 0<=ni<n and 0<=nj<m and matrix[ni][nj] == 0 and (ni, nj) not in hs:
                hs.add((ni, nj))
                q.append(((ni, nj), distance + 1))
    return -1

n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
starti,startj = (int(x) for x in input().split())
ei,ej = (int(x) for x in input().split())
mi,mj = (int(x) for x in input().split())

result = move(matrix,starti,startj,ei,ej,mi,mj)
print(result)