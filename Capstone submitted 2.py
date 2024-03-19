from tabulate import tabulate

employee_data = [
    {"Index": "0", "Nama": "Chris Bismar", "Umur": 23, "Posisi": "Manager", "Gaji": 50000.0},
    {"Index": "1", "Nama": "Jo Sianipar", "Umur": 22, "Posisi": "Developer", "Gaji": 40000.0},
    {"Index": "2", "Nama": "Alif Putrawan", "Umur": 21, "Posisi": "Data Analyst", "Gaji": 45000.0},
    {"Index": "3", "Nama": "John Doe", "Umur": 30, "Posisi": "Manager", "Gaji":50000.0 },
    {"Index": "4", "Nama": "Jane Smith", "Umur": 25, "Posisi": "Developer", "Gaji": 60000.0},
    {"Index": "5", "Nama": "Alice Johnson", "Umur": 35, "Posisi": "Designer", "Gaji":50000.0 }
]


def View_by_Index(index):
    found_worker = None
    
    for worker in employee_data:
        if worker["Index"] == index:
            found_worker = worker
            break
    
    if found_worker:
        headers = ["Index", "Nama", "Umur", "Posisi", "Gaji"]
        data = [[found_worker["Index"], found_worker["Nama"], found_worker["Umur"], found_worker["Posisi"], found_worker["Gaji"]]]
        print(tabulate(data, headers=headers, tablefmt="pretty"))
    else:
        print("Tidak ada pekerja dengan indeks tersebut.")

    input("Tekan Enter untuk melanjutkan...")

def View_by_Position(position):
    matched_workers = []
    headers = ["Index", "Nama", "Umur", "Posisi", "Gaji"]
    
    for worker in employee_data:
        if worker["Posisi"] == position:
            matched_workers.append([worker["Index"], worker["Nama"], worker["Umur"], worker["Posisi"], worker["Gaji"]])

    if matched_workers:
        print(tabulate(matched_workers, headers=headers, tablefmt="pretty"))
    else:
        print("Tidak ada pekerja dengan posisi tersebut.")

    input("Tekan Enter untuk melanjutkan...")

def view_workersMain():
    while True:
        print('''
            Masukan pilihan yang Anda ingin melaksanakan
                      
            Menu:
            1. Tampilkan semua Data
            2. Tampilkan Data berdasarkan Posisi
            3. Tampilkan Data berdasarkan Index
            4. Balik ke Main Menu
            ''')
        pilihan = input("Masukan pilihan Anda!: ")
        if pilihan == "1":
            view_workers()
        elif pilihan == "2":
            position = input("Masukan Posisi yang Anda ingin mencari: ")
            position = position.capitalize()
            View_by_Position(position)
        elif pilihan == '3':
            Index = input("Masukan Index yang ingin dicari: ")
            View_by_Index(Index)
        elif pilihan == "4":
            menu()
        else:
            print('Pilihlah 1 sampai 4!')

def add_workerMain():
    while True:
        print('''
            Masukan pilihan yang Anda ingin melaksanakan
                      
            Menu:
            1. Tambahkan Data
            2. Kembali ke Menu Awal
            ''')
        pilihan = input("Masukan pilihan Anda!: ")
        if pilihan == "1":
            add_worker()
        elif pilihan == "2":
            menu()
        else:
            print('Pilihlah 1 sampai 2!')

def add_worker():
    print("Tambahkan data pekerja:" )
    Index = input("Masukan Index pekerja: ")
    for i in range(len(employee_data)):
        print(employee_data[i]['Index'])
        if Index == employee_data[i]['Index']:
            print('Index yang anda masukan sudah ada')
            add_worker()
        else:
            name = input("Masukan nama pekerja: ")
            age = int(input("Masukan umur pekerja: "))
            position = input("Masukan posisi pekerja: ")
            salary = float(input("Masukan gaji pekerja: "))
            confirm = input("Apakah Anda yakin ingin menambahkan pekerja ini? (iya/tidak): ")
            if confirm.lower() == "iya":
                employee_data.append({"Index": Index, "Nama": name, "Umur": age, "Posisi": position, "Gaji": salary})
                print("Pekerja berhasil ditambahkan!")
                menu()
            else:
                print("Pekerja tidak ditambahkan.")
                menu()

        
            

def view_workers1():
    headers = ["Index", "Nama", "Umur", "Posisi", "Gaji"]
    data = []
    for worker in employee_data:
        index = worker["Index"]
        name = worker["Nama"]
        age = worker["Umur"]
        position = worker["Posisi"]
        salary = worker["Gaji"]
        data.append([index, name, age, position, salary])
    print(tabulate(data, headers=headers, tablefmt='pretty'))

def view_workers():
    headers = ["Index", "Nama", "Umur", "Posisi", "Gaji"]
    data = []
    for worker in employee_data:
        index = worker["Index"]
        name = worker["Nama"]
        age = worker["Umur"]
        position = worker["Posisi"]
        salary = worker["Gaji"]
        data.append([index, name, age, position, salary])
    print(tabulate(data, headers=headers, tablefmt='pretty'))
    input("Tekan Enter untuk melanjutkan...")


def update_workerMain():
    while True:
        print('''
            Masukan pilihan yang Anda ingin melaksanakan
                      
            Menu:
            1. Update Data
            2. Kembali ke Menu Awal
            ''')
        pilihan = input("Masukan pilihan Anda!: ")
        if pilihan == "1":
            update_worker()
        elif pilihan == "2":
            menu()
        else:
            print('Pilihlah 1 sampai 2!')
            update_workerMain()


def update_worker():
    print('Perbarui Data Pekerja\n')
    view_workers1()
    index = int(input('Masukkan indeks pekerja yang datanya ingin Anda perbarui: '))
    
    if 0 <= index < len(employee_data):
        updates = {}  

        while True:
            print("Apa yang ingin Anda perbarui?")
            print("1. Nama")
            print("2. Umur")
            print("3. Posisi")
            print("4. Gaji")
            print("5. Selesai mengupdate")
            
            choice = input("Masukan pilihan Anda (1/2/3/4/5): ")
            if choice == "1":
                new_name = input("Masukan nama pekerja baru: ")
                updates["Nama"] = new_name
            elif choice == "2":
                new_age = int(input("Masukan umur pekerja baru: "))
                updates["Umur"] = new_age
            elif choice == "3":
                new_position = input("Masukan posisi pekerja baru: ")
                updates["Posisi"] = new_position
            elif choice == "4":
                new_salary = float(input("Masukan gaji pekerja baru: "))
                updates["Gaji"] = new_salary
            elif choice == "5":
                break
            else:
                print("Pililah opsi 1 sampai 5!")

        if updates:  
            print("\nInformasi yang akan diperbarui:")
            for key, value in updates.items():
                print(f"{key}: {value}")

            confirm = input("Apakah Anda yakin ingin memperbarui data pekerja ini?(iya/tidak): ")
            if confirm.lower() == "iya":
                for key, value in updates.items():
                    employee_data[index][key] = value
                print("Data pekerja berhasil diperbarui!")
                view_workers1()
                input("Tekan Enter untuk melanjutkan...")
            else:
                print("Pembaruan dibatalkan.")
        else:
            print("Tidak ada pembaruan yang dimasukkan.")

    else:
        print("Indeks pekerja tidak valid.")


def delete_workerMain():
    while True:
        print('''
            Masukan pilihan yang Anda ingin melaksanakan
                      
            Menu:
            1. Hapus Data
            2. Kembali ke Menu Awal
            ''')
        pilihan = input("Masukan pilihan Anda!: ")
        if pilihan == "1":
            delete_worker()
        elif pilihan == "2":
            menu()
        else:
            print('Pilihlah 1 sampai 2!')
            delete_workerMain


def delete_worker():
    print("Hapus data pekerja\n")
    print("Detail terkini:")
    view_workers1()
    index = int(input("Masukkan indeks pekerja yang akan dihapus: "))
    if 0 <= index < len(employee_data):
    
        
        confirm = input(" Apakah Anda yakin ingin menghapus pekerja ini?(iya/tidak): ")
        if confirm.lower() == "iya":
            del employee_data[index]
            print("Data pekerja berhasil dihapus!")
        else:
            print("Pekerja tidak dihapus.")
    else:
        print("Pililah Index yang benar")
        
    view_workers()
    menu()

def menu():
    while True:
        print('''
            Selamat Datang ke Purwadhika Worker Databank, apakah yang Anda mencari
                      
            Menu:
            1. Tampilkan Data pekerja
            2. Tambahkan Data Pekerja
            3. Update Data Pekerja
            4. Hapus Data Pekerja
            5. Exit
            ''')
        choice = input("Masukan pilihan Anda!: ")
        if choice == "1":
            view_workersMain()
        elif choice == "2":
            add_workerMain()
        elif choice == "3":
            update_workerMain()
        elif choice == "4":
            delete_workerMain()
        elif choice == "5":
            input("Exiting.....")
            break
        else:
            print("Pililah Angka dari 1 sampai 5!")

menu()