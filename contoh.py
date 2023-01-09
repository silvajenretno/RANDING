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
        if isinstance(i, list) :
            output.extend(pisah(i))
        else :
            output.append(i)
    return output 
 
listacak = [12, 1, [22, 3,[8, 14]], 2, 6,[11], 90] 
output = [] 
print("""
======================
List Sebelum Diurutkan
======================
""")
print(listacak) 
pisah(listacak) 
sorted_list = mergeSort(output) 
print("""
======================
List Setelah Diurutkan
======================
""")
print(sorted_list)
print("")