#menampilkan notifikasi jika Table kosong
def notifikasi_data_kosong(): 
    print('''
    Mohon maaf data tidak ditemukan
    ''')

#menampilkan notifikasi jika terdapat data double
def notifikasi_data_double(data): 
    data = bubble_sort(data)
    id = show_id(data)
    print(f'''
    Mohon maaf ID tersebut sudah digunakan, mohon masukkan ID yang lain. 
    ID yang telah terdaftar adalah: {id}
    ''')

#Menampilkan notifikasi jika feature belum tersedia
def notifikasi_menu_belum_tersedia(): 
    print('''
    Mohon Maaf pilihan belum tersedia, silahkan pilih menu yang tersedia: 
    ''')

#Error handling - menampilkan notifikasi jika terjadi Value Error
def notifikasi_value_error(): 
    print('''
    ERROR! MOHON INPUT ANGKA SESUAI MENU YANG TERSEDIA
    ''')

#Menampilkan notifikasi jika ID Pegawai belum tersedia
def notifikasi_salah_input_id(): 
    print('''
    ERROR!! MOHON MASUKKAN ID PEGAWAI YANG VALID [1,2,3,...)
    ''')

#Mengembalikan nilai semua ID yang terdaftar pada table. 
# Input: any data pada table, Output: all ID.
def show_id(data): 
    data.pop(0)
    data_id = []
    for datum in data:
        data_id.append(datum[0])
    return data_id

#Memproses data yang sebelumnya acak menjadi ter-sorting secara ascending. 
# Input: any data pada table, Output: data pada table sorted ascending
def bubble_sort(data):
    val = data.copy()
    first_column = val.pop(0)
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
    val.insert(0, first_column)
    return val

#check apakah terdapat data pada table
# Input: any data pada table. Return True jika data kosong, return False jika terdapat data
def is_exist(data): 
    if len(data) != 1: 
        return True
    else: 
        return False

#menampilkan seluruh data pada table. 
def show_data(data): 
    hasil_sort = bubble_sort(data)
    if is_exist(hasil_sort):
        for datum in hasil_sort: 
            print(datum)
    else:
        notifikasi_data_kosong()

#melakukan pengecekan pada kolom ID. 
# Input: any data pada table. Return True Jika ID sudah digunakan, return False jika ID Belum digunakan.
def check_double(data, input): 
    isFound = False
    for datum in data: 
        if datum[0] == input: 
            isFound = True
            break   #karena select diharuskan menuju ke kolom primary key maka hasilnya pasti 1 data saja.
    if not(isFound):
        return False
    else: 
        return True

#Melakukan insert data pada table dan mengembalikan nilai data pada table setelah proses insert. 
def insert_data(data, data1, data2, data3, data4, data5): 
    return data.append([data1, data2, data3, data4, data5])

#Melakukan update data pada table sesuai column yang dipilih user. 
# Input: dataOriginal = data pada table, dataSelected = data pilihan user yang ingin di update berdasarkan ID, 
#   kolom = informasi nama kolom yang ingin di update, updateData = informasi data yang nantinya akan me-replace data original.
def update_data(dataOriginal, dataSelected, kolom, updateData): 
    i = 0
    for datum in dataOriginal: 
        if datum == dataSelected[0]:
            flagKonfirmasi = True
            while flagKonfirmasi:
                userInput = input(f"\nApakah anda yakin ingin mengupdate kolom {kolom} dengan {updateData}? [y/n]  ").lower()
                if userInput == "y": 
                    dataOriginal[i][dataOriginal[0].index(kolom)] = updateData
                    print("\n===DATA BERHASIL DI UPDATE!===")
                    flagKonfirmasi = False
                elif userInput == "n": 
                    print("\n===DATA GAGAL TERUPDATE, MOHON INPUT DATA ULANG!===")
                    flagKonfirmasi = False
                else: 
                    print("\nInvalid Input!")
        i+=1

#Menampilkan data yang di Select oleh user lengkap dengan informasi nama kolomnya berdasarkan ID.  
def check_data(data): 
    data_exist = []
    if is_exist(data):
        try:
            userInput = int(input("masukkan user id Pegawai: "))
            if check_double(data, userInput):
                for datum in data: 
                    if datum[0] == userInput: 
                        print(data[0])
                        print(datum)
                        data_exist.append(datum)
            else:
                notifikasi_data_kosong()
        except ValueError: 
            notifikasi_salah_input_id()
    else:
        notifikasi_data_kosong()
    return data_exist

#Meghapus data sesuai input user. 
def hapus_data(data, delete):
    i = 0
    for datum in data: 
        if datum == delete[0]:
            data.pop(data.index(delete[0]))
            print("===DATA BERHASIL DIHAPUS===")
        
#Menu utama
def main_menu():
    print(f'''
    ===Pilihan Menu Data Karyawan===
    1. Show Data Karyawan
    2. Tambahkan Data Karyawan
    3. Update Data Karyawan
    4. Hapus Data Karyawan
    5. Exit

    ''')

#sub menu 1
def sub_menu_1(data): 
    flag = True
    while flag:
        print(f'''
    
    ===Show Data Karyawan===
    1. Report seluruh karyawan
    2. Report Data karyawan tertentu
    3. Kembali ke Menu Utama

    ''')
        try:
            userInput = int(input("pilih menu berapa: "))
            if userInput == 1: 
                show_data(data)
            elif userInput == 2: 
                if not(is_exist(data)):
                    notifikasi_data_kosong()
                else:
                    check_data(data)
            elif userInput == 3: 
                flag = False
            else: 
                notifikasi_menu_belum_tersedia()
        except ValueError: 
            notifikasi_value_error()
        

#sub menu 2
def sub_menu_2(data): 
    flag = True
    while flag: 
        print(f'''
    
    ===Input Data Karyawan===
    1. Tambah data karyawan
    2. Kembali ke Menu Utama

    ''')
        try:
            userInput = int(input("pilih menu berapa: "))
            if userInput == 1: 
                try:
                    userInputID = int(input("Masukkan ID Pegawai: "))
                    if userInputID <= 0: 
                        notifikasi_salah_input_id()
                    else:
                        if check_double(data, userInputID): 
                            notifikasi_data_double(data)
                        else: 
                            userInputNama = input("Masukkan Nama Pegawai: ")
                            try:
                                userInputUsia = int(input("Masukkan Umur Pegawai: "))
                            except ValueError:
                                print('''\n   Umur tidak Valid!\n''')
                            userInputJabatan = input("Masukkan Jabatan Pegawai: ")
                            userInputTglMasuk = input("Masukkan Tanggal Masuk Pegawai: ")

                            flagKonfirmasi = True
                            while flagKonfirmasi:
                                userInputKonfirmasi = (input(f'''
                Apakah anda yakin akan menginput data berikut?  
                {[userInputID, userInputNama, userInputUsia, userInputJabatan, userInputTglMasuk]}.... [y/n]   ''')).lower()
                                if userInputKonfirmasi == "y":
                                    insert_data(data, userInputID, userInputNama, userInputUsia, userInputJabatan, userInputTglMasuk)
                                    print('''\n   data berhasil diinput... Terima kasih.''')
                                    flagKonfirmasi = False
                                elif userInputKonfirmasi == "n": 
                                    print('''\n   DATA TIDAK BERHASIL TERUPDATE.. MOHON INPUT ULANG!''')
                                    flagKonfirmasi = False
                                else: 
                                    print("\nInvalid Input!")
                except ValueError: 
                    notifikasi_salah_input_id()
            elif userInput == 2: 
                flag = False
            else: 
                notifikasi_menu_belum_tersedia()
        except ValueError: 
            notifikasi_value_error()
    return data

#sub_menu_3
def sub_menu_3(data): 
    flag = True
    while flag: 
        print(f'''
    
    ===Update Data Karyawan===
    1. Ubah data karyawan
    2. Kembali ke Menu Utama

    ''')
        userInput = int(input("Pilih menu berapa: "))
        if userInput == 1: 
            dataBeingUpdate = check_data(data)
            if len(dataBeingUpdate) != 0:
                flagKonfirmasi = True
                while flagKonfirmasi:
                    userInputKonfirmasiLanjut = input("\nIngin melanjutkan Update data? [y/n]  ").lower()
                    if userInputKonfirmasiLanjut == "y":
                        userInputUpdateKolom = input("\nMasukkan kolom yang ingin diupdate: ").lower()
                        if userInputUpdateKolom == "id":
                            userInputUpdate = int(input("Masukkan id baru: "))
                            if check_double(data, userInputUpdate):
                                notifikasi_data_double(data)
                            else:
                                update_data(data, dataBeingUpdate, userInputUpdateKolom, userInputUpdate)
                        elif userInputUpdateKolom == "full_name": 
                            userInputUpdate = input("Masukkan full_name baru: ")
                            update_data(data, dataBeingUpdate, userInputUpdateKolom, userInputUpdate)
                        elif userInputUpdateKolom == "age": 
                            userInputUpdate = input("Masukkan age baru: ")
                            update_data(data, dataBeingUpdate, userInputUpdateKolom, userInputUpdate)
                        elif userInputUpdateKolom == "title": 
                            userInputUpdate = input("Masukkan title baru: ")
                            update_data(data, dataBeingUpdate, userInputUpdateKolom, userInputUpdate)
                        elif userInputUpdateKolom == "from_date":
                            userInputUpdate = input("Masukkan from_date baru: ")
                            update_data(data, dataBeingUpdate, userInputUpdateKolom, userInputUpdate)
                        flagKonfirmasi = False
                    elif userInputKonfirmasiLanjut == "n": 
                        print("\n===DATA GAGAL TERUPDATE, MOHON INPUT DATA ULANG!===")
                        flagKonfirmasi = False
                    else:
                        print("\nInvalid Input!")
        elif userInput == 2: 
            flag = False
        else: 
            notifikasi_menu_belum_tersedia()
            
#sub_menu_4
def sub_menu_4(data): 
    flag = True
    while flag: 
        print(f'''
    
    ===Delete Data Karyawan===
    1. Delete data karyawan
    2. Kembali ke Menu Utama

    ''')
        userInput = int(input("Pilih menu berapa: "))
        if userInput == 1: 
            dataBeingDeleted = check_data(data)
            if len(dataBeingDeleted) != 0:
                flagKonfirmasi = True
                while flagKonfirmasi:
                    userInputKonfirmasiLanjut = input("\nYakin ingin menghapus data? [y/n]  ").lower()
                    if userInputKonfirmasiLanjut == "y":
                        hapus_data(data, dataBeingDeleted)
                        flagKonfirmasi = False
                    elif userInputKonfirmasiLanjut == "n": 
                        print("\n===HAPUS DATA DIBATALKAN===")
                        flagKonfirmasi = False
                    else: 
                        print("\nInvalid Input!")
        elif userInput == 2: 
            flag = False
        else: 
            notifikasi_menu_belum_tersedia()
            
#Main program
def main():
    data_karyawan = [
        ["id", "full_name", "age", "title", "from_date"],
        [1, "stevani sulis", 21, "staff", "27/10/2022"],
        [2, "joni joni", 22, "senior staff", "10/10/2010"],
        [3, "yes papa", 30, "manajer", "11/12/2008"]
    ]

    flag = True
    while flag: 
        main_menu()
        try:
            input_menu = int(input("masukkan pilihan menu: "))
            if input_menu == 1:
                sub_menu_1(data_karyawan)
            elif input_menu == 2: 
                sub_menu_2(data_karyawan)
            elif input_menu == 3: 
                sub_menu_3(data_karyawan)
            elif input_menu == 4: 
                sub_menu_4(data_karyawan)
            elif input_menu == 5: 
                print("\n====Terima kasih telah menggunakan program Data Karyawan. SEE YOU!====\n")
                flag = False
            else: 
                notifikasi_menu_belum_tersedia()
        except ValueError: 
            notifikasi_value_error()

main()