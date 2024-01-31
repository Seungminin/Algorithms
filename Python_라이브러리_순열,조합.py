#Python 라이브러리 : Permutation, Combination
import itertools

arr = ['A','B','C','D','E','F']
nPr = itertools.permutations(arr,2) #nPr
nCr = itertools.combinations(arr,2) #nCr
print(list(nPr))
print(list(nCr))

#조건은 r이 한 개일 때 나열, 2개일 때 나열, 3개일 때 나열, 결국에는 (N+1)//2+1일 때까지 나열.
for r in range(1,4):
    for comb in itertools.combinations(range(1,7),r):
        row_list = list(comb)
        print(row_list)
'''만약 문제 조건 중에서 속한 영역에 어떤 거를 넣을 지 모르면 조합을 이용하면 된다.
    Permutation : 순열 nPr : 순서에 영향을 받는다.
    Combination : 조합 nCr : 순서에 영향을 받지 않는다.
'''