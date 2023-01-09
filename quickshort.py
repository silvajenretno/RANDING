def partition(l, bwh, atas): #Melakukan quicksorting pada setiap partisi yang telah dibagi
    # print("List : ",l,"\n")
    pivot = l[atas]
    index = bwh
    current = bwh
    while (current < atas) :
        if l[current] <= pivot:
            l[index],l[current]=l[current],l[index] #Swapping antara value[index] dan value[current]
            index += 1
        current += 1
    l[index],l[atas] = l[atas],l[index] #Swapping antara value[pivot] dan value[index]
    # print("Partisi : ",l,"\n")
    return index

def quicksort(l, bwh, atas): #Melakukan pembagian partisi
  if bwh < atas:
    index = partition(l, bwh, atas) #mendapatkan index untuk membagi partisi
    quicksort(l, bwh, index-1) #quicksorting partisi kiri (lebih kecil dari pivot)
    quicksort(l, index+1, atas) #quicksorting partisi kanan (lebih besar dari pivot)
    return l

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
angka = [34,21,31,32,12,30]
akhir = quicksort(angka,0,len(angka)-1)
print("Setelah disort : ",akhir)


#Melakukan sorting pada variabel list dengan value bertipe data campuran (Integer dan String)
campuran = ["kamu",21,"aku",32,12,31,19,23,54,31,"dia",27]
pisah_int_str(campuran)

quicksort(integ,0,len(integ)-1)
quicksort(stri,0,len(stri)-1)
akhir = integ + stri
print("Setelah disort : ",akhir)