#python_라이브러리 queue
#python에서 Stack을 구현하는 방법
'''
    #Push
    a_list = [1,2,3]
    a_list.append(1)
    => [1,2,3,1]
    #Pop
    a_list = [1,2,3]
    a_list.pop()
    => [1,2]

    print(a_list.pop())
    출력: 2
    a_list : [1]
'''
import queue
#put : queue에 정보를 넣는 것
#get : 정보를 빼는 것.

#FIFO version
data_queue = queue.Queue()

data_queue.put('abc')
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get()) #abc가 먼저 들어갔기 때문에 먼저 출력이된다.

print(data_queue.qsize())
print(data_queue.get())

print("------------------------------------------------------")
#LIFO -> Last in First out : 마직막으로 들어온 게 먼저 나가는 것 = Stack구조
data_queue2 = queue.LifoQueue()

data_queue2.put('abc')
data_queue2.put(1)

print(data_queue2.qsize())
print(data_queue2.get()) #1이 마지막 들어갔기 때문에 먼저 출력이된다.

print(data_queue2.qsize())
print(data_queue2.get())

print("------------------------------------------------------")
#Priority Queue사용
data_queue3 = queue.PriorityQueue()

data_queue3.put((10,"abc")) #우선순위를 표현하기 위해 튜플로 인서트 (우선순위,value)
data_queue3.put((5,1))
data_queue3.put((15,'efff'))
#우선순위가 높은 순서, 숫자가 낮은 것부터 출력 -> 튜플 형태로 출력이 된다.
print(data_queue3.qsize())
print(data_queue3.get()) 
#만약 data value값만 받고 싶다면 
# value = data_queue3.get()
#print(value[3:]) -> data value값만 출력.

print(data_queue3.qsize())
print(data_queue3.get())

print(data_queue3.qsize())
print(data_queue3.get())
