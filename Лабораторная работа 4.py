class Student():
    '''
    Базовый класс - студенты.
    '''


    def __init__(self, surname: str, name: str, patronymic: str, education: str, education_unit: str,\
                 qualification: str, form_education: str, year_admission: int, course_study: int, group: str, id: int=None):
        '''
        Создание и подготовка к работе объекта Студент1.
        :param surname: Фамилия студента
        :param name: Имя студента
        :param patronymic: Отчество студента
        :param education: Учебное подразделение студента
        :param education_unit: Направление подготовки студента
        :param qualification: Квалифицкация студента
        :param form_education: Форма обучения студента
        :param year_admission: Год поступления студента
        :param course_study: Курс студента
        :param group: Группа студента
        '''
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.education = education
        self.education_unit = education_unit
        self.qualification = qualification
        self.form_education = form_education
        self.year_admission = year_admission
        self.course_study = course_study
        #self.term = term
        self.group = group
        self.id = id


    def __str__(self):
        '''
        Строковый метод класса Student
        :return: Возвращает строку с ФИО студента и его направление подготовки
        '''
        return '{} {} {} с направления подготовки {}'.format(self.surname,self.name, self.patronymic, self.education_unit)

    '''
    ещё один вариант записи такой: 
         return f'{self.surname}  {self.name} {self.patronymic} с направления подготовки {self.education_unit})'
    но вопрос: можно ли как-то {self.surname + self.name} но чтобы было не ИмяФамилия? 
    '''

    def __repr__(self):
         '''
         Метод, возвращающий строку формата "Фамилия имя отчество"
         :return: Возвращает валидную питоновскую строку
         '''
         return f'{self.__class__.__name__}(surname={self.surname}, name={self.name}, patronymic={self.patronymic}'

    def get_next_student_id(self):
         '''
         Определяет номер идентификатора студента
         :return: Возвращает идентификатор студента
         '''
         if self.id is None:
            return 1
         else:
           return self.id[-1].id_ + 1

    def incentive_measures(self, average_score: float, scholarship: int=377718):
        '''
        Метод, определяющий размер академической стипендии студента, если он таковую имеет.
        Если средний балл равен 5, то это счастливчики, которые будут получать повышенную академическую (503624). НО вообще стипендия начисляется тем,
        у кого средний балл больше или равен 4, в размере -25% от размера повышенной академической (377718).
        :param average_score: средний балл за сессию
        :param scholarship: размер повышенной академический стипендии (руб.)
        :return: размер стипендии (руб.)
        '''
        self.average_score = average_score
        if average_score == 5:
            scholarship = 503624
        elif average_score >= 4:
            scholarship = 377718
        else:
            scholarship = 0
        self.scholarship = scholarship
        return f'Размер вашей стипендии: {self.scholarship} рублей'


    # def status_student(self, status='учится'):
    #     '''
    #     Определяет статус студента
    #     :return:
    #     '''
    #     self.status = status
    #     return self.status


class Underachieving_Students(Student):
    '''
    Класс неуспевающих студентов
    '''
    def __init__(self, surname: str, name: str, patronymic: str, education: str, education_unit: str,\
                 qualification: str, form_education: str, year_admission: int, course_study: int, group: str, id: int=None, status: int='на допсессии'):
        '''
        Создание и подготовка к работе объекта SimpleBody
        Создание и подготовка к работе объекта Студент1
        :param surname: Фамилия студента
        :param name: Имя студента
        :param patronymic: Отчество студента
        :param education: Учебное подразделение студента
        :param education_unit: Направление подготовки студента
        :param qualification: Квалифицкация студента
        :param form_education: Форма обучения студента
        :param year_admission: Год поступления студента
        :param course_study: Курс студента
        :param group: Группа студента
        :param status: Статус студента студента
        '''
        super().__init__(surname, name, patronymic, education, education_unit, qualification, form_education, year_admission, course_study, group, id)
        self.status = status

    def __repr__(self):
        '''
        Метод, возвращающий строку формата "Фамилия имя отчество", с уведомлением о том, что человек находится на доп.сессии. Обычно студент, если вдруг
        попал на допсессию, сам знает, но иногда в системе бывают сбои, так что если человек увидит данное уведомление, которое ему не должно было быть предназначено,
        он сможет вовремя отреагировать на случившееся и избежать возможные негативные последствия.
        :return: Возвращает валидную питоновскую строку
        '''
        return f'К великому несчастью, Вы, {self.surname} {self.name} {self.patronymic}, находитесь на допсессии. Пожалуйста, учитесь усерднее, иначе мы будем вынуждены...'


if __name__ == "__main__":
    me = Student('Барышникова', 'Ульяна', 'Александровна', 'Физико - механический \
    институт', '03.02.02. Физика', 'бакалавр', 'очная', 2021, 2, '5030302/10004')
    b = me.__str__()
    print(f'{b}, вы получаете стипендию в размере {me.incentive_measures(average_score=5)}')
    print(f'{me.__repr__()}')
    someone = Underachieving_Students('Грязных', 'Виктор', 'Владимирович','Физико - механический \
    институт', '03.02.02. Физика', 'бакалавр', 'очная', 2021, 2, '5030302/70003')
    print(f'{someone.__repr__()}')
