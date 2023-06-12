import threading
import queue

print("Funkcija 4, igra sa prostima brojama")

summ = 0  #summa svih prostih brojeva

minq = queue.Queue(5)    #red naj manih prostih brojava u granama
maxq = queue.Queue(5)    #red naj vecih prostih brojava u granama

def IsPrime(n):     #algoritm trazenja prostog broja
    d = 2
    while d * d <= n and n % d != 0:    #optimiziranje obicnog trazne isklucivanjem svega sta vise od korenja broja n
        d += 1
    return d * d > n
def prime_numbers(startnum,stopnum):    #funkcija istrazivanja naimanih,naj visih i sume prostih broja


    global summ         #summa svih prostih brojeva
    minflag = 1 #flag za uhvat najmanjeg broja (prvi broj koj njemo)
    min_prime = None  # naj mani prosti broj
    max_prime = None  # naj veci prosti broj

    if(startnum==1):    #if za odabir grane sa diopozonom od 1
        summ+=3         #dodanje u sumu 1 i 2
        startnum=3      #promjena startnog broja na 3
        min_prime=1           #minimalni broj
        minflag =0;     #promjena flaga za minimalni broj

    i = startnum        #pocetni broj za cikl

    while i < stopnum:   #pocetni cikl trazje prostih broja u diopozoni grane
        if(IsPrime(i)):     #provjera proja i, jeli prost broj

            if (minflag):   #provjera ili ikad upisivalose minimalni broj u ovom redku
                min_prime = i
                minflag = 0

            summ += i
            max_prime = i

        i += 1
    minq.put(min_prime)   #zapis u stup najmanjeg broja u ovom redku
    maxq.put(max_prime)   #zapis u stup najviseg broja u redku



thread1 = threading.Thread(target = prime_numbers, args = (1,410000))           #objava 1 grane
thread2 = threading.Thread(target = prime_numbers, args = (410001,820001))      #objava 2 grane
thread3 = threading.Thread(target = prime_numbers, args = (820002,1230000))     #objava 3 grane

thread1.start()     #pustanje 1 grane
thread2.start()     #pustanje 2 grane
thread3.start()     #pustanje 3 grane

thread1.join()      #cekanje zavrsetka rada 1 grane
thread2.join()      #cekanje zavrsetka rada 2 grane
thread3.join()      #cekanje zavrsetka rada 3 grane

#------------------------------------------------blok sortiranja i traznje potrebnih elemenata
min_prime = minq.get()
max_prime = maxq.get()

while not minq.empty():
    min_prime = min(min_prime, minq.get())
while not maxq.empty():
    max_prime = max(max_prime, maxq.get())
#-------------------------------------------------

    with open("minmax.txt", 'w') as file:               #otvorenje dokumenata minmax.txt
        file.write(f"Minimalni broj: {min_prime}\n")
        file.write(f"Maksimalni broj: {max_prime}\n")
print ("summa prostih brojeva = " + str(summ) + "\nminimalni broj = " + str(min_prime) +"\nmaxsimalni broj = " + str(max_prime)) #izvodenje svih rezultatov