import threading, time, os, os.path



def prime_numbers(startnum,stopnum):
    if (path.isdir("minmax.txt")):
        file = open("minmax.txt", 'a')
        file.close()
    file = open("minmax.txt", 'w+')
    if(startnum==1):
        summ=3
        min=1
        startnum=3
    else :
        summ=0
        min=1230000



    for i in range(startnum,stopnum):
        flag = 1
        for j in range(2,i-1):
            if(i/j == int):
                    flag=0
                    break
        if (flag):
            summ+=i
            if(min<i):
                min=i
            max=i

    minlin = file.readline()
    if min>minlin :
        min=minlin
    maxlin = file.readline()
    if max<maxlin :
        max=maxlin

    summlin=file.readline() + summ

    file =minlin + '\n' + maxlin + '\n' + summlin


thread1 = threading.Thread(target=prime_numbers(1,410000), args=(20,))
thread2 = threading.Thread(target=prime_numbers(410001,820001), args=(50,))
thread3 = threading.Thread(target=prime_numbers(820002,1230000), args=(10,))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread1.join()
thread1.join()

file = open("minmax.txt", 'w+')
min = file.readline()
max = file.readline()
summ = file.readline()
file = min + '- minimalni broj\n' + max + "- maximalni broj"
print ("summa prostih brojeva = " + summ + "\nminimalni broj = " + min +"\nmaxsimalni broj = " + max)

