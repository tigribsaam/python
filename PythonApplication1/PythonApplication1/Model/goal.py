class Goal(object):
    def __init__(self, nm):
        self.__g_name = nm

    def get_g_name(self):
        return self.__g_name

    def set_g_name(self, nm):
        self.__name = nm

    def __repr__(self):
        return self.__g_name

    def __str__(self):
        return self.__g_name
