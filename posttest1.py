def mergeSort(x): 
    panjang_list = len(x) 
    if panjang_list == 1: 
        return x 
 
    mid_point = panjang_list // 2 
    partisi_kiri = mergeSort(x[:mid_point]) 
    partisi_kanan = mergeSort(x[mid_point:]) 
    return merge(partisi_kiri, partisi_kanan) 
 
def merge(kiri, kanan): 
    hasil = [] 
    p = q = 0 
    while p < len(kiri) and q < len(kanan): 
        if isinstance(kiri[p], int) and isinstance(kanan[q], int):  
            if kiri[p] < kanan[q]: 
                hasil.append(kiri[p]) 
                p += 1 
            else: 
                hasil.append(kanan[q]) 
                q += 1 
        elif isinstance(kiri[p], int): 
            hasil.append(kiri[p]) 
            p += 1 
        elif isinstance(kanan[q], int): 
            hasil.append(kanan[q]) 
            q += 1 
        else:  
            if kiri[p] < kanan[q]: 
                hasil.append(kiri[p]) 
                p += 1 
            else: 
                hasil.append(kanan[q]) 
                q += 1 
    hasil.extend(kiri[p:]) 
    hasil.extend(kanan[q:]) 
 
    return hasil 
 
def pisah(listnya): 
    for i in listnya: 
        tampung.append(i) 
 
listacak = [12, 1, [22, 3,[8, 14]], 2, 6,[11], 90] 
tampung = [] 
print("""
======================
List Sebelum Diurutkan
======================
""")
print(listacak) 
pisah(listacak) 
sorted_list = mergeSort(tampung) 
print("""
======================
List Setelah Diurutkan
======================
""")
print(sorted_list)
print("")