def mergeSort(list): 
    list_length = len(list) 
    if list_length == 1: 
        return list 
 
    mid_point = list_length // 2 
    left_partition = mergeSort(list[:mid_point]) 
    right_partition = mergeSort(list[mid_point:]) 
    return merge(left_partition, right_partition) 
 
def merge(left, right): 
    output = [] 
    i = j = 0 
    while i < len(left) and j < len(right): 
        if isinstance(left[i], str) and isinstance(right[j], str): 
            # jika kedua elemen adalah string, bandingkan string tersebut 
            if left[i] < right[j]: 
                output.append(left[i]) 
                i += 1 
            else: 
                output.append(right[j]) 
                j += 1 
        elif isinstance(left[i], str): 
            # jika hanya elemen kiri adalah string, tambahkan elemen kiri ke output 
            output.append(left[i]) 
            i += 1 
        elif isinstance(right[j], str): 
            # jika hanya elemen kanan adalah string, tambahkan elemen kanan ke output 
            output.append(right[j]) 
            j += 1 
        else: 
            # jika kedua elemen bukan string, bandingkan elemen tersebut seperti biasa 
            if left[i] < right[j]: 
                output.append(left[i]) 
                i += 1 
            else: 
                output.append(right[j]) 
                j += 1 
    output.extend(left[i:]) 
    output.extend(right[j:]) 
 
    return output 
 
def pisah(listnya): 
    for i in listnya: 
        tampung.append(i) 
 
listacak = ["3", 7, 2, 5,22,"10","b","a"] 
tampung = [] 
print("Sebelum diurutkan ",listacak) 
pisah(listacak) 
print("setelah diurutkan = ", tampung) 
sorted_list = mergeSort(tampung) 
print("hasil akhir", sorted_list)

