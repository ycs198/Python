class SchoolMember:
    """Represents any school member"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print '(Initialzed SchoolMember:{})'.format(self.name)

    def tell(self):
        """Tell my details"""
        print 'Name:"{}" Age:"{}"'.format(self.name,self.age),


class Teacher(SchoolMember):
    """Represents any Teacher part of the school"""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print '(Initialzed Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{}"'.format(self.salary)


class Student(SchoolMember):
    """Represents the Student."""
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print '(Initialized Student : {})'.format(self.name)
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks : "{}"'.format(self.marks)


t = Teacher('bala','40','30000')
s = Student('krishna','14','50')


print

members = [t,s]
for member in members:
    member.tell()


