BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id, name, pages):
        '''
        Метод конструктор объекта 'Book'.
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        ''''
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        '''
        Метод, возвращающий строку формата, где "название_книги" берется с помощью атрибута name.
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        :return: >> Книга "название_книги"
        ''''
        return f'Название книги: {self.name}'

    def __repr__(self):
        return f'Book(id_={self.id}, name={self.name}, pages={self.pages})'

class Library:
    def __init__(self, books:list=None):
        '''
        Метод конструктор объекта 'Library'.
        :param books: Список книг
        ''''
        self.books = [] if books is None else books


    def get_next_book_id(self):
        '''
        Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        :return: возвращает идентификатор последней книги, увеличенный на 1, в случае, если книга в библиотеке есть.
        Если книги нет, то возвращает 1.
        ''''
        if self.books is None:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self):
        '''
        Метод, возвращающий индекс книги в списке, который хранится в атрибуте экземпляра класса.
        :return: возвращает индекс из списка, в случае, если книга существует, если её нет, то возвращает ошибку.
        ''''
        for index, book in enumerate(self.books):
            if number_id == book.id_:
                return index
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

#testing
if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))