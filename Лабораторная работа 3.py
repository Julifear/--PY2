class Book:
  '''
  Базовый класс - книги.
  '''

  def __init__(self, name, author):
    '''
    Создание и подготовка к работе объекта Книга1 класса Book
    :param name: Название книги
    :param author: Автор книги
    '''
    self._name = name
    self._author = author


  def __setattr__(self, name, author):
    '''
    Метод, который проверяет то, что аргумент установлен только один раз и его менять нельзя
    :param name: Название книги
    :param author: Автор книги
    :return: возвращает ошибку, которая предупреждает пользователя о том, что нельзя "переустановить" аргумент
    '''
    if name == '_name' and hasattr(self, '_name'):
      raise AttributeError('This attribute can only be set once in the init method')
    self.__dict__[name] = author


  def __str__(self):
    '''
    Строковый метод класса Book
    :return: Возвращает строку с названием книги и её автором
    '''
    return f'Автором книги под названием "{self._name}" является {self._author}'


  def __repr__(self):
    '''
    Строковый метод класса Book
    :return: Возвращает строку с названием книги и её автором
    '''
    return f'Название книги: {self._name}\nАвтор: {self._author}'


class PaperBook(Book):
  '''
  Дочерний класс класса Book - бумажные книги
  '''
  def __init__(self, name, author, pages: int):
    '''
    Создание и подготовка к работе объекта Бумажная книга1 класса PaperBook
    :param name: Название книги
    :param author: Автор книги
    :param pages: Количество страниц
    '''
    super().__init__(name, author)
    if type(pages) != int or pages > 1000:
      raise ValueError
    self.pages = pages


  def __repr__(self):
    '''
    Строковый метод класса PaperBook
    :return: Возвращает строку, в которой содержатся название, автор выбраной книги, как параметры базового класса,
    и количество страниц, как параметр, специально устанавливающийся для класса Бумажные книги
    '''
    return f'{super().__repr__()}\nКоличество страниц: {self.pages}'


class AudioBook(Book):
  '''
  Дочерний класс класса Book - аудиокниги
  '''
  def __init__(self, name, author, duration: float):
    '''
    Создание и подготовка к работе объекта Аудиокнига1 класса AudioBook
    :param name: Название аудиокниги
    :param author: Автор аудиокниги
    :param duration: Продолжительность аудиокниги (мин.)
    '''
    super().__init__(name, author)
    if type(duration) != float or duration > 250.00:
        raise ValueError
    self.duration = duration


  def __repr__(self):
    '''
    Строковый метод класса AudioBook
    :return: Возвращает строку со всеми унаследованнми параметрами класса Book и вводит новый параметр продолжительность аудиокниги (мин.)
    '''
    return f'{super().__repr__()}\nПродолжительность: {self.duration} минут'


if __name__ == "__main__":
  book1 = PaperBook('The Golden Fish', 'Alexander Pushkin', 120)
  book2 = AudioBook('The Picture of Dorian Gray', 'Oscar Wilde', 220.10)

  print(book1._name)
  print(book2.duration)

  print(str(book1))
  print(repr(book1))

  print(str(book2))
  print(repr(book2))

  book1._name = 'Aaa'
  print(book1._name)
  print(str(book1))
