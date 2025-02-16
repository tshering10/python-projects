import json

# Initial book data
books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "year": 1925,
        "rating": 5
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "rating": 4
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "rating": 5
    }
]

# Write the initial book data to books.json
with open('books.json', 'w') as file:
    json.dump(books, file, indent=4)

print("Initial book data written to books.json")

with open("books.json", "r") as file:
    book_data = json.load(file)
print("Do you want to add books?")
choice = input("Enter (y/n): ").lower()
if choice == "y":
    
    title = input("Enter the title: ")
    author = input("Enter the name of author: ")
    genre = input("Enter the genre: ")
    year = input("Enter the year: ")
    rating = input("Enter the rating(1-5): ")

    dict = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "rating": rating
    }

    book_data.append(dict)
   

    with open("books.json", "w") as f:
        json.dump(book_data,f,indent=3)
        
    print("Your Book added successfully..")