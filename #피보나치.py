#피보나치수.py
arr = [0] * 91 #배열은 90보다 작거나 같은 수.

def Fibbo(n):
    arr[0]=0
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

num = int(input("Please type num : "))
print("결과값은 : ",Fibbo(num))