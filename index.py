# Simple Python Calculator 


print("===== Python Calculator =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"

else:
    result = "Invalid operator!"

print("Result:", result) 




# Simple Library Management System


books = {
    "python": "Available",
    "c programming": "Available",
    "html": "Available",
    "css": "Available",
    "javascript": "Available"
}


def show_books():
    print("\n----- BOOKS -----")

    for book, status in books.items():
        print(f"{book.title()} : {status}")


def add_book():
    book = input("Enter book name: ").lower()

    if book in books:
        print("Book already exists!")
    else:
        books[book] = "Available"
        print("Book added successfully!")


def borrow_book():
    book = input("Enter book name to borrow: ").lower()

    if book not in books:
        print("Book not found!")

    elif books[book] == "Borrowed":
        print("Sorry, this book is already borrowed.")

    else:
        books[book] = "Borrowed"
        print("Book borrowed successfully!")


def return_book():
    book = input("Enter book name to return: ").lower()

    if book not in books:
        print("Book not found!")

    elif books[book] == "Available":
        print("This book is already available.")

    else:
        books[book] = "Available"
        print("Book returned successfully!")


while True:

    print("\n==============================")
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Show Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")