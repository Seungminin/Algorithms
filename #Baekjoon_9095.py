#Baekjoon_9095.py

dp = [0] * (11) #initialize the array with zero

def Ways_Sums(num):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if(num>3):
        for i in range (4, num+1):
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[num])
    else:
        print(dp[num])

test_case = int(input("Please type test case : "))

for _ in range(test_case):
    num = int(input("Please type num : "))
    Ways_Sums(num)