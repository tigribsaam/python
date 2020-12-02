from Model.person import Person

class Employee(Person):
    def __init__(self, nm, em, jb):
        super().__init__(nm, em)
        self.__job = jb

    def get_job(self):
        return self.__job

    def set_job(self, jb):
        self.__job = jb

    def __repr__(self):
        return "name: " + self.get_p_name() + ", email: " + self.get_email() + ", job: " + self.__job

    def __str__(self):
        return "Name: " + self.get_p_name() + "\nEmail: " + self.get_email() + "\nJob: " + self.__job
