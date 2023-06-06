def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

angka = [9, 5, 3, 8, 2]
hasil = selection_sort(angka)
print("Daftar angka setelah diurutkan:",hasil)
