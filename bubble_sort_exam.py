def bubble_sort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(n-i-1): 
            if arr[j] > arr[j+1]: 
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    
arr = [78, 65, 90, 82, 70]
bubble_sort(arr) 
print("Hasil pengurutan:" ,arr) 
