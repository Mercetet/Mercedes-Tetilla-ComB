class Triangle:
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, new_at):
        self.__side1 = new_at

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, new_at):
        self.__side2 = new_at

    @property
    def side3(self):
        return self.__side3

    @side3.setter
    def side3(self, new_at):
        self.__side3 = new_at

    def max_side(self):
        list_t = [self.__side1, self.__side2, self.__side3]
        max = 0
        for i in list_t:
            if i > max:
                max = i
        return max
    
    def type_t(self):
        if self.__side1 != self.__side2 and self.__side1 != self.__side3 and self.__side2 and self.__side3:
            print("Es un triangulo escaleno. 🍕")
        elif self.__side1 == self.__side2 and self.__side1 == self.__side3:
            print("Es un triangulo equilatero 👀 ")
        else:
            print("Es un triangulo isosceles. 📐")