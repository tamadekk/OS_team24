import threading, time, os



def prime_numbers(startnum,stopnum):
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
        for j in range(startnum,i-1):
            if(i!=j):
                if(i/j == int):
                    flag=0
                    break
        if (flag):
            summ+=i
            if(min<i):
                min=i
            max=i









thread1 = threading.Thread(target=prime_numbers(1,410000), args=(20,))
thread2 = threading.Thread(target=prime_numbers(410001,820001), args=(50,))
thread3 = threading.Thread(target=prime_numbers(820002,1230000), args=(10,))

