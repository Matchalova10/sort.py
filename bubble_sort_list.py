def bubble_sort_descending(numbers):
    n = len(numbers)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

numbers = [42, 19, 33, 8, 55]
sorted_numbers = bubble_sort_descending(numbers)
print("Daftar angka setelah diurutkan secara descending:")
for number in sorted_numbers:
    print(number)
