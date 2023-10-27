class Phonebook:
    def __init__(self, name, tel, email):
        self.__name = name
        self.__tel = tel
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_at):
        self.__name = new_at

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, new_at):
        self.__tel = new_at

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_at):
        self.__email = new_at

    def add(self):
        name2 = input("Ingrese el nombre del nuevo contacto: ").title()
        tel2 = int(input("Ingrese el telefono del nuevo contacto: "))
        email2 = input("Ingrese el email del nuevo contacto: ").lower()
        contact = [name2, tel2, email2]
        return contact
    
    def serch(self, book):
        found = False
        serch_name = input("Ingrese el nombre del contacto que esta buscando.").title()
        for i, contact in enumerate(book):
            if contact[0] == serch_name:
                found = True
                break
        if not found:
            return -1
        else:
            return i
    
    def edit(self, book, num):
        op = int(input("Que desea editar? \n 1.Nombre \n 2.Telefono. \n 3.Email."))
        while True:
            if op == 1:
                new_name = input(f"Ingrese el nuevo nombre para: {book[num][0]}")
                book[num][0]=new_name
                break
            elif op == 2:
                new_num = input(f"Ingrese el nuevo telefono de: {book[num][0]}")
                book[num][1]=new_num
                break
            elif op == 3:
                new_email = input(f"Ingrese el nuevo email para: {book[num][0]}")
                book[num][2]=new_email
                break
            else:
                print("Ingreso mal. Intente nuevamente. ")


