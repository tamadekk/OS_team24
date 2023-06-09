from datetime import datetime
import platform, os, string,signal
import threading, queue
import subprocess, inspect

current_date = datetime.now().date()
adresa = os.path.abspath('main.py')
izbor = string
print("\n Dobrodošli u naš tim 28 \n",
      f"Trenutni datum: {current_date}, Trenutna versia os: {platform.platform()}\n Trenutna adresa kučnoj direktoriji: {adresa}")

while True:
    print("\n 1 - Obrada naredbe \n", "2 - Brisanje direktorija \n", "3 - Poslati signal procesu \n", "4 - Igra sa prostima brojama \n",
          "5 - Obračun s modelom višedretvenosti \n", "exit or izlaz \n", "Unesite vaš izbor: ")
    izbor = (input())
    match izbor:
        case "1":
            def get_command():
                """
                Upisujemo željenu naredbu koju želimo izvršiti

                Vraća:
                Šalje programu tip naredbe i argumente koje smo unijeli
                """
                try:
                    command = input("Unos naredbe: ")
                    return command
                except KeyboardInterrupt:
                    return None


            def execute_command(command):
                """
                Pokreće se novi proces koji izvađa unesenu naredbu s zadanim
                argumentima i parametrima. Uspješnost izvedene naredbe se
                ispisuje kao rezultat korisniku na zaslon, te se ispisuje
                poruka o korektnoj izvršenosti. Ukoliko koristimo naredbu
                cal 999 ispisuje se kalendar s postavkama kalendara
                prilagođenim za Ujedinjeno Kraljevstvo.

                Argumenti:
                command -- Ovo je naredba koju treba izvršiti kao podproces

                Vraća:
                Poruku u uspješno odrađenoj naredbi te njezin output tipa
                string ili poruku o grešci i poruku greške ukoliko se ona dogodila
                isto tipa string
                """
                if command.startswith("cal 999"):
                    env = os.environ.copy()
                    env["LC_TIME"] = "en_GB.UTF-8"
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                               env=env)
                else:
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                output, error = process.communicate()
                return_code = process.wait()
                if return_code == 0:
                    print("Naredba je izvršena uspješno.")
                    print("Output:")
                    print(output.decode())
                else:
                    print("Dogodila se greška prilikom izvođenja programa.")
                    print("Poruka greške:")
                    print(error.decode())


            def timeout_handler(signum, frame):
                """
                Pokreće se TimeoutError tj. događa se greška kada se pošalje signal

                Argumenti:
                signum -- Broj signala
                frame -- Trenutni stog okvira, stanje izvođenja programa u određenom
                trenutku
                """
                raise TimeoutError


            def main():
                while True:
                    print("Imaš 13 sekundi za unos naredbe.")
                    command = None

                    try:
                        signal.signal(signal.SIGALRM, timeout_handler)
                        signal.alarm(13)
                        command = get_command()
                        signal.alarm(0)  # Resetira se alarm
                    except TimeoutError:
                            print("Vrijeme unosa je završilo.")

                    if command is None:
                        break

                    execute_command(command)
                    break


            if __name__ == "__main__":
                main()
        case "2":
            def brisanje(adresa):
                """
                Funkcija traži unesenu relativnu ili apsolutnu adresu i briše nju. Prepoznaje je li ispravno unesena adresa,
                je li ona direktorijeju i je li ona prazna. Nakon toga briše nju (ako za svi vrijednosti je True)
                i ispisuje na zaslon ID grupe, apsolutnu adresu kojoj je nadređena direktorija i popis svih poddirektorijev i dadotek
                koji nalazi u nadređenu direktoriju da bi proveriti što unesena direktorija je obrisana.

                Argumenti:
                adresa-- relativna ili apsolutna adresa koju treba obrisati.
                """
                if not os.path.exists(adresa):
                    print("Adresa nije točna")
                    return
                """
                'exists' koristimo da proveriti je li adresa tochna, nalazi li tamo direktorija.  'exists' vraca vrijednost True ako adresa je točna.
                koristimo tu 'if not' da programa izvodi što ako vrijednost nije true, da piše informaciju o greške 
                """
                if not os.path.isdir(adresa):
                    print("Ova adresa nije direktorija")
                    return
                """
                'isdir' proverjava je li točno ovo direktorija. jer moramo brisati samo direktoriju a ne neki file
                """
                if len(os.listdir(adresa)) > 0:
                    print("Direktorija nije prazna. Nemogu će obrisati")
                    return
                """
                'listdir' provjerjava kolicinu poddirektorij i dadotek u direktoriji koji upisali smo. I ako značenje je veci
                od nula, znaci da direktorija nije praza, a u ovom slucaju ne možemo obrisati nju
                """
                apsolutna_adresa = os.path.dirname(adresa)
                id_grupe = os.stat(adresa).st_gid

                try:
                    os.rmdir(adresa)
                    print(
                        f"\n Direktorija je uspješna izbrisana \n Apsolutna adresa: {apsolutna_adresa}\n ID grupe: {id_grupe}\n"
                        f" Sadržaj nadređenoj direktoriji nakon brisanja:\n {os.listdir(apsolutna_adresa)}")
                    """
                    u ovom slucaju 'listdir' ispisuje svi poddirektoriji i filovi koji nalazi u nadređenoj direktoriji
                    """
                except OSError as e:
                    """
                    'OSError' služi za slučaj kad imamo neku tehničnu pogresku, zbog kojoj nije moguće brisanje
                    """
                    print("Došlo je do pogreške prilikom brisanja direktoriji:", str(e))


            adresa_direktoriji = input("Unesite apsolutnu ili relativnu adresu direktoriji za brisanje: ")
            brisanje(adresa_direktoriji)
        case "3":
            def upravljac_signala_1415(signals):
                """
                Funkcija je isključivo za kontrolu procesa ako je broj signala 14 ili 15. Na zaslon ispisuje poruku o
                zaprimljenom signalu i njegovu rednu broju, zapisuje PPID i PID procesa, te trenutno stanje stoga u
                datoteku stog1.txt koja se stvara u kućnom direktoriju, obavještava korisnika porukom o tome što je
                napravio.

                Argumenti:
                signals -- broj signala

                Vraća:
                Ništa
                """
                if signals == 14 or signals == 15:
                    home_dir = os.path.expanduser("~")
                    file_path = os.path.join(home_dir, "stog1.txt")
                    stog_status = inspect.stack()
                    with open(file_path, 'w') as file:
                        file.write("PPID: {} \n".format(os.getppid()))
                        file.write("PID: {} \n".format(os.getpid()))
                        file.write("Status stoga:\n")
                        print('Trenutni status stoga spremljen je u datoteku "stog1.txt" u {}'.format(file_path))
                        for frame_info in stog_status:
                            frame = frame_info.frame
                            file.write("Funkcija: {} \n".format(frame.f_code.co_name))
                            file.write("Dadoteka: {} \n".format(frame.f_code.co_filename))
                            file.write("Linija koda: {} \n".format(frame.f_lineno))
                            file.write("\n")
                    print(
                        "Pristigao je signal broj: {}, PPID procesa: {}, PID procesa: {}".format(signals, os.getppid(),
                                                                                                 os.getpid()))


            def upravljac_signala_18(signals):

                """
                Provjerava je li broj signala u rasponu od 1 do 8. Ako je uvjet istinit, signal se zanemaruje.

                Argumenti:
                signals -- broj signala

                Vraća:
                Ništa.
                """
                if 1 <= signals <= 8:
                    signal.signal(signal.SIGINT, signal.SIG_IGN)
                    print("Signal je ignoriran.")


            def upravljac_ostale(signals):
                """
                Provjerava je li broj signala između 9 i 31. Ako je uvjet istinit, signal se šalje trenutnom procesu.

                Argumenti:
                signals - broj signala.

                Vraća:
                Ništa.
                """
                if 8 < signals <= 31:
                    os.kill(os.getpid(), signals)


            while True:
                broj_sig = int(input("Unesite broj signala koji ćete se poslati trenutnome procesu: "))
                if broj_sig > 31 or broj_sig < 0:
                    print("Krivi unos! Broj signala mora biti u rasponu od 0 do 31.")
                else:
                    break

            upravljac_signala_1415(broj_sig)
            upravljac_signala_18(broj_sig)
            upravljac_ostale(broj_sig)
        case "4":
            import threading
            import queue

            print("Obračun... ")

            summ = 0  # summa svih prostih brojeva

            minq = queue.Queue(5)  # red naj manih prostih brojava u granama
            maxq = queue.Queue(5)  # red naj vecih prostih brojava u granama


            def IsPrime(n):  # algoritm trazenja prostog broja
                d = 2
                while d * d <= n and n % d != 0:  # optimiziranje obicnog trazne isklucivanjem svega sta vise od korenja broja n
                    d += 1
                return d * d > n


            def prime_numbers(startnum, stopnum):  # funkcija istrazivanja naimanih,naj visih i sume prostih broja

                global summ  # summa svih prostih brojeva
                minflag = 1  # flag za uhvat najmanjeg broja (prvi broj koj njemo)
                min_prime = None  # naj mani prosti broj
                max_prime = None  # naj veci prosti broj

                if (startnum == 1):  # if za odabir grane sa diopozonom od 1
                    summ += 3  # dodanje u sumu 1 i 2
                    startnum = 3  # promjena startnog broja na 3
                    min_prime = 1  # minimalni broj
                    minflag = 0;  # promjena flaga za minimalni broj

                i = startnum  # pocetni broj za cikl

                while i < stopnum:  # pocetni cikl trazje prostih broja u diopozoni grane
                    if (IsPrime(i)):  # provjera proja i, jeli prost broj

                        if (minflag):  # provjera ili ikad upisivalose minimalni broj u ovom redku
                            min_prime = i
                            minflag = 0

                        summ += i
                        max_prime = i

                    i += 1
                minq.put(min_prime)  # zapis u stup najmanjeg broja u ovom redku
                maxq.put(max_prime)  # zapis u stup najviseg broja u redku


            thread1 = threading.Thread(target=prime_numbers, args=(1, 410000))  # objava 1 grane
            thread2 = threading.Thread(target=prime_numbers, args=(410001, 820001))  # objava 2 grane
            thread3 = threading.Thread(target=prime_numbers, args=(820002, 1230000))  # objava 3 grane

            thread1.start()  # pustanje 1 grane
            thread2.start()  # pustanje 2 grane
            thread3.start()  # pustanje 3 grane

            thread1.join()  # cekanje zavrsetka rada 1 grane
            thread2.join()  # cekanje zavrsetka rada 2 grane
            thread3.join()  # cekanje zavrsetka rada 3 grane

            # ------------------------------------------------blok sortiranja i traznje potrebnih elemenata
            min_prime = minq.get()
            max_prime = maxq.get()

            while not minq.empty():
                min_prime = min(min_prime, minq.get())
            while not maxq.empty():
                max_prime = max(max_prime, maxq.get())
                # -------------------------------------------------

                with open("minmax.txt", 'w') as file:  # otvorenje dokumenata minmax.txt
                    file.write(f"Minimalni broj: {min_prime}\n")
                    file.write(f"Maksimalni broj: {max_prime}\n")
            print("summa prostih brojeva = " + str(summ) + "\nminimalni broj = " + str(
                min_prime) + "\nmaxsimalni broj = " + str(max_prime))  # izvodenje svih rezultatov
        case "5":
            rezultat1 = 0
            lock = threading.Lock()
            def oduzimaj(pocetak, kraj):
                lock.acquire()
                global rezultat1
                for i in range(pocetak, kraj+1):
                    i *= i
                    rezultat1 += i
                lock.release()
            while True:
                broj = int(input("Unesite broj od 50 do 144 000: "))
                if not 50 <= broj <= 144000:
                    print("Krivi unos!")
                else:
                    break
            interval = broj // 4
            t1 = threading.Thread(target=oduzimaj, args=(1, interval))
            t2 = threading.Thread(target=oduzimaj, args=(interval + 1, 2 * interval,))
            t3 = threading.Thread(target=oduzimaj, args=(2 * interval + 1, 3 * interval,))
            t4 = threading.Thread(target=oduzimaj, args=(3 * interval + 1, broj,))

            t1.start()
            t2.start()
            t3.start()
            t4.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            var = 55550550550550550550
            kraj = var - rezultat1
            print ("Konačna vrijednost varijable je: {}".format(kraj))
        case "exit":
            break
        case "izlaz":
            break
        case "":
            print("")
        case _:
            print("Vaš unos je pogresan")
