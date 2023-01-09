def shellSort(sample):
    length = len(sample)
    gap = int(length/2) #Menentukan jarak lompatan index berdasarkan pembagian panjang data

    while(gap>=1):
        i = gap #Menginisiasi index i
        while(i<length):
            value = sample[i] # Mengambil value dari index i
            j = i #Inisiasi index j
            while(j - gap >= 0 and value < sample[j-gap]):
                sample[j] = sample[j-gap] #Menginisiasi value index j dengan value dengan index (j-gap)
                j -= gap #Untuk menghentikan perulangan
            sample[j] = value #Menginisiasikan value index j dengan value index i
            i+=1 #Menggeser posisi index
        gap = int (gap/2) #Memperkecil gap
        # print(sample,"\n")
    print("Sorted sample = ",sample)

def pisah_int_str (pisahin): #Untuk memisahkan Integer dan String
    global integ
    global stri
    integ = []
    stri = []
    for datain in range(len(pisahin)):
        #Jika tipe dayanya integer
        if type(pisahin[datain]) == int:
            integ.append(pisahin[datain])
        #Jika tipe datanya bukan integer
        else:
            stri.append(pisahin[datain])


#Melakukan sorting pada variabel list dengan value bertipe data integer saja
sampel = [32,54,12,76,43,21,87,23]
shellSort(sampel)


#Melakukan sorting pada variabel list dengan value bertipe data campuran (Integer dan String)
campuran = ["kamu",21,"aku",32,12,31,19,23,54,31,"dia",27]
pisah_int_str(campuran)

shellSort(stri)
shellSort(integ)
akhir = integ + stri
print("Setelah disort : ",akhir)