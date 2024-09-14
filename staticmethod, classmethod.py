from datetime import date


class MyClass1:
    count_adult = 0
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

#Завдання 5
    @staticmethod
    def adult_age(surname: str, name: str, birth_year: int, nation: str):
        if birth_year >= 18 and nation == 'Ukrainian':
            print('The person is adult.')
        elif birth_year >= 21 and nation == 'American':
            print('The person is adult in America.')
        else:
            print('The person is not adult.')


    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    @classmethod
    def count_adult_people(cls, name: str, age: int, nation: str):
        if age >= 18 and nation == 'Ukrainian':
            print(f'Adult person in Ukraine: {cls.count_adult + 1}')
        elif age >= 21 and nation == 'American':
            print(f'Adult person in America: {cls.count_adult + 1}')



    def print_info(self):
        print(self.surname + " " + self.name + "'s age is: " + str(self.age))


class MyClass2(MyClass1):
    color = 'White'


m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
m_per2.print_info()

m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
print(isinstance(m_per3, MyClass2))

m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
print(isinstance(m_per4, MyClass1))

print(issubclass(MyClass1, MyClass2))
print(issubclass(MyClass2, MyClass1))

person = MyClass1('Oleh', 'Yemelianov', 20)
person.adult_age('Yemelianov', 'Oleh', 20, 'Ukrainian')
person.adult_age('Ivanenko', 'Dmytro', 17, 'Ukrainian')
person.adult_age('Doe', 'Jane', 20, 'American')
person.adult_age('Joe', 'Ellen', 24, 'American')

person.count_adult_people('Oleh', 20, 'Ukrainian')
person.count_adult_people('Ivan', 15, 'Ukrainian')
person.count_adult_people('John', 24, 'American')
person.count_adult_people('Ashley', 20, 'American')
person.count_adult_people('Jack', 25, 'American')