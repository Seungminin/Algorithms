#Baekjoon_1463 -> 정수 N을 입력받았을 때 1로 만드는 최솟값을 출력.
def Min_count(num):
    number[1] = 0
    number[2] = 1
    number[3] = 1

    for i in range (4,num+1):
        if(i%3==0 and i%2==0): #3과 2로 나누어 떨어질 경우
            number[i] = min(number[i//3],number[i//2],number[i-1])+1
            print("{} index store the minimal count {}".format(i,number[i]))
        elif(i%3==0): #3으로만 나누어 떨어질 경우
            number[i] = min(number[i//3], number[i-1])+1
            print("{} index store the minimal count {}".format(i,number[i]))
        elif(i%2==0): #2로만 나누어 떨어질 경우
            number[i] = min(number[i//2], number[i-1])+1
            print("{} index store the minimal count {}".format(i,number[i]))    
        else:       #그렇지 않은 경우는 -1을 해주어서 횟수를 구한다 
            number[i] = number[i-1]+1
            print("{} index store the minimal count {}".format(i,number[i]))
    return number[num]

N = int(input("Please type number : "))
number = [0]*(N+1)
while 1:
    if(N<0 and N>10**6):
        N=int(input("Please type integer again : "))
    else:
        print("The minial count : ", Min_count(N))
        break