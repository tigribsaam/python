class Person(object):
    def __init__(self, nm, em):
        self.__p_name = nm
        self.__email = em

    def get_p_name(self):
        return self.__p_name

    def set_p_name(self, nm):
        self.__p_name = nm

    def get_email(self):
        return self.__email

    def set_email(self, em):
        self.__email = em

    def __repr__(self):
        return "name: " + self.__p_name + ", email: " + self.__email

    def __str__(self):
        return "Name: " + self.__p_name + "\nemail: " + self.__email
