searched_book = input()
total_books_checked = 0
book_is_found = False
current_book = input()

while current_book != "No More Books":

    if current_book == searched_book:
        book_is_found = True
        break

    total_books_checked += 1
    current_book = input()

if book_is_found:
    print(f'You checked {total_books_checked} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {total_books_checked} books.')
