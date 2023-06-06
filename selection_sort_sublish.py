#mengurutkan sublist dalam daftar 

def selection_sort(arr):
    for i in range(n-1):
        min_index = 1
        for j in range(i+1, n):
            if arr[j][0] < arr[min_index][0]:
                min_index = j
                
arr[[3,5],[1,2],[4,6],[2,1]]
selection_sort(arr)
print("Hasil penghitungan:", arr)
