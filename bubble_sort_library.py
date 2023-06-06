def bubble_sort_books(books):
    n = len(books)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j][3] > books[j+1][3]:
                books[j], books[j+1] = books[j+1], books[j]
    
    return books

books = [
    [1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 320],
    [2, "To Kill a Mockingbird", "Harper Lee", 281],
    [3, "The Great Gatsby", "F. Scott Fitzgerald", 180],
    [4, "Pride and Prejudice", "Jane Austen", 432],
    [5, "1984", "George Orwell", 328]
]

sorted_books = bubble_sort_books(books)
print("Daftar buku setelah diurutkan:")
for book in sorted_books:
    print(f"No. {book[0]} | Judul Buku: {book[1]} | Penulis: {book[2]} | Jumlah Halaman: {book[3]}")
