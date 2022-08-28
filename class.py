#isinstance
isinstance('abc',str) # True
isinstance(55.2,str) #False
isinstance(55.2,float) #True

#class student
class Student: #class는 대문자로 하고 파일명은 같은 이름의 소문자로 하는경우가 대부분
    name = ""
    id = 0
    gender = "female" #이안에서 기본 default 값을 설정해놔도 되고

    def num_courses(self):
        return len(self.course)
a = Student()
b = Student()
c = Student()

a.name = "Harry Potter"
a.id = 2017103701
a.gender = "male"

b.name = "Herminone Granger"
b.id = 2018103722
b.birthyear = 1999 #이렇게 따로 추가를 해도 된다.

c.name = "Ron Weasley"

a.course = ["English","Programming"]
b.course = ["Writing","Physics","Programming"]
c.course = ["Programming"]

a.num_courses() # 2
Student.num_courses(a) # 2

#object, 모든 종류의 class
isinstance(55.2,object) #True
isinstance('abc',object) #True

class Book:
    def num_authors(self):
        return len(self.authors)

import book
ruby_book = book.Book()
ruby_book.title = "Programming Ruby"
ruby_book.authors = ["Thomas","Fowler","Hunt"]

book.Book.num_authors(ruby_book) # 3
ruby_book.num_authors #둘 다 같은 거지만 위에껀 module로 부른거기 떄문에 book붙여준다

#__init__method refined, return 필요없음, overload한 것
class Book:
    def __init__(self, title='', authors=[], publisher='', isbn='0', price=10.0):
        self.title = tile
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price
python_book = book.Book("Practical Programming",['Campbell','Gries','Montojo'],'Pragmatic Bookslef','978-1-93778-545-1',25.0)

#__str__method, 어떤 개체를 print할 때 쓰이는 method, string으로 return
def __str__(self):
    rep = "Title: {0}\n Authors: {1}\n Publisher: {2}\n ISBN: {3}\n Price: {4}".format(self.title, self.authors, self.publisher, self.ISBN, self.price)
    return rep

#__eq__ method, 안에 든 정보가 같아도 서로 다르다고 다옴 이를 수정하기 위해 override
def __eq__(self, other):
    return self.ISBN == other.ISBN

#Override, Overload
#override
def __init__(self, title, authors, publisher, isbn, price):
        self.title = tile
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price
#overload
        def __init__(self, title='', authors=[], publisher='', isbn='0', price=10.0):
        self.title = tile
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

#Inheritance(상속)
class Member:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
    def __str__(self):
        rep = "{}\n{}\n{}\n".format(self.name, self.address, self.email)
        return rep
    
class Faculty(Member):
    def __init__(self, name, address, email, faculty_num):
        super().__init__(name, address, email) #super class 상속받기
        self.faculty_number = faculty_num
        self.courses_teaching = []
    def __str__(self):
        member_string = super().__str__()
        rep = "{}\n{}\nCourses:{}".format(member_string, self.falculty_number, self.courses_teaching)
        return rep
    
class Student(Member):
    def __init__(self, name, address, email, student_num):
        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
