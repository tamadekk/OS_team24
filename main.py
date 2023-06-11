from datetime import datetime
import platform, os, string, subprocess, inspect


current_date = datetime.now().date()
adresa=os.path.abspath('main.py')
izbor=string
print("\n Dobrodošli u naš tim 28 \n",f"Trenutni datum: {current_date}, Trenutna versia os: {platform.platform()}\n Trenutna adresa kučnoj direktoriji: {adresa}")


while True:
    print("\n 1 - Prva funkcija \n","2 - Druga funkcija \n", "3 - Treca funkcija \n", "exit or izlaz \n","Unesite vaš izbor: ")
    izbor = (input())
    match izbor:
        case "1":
            def display_menu():
                print("Main Menu")
                print("1. Unesi naredbu")
                print("2. Izlaz")
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
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
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
                    display_menu()
                    choice = input("Odaberi opciju: ")

                    if choice == "1":
                        print("Imaš 13 sekundi za unos naredbe.")
                        command = None

                        try:
                            signal.signal(signal.SIGALRM, timeout_handler)
                            signal.alarm(13)
                            command = get_command()
                            signal.alarm(0) #Resetira se alarm
                        except TimeoutError:
                            print("Vrijeme unosa je završilo.")

                        if command is None:
                            continue

                        execute_command(command)
                    elif choice == "2":
                        print("Izlazim iz programa.")
                        break
                    else:
                        print("Pogrešan unos.")

            if __name__ == "__main__":
                main()
        case "2":
             print("Funkcija 2")
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
        case "exit":
            break
        case "izlaz":
            break
        case "":
            print("")
        case _:
            print("Vaš unos je pogresan")

