import threading
import queue

summ = 0
min = 1200000
max = 0
minq = queue.Queue()
maxq = queue.Queue()
def prime_numbers(startnum,stopnum):
    global summ
    if(startnum==1):
        summ+=3
        startnum=3

    minflag = 1
    for i in range(startnum,stopnum):
        flag = 1
        for j in range(2,i-1):
            if(i/j == int):
                    flag=0
                    break
            if (flag):
                summ+=i
                if( minflag):
                    min=i
                    minflag = 0
                max=i


    minq.put(min)
    max.put(max)


thread1 = threading.Thread(target = prime_numbers, args = (1,410000))
thread2 = threading.Thread(target = prime_numbers, args = (410001,820001))
thread3 = threading.Thread(target = prime_numbers, args = (820002,1230000))

thread1.start()
thread2.start()
thread3.start()


while not minq.empty():
    if min>minq.get_nowait():
        min=minq.get()
while  maxq.full():
    if max<maxq.get_nowait():
        max=maxq.get()

file = open("minmax.txt", 'w')
file = min + '- minimalni broj\n' + max + "- maximalni broj"
file.close()
print ("summa prostih brojeva = " + summ + "\nminimalni broj = " + min +"\nmaxsimalni broj = " + max)