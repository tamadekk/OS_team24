import threading
import queue

summ = 0  #summa svih prostih brojeva

minq = queue.Queue(3)    #red naj manih prostih brojava u granama
maxq = queue.Queue(3)    #red naj vecih prostih brojava u granama

def IsPrime(n):     #algoritm trazenja prostog broja
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n
def prime_numbers(startnum,stopnum):    #funkcija istrazivanja prostih brojeva
    print ('.')
    global summ         #summa svih prostih brojeva
    minflag = 1 #flag za uhvat najmanjeg broja (prvi broj koj njemo)
    min = None  # naj mani prosti broj
    max = None  # naj veci prosti broj
    if(startnum==1):    #if za odabir grane sa diopozonom od 1
        summ+=3         #dodanje u sumu 1 i 2
        startnum=3      #promjena startnog broja na 3
        min=1           #minimalni broj
        minflag =0;     #promjena flaga za minimalni broj
    i = startnum
    while i < stopnum:
        if(IsPrime(i)):
            if (minflag):
                min = i
                minflag = 0
            summ += i
            print(i)
            max = i
        i+=1


    print(str(min) + " " + str(max))
    minq.put(min)
    maxq.put(max)



thread1 = threading.Thread(target = prime_numbers, args = (1,410000))
thread2 = threading.Thread(target = prime_numbers, args = (410001,820001))
thread3 = threading.Thread(target = prime_numbers, args = (820002,1230000))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

min = 1200000  # naj mani prosti broj
max = 0  # naj veci prosti broj

while not minq.empty():
    if min>minq.get_nowait():
        min=minq.get()
while  maxq.full():
    if max<maxq.get_nowait():
        max=maxq.get()

f = open("minmax.txt", 'w')
f = str(min) + '- minimalni broj\n' + str(max) + "- maximalni broj"
#f.close()
print ("summa prostih brojeva = " + str(summ) + "\nminimalni broj = " + str(min) +"\nmaxsimalni broj = " + str(max))