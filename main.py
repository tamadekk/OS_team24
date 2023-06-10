import subprocess
import signal
import os

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
