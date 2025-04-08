import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
        return[]
    
def save_library(library):
     with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    tittle = input('Enter the tittle of book: ')
    Author = input('Enter the Auther of book: ')
    Year = input('Enter the year of book: ')
    Genre = input('Enter the genre of book: ')
    Read = input('Enter the read of book? (yes/no): ').lower() == 'yes'

            
    new_book = {
        'tittle': tittle,
        'author': Author,
        'year': Year,
        'Genre': Genre,
        'read' : Read,
    }

    library.append(new_book)
    save_library(library)
    print(f'Book {tittle} added successfully!')

def remove_book(library):
    tittle = input('Enter the tittle of the book to remove from library: ')
    initial_lenth = len(library)
    library = [book for book in library if book['tittle'].lower() != tittle]
    if len(library) < initial_lenth:
        save_library(library)
        print(f'Book {tittle} removed successfully!')
    else:
        print(f'Book {tittle} not found in the library!')


def search_library(library):
    search_by = input('Search by tittle or author: ').lower()
    search_term = input(f'Enter the {search_by}').lower()

    result = [book for book in library if search_term in book[search_by].lower()]

    if result:
        for book in result:
            status = "Read" if book['read'] else "unread"
            print(f'{book["tittle"]} by {book["author"]} - {book["year"]} - {book["Genre"]} - {status}')

    else:
        print(f"no book found matching'{search_term}' in the {search_by} failed.")
            

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "unread"
            print(f'{book["tittle"]} by {book["author"]} - {book["year"]} - {book["Genre"]} - {status}')

    else:
        print('Library is empty!')

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f'Total books: {total_books}')
    print(f'percentage read: {percentage_read: .2f}%')

def main():
    library = load_library()
    while True:
        print('menu')
        print('1. Add a book')
        print('2. Remove a book')
        print('3. Search the library')
        print('4. Display all books')
        print('5. Display statistics')
        print('6. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print('exiting...')
            break
        else :
            print('invalid choice try again...')

if __name__ == '__main__':
    main()