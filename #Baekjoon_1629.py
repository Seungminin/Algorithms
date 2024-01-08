#Baekjoon_1629 Solution (파이썬으로 2진수 변환하기), bin함수 사용, Numberic Algorithm이용
import sys
def Make_bits(N): #파이썬 이진수 만들기
    binarynum = bin(N)
    return binarynum[2:]

def Find_reaminder(a, b_bits,n): #RSA 나머지 구하기 공식 사용
    c=0
    d=1
    k = len(b_bits)

    for i in range(k-1, -1,-1): 
        c=2*c
        d = (d*d) % n
        if b_bits[i] == '1':
            c+=1
            d=(d*a) % n
    return d

a,b,c = map(int,sys.stdin.readline().split())
B = []
B=Make_bits(b)
res = Find_reaminder(a,B,c)
print(res)