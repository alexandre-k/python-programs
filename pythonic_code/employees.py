class Employee:

    num_emps = 90
    raise_wage = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname.lower() + '.' + lastname.lower() + '@mycompany.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_wage)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_wage = amount

    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, pay = emp_str.split(',')
        return cls(firstname, lastname, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Sandrine', 'Schaeffer', 2000)

emp2 = Employee.from_string('Alexandre,Krispin,3000')
Employee.set_raise(1.08)

