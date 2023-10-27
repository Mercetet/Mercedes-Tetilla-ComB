class Person:
    def __init__(self, name, age, dni):
        self.__name = name
        self.__age = age
        self.__dni = dni

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_at):
        self.__name = new_at

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_at):
        self.__age = new_at

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, new_at):
        self.__dni = new_at

    def show(self):
        print(f"{self.__name}, {self.__age}, {self.__dni}")

    def adult(self):
        bo = True
        if(self.__age >= 18):
            bo = True
        else:
            bo = False
        return bo
    