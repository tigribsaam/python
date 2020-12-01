class Training(object):
    def __init__(self, nm, des):
        self.__tr_name = nm
        self.__description = des

    def get_tr_name(self):
        return self.__tr_name

    def set_tr_name(self, nm):
        self.__tr_name = nm

    def get_des(self):
        return self.__description

    def set_des(self, des):
        self.__description = des

    def __repr__(self):
        return "training: " + self.__tr_name + ", des: " + self.__description

    def __str__(self):
        return "Training: " + self.__tr_name + "\ndescription: " + self.__description
